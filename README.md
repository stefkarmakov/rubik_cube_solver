# Testing if a Rubik's Cube can be solved using a Simulated Annealing Algorithm

The idea of this project is to walk you through the way I tackled a problem that I found interesting and worth exploring: can you solve a Rubik's cube using Simulated Annealing. 
The most popular ways of solving the cube are either by applying a set of rules, depending on the configuration of the cube at each stage of the solving process, or using graph 
search algorithms, like A*, or Kociemba’s algorithm. But I wanted to know if you can use a Genetic Algorithm, like Simulated Annealing, to solve the problem, not by simply brute-
forcing all combinations and finding the fastest way to the solution. So here I'm attempting exactly this.

------

The Jupyter notebook gives a thorough description of the code and all the aspects and decisions behind the functions and the overall script.

The python code is a script that can be ran in python separately, or on a shell script by giving it the required inputs. The script runs 100 sessions, where each time it mixes the Rubik's cube by the specified number of random moves and tries to solve it with the given parameters `temperature`, `cooling rate` and `maximum number of moves`. The output is the number of cubes that were solved, so the number can be read as percentage of solved cubes, or accuracy of the Simulated Annealing algorithm for the given set-up. The function can be ran from the terminal as:
```
python3 simulated_annealing_rubik_solver.py --mix_moves 4 --temp 2 --cool_rate 0.98 --max_iterations 1000
```

------
My conclusion for this project is that Simulated Annealing is able to solve some Rubik's cubes, if they are a bit simpler, but is not a reliable way of finding the solution to the 
problem. It also takes a very large number of moves to reach a solution, more than if more conventional algorithms are used. So overall it's a fun way of approaching the problem, 
but better and faster methods exist, and it doesn't seem to improve on any aspect, other than maybe the complexity of coding the solution.

I'll be happy if I get recommendation on how to make the code run faster, or on how to improve the accuracy and make the algorithm actually perform good and solve complex cubes. I tried different methods of fixing the algorithm to not get stuck, but I haven't been able to find a solution yet. 
