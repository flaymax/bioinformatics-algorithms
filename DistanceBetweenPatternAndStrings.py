def HammingDistance(Pattern, Pattern1):
    count = 0
    for i in range(len(Pattern)):
        if Pattern[i]!=Pattern1[i]:
            count+=1
    return count

def DistanceBetweenPatternAndStrings1(Pattern, DNA_strings):
    dist = 0
    k = len(Pattern)
    for DNA_string in DNA_strings:
        min_dist = HammingDistance(Pattern, DNA_string[:k])
        for i in range(len(DNA_string)-k+1):
            tmp_dist = HammingDistance(Pattern, DNA_string[i: i + k])
            if min_dist > tmp_dist:
                min_dist = tmp_dist
        dist += min_dist
    return dist

with open('rosalind_ba2h.txt') as f:
    Pattern = f.readline().replace('\n', '')
    DNA_strings = f.readline().split()
f.close()

DistanceBetweenPatternAndStrings1(Pattern, DNA_strings)