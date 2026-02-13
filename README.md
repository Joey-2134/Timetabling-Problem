# Timetabling-Problem
The code is divided into 2 files, the main notebook and Utils.py. Utils.py contains most of the logic used in the GA while the notebook mainly runs the algorithm and plots and prints results.

generate_next_generation() contains the logic for elitism, selection, crossover and mutation

initialize_population() generates a completely random initial population to use

check_solution() counts violations and returns a fitness score for a solution

run_ga() is a super function which essentially just runs the algorithm