def looking_for_patterns(Text, k, d): 
    
    frequent_patterns = {}
    
    for i in range(len(Text)-k +1):
        pattern = Text[i:i+k]
        Pair = [pattern, find_reverse_complement(pattern)]
        for pat in Pair:
            neighborhood = neighbors(pat, d)
            
            for neighbor in neighborhood:
                if neighbor not in frequent_patterns:
                    frequent_patterns[neighbor] = 1
                else:
                    frequent_patterns[neighbor] += 1

    return frequent_patterns


def find_reverse_complement(pattern):
    replacing = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join(replacing.get(i) for i in reversed(pattern))


def HammingDistance(Pattern, Pattern1): 
    
    count = 0
    for i in range(len(Pattern)):
        if Pattern[i]!=Pattern1[i]:
            count+=1
    return count


def neighbors(Pattern, d): 
    nucleotides = {'A' , 'C', 'G', 'T'}
    
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return nucleotides
    
    neighborhood = set()
    suffix_neighbors = neighbors(Pattern[1:], d)
    
    for string in suffix_neighbors:
        if HammingDistance(Pattern[1:], string) < d:
            for nucleotide in nucleotides:
                neighborhood.add(nucleotide + string)
        else:
            neighborhood.add(Pattern[0] + string)
    return neighborhood


def main_function(Text, k, d):
    
    frequent_patterns = []
    Patterns = looking_for_patterns(Text, k, d)
    maxCount = sorted(Patterns.values(), reverse=True)[0]
    
    for pattern in Patterns:
        if maxCount == Patterns[pattern]:
            frequent_patterns.append(pattern)
    return frequent_patterns


with open('rosalind_ba1j (1).txt') as f:
    Text = f.readline()
    Data = f.readline()
f.close()

Text = Text.replace('\n','')
k, d = [int(i) for i in Data.replace('\n', '').split(' ')]


#Text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
#k = 4
#d = 1
a = main_function(Text, k, d)

for i in a:
    print(i, end=' ')