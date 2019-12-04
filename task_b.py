import time
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functions import prog_dyn
from helper import processFile, getInstancesFiles
from timeout_decorator.timeout_decorator import TimeoutError

__DIR__ = 'Instances_genome/'

def solve():
    path = ''
    errorFile = open('errorLog_task_b.txt', 'w')

    # the following two lists will be used to plot the graph
    cpu_time = []
    first_seq_len = []

    total_time = time.perf_counter()
    sorted_files = getInstancesFiles(__DIR__, sort=True) # sort the list of files (key = len(s1))
    i = 0

    for f in sorted_files:
        path = f
        print(path)
        s1, s2 = processFile(path)

        time_start = time.perf_counter()

        try:
            ans = prog_dyn(s1, s2)
            i += 1
            print(ans)
        except MemoryError:
            print('mem error')
            continue
        except TimeoutError:
            msg = 'Timed out the following instance: ' + path
            print(msg)
            errorFile.write(msg + '\n')
            continue
        except KeyboardInterrupt:
            break
        
        time_elapsed = (time.perf_counter() - time_start) # in seconds
        
        first_seq_len.append(len(s1))
        cpu_time.append(time_elapsed)

    errorFile.close()
    
    print("It took " + str(time.perf_counter() - total_time) + " secs to process all the " + str(i) + " instances.")

    x = np.array(first_seq_len)
    y = np.array(cpu_time)

    d = {'|x|' : x, 'time (s)' : y}
    data = pd.DataFrame(d)
    
    sns.set(style='darkgrid')
    sns.lineplot(x='|x|', y='time (s)', data=data)
    plt.title('PROG_DYN: courbe de consommation de temps CPU en fonction de la taille |x|')
    plt.savefig('task_b.png', dpi=300)
    plt.show()
    
    with open('plotted_values_task_b.txt', 'a+') as f:
        f.write('\n')
        f.write(str(list(x)))
        f.write('\n')
        f.write(str(list(y)))
        f.write('\n\n')


if __name__ == '__main__':
    solve()


