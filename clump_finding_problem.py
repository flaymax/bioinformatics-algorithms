def clump_finding(Genome, k, L, t):
    
    frequentpatterns = set()
    clump = [0 for i in range(0, 4**k)]
    text = Genome[0:L]
    frequencyarray = compute_frequences(text, k)
    
    for i in range(0, 4**k):
        if frequencyarray[i] >= t:
            clump[i] = 1
            
    for i in range(len(Genome) - L + 1):
        firstpattern = Genome[i-1:i-1 + k]
        index = pattern_to_number(firstpattern)
        frequencyarray[index] -= 1
        lastpattern = Genome[i+L-k:i+L]
        index = pattern_to_number(lastpattern)
        frequencyarray[index] += 1
        if frequencyarray[index] >= t:
            clump[index] = 1
    
    for i in range(0, 4**k):
        if clump[i] == 1:
            pattern = number_to_pattern(i,k)
            frequentpatterns.add(pattern)
    return frequentpatterns


def compute_frequences(Text, k): 
    
    frequencyarray = [0 for i in range(0, 4**k)]
    for i in range(0, len(Text) - k +1):
        Pattern = Text[i:i+k]
        j=pattern_to_number(Pattern)
        frequencyarray[j]+= 1
    return frequencyarray


def pattern_to_number(Pattern):
    
    if Pattern=='':
        return 0
    symbol = Pattern[-1]
    Prefix = Pattern[:-1]
    return 4 * pattern_to_number(Prefix) + symbol_to_number(symbol)


def number_to_pattern(index, k): 
    
    if k == 1:
        return number_to_symbol(index)
    prefIndex = index // 4
    r = index % 4
    symbol = number_to_symbol(r)
    PrefixPattern = number_to_pattern(prefIndex, k-1)
    return PrefixPattern + symbol



def symbol_to_number(symbol): 
    
    if symbol == 'A':
        return 0
    elif symbol == 'C':
        return 1
    elif symbol == 'G':
        return 2
    else:
        return 3
    
    
def number_to_symbol(number):
    
    if number == 0:
        return 'A'
    elif number == 1:
        return 'C'
    elif number == 2:
        return 'G'
    else:
        return 'T'



with open('file.txt') as f:
    Genome = f.readline()
    Data = f.readline()
f.close()

Genome = Genome.replace('\n','')
k, L, t = [int(i) for i in Data.replace('\n', '').split(' ')]


a = clump_finding(Genome, k, L, t)



for i in a:
    print(i, end=' ')