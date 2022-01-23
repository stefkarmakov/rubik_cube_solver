import numpy as np
import random
import argparse

# GROUND_TRUTH == solved cube
GROUND_TRUTH = np.array([mat*(idx+1) for idx,mat in enumerate(np.ones((6,3,3)))])
 
ROTATION_LOOKUP_TABLE = np.array([
    [[0,0,2], [0,0,3], [0,0,4], [0,0,1], [0,0,2]],      # rotate side 1
    [[0,1,0], [0,1,4], [0,1,5], [2,1,2], [0,1,0]],      # rotate side 2
    [[0,0,0], [0,1,1], [2,0,5], [2,1,3], [0,0,0]],      # rotate side 3              
    [[2,1,0], [0,1,2], [2,1,5], [2,1,4], [2,1,0]],      # rotate side 4
    [[2,0,0], [0,1,3], [0,0,5], [2,1,1], [2,0,0]],      # rotate side 5              
    [[2,0,4], [2,0,3], [2,0,2], [2,0,1], [2,0,4]] ])    # rotate side 6


def rotate_face(face_matrix, direction):
    """Looking at the cube face, rotate/flip the face matrix representation
    either CW(direction = 1) or CCW(direction = -1)
    """
    reflection_matrix = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    if direction == 1:
        return np.matmul(face_matrix.transpose(), reflection_matrix)
    elif direction == -1:
        return np.matmul(face_matrix, reflection_matrix).transpose()


def flip_XOR(i_0, j_0, i_1, j_1):
    """This function serves the purpose of flipping the row/col order in
    reverse if the move/transformation results in such a flip. This is needed
    because of the cube representation that we use to map a 3D object on a 
    2D plane, so we need to account for unfolding directions, and thus
    such flips during face rotations
    """
    diffs = [i_0 - i_1, j_0 - j_1] 
    # flip only if one of the row/col params differs => XOR gate =>
    # (-1)^1=-1 otherwise (-1)^2=1 or (-1)^0=1
    return (-1)**np.count_nonzero(diffs)
    
def move(face_matrix_num, direction, current_cube_state):  
    """Transform the cube under a signle face rotation"""
    new_cube_state = current_cube_state.copy()
    face_matrix = current_cube_state[face_matrix_num]
    # update just the rotated face
    new_cube_state[face_matrix_num] = rotate_face(face_matrix, direction)
    
    # get the rotation row for the particular face   
    transfomations_table = ROTATION_LOOKUP_TABLE[face_matrix_num,:,:][::direction]
    # update the affected sides around the rotated face (using the lookup table)
    for t in range(len(transfomations_table)-1):
        i_0 = transfomations_table[t][0]
        j_0 = transfomations_table[t][1]
        k_0 = transfomations_table[t][2]
        
        i_1 = transfomations_table[t+1][0]
        j_1 = transfomations_table[t+1][1]
        k_1 = transfomations_table[t+1][2]
        
        flip_sign = flip_XOR(i_0, j_0, i_1, j_1) # -1 or 1
        # make sure that row/col is in an array form (flatten part)
        new_cubelets = (current_cube_state[k_0].take((i_0,), axis=j_0)).flatten()
        # check if new tile position is row or col, and flip the row/col accordingly
        if j_1 == 0:
            new_cube_state[k_1][i_1,:] = new_cubelets[::flip_sign]
        elif j_1 == 1:
            new_cube_state[k_1][:,i_1] = new_cubelets[::flip_sign]
       
    return new_cube_state


def mix_cube(num_mixing_moves):
    """Randomly mix cube a set number of moves -> output mixed cube and 
    the history of the moves, for reference and back-tracing
    """
    mix_history = []
    current_cube_state = GROUND_TRUTH.copy()
    for move_idx in range(num_mixing_moves):
        rand_move = random.randint(0,5)
        rand_dir = random.choice([-1, 1])
        current_cube_state = move(rand_move, rand_dir, current_cube_state)
        mix_history.append((rand_move,rand_dir))
        
    return mix_history, current_cube_state   


def calculate_fitness(cube_state):
    """Calculate the difference between the current cube state and the solved
    cube, how many tiles are not in position = fitness of cube. Worst case,
    48 tiles are not in position because the 6 center tiles will always be in 
    position
    """
    return np.count_nonzero(GROUND_TRUTH - cube_state)


def choose_move(current_cube_state, current_cube_fitness, T, previous_move):
    no_move = True
    count_iters = 0
    while no_move:
        # add counter if while loop gets stuck at local minima, revert the 
        # cube state to the previous move, and denote it with -100 delta
        if count_iters == 100:
            prev_cube_state = move(previous_move[0], -previous_move[1], current_cube_state)
            prev_move_reversed = [previous_move[0], -previous_move[1]]
            return prev_move_reversed, -100, prev_cube_state
        count_iters += 1 
        
        # randomly choose new move and assess it's fitness -> decide by the
        # evaluation/goodness of move if the move should be taken
        new_move = random.randint(0,5)
        new_move_direction = random.choice([-1, 1])   
        new_cube_state = move(new_move, new_move_direction, current_cube_state)
        delta = calculate_fitness(new_cube_state) - current_cube_fitness
        
        if delta <= 0:
            break
        P = np.exp(-delta/T) # returns probabilty for a move between (0,1)
        random_prob = np.random.uniform(0,1) # generate random (0,1) probability
        # if random probability is smaller -> take move
        if P > random_prob:
            break
            
    chosen_move = [new_move, new_move_direction] 
    return chosen_move, delta, new_cube_state
  
       
def cooling_process(current_cube_state, T, temp_cooling_rate, max_iterations):
    moves_history = [[0, 1, 0, 0, 0]] # initiate with random wrong nums so choose_move function works
    
    cube_developemnt = list()
    cube_developemnt.append(current_cube_state)
    for iterate in range(max_iterations):
        
        current_cube_fitness = calculate_fitness(current_cube_state)
        if current_cube_fitness == 0:
            solved_cube = current_cube_state.copy()
            # cube is solved
            return moves_history, solved_cube
        chosen_move, delta, current_cube_state = choose_move(current_cube_state, 
                                                             current_cube_fitness, 
                                                             T,
                                                             moves_history[-1][:2])
        cube_developemnt.append(current_cube_state)
        new_cube_fitness = calculate_fitness(current_cube_state)

        moves_history.append([chosen_move[0], chosen_move[1],
                              delta, new_cube_fitness, T])
        T = T*temp_cooling_rate
    
    partially_solved_cube = current_cube_state.copy()
    # cube is partially/not solved
    return moves_history, partially_solved_cube


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--mix_moves', type=int , required=True, 
                        help='Number of mixing moves for cube')
    parser.add_argument('--temp', type=float, required=True, 
                        help='Initial temperature for cooling rate')
    parser.add_argument('--cool_rate', type=float, required=True, 
                        help='The temp decrease/cooling rate')
    parser.add_argument('--max_iterations', type=int, required=True, 
                        help='Maximum number of iterations for algorithm')
    args = parser.parse_args()

    num_mixing_moves = args.mix_moves
    T = args.temp
    temp_cooling_rate = args.cool_rate
    max_iterations = args.max_iterations
    
    results = list()
    for ii in range(100): 
        mix_history, mixed_cube = mix_cube(num_mixing_moves)
        moves_history1, cube1 = cooling_process(mixed_cube, T, temp_cooling_rate, max_iterations)
    
        results.append([calculate_fitness(mixed_cube), calculate_fitness(cube1)])
    
    results = np.array(results)
    print(len(results[results==0]))


