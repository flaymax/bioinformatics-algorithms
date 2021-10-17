def main_function(k_mers, k):
    n = len(k_mers) + k - 1
    kmers_flags = [0 for i in k_mers] # flags array
    pref = set(i[:k - 1] for i in k_mers)
    suf = set(i[1:] for i in k_mers)
    curr_k_mer = 0
    
    i=0
    while 1:
        if k_mers[i][:k - 1] not in suf:
            curr_k_mer = i
            break
        i+=1
    
    kmers_flags[curr_k_mer] = 1 
    ans = k_mers[curr_k_mer]
    
    while sum(kmers_flags)!= len(kmers_flags):
        for i in range(len(k_mers)):
            if (k_mers[i][:k - 1] != ans[-k+1:] or 
                kmers_flags[i] or False):
                continue
            kmers_flags[i] = 1 # flag up
            if (k_mers[i][1:] not in pref 
                and sum(kmers_flags)!= len(kmers_flags)):
                kmers_flags[i] = 0
                continue
            ans += k_mers[i][-1]
    
    return print(ans)
#################################################################


with open("rosalind_ba3h.txt") as f:
    kmers = []
    k = int(f.readline().replace('\n', ''))
    while 1:
        line = f.readline().replace('\n', '')
        if not line:
            break
        kmers.append(line)
f.close()
main_function(kmers, k)