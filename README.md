# DNAlgo
Ce projet porte sur un problème de génomique : l'alignement de séquences. <br><br>
D'un point de vue biologique, il s'agit de mesurer la similarité entre deux séquences d'ADN, que l'on
voit simplement comme des suites de nucléotides. Cela permet, lorsqu'un nouveau génome est séquencé, de
comparer ses gênes à ceux de génomes précédemment séquencés, et de repérer ainsi des homologies, c'est-à-
dire les ressemblances dues au fait que les deux espèces ont un ancêtre commun qui leur a transmis ce gêne,
même si ce gêne a pu subir des mutations (évolutions) au cours du temps. <br><br>
D'un point de vue informatique, les séquences de nucléotides sont vues comme des mots sur l'alphabet
{ A,T,G,C } et l'on est ramené à deux problèmes d'algorithmique du texte : le calcul de la distance d'édition
entre deux mots quelconques et la production d'un alignement réalisant cette distance. Pour chacun de ces
problèmes, on s'intéresse d'abord à un algorithme naïf, puis à un algorithme de programmation dynamique.
Enfin, on utilise la méthode diviser pour régner pour améliorer la complexité spatiale de ces algorithmes. En
ouverture, on s'intéresse à un problème légèrement différent : l'alignement local de séquences.
