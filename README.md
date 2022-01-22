# Testing if a Rubik's Cube can be solved using a Simulated Annealing Algorithm

The idea of this project is to walk you through the way I tackled a problem that I found interesting and worth exploring: can you solve a Rubik's cube using Simulated Annealing. 
The most popular ways of solving the cube are either by applying a set of rules, depending on the configuration of the cube at each stage of the solving process, or using graph 
search algorithms, like A*, or Kociemba’s algorithm. But I wanted to know if you can use a Genetic Algorithm, like Simulated Annealing, to solve the problem, not by simply brute-
forcing all combinations and finding the fastest way to the solution. So here I'm attempting exactly this.

------

The Jupyter notebook gives a thorough description of the code and all the aspects and decisions behind the functions and the overall script.
The python code is a script that can be ran in python separately, or on a shell script by giving it the required inputs.



------
My conclusion for this project is that Simulated Annealing is able to solve some Rubik's cubes, if they are a bit simpler, but is not a reliable way of finding the solution to the 
problem. It also takes a very large number of moves to reach a solution, more than if more conventional algorithms are used. So overall it's a fun way of approaching the problem, 
but better and faster methods exist, and it doesn't seem to improve on any aspect, other than maybe the complexity of coding the solution.
