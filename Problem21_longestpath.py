def ManhattanTourist(down_matrix, right_matrix, n, m):
    k0 = len(right_matrix[0])
    
    matrix = [[0 for i in range((k0 + 1))] for i in range(n + 1)]
    #print(matrix)
    for i in range(k0):
        matrix[0][i+1] = right_matrix[0][i] + matrix[0][i]
    for i in range(len(down_matrix)):
        matrix[i+1][0] = down_matrix[i][0] + matrix[i][0]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            
            right = right_matrix[i][j-1]
            down = down_matrix[i-1][j]
            matrix[i][j] = max(matrix[i-1][j] + down, matrix[i][j-1] + right)
    res = matrix[-1]
    return res[len(res)-1]

with open('rosalind_ba5b.txt') as f:
    n, m  = f.readline().split()
    n = int(n)
    m = int(m)
    down = []
    for i in range(n):
        down.append([int(x) for x in f.readline().split()])
    a = f.readline()
    right = []
    for i in range(n + 1):
        right.append([int(x) for x in f.readline().split()])

f.close()
longest_path = ManhattanTourist(down, right, n,m)
print(longest_path)