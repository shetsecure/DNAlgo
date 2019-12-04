from functions import *

print('Executing DIST_2 on : Instances_genome/Inst_0050000_6.adn')
s1,s2 = processFile('Instances_genome/Inst_0050000_6.adn')
print('|x| = ', len(s1))
dist_2(s1,s2)
