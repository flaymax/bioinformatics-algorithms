
def main_function(k,d,pairs):
    Text = ''
    for i in range(d):
        Text+=pairs[i + 1][0][-1]
        if i==d-1:
            Text+=pairs[0][1]
    for i in range(len(pairs[1:])):
        Text+=pairs[1:][i][1][-1]
    return print(pairs[0][0] + Text) #=='GACCGAGCGCCGGA'

with open("rosalind_ba3l.txt") as f:
    k, d = [int(i) for i in f.readline().strip().split()]
    pairs=[]
    for line in f.readlines():
        pairs.append(tuple(line.rstrip().split('|')))

main_function(k,d,pairs)