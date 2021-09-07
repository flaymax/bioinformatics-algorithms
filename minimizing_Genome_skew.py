def minimizing_the_skew(Genome):
    
    current_min = 0
    count_g = 0
    count_c = 0
    indices = set()
    
    for i in range(len(Genome)):
        
        if Genome[i] == 'G':
            count_g+=1
        elif Genome[i] == 'C':
            count_c+=1
            
        if current_min > count_g - count_c:
            indices = set()
            indices.add(i+1)
            current_min = count_g - count_c
        elif current_min == count_g - count_c:
            indices.add(i+1)
            current_min = count_g - count_c
            
    return indices

with open('rosalind_ba1f.txt') as f:
    Genome = f.readline()
    
f.close()

a = minimizing_the_skew(Genome)

for i in a:
    print(i, end=' ')