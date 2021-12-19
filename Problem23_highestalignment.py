def LongestCommonSubsequence(search, v, w,sigma=None):    
    res = [[]for i in range(2)]
    i = len(v)
    j = len(w)
    
    
    while i > 0 and j > 0:
        if search[i-1][j-1] == '|':
            res[0].append(v[i-1])
            res[1].append(w[j-1])
            i = i - 1
            j = j - 1
        elif search[i-1][j-1] == '/':
            res[1].append('-')
            res[0].append(v[i-1])
            
            i = i - 1
        else:
            
            res[1].append(w[j-1])
            res[0].append('-')
            j = j - 1
    
    
    
    for k in range(j):
        if j >0:
            res[1].append(w[j-1])
            res[0].append('-')
            j = j - 1
        else:
            break
    for k in range(len(v)):
        if i > 0:
            res[0].append(v[i-1])
            res[1].append('-')
            
            i = i - 1
        else:
            break
   
    return res

sigma=5

with open('blosum62.txt', 'r') as f:
    content_list = [line.strip() for line in f.readlines()]
    letters = content_list[0].split()
    #print(letters)
    p = len(letters)
    table = {}
    for i in range(p):
        for j in range(p):
            value =  int(content_list[i+1].split()[j+1])
            table[letters[i] + letters[j]] = value
f.close()

with open('rosalind_ba5e.txt', 'r') as f:
    seq_1 = f.readline().strip()
    seq_2 = f.readline().strip()
    k = len(seq_1)
    m = len(seq_2)

f.close()

    
seq = [[0 for k in range(m+1)] for i in range(k+1)] 
search = [[0]*m for i in range(k)] 


for i in range(k+1):
    seq[i][0] = - sigma* i  

seq[0]  = [- sigma*j for j in range(m+1)]


for i in range(1, k+1):
    for j in range(1, m+1):
        t = table[seq_1[i-1] + seq_2[j-1]]
        a = [seq[i-1][j]-sigma, seq[i][j-1] - sigma, t + seq[i-1][j-1]]
        seq[i][j] = max(a)

        if seq[i][j] == seq[i-1][j] - sigma:
            search[i-1][j-1] = '/'
        
        elif seq[i][j] == seq[i-1][j-1] + t:
            search[i-1][j-1] = '|'


print(seq[-1][-1])
seq1, seq2 = LongestCommonSubsequence(search, seq_1, seq_2, sigma=5)
#assert ''.join(seq1[::-1]) == 'PLEASANTLY'
#assert ''.join(seq2[::-1]) == '-MEA--N-LY'
#print('Right')
print(''.join(seq1[::-1]))
print(''.join(seq2[::-1]))


#8