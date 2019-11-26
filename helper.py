import random
from os.path import isfile

def toString(List): 
    return ''.join(List) 

def validPermutation(permutation, orderToBeRespected):
    i = 0 # iterate over the orderString
    j = 0 # iterate over the permutation chars
    
    while i < len(orderToBeRespected):
        try:
            while permutation[j] != orderToBeRespected[i]:
                j += 1

            i += 1
            j += 1
            # if the inner loop finished, it means they are the same, go to the next char to check.
        except IndexError:
            return False
        
    # if the outer loop is done with no Index error, means we're good
    return True

def find(s, ch): 
    '''
        params: s -> string, ch -> character
        return: all indexes of ch in s
    '''
    return [i for i, ltr in enumerate(s) if ltr == ch]

def getRandomSequence(length):
    if not representsInt(length) or int(length) < 0:
        print('Bad k gaps to add argument, ensure that you give a positive int')
        raise SystemExit

    length = int(length)
    chars = ['A', 'T', 'G', 'C']
    s = ""
    n = len(chars)

    for i in range(0, length):
        s += chars[random.randint(0, n-1)]
    
    return s

def representsInt(s): # used in argv
    try:
        int(s)
        return True
    except ValueError:
        return False

def csub(x, y):
    # x and y are chars, this returns the cost of sub
    if x == y:
        return 0
    if (x == 'A' and y == 'T') or (x == 'T' and y == 'A') or (x == 'G' and y == 'C') or (x == 'G' and y == 'C'):
        return 3
    if x == '−' or y == '−': # this case is added to get the implementation correct. (can be interpreted as cIns or cDel)
        return 2
    else:
        return 4

def usage():
    pass

def processFile(path):
    '''
        Extracting sequences from the file
    '''
    try:
        f = open(path, 'r')
        f.readline()
        f.readline()
        s1 = f.readline()
        s2 = f.readline()
        
        s1 = s1.replace(' ', '')
        s1 = s1.replace('\n', '')
        s2 = s2.replace(' ', '')
        s2 = s2.replace('\n', '')
        
        return [s1, s2]
        f.close()

    except FileNotFoundError:
        print(path + ' Not found. Exiting...')
        raise SystemExit
    except IOError:
        print('Need the privileges to read the file: ' + path)
        raise SystemExit
