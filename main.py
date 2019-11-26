import sys
import time
from functions import *

if __name__ == '__main__':
    argsLength = len(sys.argv)
    resourceImported = False

    try:
        import resource
        resourceImported = True
    except ImportError:
        pass

    if argsLength >= 2:
        if sys.argv[1] == '-p': # needs length to be 4: the last 2 are the sequence and number of gaps to add
            if argsLength == 4:
                generateBar(sys.argv[2], sys.argv[3], show=True)
            else:
                print(usage(sys.argv[1]))
                raise SystemExit
        
        # fix the ambigious shit here (switch -f condition to first)

        elif sys.argv[1] == '-dist':
            if argsLength == 4 and sys.argv[2] == '-f': # get data from file, and calculate distance
                time_start = time.perf_counter()
                print(dist_naif_from_file(sys.argv[3]))
                time_elapsed = (time.perf_counter() - time_start)

                if resourceImported:
                    memKb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0
                    print("Time and memory used respectively : %5.1f secs %5.1f KBytes" % (time_elapsed,memKb))
                else:
                    print("Time taken: %5.1f secs" % (time_elapsed))

            else:
                try:
                    print(dist_naif(sys.argv[2], sys.argv[3])) # calculate distance, data is provided through arguments
                except IndexError:
                    print('Maybe you want to calculate it providing the data from a file ? if so add -f option.')

        elif sys.argv[1] == '-dist1':
            if argsLength == 4 and sys.argv[2] == '-f': # get data from file, and calculate distance
                time_start = time.perf_counter()
                print(dist_1_from_file(sys.argv[3]))
                time_elapsed = (time.perf_counter() - time_start)

                if resourceImported:
                    memKb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0
                    print("Time and memory used respectively : %5.1f secs %5.1f KBytes" % (time_elapsed,memKb))
                else:
                    print("Time taken: %5.1f secs" % (time_elapsed))
            else:
                try:
                    print(dist_1(sys.argv[2], sys.argv[3])) # calculate distance, data is provided through arguments
                except IndexError:
                    print('Maybe you want to calculate it providing the data from a file ? if so add -f option.')
        
        elif sys.argv[1] == '-dyn':
            if argsLength == 4 and sys.argv[2] == '-f': # get data from file, and calculate distance
                time_start = time.perf_counter()
                print(prog_dyn_from_file(sys.argv[3]))
                time_elapsed = (time.perf_counter() - time_start)

                if resourceImported:
                    memKb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0
                    print("Time and memory used respectively : %5.1f secs %5.1f KBytes" % (time_elapsed,memKb))
                else:
                    print("Time taken: %5.1f secs" % (time_elapsed))
            else:
                try: # fix this -> failed case -> py main.py -dyn ACTG CCG
                    print(prog_dyn(sys.argv[2], sys.argv[3])) # calculate distance, data is provided through arguments
                except IndexError:
                    print('Maybe you want to calculate it providing the data from a file ? if so add -f option.')

        elif sys.argv[1] == '-align':
            if argsLength == 5:
                if representsInt(sys.argv[2]):
                    # if given 3 arguments as ints, generate 2 random sequence (1st and 3rd), the 2nd is the number of gaps to add
                    # to the 1st 
                    sys.argv[2] = int(sys.argv[2])
                    sys.argv[4] = int(sys.argv[4])
                    generateAlignments(getRandomSequence(sys.argv[2]), sys.argv[3], getRandomSequence(sys.argv[4]))
                    #generateAlignments('abc', sys.argv[2], 'df')
                else:
                    generateAlignments(sys.argv[2], sys.argv[3], sys.argv[4])

        else:
            print(usage())
