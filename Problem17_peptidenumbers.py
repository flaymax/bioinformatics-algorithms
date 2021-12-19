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

ma = aa_table.keys()
def main(mass, masses={}):
    # base
    if mass >= 57:
        if mass in masses:
            return masses[mass], masses
    elif mass == 0:
        return 1, masses
    elif mass < 57:
        return 0, masses
    

    cnt = 0
    #recursion
    for weight in ma:
        k, masses = main(mass-weight, masses=masses)
        cnt += k
        
    masses[mass] = cnt
    return cnt, masses


res, mass_list_res = main(1409)
print(res)
#print(res == test)