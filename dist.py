from functions import dist_1, dist_2
from helper import processFile
import pdb

if __name__=='__main__':
    s1,s2 = processFile('Instances_genome/Inst_0000015_76.adn')
    print(dist_2(s1,s2))
