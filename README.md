# Testing if a Rubik's Cube can be solved using a Simulated Annealing Algorithm

The idea of this project is to walk you through the way I tackled a problem that I found interesting and worth exploring: can you solve a Rubik's cube using Simulated Annealing. 
The most popular ways of solving the cube are either by applying a set of rules, depending on the configuration of the cube at each stage of the solving process, or using graph 
search algorithms, like A*, or Kociemba’s algorithm. But I wanted to know if you can use a Genetic Algorithm, like Simulated Annealing, to solve the problem, not by simply brute-
forcing all combinations and finding the fastest way to the solution. So here I'm attempting exactly this.

------

## Notebook
- The Jupyter notebook gives a thorough description of the code and all the aspects and decisions behind the functions and the overall script. There are also included explanations about how the Simulation Annealing algorithm works and how the Rubik's cube "simulation" was encoded as matrix manipulations.   

## Python Script
- The python code is a script that can be ran in python separately, or on a shell script by giving it the required inputs. The script runs 100 sessions, where each time it mixes the Rubik's cube by the specified number of random moves and tries to solve it with the given parameters `temperature`, `cooling rate` and `maximum number of moves`. The output is the number of cubes that were solved, so the number can be read as percentage of solved cubes, or accuracy of the Simulated Annealing algorithm for the given set-up. The function can be ran from the terminal as (example values are given):
```
python3 simulated_annealing_rubik_solver.py --mix_moves 4 --temp 2 --cool_rate 0.98 --max_iterations 1000
```
Only `numpy` is required as an external python library. 


As the idea is to have a solution for any number of mixing moves, here is a quick example exploring the accuracy of the algorithm, in terms of solved cubes, by varying only `mix_moves`, and the other params are fixed:

**T = 2 , cooling rate = 0.99 , maximum iterations = 500**

| `mix_moves` | Percentage solved cubes |
|-------------|:-----------------------:|
| 1           |           100           |
| 2           |           68            |
| 3           |           31            |
| 4           |           18            |
| 5           |           12            |
| 6           |            7            |
| 7           |            3            |
| 8           |            1            |

The results in the table are stochastic because of the random element of the mixing of the cube, so they can differ when ran again, but not by much. Nevertheless, they show a pattern overall, that with the increasing of the mixing, and thus of complexity, the algorithm becomes less and less accurate.

------

## Contributions
The task was to explore if Simulated Annealing is a viable way to solve the Rubik's cube. My conclusion for this project is that Simulated Annealing is able to solve some Rubik's cubes, if they are a bit simpler, but is not a reliable way of finding the solution to the 
problem. It also takes a very large number of moves to reach a solution, more than if more conventional algorithms are used. So overall it's a fun way of approaching the problem, 
but better and faster methods exist, and it doesn't seem to improve on any aspect, other than maybe the complexity of coding the solution.

I'll be happy if I get recommendation on how to make the code run faster, or on how to improve the accuracy and make the algorithm actually perform good and solve complex cubes. I tried different methods of fixing the algorithm to not get stuck, but I haven't been able to find a solution yet. 
