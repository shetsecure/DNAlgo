from scipy.special import binom
from helper import *
import sys
import itertools
import timeout_decorator
import numpy as np

def generateBar(sequence, kGaps, show = False):
    if not representsInt(kGaps) and not isinstance(kGaps, int):
        print("Bad argument for how many gaps to add.")
        return False
    
    kGaps = int(kGaps)
    assert(kGaps >= 0)

    sequenceBar = sequence + '−' * int(kGaps)
    uniq = set()
    allPermutations = list(itertools.permutations(list(sequenceBar)))

    for permutation in allPermutations:
        if validPermutation(permutation, sequence):
            uniq.add(toString(permutation))

    if show:
        print("Predicted answer : " + str(binom(len(sequenceBar), kGaps)))
        print("Constructed " + str(len(uniq)) + " permutations.")
        print(uniq)
    
    return uniq

def generateAlignments(seq1, kGaps, seq2): 
    '''
    generate alignments given 2 sequences and k the number of gaps to add to the first sequence.
    '''
    n, m = len(seq1), len(seq2)
    print(seq1 + ' -> n = ' + str(n))
    print(seq2 + ' -> m = ' + str(m))
    print('Number of gaps to add to ' + seq1 + ' is ' + kGaps + ' -> k = ' + kGaps)
    kGaps = int(kGaps)

    if kGaps > m:
        print("Can't make alignments with these data. The following condition is violated: n+k <= n+m")
        raise SystemExit

    number_of_gaps2 = len(seq1) + kGaps - len(seq2)
    print('Number of gaps to add to ' + seq2 + ' is n + k -m = ' + str(number_of_gaps2))
    if (number_of_gaps2 < 0):
        print('Cant generate alignements with this configuration. ')
        raise SystemExit

    uniq1 = generateBar(seq1, kGaps)
    uniq2 = generateBar(seq2, number_of_gaps2)
    
    # converting sets to lists to make it iterable
    uniq1 = list(uniq1)
    uniq2 = list(uniq2)

    #print(uniq1)
    #print(uniq2)

    print("All possible combinations: " + str(len(uniq1) * len(uniq2)))
    allPossibleAlignements = []

    for i in range(0, len(uniq1)):
        for j in range(0, len(uniq2)):
            gaps1 = find(uniq1[i], '−') # get all indexes of gaps in the element from the first list
            gaps2 = find(uniq2[j], '−') # get all indexes of gaps in the element from the second list
            commonGap = any(check in gaps1 for check in gaps2)
            
            if not commonGap:
                allPossibleAlignements.append((uniq1[i], uniq2[j]))
    
    print("But there are only " + str(len(allPossibleAlignements)) + " alignements")
    print("Predicted answer: " + str(binom(n+kGaps, kGaps) * binom(n, number_of_gaps2)))
    print(allPossibleAlignements)

    #for al in allPossibleAlignements:
    #    print(al[0])
    #    print(al[1])
    #    print()

########################################### IMPLEMENTATIONS ###########################################

def dist_naif_rec(x, y, i, j, c, dist):
    '''
        x et y deux mots,
        i un indice dans [0..|x|], j un indice dans [0..|y|],
        c le coût de l'alignement de (x[1..i] , y[1..j])
        dist le coût du meilleur alignement de (x, y) connu avant cet appel
    '''
    #assert(i >= 0 and i < len(x))
    #assert(j >= 0 and j < len(y))
    #assert(c >= 0)
    #assert(isinstance(x, str) and isinstance(y, str))
    cdel = cins = 2

    if i == len(x)-1 and j == len(y)-1:
        if (c < dist):
            dist = c

    else:
        if (i < len(x) - 1 and j < len(y) - 1):
            dist = dist_naif_rec(x, y, i+1, j+1, c + csub(x[i], y[j]), dist) # why x[i+1] ???
        
        if (i < len(x)):
            dist = dist_naif_rec(x, y, i+1, j, c + cdel, dist)

        if (j < len(y)):
            dist = dist_naif_rec(x, y, i, j+1, c + cins, dist)
            
    return dist

def dist_naif(x, y):
    return dist_naif_rec(x, y, 0, 0, 0, sys.maxsize)

def dist_naif_from_file(path):
    s = processFile(path)
    return dist_naif(s[0], s[1])


def dist_1(x, y, wholeTable=False): # Question 12
    assert (isinstance(x, str) and isinstance(x, str))
    x = x.replace(' ', '')
    y = y.replace(' ', '')
    
    # adding empty string to both sequence to make indexing below simpler
    x = ' ' + x
    y = ' ' + y 
    n, m = len(x), len(y)

    cdel = cins = 2
    try:
        T = np.zeros((n, m), dtype=int)
    except MemoryError:
        print('Couldnot load this instance to RAM. Too large !')
        return False
    
    for j in range(1, m):
        T[0, j] = j * cins

    for i in range(1, n):
        T[i, 0] = i * cdel

    for i in range(1, n):
        for j in range(1, m):
            T[i, j] = min(T[i-1, j-1] + csub(x[i], y[j]), T[i, j-1] + cins, T[i-1, j] + cdel)


    if wholeTable:
        return T

    return int(T[n-1, m-1]) # converting to int to not pass the assertion below (in sol_1)

def dist_1_from_file(path):
    s = processFile(path)
    return dist_1(s[0], s[1])


def sol_1(x, y, T): # question 16
    '''
        returns the optimal alignment for (x,y) given the matrix T ( we are relying on T to be true )
        params: - x : string
                - y : string
                - T : numpy matrix or 2d list
    '''
    assert( isinstance(x, str) and isinstance(y, str))
    assert( type(T).__module__ == np.__name__ or isinstance(T, list))
    x = ' ' + x
    y = ' ' + y 

    cins = cdel = 2

    n, m = len(T), len(T[0])
    xBar = yBar = ""
    
    i = n-1
    j = m-1

    while i > 0 or j > 0:
        if j > 0 and (T[i][j] == (T[i][j-1] + cins)):
            # go left only
            xBar = "−" + xBar
            yBar = y[j] + yBar
            j -= 1
        elif i > 0 and (T[i][j] == (T[i-1][j] + cdel)):
            # go up only
            xBar = x[i] + xBar
            yBar = "−" + yBar
            i -= 1
        elif T[i][j] == (T[i-1][j-1] + csub(x[i], y[j])):
            # go up and left
            xBar = x[i] + xBar
            yBar = y[j] + yBar
            i -= 1
            j -= 1
    
    return (xBar, yBar)

@timeout_decorator.timeout(600)
def prog_dyn(x, y):
    '''
        @param: 
            - x : string
            - y : string

        return a list ( 1st element is min distance, followed by the tuple (xBar, yBar) ) 
    '''
    T = dist_1(x, y, wholeTable=True)
    #distance = T[-1][-1]
    #xBar, yBar = sol_1(x,y,T)
        

    if T is not False:
        return [T[-1][-1], sol_1(x,y,T)]
    

def prog_dyn_from_file(path):
    x,y = processFile(path)
    ans = prog_dyn(x,y)

    if ans is not None:
        return ans
    
    # if the caller is solver then catch memError there in order to add the error to log file
    if sys._getframe().f_back.f_code.co_name == 'solver': 
        raise MemoryError # fix this later 


@timeout_decorator.timeout(600)
def dist_2(x, y): # question 20, spacial complexity in O(m)
    assert (isinstance(x, str) and isinstance(x, str))
    x = x.replace(' ', '')
    y = y.replace(' ', '')
    
    # adding empty string to both sequence to make indexing below simpler
    x = ' ' + x
    y = ' ' + y 
    n, m = len(x), len(y)
    cdel = cins = 2

    first_col = [x for x in range(0, 2*m, 2)] # 2 is cins
    second_col = [0] * m

    for i in range(1, n):
        second_col[0] = cdel * i

        for j in range(1, m):
            second_col[j] = min( first_col[j-1] + csub(x[i], y[j]), second_col[j-1] + cins, first_col[j] + cdel)

        first_col = second_col
        second_col = [0] * m

    return first_col[-1]

def dist_2_from_file(path):
    s = processFile(path)
    return dist_2(s[0], s[1])

# question 21
def mot_gaps(k):
    assert(isinstance(k, int))
    assert(k >= 0)

    return ''.join('−' * k)

# question 22
def align_lettre_mot(x, y):
    #assert(isinstance(x, str) and len(x) == 1)
    assert(isinstance(x, str) and len(x) >= 0)
    assert(isinstance(y, str) and len(y) > 0)
    
    cins = cdel = 2

    u = ""
    v = ""

    minimum = sys.maxsize
    pos = 0

    if len(x) == 1:
        for i in range(0, len(y)):
            tmp = csub(x[0], y[i])
            if tmp < cins + cdel and tmp < minimum:
                pos = i
                minimum = tmp

        if minimum == sys.maxsize:
            u = mot_gaps(len(y)) + x
            v = y + '−'
        else:
            u = mot_gaps(pos) + x + mot_gaps(len(y) - 1 - pos)
            v = y

        return (u,v)
    else:
        for i in range(0, len(y)):
            tmp = csub(x[i], y[0])
            if tmp < cins + cdel and tmp < minimum:
                pos = i
                minimum = tmp

        if minimum == sys.maxsize:
            u = x + '−'
            v = mot_gaps(len(y)) + y
        else:
            u = x
            v = mot_gaps(pos) + y + mot_gaps(len(y) - 1 - pos)

        return (u,v)


# question 25
def coupure(x, y):
    n, m = len(x), len(y)
    x = ' ' + x
    y = ' ' + y

    iEtoile = n/2
    cins = cdel = 2

    d1 = [0] * (m+1)
    d2 = [0] * (m+1)
    coup1 = [0] * (m+1) 
    coup2 = [0] * (m+1)

    for i in range(0, m+1):
        d1[i] = i * cins
        coup1[i] = i

    
    for i in range(1, n+1):
        d2[0] = i * cdel

        for k in range(1, m+1):
            tmp = min(d2[k-1] +cins, d1[k] + cdel, d1[k-1] + csub(x[i], y[k]))
            d2[k] = tmp

            if i > iEtoile:
                if tmp == (d2[k-1] + cins):
                    coup2[k] = coup2[k-1]

                else:
                    if tmp == (d1[k] + cdel):
                        coup2[k] = coup1[k]
                    else:
                        coup2[k] = coup1[k-1]

        d1 = d2
        d2 = [0] * (m+1)
        
        if i > iEtoile:
            coup1 = coup2
            coup2 = [0] * (m+1)

    return int(coup1[m])

# question 24
@timeout_decorator.timeout(600)
def sol_2(x, y):
    n, m = len(x), len(y)
    
    if n == 0:
        return (mot_gaps(m), y)
    if m == 0:
        return (x, mot_gaps(n))

    if m == 1 or n == 1:
        return align_lettre_mot(x,y)

    j = coupure(x,y)
    i = int(n/2)

    x, y = sol_2(x[0:i], y[0:j]), sol_2(x[i:n], y[j:m])
    
    return (x[0]+y[0], x[1]+y[1])
