import sys
import time
from functions import *

if __name__ == '__main__':
    argsLength = len(sys.argv)
    resourceImported = False

    try:
        import resource
        resourceImported = True # resource is in Linux only
    except ImportError:
        pass

    if argsLength >= 2:
        if sys.argv[1] == '-p': # needs length to be 4: the last 2 are the sequence and number of gaps to add
            if argsLength == 4:
                generateBar(sys.argv[2], sys.argv[3], show=True)
            else:
                print(usage(sys.argv[1]))
                raise SystemExit
        
        elif sys.argv[1] == '-f' and argsLength == 4:
            if sys.argv[2] == '-dist': # get data from file, and calculate distance using recursive algo
                time_start = time.perf_counter()
                print(dist_naif_from_file(sys.argv[3]))
                time_elapsed = (time.perf_counter() - time_start)

                if resourceImported:
                    memKb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0
                    print("Time and memory used respectively : %5.1f secs %5.1f KBytes" % (time_elapsed,memKb))
                else:
                    print("Time taken: %5.1f secs" % (time_elapsed))

            elif sys.argv[2] == '-dist1': # get data from file, and calculate distance using iteratif algo
                time_start = time.perf_counter()
                print(dist_1_from_file(sys.argv[3]))
                time_elapsed = (time.perf_counter() - time_start)

                if resourceImported:
                    memKb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0
                    print("Time and memory used respectively : %5.1f secs %5.1f KBytes" % (time_elapsed,memKb))
                else:
                    print("Time taken: %5.1f secs" % (time_elapsed))


            elif sys.argv[2] == '-dyn': # get data from file -> calculate distance and an optimal alignment
                time_start = time.perf_counter()
                print(prog_dyn_from_file(sys.argv[3]))
                time_elapsed = (time.perf_counter() - time_start)

                if resourceImported:
                    memKb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0
                    print("Time and memory used respectively : %5.1f secs %5.1f KBytes" % (time_elapsed,memKb))
                else:
                    print("Time taken: %5.1f secs" % (time_elapsed))


        elif sys.argv[1] == '-align':
            if argsLength == 5:
                allInts = True

                for i in range(2,5):
                    if not reprensentsInt(sys.argv[i]):
                        allInts = False
                        break

                if allInts :
                    # if given 3 arguments as ints, generate 2 random sequence (1st and 3rd), the 2nd is the number of gaps to add
                    # to the 1st 
                    sys.argv[2] = int(sys.argv[2])
                    sys.argv[4] = int(sys.argv[4])
                    generateAlignments(getRandomSequence(sys.argv[2]), sys.argv[3], getRandomSequence(sys.argv[4]))
                else:
                    generateAlignments(sys.argv[2], sys.argv[3], sys.argv[4])

        elif sys.argv[1] == '-dist': # calculate the distance using the recursive algo
            if argsLength == 4:
                time_start = time.perf_counter()
                print(dist_naif(sys.argv[2], sys.argv[3]))
                time_elapsed = (time.perf_counter() - time_start)

                if resourceImported:
                    memKb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0
                    print("Time and memory used respectively : %5.1f secs %5.1f KBytes" % (time_elapsed,memKb))
                else:
                    print("Time taken: %5.1f secs" % (time_elapsed))
            else:
                print(usage(sys.argv[1]))

        elif sys.argv[1] == '-dist1': # calculate distance using the iteratif algo
            if argsLength == 4:
                time_start = time.perf_counter()
                print(dist_1(sys.argv[2], sys.argv[3]))
                time_elapsed = (time.perf_counter() - time_start)

                if resourceImported:
                    memKb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0
                    print("Time and memory used respectively : %5.1f secs %5.1f KBytes" % (time_elapsed,memKb))
                else:
                    print("Time taken: %5.1f secs" % (time_elapsed))
            else:
                print(usage(sys.argv[1]))

        elif sys.argv[1] == '-dyn': # calculate distance and an optimal alignment
            if argsLength == 4:
                time_start = time.perf_counter()
                print(prog_dyn(sys.argv[2], sys.argv[3]))
                time_elapsed = (time.perf_counter() - time_start)

                if resourceImported:
                    memKb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0
                    print("Time and memory used respectively : %5.1f secs %5.1f KBytes" % (time_elapsed,memKb))
                else:
                    print("Time taken: %5.1f secs" % (time_elapsed))
            else:
                print(usage(sys.argv[1]))

        else:
            print(usage())
