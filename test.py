
from functions import sol_2, prog_dyn, dist_2
from helper import processFile, getInstancesFiles
__DIR__ = 'Instances_genome/'

sorted_files = getInstancesFiles(__DIR__, sort=True) # sort the list of files (key = len(s1))

for f in sorted_files:
    s1,s2 = processFile(f)

    ans1 = prog_dyn(s1,s2)
    ans1 = ans1[1]
    ans2 = sol_2(s1,s2)

    if dist_2(ans1[0], ans1[1]) != dist_2(ans2[0], ans2[1]):
        print('A7chitih')
        print(f)
        print(ans1)
        print(ans2)

