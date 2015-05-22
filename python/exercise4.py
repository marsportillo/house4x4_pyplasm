from pyplasm import *
from larcc import *
import exercise3
def rgb2color(rgb):
	r,g,b = rgb
	nr = float(r)/255
	nb = float(b)/255
	ng = float(g)/255
	return [nr,nb,nb]
city = exercise3.area

woodRails_color= rgb2color([112,85,69])
glass = [0.1,0.2,0.47,1,  0,0,0,0.48,  2,2,2,1, 0,0,0,1, 50]
wall_color = rgb2color([149,143,140])

rail = CUBOID([0.2,50,0.2])
rails = STRUCT(NN(2) ([rail,T(1)(1)]))
rails = T(3)(0.1)(rails)
rails = T(1)(0.5)(rails)
rails = COLOR(GRAY)(rails)
woodRail = CUBOID([0.9,0.5,0.1])
woodRails = STRUCT(NN(50)([woodRail,T(2)(1)]))
woodRails = T(1)(0.6)(woodRails)
woodRails = T(3)(0.15)(woodRails)
woodRails = COLOR(woodRails_color)(woodRails)

wallRailRoad = CUBOID([0.3,50,1])
wallRailRoad = T([1,3])([5,0.2])(wallRailRoad)
wallRailRoad = COLOR(wall_color)(wallRailRoad)
railRoad = STRUCT([rails,woodRails])
railRoads = STRUCT(NN(2) ([railRoad,T(1)(2)]))

streetLine = CUBOID([0.5,0.8])
streetlines = STRUCT(NN(50)([streetLine,T(2)(1)]))
streetlines = T(1)(12)(streetlines)
streetlines = T(3)(0.3)(streetlines)

rodlamps = larRod([0.07,3])([48,2])
rodlamps = STRUCT(MKPOLS(rodlamps))
rodlamps = COLOR(BLACK)(rodlamps)
ball = larBall(0.2)([18,36])
ballLamps = STRUCT(MKPOLS(ball))
ballLamps = T(3)(2.9)(ballLamps)
ballLamps = COLOR(YELLOW)(ballLamps)
lamp = STRUCT([rodlamps,ballLamps])
lamps = STRUCT(NN(10)([lamp,T(2)(5)]))
lamps = T([1,2])([7,0.5])(lamps)
#VIEW(lamps)
lamp = T([1,2])([2,6.5])(lamp)

backBus = CUBOID([0.02,4,2.5])
backBus = MATERIAL(glass)(backBus)

latoBus = CUBOID([1.5,0.02,2.5])
latoBus = MATERIAL(glass)(latoBus)

latiBus = STRUCT(NN(2)([latoBus,T(2)(4)]))
tettoBus = CUBOID([1.5,4,0.05])
tettoBus = T(3)(2.5)(tettoBus)

bench = CUBOID([0.6,3.8,0.03])
bench = T([2,3])([0.1,0.65])(bench)
busStop = STRUCT([backBus,latiBus,tettoBus,bench])

busStop = R([1,2])(PI)(busStop)
busStop = T([1,2])([20,25])(busStop)
#VIEW(busStop)

rodtree = larRod([0.2,3])([48,2])
rodtree = STRUCT(MKPOLS(rodtree))
rodTreeColor = rgb2color([76,22,10])
rodtree = COLOR(rodTreeColor)(rodtree)

treeChioma = larBall(1.2)([18,36])
treeChioma = STRUCT(MKPOLS(treeChioma))
treeChioma = T(3)(2.9)(treeChioma)


treeChiomaColor = rgb2color([4,186,24])
treeChioma = COLOR(treeChiomaColor)(treeChioma)
tree = STRUCT([rodtree,treeChioma])
trees = STRUCT(NN(4)([tree,T(2)(5)]))
trees = T([1,2])([18.5,1.5])(trees)

parkingLine = CUBOID([4,0.2])
parkingLines = STRUCT(NN(6)([parkingLine,T(2)(3)]))

parkingLines = T([1,2,3])([20,1,0.3])(parkingLines)
parkingLineX = CUBOID([0.2,15.2])
parkingLineX = T([1,2,3])([24,1,0.3])(parkingLineX)
parking = STRUCT([parkingLines,parkingLineX])

busIrod =larRod([0.04,3])([48,2])
busIrod = STRUCT(MKPOLS(busIrod))
busIrod = COLOR(YELLOW)(busIrod)
busIrod = T(2)(0.05)(busIrod)
busICube = CUBOID([0.8,0.1,1])
busICube = COLOR(YELLOW)(busICube)
busICube = T(3)(2)(busICube)

busInfo = STRUCT([busIrod,busICube])
busInfo = T([1,2])([18,26])(busInfo)
#VIEW(busInfo)

smallCylinder = larRod([1.5,0.3])([48,2])
smallCylinder = STRUCT(MKPOLS(smallCylinder))
largePizza = larPizza([1,0.1])([8,48])
largePizza = STRUCT(MKPOLS(largePizza))
largePizza = T(3)(0.2)(largePizza)

bench = STRUCT([smallCylinder,largePizza])
bench = COLOR(GRAY)(bench)
bench = T([1,2,3])([25,25,1])(bench)

wallsea = CUBOID([2,50,1])
wallsea = T(1)(40)(wallsea)

palo = larRod([0.07,1.2])([48,2])
palo = STRUCT(MKPOLS(palo))
palizzata = STRUCT(NN(2) ([palo,T(1)(1.8)]))

palizzata = COLOR(rodTreeColor)(palizzata)
# palizzata = R([2,3])(PI/2)(palizzata)
palizzata = R([1,2])(PI/2)(palizzata)
palizzata = T([1,2])([43,40])(palizzata)
palizzata = STRUCT(NN(10) ([palizzata,T(1)(1.5)]))
passerella = CUBOID([15,2.3,0.3])
passerella = T([1,2,3])([42,39.8,1.2])(passerella)
passerella = COLOR(rodTreeColor)(passerella)
gradino = CUBOID([0.5,2,0.3])
gradino = T([1,2,3])([41.5,40,1])(gradino)
gradino = COLOR(rodTreeColor)(gradino)
gradino2 = CUBOID([0.5,50,0.6])
gradino2 = T([1,3])([39.5,0.1])(gradino2)
gradino3 = CUBOID([0.5,50,0.3])
gradino3 = T([1,3])([39,0.1])(gradino3)
ponticello = STRUCT([palizzata,passerella,gradino,gradino2,gradino3])

cespuglio = larBall(0.4)([18,36])
cespuglio = STRUCT(MKPOLS(cespuglio))
cespuglio = T([1,2,3])([0.5,0.5,1])(cespuglio)
cespuglio = COLOR(treeChiomaColor)(cespuglio)
vaso = CUBOID([1,1,1])
diff = CUBOID([0.8,0.8,0.2])
diff = T([1,2,3])([0.1,0.1,0.8])(diff)
diff = COLOR(GREEN)(diff)
vaso = DIFFERENCE([vaso,diff])
vaso = STRUCT([vaso,diff,cespuglio])
vasi = STRUCT(NN(5)([vaso,T(2)(4)]))
vasi = T([1,2])([18,30])(vasi)
vasi = COLOR(wall_color)(vasi)


city = STRUCT([city,streetlines,parking,railRoads,wallRailRoad,lamps,busStop,trees,busInfo,bench,wallsea,ponticello,vasi])
VIEW(city)