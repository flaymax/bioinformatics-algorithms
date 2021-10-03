def HammingDistance(Pattern, Pattern1):
    count = 0
    for i in range(len(Pattern)):
        if Pattern[i]!=Pattern1[i]:
            count+=1
    return count

def Score(Motifs):
    
    curr_profile = Profile(Motifs)
    nucl = "ATGC"
    consensus = ''
    consensus = ''
    
    for i in range(len(curr_profile[0])):
        curr_array = [curr_profile[j][i] for j in range(4)]
        max_value = max(curr_array)
        max_i = curr_array.index(max_value)
        consensus += nucl[max_i]
    curr_score = 0
    
    for Motif in Motifs:
        curr_score += HammingDistance(Motif, consensus)
    return curr_score







def Profile(Motifs):
    
    profile = [[1. for i in range(len(Motifs[0]))] for j in range(4)]
    for Motif in Motifs:
        for i, nucleotide in enumerate(Motif):
            nucleotide_position = "ATGC".index(nucleotide)
            profile[nucleotide_position][i] += 1 / ((len(Motifs))*2)
    return profile





def max_prob_kmer(DNA, Profile, k):
    best_kmer = DNA[:k]
    max_prob = Probability(Profile, best_kmer)
    for i in range(len(DNA) - k + 1):
        k_mer = DNA[i: i + k]
        prob = Probability(Profile, k_mer)
        
        if prob > max_prob:
            max_prob = prob
            best_kmer = k_mer
        #elif:
            
            #prob
    return best_kmer


def Probability(Profile, k_mer):
    Prob = 1
    for i, nucleotide in enumerate(k_mer):
        nucleotide_position = "ATGC".index(nucleotide)
        Prob *= Profile[nucleotide_position][i]
    return Prob


#probability('TCGGG', pro)




def Greedy_Motif_Search(DNA, k, t):
    best_motifs = list()
    
    for Pattern in DNA:
        best_motifs.append(Pattern[:k])
    #print(best_motifs)
    best_score = Score(best_motifs)
    for i in range(len(DNA[0])-k+1):
        curr_motifs = [DNA[0][i: i + k]]
        
        for j in range(1, t):
            curr_profile = Profile(curr_motifs)
            curr_motifs.append(max_prob_kmer(DNA[j], curr_profile, k))
        curr_score = Score(curr_motifs)
        
        if curr_score < best_score:
            best_score = curr_score
            best_motifs = curr_motifs
    return best_motifs


with open('rosalind_ba2e (1).txt') as f:
    Data = f.readline()
    k, t = [int(i) for i in Data.replace('\n', '').split(' ')]
    DNA = [f.readline().replace('\n', '') for i in range(t)]
f.close()

a  = Greedy_Motif_Search(DNA, k, t)
for i in a:
    print(i)