import os
import time
import matplotlib.pyplot as plt
from functions import *
from timeout_decorator.timeout_decorator import TimeoutError

__DIR__ = 'Instances_genome/'

def solve():
    path = ''
    errorFile = open('errorLog_task_a.txt', 'w')

    # the following two lists will be used to plot the graph
    cpu_time = []
    first_seq_len = []

    path = 'Instances_genome/Inst_0000500_8.adn'
    print(path.split('/')[-1] + " -> ", end='')
    s1, s2 = processFile(path)

    time_start = time.perf_counter()

    try:
        ans = dist_naif_from_file(path)
        time_elapsed = (time.perf_counter() - time_start)
        print("distance d'edition: " + str(ans) + ". -> Calculated in %.4f seconds." % (time_elapsed))
    except MemoryError:
        print('mem error')
    except TimeoutError:
        msg = 'Timed out the following instance: ' + path
        print(msg)
        errorFile.write(msg + '\n')
    except KeyboardInterrupt:
        raise SystemExit
    
    
    errorFile.close()

    x = first_seq_len
    y = cpu_time

    plt.plot(first_seq_len, cpu_time, 'r*')
    #plt.xticks(np.arange(min(first_seq_len), max(first_seq_len)+1, 50.0))

    for i_x, i_y in zip(x, y):
        plt.text(i_x, i_y, '({}, {:10.4f})'.format(i_x, i_y))

    plt.savefig('plot_task_a.png')

    plt.show()


if __name__ == '__main__':
    solve()
