def CyclopeptideSequencing(Spectrum, Spectrum_best_match = []):
    k =len(Spectrum)
    Peptides = [[]]
    while Peptides:
        Peptides = Expand(Peptides)
        Peptides = [pep for pep in Peptides if 
                    all(x in Spectrum for x 
                        in sorted(LinearSpectrum(pep)))]
        for Peptide in Peptides:
            if (Spectrum[-1] if k>0 else 0) == sum([aa for aa in Peptide]):
                if Spectrum == sorted(CycloSpectrum(Peptide)):
                    Spectrum_best_match.append(Peptide)
    r = ["-".join(str(x) for x in l) 
         for l in reversed(Spectrum_best_match)]
    
    return ' '.join(r)

aa_table = {57: 'G', 
            71: 'A', 
            87: 'S', 
            97: 'P',
            99: 'V', 
            101: 'T', 
            103: 'C', 
            113: 'I/L',
            114: 'N', 
            115: 'D', 
            128: 'K/Q', 
            129: 'E',
            131: 'M', 
            137: 'H', 
            147: 'F', 
            156: 'R', 
            163: 'Y', 
            186: 'W'}

def Expand(Peptides):
    k = len(Peptides)
    res = []
    for i in range(k):
        for a in aa_table.keys():
            res.append(Peptides[i] + [a])
    return res

def CycloSpectrum(Peptide):
    k = len(Peptide)
    prev = [0]
    for i in range(k):
        prev.append(prev[i] + Peptide[i])
    peptide_mass = sum([aa for aa in Peptide])
    
    cyclospec = [0]
    for i in range(k):
        for j in range(i+1, k + 1):
            cyclospec.append(prev[j]-prev[i])
            if j < k and i > 0:
                cyclospec.append(peptide_mass+ prev[i] - prev[j])
    return cyclospec

def LinearSpectrum(Peptide, masses=[]):
    p = len(Peptide)
    masses = [0]
    for i in range(p):
        masses.append(Peptide[i] + masses[i])
    res=[0] +[masses[j]-masses[i] for j in range(i+1, p + 1) 
                      for i in range(p)] 
    return res



r = []
with open('rosalind_ba4e.txt') as f:
    input_spectrum = [int(x) for x in f.readline().split(" ")]
f.close()
#CyclopeptideSequencing(input_spectrum) == test_str
print(CyclopeptideSequencing(input_spectrum))