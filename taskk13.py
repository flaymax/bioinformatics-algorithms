def main_function(k, dist, graph):
    
    
    while 1:  

        keys = []
        vals = []
        
        for key, value in zip(graph.keys(), graph.values()):
            if value in list(graph.keys()):
                curr_pair = graph[value]
                keys.append((key[0] + value[0][-1], key[1] + value[1][-1]))
                vals.append((value[0] + curr_pair[0][-1], value[1] + curr_pair[1][-1]))
        dist -= 1
        graph = dict(zip(keys, vals))
        if dist==0:
            break
        
        
        
    graph = {key[0] + key[1]: value[0] + value[1] 
             for key, value in zip(graph.keys(), graph.values())}

    while len(graph) != 1:
        keys = []
        vals = []
        for key, value in zip(graph.keys(), graph.values()):
            if value in list(graph.keys()):
                keys.append(key + value[-1])
                vals.append(value[0] + graph[value])
        graph = dict(zip(keys, vals))
        
        
            
            
    return print(keys[0] + vals[0][-1])



with open("rosalind_ba3j.txt") as f:
    k, d = [int(i) for i in f.readline().strip().split()]
    graph = {}
    for line in f.readlines():
        l, r = line.strip().split('|')
        key = (l[:k-1], r[:k-1])
        val = (l[1:k], r[1:k])
        graph[key] = val
main_function(k,d+1,graph) # == 'GTGGTCGTGAGATGTTGA'