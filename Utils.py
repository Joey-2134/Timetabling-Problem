def read_instance(filename):
    """
    Parse the exam timetabling input file.

    Returns:
        N: number of exams
        K: number of time slots
        M: number of students
        matrix: M x N matrix (matrix[student][exam])
    """
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