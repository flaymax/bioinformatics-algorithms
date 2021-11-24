def printing(revers):
    for itter in revers:
        for i in range(len(itter)):
            #print(itter)
            if itter[i] <= 0:
                itter[i] = str(itter[i])
            else:
                itter[i] = '+' + str(itter[i])
    
        tmp_itter = str(' '.join(itter))
        print('(' + tmp_itter + ')')

def greedy_sorting(P):
    approxReversalDistance = []
    for k in range(len(P)):
        while not (P[k] == k + 1):
            idx = k
            while (P[idx] != -(k+1)) and (P[idx] != k+1):
                idx += 1
            rev = P[k:idx+1]
            P[k : idx+1] = [-i for i in rev[::-1]]
            approxReversalDistance.append(list(P))
    return approxReversalDistance


with open('rosalind_ba6a.txt') as f:
    Data = f.readline()
    Data = [int(i) for i in Data[1:len(Data)-1].split(' ')]
f.close()

reversal = greedy_sorting(Data)
printing(reversal)