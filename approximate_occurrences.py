def looking_for_patterns(Pattern, Text, d):
    indices = []
    counter = 0 
    for i in range(0, len(Text) - len(Pattern) + 1):
        text_Pattern = Text[i:i+len(Pattern)]
        if HammingDistance(Pattern, text_Pattern) <= d:
            indices.append(i)
            counter += 1
    return indices

def HammingDistance(Pattern, Pattern1):
    count = 0
    for i in range(len(Pattern)):
        if Pattern[i]!=Pattern1[i]:
            count+=1
    return count

with open('rosalind_ba1h.txt') as f:
    Pattern = f.readline()
    Text = f.readline()
    d = f.readline()
f.close()

Pattern = Pattern.replace('\n','')
Text = Text.replace('\n','')
d = int(d.replace('\n',''))
a = looking_for_patterns(Pattern,Text,d)

for i in a:
    print(i, end=' ')
