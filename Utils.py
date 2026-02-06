import random

def read_instance(filename):
    with open(filename, 'r') as file:
        first_line = file.readline().strip().split()
        N = int(first_line[0])
        K = int(first_line[1])
        M = int(first_line[2])

        matrix = []
        for i in range(M):
            row = file.readline().strip().split()
            matrix.append([int(x) for x in row])

    return N, K, M, matrix

def check_solution(solution, student_matrix):
    violations = 0
    for (i, row) in enumerate(student_matrix):
        student_exams = [j for j, exam in enumerate(row) if exam == 1]
        student_timeslots = [solution[exam] for exam in student_exams]
        # print(f"Student {i:2d} is enrolled in exams: {student_exams} which take place in timeslots: {student_timeslots}")

        if len(student_timeslots) != len(set(student_timeslots)):
            # print(f"Student {i:2d} has a hard constraint violation")  # example: Student2 exams: [0, 4, 6] in timeslots: [1, 1, 3], violation
            violations += 1
        # else:
        #     print(f"Student {i:2d} has no conflicts")  # example: Student0 exams: [5, 6, 7] in timeslots: [2, 3, 4], no violation

    return len(student_matrix) - violations # number of students without hard constraint violations, higher the better

def initialize_population(population_size, num_exams, num_timeslots):
    population = []
    for solution in range(population_size):
        solution = []
        for j in range(num_exams):
            solution.append(random.randint(0, num_timeslots - 1))
        population.append(solution)
    return population

def generate_next_generation(population, student_matrix, pop_size, tournament_size, crossover_rate, mutation_rate, num_timeslots, elite_percentage):
    next_gen_population = []
    fitnesses = [check_solution(solution, student_matrix) for solution in population]

    # Elitism - Keep the top elite_percentage of solutions
    num_elites = max(1, int(pop_size * elite_percentage))
    sorted_indices = sorted(range(pop_size), key=lambda i: fitnesses[i], reverse=True)
    for i in range(num_elites):
        next_gen_population.append(population[sorted_indices[i]])

    # Tournament selection and Crossover
    while len(next_gen_population) < pop_size:
        parents = []
        for _ in range(2):
            randIdxs = [random.randint(0, pop_size - 1) for _ in range(tournament_size)]
            tournament_fitnesses = []
            for idx in randIdxs:
                tournament_fitnesses.append(fitnesses[idx])
            best_selected_index = tournament_fitnesses.index(max(tournament_fitnesses))
            parents.append(population[randIdxs[best_selected_index]])

        split_idx = random.randint(1, len(parents[0]) - 1)  # index where we split for crossover
        if random.random() < crossover_rate:
            child1 = parents[0][:split_idx] + parents[1][split_idx:]
            child2 = parents[1][:split_idx] + parents[0][split_idx:]
        else:
            child1, child2 = parents[0][:], parents[1][:]

        # Mutation
        for child in [child1, child2]:
            for i in range(len(child)):
                if random.random() < mutation_rate:
                    child[i] = random.randint(0, num_timeslots - 1)

        next_gen_population.extend([child1, child2])

    return next_gen_population