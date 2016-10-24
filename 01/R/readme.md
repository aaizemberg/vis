# R

```R
p1p <- read.table(
"https://raw.githubusercontent.com/aaizemberg/acn/gh-pages/01/data/poblacion.tsv?token=ABkLBxx44AWpu16rvxHb8EdTcpi96OrFks5YF3rRwA%3D%3D",
  sep="\t", header=TRUE, encoding="UTF-8")

dim(p1p)
head(p1p)
tail(p1p)
summary(p1p)

p1p

   poblacion
1   15625084
2    3308876
3    3194537
4    2890151
5    1738929
6    1448188
7    1235994
8    1214441
9    1101593
10   1055259
11    992595
12    874006
13    681055
14    673307
15    638645
16    551266
17    530162
18    509108
19    432310
20    367828
21    333642
22    318951
23    273964
24    127205

p1p[0]
p1p[1]
p1p[2]
# p1p[2] = p1p["poblacion"]
p1p["poblacion"]

> min(p1p["poblacion"])
[1] 127205

> max(p1p["poblacion"])
[1] 15625084

> summary(p1p["poblacion"])
   poblacion       
 Min.   :  127205  
 1st Qu.:  489908  
 Median :  777530
 Mean   : 1671546  
 3rd Qu.: 1289042  
 Max.   :15625084  

Mediana: 777530, esta entre 681055 y 874006

https://en.wikipedia.org/wiki/Median#/media/File:Finding_the_median.png

plot(p1p["poblacion"])

boxplot(p1p["poblacion"]) 

fix(p1p)

x <- c(1, 2, 10, 100)

x <- c(15625084, 3308876, 3194537, 2890151, 1738929, 1448188, 1235994, 1214441, 1101593, 1055259, 992595, 874006, 681055, 673307, 638645, 551266, 530162, 509108, 432310, 367828, 333642, 318951, 273964, 127205)

plot(x)
```
