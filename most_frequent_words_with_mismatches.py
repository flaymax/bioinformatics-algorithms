def looking_for_patterns(Pattern, Text, d): 
    counter = 0 
    for i in range(0, len(Text) - len(Pattern) + 1):
        text_Pattern = Text[i:i+len(Pattern)]
        if HammingDistance(Pattern, text_Pattern) <= d:
            counter += 1
    return counter

def HammingDistance(Pattern, Pattern1): 
    count = 0
    for i in range(len(Pattern)):
        if Pattern[i]!=Pattern1[i]:
            count+=1
    return count

def neigbors(Pattern, d): 
    nucleotides = {'A' , 'C', 'G', 'T'}
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return nucleotides
    
    neighborhood = set()
    suffix_neighbors = neigbors(Pattern[1:], d)
    for string in suffix_neighbors:
        if HammingDistance(Pattern[1:], string) < d:
            for nucleotide in nucleotides:
                neighborhood.add(nucleotide + string)
        else:
            neighborhood.add(Pattern[0] + string)
    return neighborhood

def main_function(Text, k, d):
    frequent_patterns = set()
    frequency_array = [0 for i in range(0, 4**k)]
    close = [0 for i in range(0, 4**k)]
    
    for i in range(0, len(Text) - k + 1):
        neighborhood = neigbors(Text[i:i+k], d)
        for pattern in neighborhood:
            index = pattern_to_number(pattern)
            close[index] = 1

    
    for i in range(0, 4**k):
        if close[i]==1:
            pattern = number_to_pattern(i,k)
            frequency_array[i] = looking_for_patterns(pattern,Text,  d)
    maxCount = max(frequency_array)
    
    for i in range(0, 4**k):
        if frequency_array[i] == maxCount:
            pattern = number_to_pattern(i,k)
            frequent_patterns.add(pattern)
    
    return frequent_patterns

with open('rosalind_ba1i.txt') as f:
    Text = f.readline()
    Data = f.readline()
f.close()


Text = Text.replace('\n','')
k, d = [int(i) for i in Data.replace('\n', '').split(' ')]


a = main_function(Text, k, d)
for i in a:
    print(i, end=' ')