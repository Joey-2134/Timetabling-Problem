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
        print(
            f"Student {i:2d} is enrolled in exams: {student_exams} which take place in timeslots: {student_timeslots}")

        if len(student_timeslots) != len(set(student_timeslots)):
            print(f"Student {i:2d} has a hard constraint violation")  # example: Student2 exams: [0, 4, 6] in timeslots: [1, 1, 3], violation
            violations += 1
        else:
            print(f"Student {i:2d} has no conflicts")  # example: Student0 exams: [5, 6, 7] in timeslots: [2, 3, 4], no violation

    return len(student_matrix) - violations # number of students without hard constraint violations, higher the better
