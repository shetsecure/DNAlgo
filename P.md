### PROJET LU3IN003

#### <u>PARTIE THEORIQUE</u>





##### Question 1

​	On montre que ($\overline{x}*\overline{u},\overline{y}*\overline{v}$) est l'alignement de ($x*u,y*v$) .

​			- $π(\overline{x}*\overline{u})=x*u$  car   $π(\overline{x}*\overline{u})=π(x)*π(u)$ 

​			- $π(\overline{y}*\overline{v})=y*v$

​			- $|\overline{x}*\overline{u}|=|\overline{y}*\overline{v}|$  car $|\overline{x}|*|\overline{u}|=|\overline{y}|*|\overline{v}|$

​            - $∀i ∈ [1..|\overline{x}*\overline{u}|],(\overline{x}*\overline{u})_i \ne −\ ou\ (\overline{y}*\overline{v})_i \ne −$ .  Comme $\overline{x}\ et\ \overline{y}$  ne présentent pas de   gap à la même postion (resp.$\overline{u}\ et\ \overline{v}$)  ,  et $\overline{x}*\overline{u}$  comme le mot $\overline{u}$ est concaténé après  $\overline{x}$ (resp.$\overline{y}*\overline{v}$) et $|\overline{x}|=|\overline{y}|$  (resp. $|\overline{u}|= |\overline{v}|$ ) . Donc  $\overline{x}*\overline{u},\overline{y}*\overline{v}$ ne présentent pas de gap à la même position.

Donc, par définition, ($\overline{x}*\overline{u},\overline{y}*\overline{v}$)  l'alignement de ($x*u,y*v$) .	

 

##### Question 2

​	La longueur maximale est $n+m$ .



##### Question 3

​	C'est une combinaison de choisir k éléments dans n + k éléments donc il y a $C_{n+k}^n$ mots possibles.

 

##### Question 4

​	Une fois k gaps ajoutés, pour y c'est une combinaison de n + k − m gaps sur n places possbles car on ne peut que ajouter des gaps dans y sur des emplacement où x a le alphabet mais pas le −, donc c'est $C_{n+k}^n$ D'après la question 3, $C_{n+k}^n$ mots possibles pour x, donc en total $C_{n+k}^n * C_n^{n+k-m}$ possibles pour (x, y). 





##### Question 5

​	Pour chaque k, compléxité temporelle en O($C_{n+k}^n * C_n^{n+k-m}$ ) = O($n^m$) 

​		
$$
C_{n+k}^n * C_n^{n+k-m} = \frac{(n+k)!}{n!k!} * \frac{n!}{(m-k)!(n+k-m)!}\\ 
\Rightarrow \frac{1*2*3...n(n+1)(n+2)...(n+k)}{(1*2*3...*n)k!} * \frac{1*2*3...(n+k-m)(n+k-m+1)...n}{1*2*3...(n+k-m)(m-k)!}\\
\Rightarrow \frac{(n+1)(n+2)..(n+k)}{k!} * \frac{(n+k-m+1)...n}{（m-k）!}\\
\Rightarrow n^k*n^{m-k} = n^m
$$


et on l'accumule pour k allant de 0 à n + m donc la compléxité temporelle est exponentielle



##### Question 6

​	Pour chaque k, $C_{n+k}^n * C_n^{n+k-m}$  possibilités à stocker, donc la compléxité spatiale est en O($n^m$)



### TACHE A

























##### Question 7

​	Si $\overline{u}_l$= − alors $\overline{v}_l$= − , en plus π($\overline{v}$) = $y_{[1..j]}$ donc en particulier π($\overline{v}_l$) = $y_{[j]}$ , donc $\overline{v}_l$ = $y_{[j]}$ 

De même si $\overline{v}_l$ = −, alors $\overline{u}_l$ = $x_{[i]}$ .  Si $\overline{u}_l$= − et $\overline{v}_l$= −, alors $\overline{u}_l$ =$x_{[i]}$  et $\overline{v}_l$ = $y_{[j]}$.



##### Question 8

​	$C(\overline{u},\overline{v})=$   $C(\overline{u}_{[1..l-1]},\overline{v}_{[1..l-1]})+C_{ins}$  si $\overline{u}_l= -$

​						 $C(\overline{u}_{[1..l-1]},\overline{v}_{[1..l-1]})+C_{del}$  si $\overline{v}_l= -$

​						 $C(\overline{u}_{[1..l-1]},\overline{v}_{[1..l-1]})+C_{sub}$  si $\overline{u}_l\ne -\ et\ \overline{v}_l\ne - $

##### Question 9

​	Soit ($\overline{u},\overline{v}$) l'alignement correspondant pour D(i, j) , et soit ses longeurs sont l,alors d'après la question 7 il n'y a que trois possibilités pour ($\overline{u}_l,\overline{v}_l$) : ( − , $y_{[j]}$) ,($x_{[i]}$ , − ) et ($x_{[i]}$ ,$y_{[j]}$). Si on est dans le cas ( − , $y_{[j]}$) , alors il reste à changer i caractères de x à j − 1 caractères de y et donc la distance vaut D(i, j − 1), donc D(i, j) = D(i, j − 1) + $c_{ins}$.

De même pour les deux autres cas. Puis on prend le minimum de ces trois valeurs. 

Donc D(i, j) = min(D(i, j − 1) + $c_{ins}$, D(i − 1, j) + $c_{del}$, D(i − 1, j − 1) + $c_{sub}$)

##### Question 10

​	D(0, 0) = 0, car il n'y a pas d'éléments qui besion de changer.

##### Question 11

​	D'après la question 9 comme i = 0 et i − 1 = −1 n'a pas de sens, donc on est toujours dans le cas D(i, j) = D(i, j − 1) + $c_{ins}$, donc D(0, j) = j ∗$c_{ins}$. De même D(i, 0) = i ∗ $c_{del}$.

##### Question 12



$$
Algorithm : DIST\_1\\

Entrée ：mot\ x\ et\ y\\

Sortie :  d\ (distance\ entre\ x\ et\ y)
$$


```pseudocode
n <- len(x)
m <- len(y)
D:tableau de taille[n][m]

for 0 =< i <= n do
	D[i][0] <- i*Cins
for 0 =< j <= m do
	D[0][j] <- j*Cdel
	
for 0 =< i <= n do
	for 0 =< j <= m do
		D[i][j] <- min(D[i][j − 1] + Cins, D[i − 1][j] + Cdel, D[i − 1][j − 1] + Csub)

return D[n][m]

```



##### Question 13

​	La compléxité spatiale est en O(n ∗ m)



##### Question 14

​	La compléxité temporelle est en O(n ∗ m) Car la première boucle  vaut O(n) et la deuxième boucle vaut O(m), la troisième boucle fait en totale O(n ∗ m). Donc la compléxité temporelle est en O(n ∗ m).



##### Question 15

​	On va montrer  "Si j  >  0 et D( i , j ) = D( i , j − 1) + $c_{ins}$, alors ∀(s,t) ∈ $Al^*$ ( i , j − 1),( $\overline{s} · −$,$\overline{t}·y_j$ ) ∈  $Al^*$ ( i, j )"

On a d(( $\overline{s} · −$,$\overline{t}·y_j$ ) ) = d(( $\overline{s}$, $\overline{t}$ ))+$c_{ins}$ par construction. ( $\overline{s}$, $\overline{t}$) ∈ Al∗ (i, j−1), donc d(( $\overline{s}$, $\overline{t}$))) = D(i, j−1). Donc on a d(($\overline{s} · −$,$\overline{t}·y_j$  )) = D( i , j − 1 ) + $c_{ins}$ = D( i ,  j )  par hypothèse. Donc ($\overline{s} · −$,$\overline{t}·y_j$   ) ∈ $Al^*$ (i, j) par la définition de $Al^*$(i, j)



##### Question 16



$$
Algorithm : SOL\_1 \\
Entrée ：mot x et y , tableau de D\\
Sortie :  Un\ alignment\ minimal\ de\ x\ y -> (\overline{u}, \overline{v})
$$


```pseudocode
i <- len(x)
j <- len(y)
cpt  <- -1
tmpu <- listvide []
tmpv <- listvide []
u <- []
v <- []

Tant que i!= 0 and j!= 0
	cpt++
	Si j > 0 and D[i][j] == D[i][j-1] + Cins 
		tmpu <- tmpu + ['-']
		tmpv <- tmpv + [y[j − 1]]
		j--
	Sinon	
		Si i > 0 and D[i][j] == D[i−1][j] + Cdel 
			tmpu <- tmpu + [x[i − 1]]
			tmpv <- tmpv + ['-']
			i--
		Sinon
			tmpu <- tmpu + [x[i − 1]]
			tmpv <- tmpv + [y[j − 1]]
			i--
			j--

Tant que cpt >= 0
	u <- u + tmpu[cpt]
	v <- v + tmpv[cpt]
	cpt--
	
return u,v


```





##### Question 17

​	Compléxité temporelle de SOL_1 est en O(m + n), car la boucle fait au plus m + n fois. Donc la compléxité temporelle pour la combinaison de DIST_1 et SOL_1 est en O(n ∗ m)

##### Question 18

​	Compléxité spatiale pour SOL_1 est en O(m + n), car on stocke au plus n + m éléments dans le tmpu et tmpv dans l'algorithme. Donc la compléxité spatiale pour la combinaison de DIST_1 et SOL_1 est en O(n ∗ m)



### TACHE B



##### Question 19

​	Pour chaque étape, on ne utilise que des donnés  à la ligne courante et la ligne précedente du tableau D.



##### Question 20


$$
Algorithm : DIST\_2 \\
Entrée ：mot\ x\ et\ y\\
Sortie : d\ (distance\ entre\ x\ et\ y)
$$

```pseudocode
n <- len(x)
m <- len(y)
D1 <- listvide[]
D2 <- listvide[]

for 0 <= i <= m
	D1[i] <- i*cins
for 1 <= j <= n
	D2[0] <- j*Cdel
	for 1 <= k <= m
		D2[k] <- min(D2[k-1] + cins, D1[k] + cdel, D1[k − 1] + csub)
	D1 <- D2
	D2 <-[]

return D1[m]
```





### TACHE C



























##### Question 21

$$
Algorithm : mot\_gaps \\
Entrée : int\ k\\ 
Sortie : mot\ consitué\ avec\ k\ gaps
$$

```pseudocode
x <- listvide[]
for 0 < i <= k 
 	x <- x + ['-']
return x
```



##### Question 22

$$
Algorithm : aligne\_lettre\_mot \\
Entrée : mot\ x\ et\ y\ \ \  avec\ |x|=1\ |y|=m \ (m>0) \\
Sortie : Un\ alignment\ minimal\ de\ x\ y -> (\overline{u}, \overline{v})
$$



```pseudocode
u <- listvide[]
v <- listvide[]
int min <- +infini  ex:100000
int tmp
int postion

for 0 <= i < m
	tmp <- Csub(x[0],y[i])
	Si tmp < Cins + Cdel and tmp < min 
		postion <- i
		min <- tmp

Si min == +infini 
	u <- mot_gaps(m) + x
	v <- y+['-']
Sinon
	u <- mot_gaps(position) + x + mot_gaps(m − 1 − position)
	v <- y
return u,v
```



##### Question 23

​	$(\overline{s},\overline{t})= (B A L,RO-)$

​    $(\overline{u},\overline{v})= (L O N -,- - N D)$	

Mais $(\overline{s}*\overline{u},\overline{t}*\overline{v})=(BALLON-,RO---ND)$  n'est pas un alignement optimal, car on a un autre alignment $(BALLON-,---ROND)$ qui peut avoir un coût ( 17 ) plus petit que $(\overline{s}*\overline{u},\overline{t}*\overline{v})$ (22)



##### Question 24

$$
Algorithm : SOL\_2 \\
Entrée : mot\ x\ et\ y\\
Sortie : Un\ alignment\ minimal\ de\ x\ y -> (\overline{u}, \overline{v})
$$

```pseudocode
n <- len(x)
m <- len(y)
Si n == 0
	return (mot_gaps(m),y)
Si m == 0
	return (x,mot_gaps(n))
Si m == 1 and n == 1
	return aligne_lettre_mot(x,y)

j <- coupure(x,y)
i <- n/2

return SOL_2(x[0:i],y[0:j])+SOL_2(x[i+1:n],y[j+1:m])
```



##### Question 25

$$
Algorithm : coupure \\
Entrée : mot\ x\ et\ y\\
Sortie : J*
$$

```pseudocode
D1 <- listvide[]
D2 <- listvide[]
Coup1 <- listvide[]
Coup2 <- listvide[]
n <- len(x)
m <- len(y)
ietoile <- n/2
int tmp

for 0 <= j <= m
	D1[j] <- j* Cins
	Coup1[j] <- j
for 1 <= i <= n
	D2[0] <- i* Cdel
	Coup2[0] <- 0
	for 1 <= k <= m
		tmp =  min(D2[k − 1] + cins, D1[k] + cdel, D1[k − 1] + csub)
		D2[k] <- tmp
		Si i > ietoile
			Si tmp == D2[k-1] + Cins
				Coup2[k] <- Coup2[k-1]
			Sinon
            	Si tmp == D1[k] + Cdel
            		Coup2[k] <- Coup1[k]
            	Sinon
            		Coup2[k] <- Coup1[k-1]
    D1 <- D2
    D2 <- []
    Coup1 <- Coup2
    Coup2 <- []
    Coup2[0] <- 0
            		
	
return Coup1[m]
```



##### Question 26

​	O(m) .  Même compléxité spatiale que DIST_2 qui utilise  des tableaux de taille m.

##### Question 27

​	O(mlog(n)). Car on a  deux appels récursifs dan l'algo et chaque appel  en  log(n) , et avec Coupure qui en O(m) , donc en total O(mlog(n))

#### Question 28

​	O(n ∗ m). Car La première boucle vaut O(m) et la deuxième vaut O(n ∗ m).



### TACHE D





##### Question 29

​	SOL_1 en O(m + n)

​	SOL_2 en O(m * n)

​	