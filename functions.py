from scipy.special import binom
from helper import *
import sys
import itertools
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
    T = np.zeros((n, m), dtype=int)
    
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

    return [T[-1][-1], sol_1(x,y,T)]

def prog_dyn_from_file(path):
    x,y = processFile(path)
    return prog_dyn(x,y)
