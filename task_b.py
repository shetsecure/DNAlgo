import os
import time
import matplotlib.pyplot as plt
from functions import *
from timeout_decorator.timeout_decorator import TimeoutError

__DIR__ = 'Instances_genome/'

def solve():
    path = ''
    errorFile = open('errorLog.txt', 'w')

    # the following two lists will be used to plot the graph
    cpu_time = []
    first_seq_len = []
    i = 0
    for f in os.listdir(__DIR__):

        path = __DIR__ + f
        if i == 3:
            print(i)
            path = 'Instances_genome/Inst_0100000_76.adn'
            i += 1
        print(path)
        s1, s2 = processFile(path)

        time_start = time.perf_counter()

        try:
            ans = prog_dyn_from_file(path)
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
        
        time_elapsed = (time.perf_counter() - time_start) * 1000
        
        first_seq_len.append(len(s1))
        cpu_time.append(time_elapsed)
        i += 1

    errorFile.close()
    #print(cpu_time)
    #print(first_seq_len)
    x = first_seq_len
    y = cpu_time

    plt.plot(first_seq_len, cpu_time, 'r*')
    #plt.xticks(np.arange(min(first_seq_len), max(first_seq_len)+1, 50.0))

    for i_x, i_y in zip(x, y):
        plt.text(i_x, i_y, '({}, {:10.4f})'.format(i_x, i_y))
    plt.show()


if __name__ == '__main__':
    solve()
