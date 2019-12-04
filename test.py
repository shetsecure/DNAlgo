from functions import *
import os

__DIR__ = 'Instances_genome/'

if __name__ == '__main__':

    all_files = (os.path.join(basedir, filename) for basedir, dirs, files in os.walk(__DIR__) for filename in files)
    sorted_files = sorted(all_files, key = os.path.getsize)
    
    for f in sorted_files:
        path = f
        s1, s2 = processFile(path)

        d1_ans = dist_1(s1,s2)
        d2_ans = dist_2(s1,s2)

        try:
            if(d1_ans != d2_ans):
                print(path)
                print("d1_ans = " + str(d1_ans) + " d2_ans = " + str(d2_ans))
                print('A7chitih')

        except MemoryError:
            print('mem error')
            continue
        except TimeoutError:
            msg = 'Timed out the following instance: ' + path
            print(msg)
            continue
        except KeyboardInterrupt:
            break
