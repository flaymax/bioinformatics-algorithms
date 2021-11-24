def main_function(P):
    cnt = 0
    shift_P = [0]
    shift_P += [i for i in P]
    
    for i in range(1, len(P)+1):
        if not (shift_P[i] - shift_P[i-1] == 1):
            cnt += 1
    print(cnt)
    
with open('rosalind_ba6b.txt') as f:
    Data = f.readline()
    Data = [int(i) for i in Data[1:len(Data)-1].split(' ')]
f.close()

main_function(Data)