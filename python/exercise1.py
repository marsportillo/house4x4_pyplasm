from larcc import *
from pyplasm import *
def rgb2color(rgb):
	r,g,b = rgb
	nr = float(r)/255
	nb = float(b)/255
	ng = float(g)/255
	return [nr,nb,nb]
V0 = [
[0,4],[4,4],[4,0],[0,0],[1.65,4],[1.65,1.7],[1.6,1.7],[1.6,3.65],[0,3.65],
[0,3.4],[0.3,3.4],[0.3,1.1],[0,1.1],[2.35,4],[4,0.75],
[3.7,0.75],[3.7,3.65],[2.45,3.65],[2.45,2.65],[2.35,2.65],[3.7,0.4],
[4,0.4],[2.4,0],[2.4,2],[2.5,2],[2.5,0.3],[3.7,0.3],[1.65,0],[1.65,0.3],
[1.3,0.3],[1.3,1.25],[1.65,1.25],[1.65,1.35],[0.85,1.35],[0.85,1],
[0.95,1],[0.95,1.25],[1.35,1.25],[1.35,0.3],[0.4,0.3],[0.4,0.4],[0,0.4],
[0.85,1.8],[0.95,1.8],[0.95,3.15],[0.85,3.15],[2.45,0.3],[2.35,0.3],[2.35,3.65],[1.65,3.65]]

FV0 = [[29,30,31,32,33,34,35,36,37,38,29],[23,24,46,47,23],[17,18,19,48,17],[5,6,7,49,5],[42,43,44,45,42]]

#floor0 = STRUCT(AA(POLYLINE)([[V0[v] for v in cell] for cell in FV0]))

#VIEW(floor0)

V1 = [
[0,3.4],[0.3,3.4],[0.3,1.1],[0,1.1],[0,0],[1.65,0],
[1.65,0.3],[0.3,0.3],[0.3,0.4],[0,0.4],[2.4,0],[4,0],[4,2],[3.7,2],
[3.7,0.3],[2.4,0.3],[0.85,1.8],[0.95,1.8],[0.95,3.15],[0.85,3.15],
[0,4],[4,4],[4,2.7],[3.7,2.7],[3.7,3.7],[1.6,3.7],[1.6,1.25],[1.5,1.25],
[1.65,3.7],[0,3.7],[1.65,0.15],[2.4,0.15],[2.4,-0.75],[1.65,-0.75]]
FV1 = [[16,17,18,19,16],[25,26,27,28,25]]

#floor1 = STRUCT(AA(POLYLINE)([[V1[v] for v in cell] for cell in FV1]))
#VIEW(floor1)
# VF1 = [[0,0],[4,0],[1.65,3.7],[1.65,1.25],[0.3,1.25],[0.3,3.65],[0,3.65],[0,3.95]]
# FV1 = [[0,1,2,3,4,5,6,7,0]]

# floor1 = STRUCT(MKPOLS([VF1,FV1]))

#VIEW(floor1)
V2 = [
[0,0],[0.3,0],[0.3,0.4],[0,0.4],[0,3.4],[0.3,3.4],[0.3,1.1],[0,1.1],
[0,4],[1.65,4],[1.65,1.7],[1.6,1.7],[1.6,3.65],[0,3.65],
[2.4,4],[4,4],[4,2.7],[3.7,2.7],[3.7,3.7],[2.4,3.7],[3.7,2],[4,2],[4,0],
[3.7,0],[0.85,1.8],[0.95,1.8],[0.95,3.15],[0.85,3.15],[1.65,3.65]]
FV2 = [[24,25,26,27,24],[10,11,12,28,10]]

V3 = [
[0,4],[1.65,3.65],[1.65,1],[1.55,1],[1.55,3.65],[0,3.65],
[0,3.4],[0.3,3.4],[0.3,1.1],[0,1.1],[0,0],
[0.3,0],[0.3,0.4],[0,0.4],[2.35,4],[4,4],
[4,3],[3.7,3],[3.7,3.7],[2.35,3.7],[4.5,3.15],[4.8,3.15],
[4.8,1.85],[4.5,1.85],[4.5,1.15],[4.8,1.15],
[4.8,-0.8],[4.5,-0.8],[0.8,1.7],[1.1,1.7],[1.1,-0.8],
[0.8,-0.8],[0.6,1.8],[1,1.8],[1,3.1],[0.6,3.1]]

FV3 = [[32,33,34,35,32],[1,2,3,4,1]]

F3V = [[0.8,0],[0.8,-0.8],[4.8,-0.8],[4.8,3.2],[4,3.2],[4,0]]
FV3V = [[0,1,2,3,4,5,0]]

#VIEW(floor3)

F35V = [[0,0],[0.8,0],[0.8,4],[0,4],[0,3.2],[4,3.2],[4,4]]
FV35V = [[0,1,2,3,0],[3,4,5,6,3]]

#VIEW(floor3m)
V4 = [[0.8,3.2],[4.8,3.2],[4.8,-0.8],[0.8,-0.8]] 
FV4 = [[0,1,2,3,0]]

upstairs = CUBOID([1.35,2.58,0.3])
upstairs = T([1,2])([0.3,1.1])(upstairs)

floor0 = CUBOID([4,4,0.3])

floor1 = CUBOID([4,4,0.3])
floor1 = DIFFERENCE([floor1,upstairs])
floor1 = T(3)(2.1)(floor1)


floor2 = CUBOID([4,4,0.3])
floor2 = DIFFERENCE([floor2,upstairs])
floor2 = T(3)(4.2)(floor2)

floor3ext = STRUCT(MKPOLS([F3V,FV3V]))
floor3ext = (PROD([floor3ext, Q(0.3)]))
floor3cube = CUBOID([4,4,0.3])
floor3cube = DIFFERENCE([floor3cube,upstairs])
#VIEW(floor3cube)
floor3 = STRUCT([floor3cube,floor3ext])
floor3 =T(3)(6.3)(floor3)

floor3m = STRUCT(MKPOLS([F35V,FV35V]))
floor3m = T(3)(8.4)(PROD([floor3m, Q(0.3)]))

floor4 = CUBOID([4,4,0.3])
floor4 = T([1,2,3])([0.8,-0.8,10.1])(floor4)


def face2edge(CV):
	edges = AA(sorted)(CAT([TRANS([face[: -1],face[1:]]) for face in CV]))
	edges = AA(str)(edges)
	edges = set(edges)
	edges = AA(eval)(edges)
	return edges 

EV0 = face2edge(FV0)
EV1 = face2edge(FV1)
EV2 = face2edge(FV2)
EV3 = face2edge(FV3)
EV4 = face2edge(FV4)

modelEdges0 = (V0,EV0)
modelEdges1 = (V1,EV1)
modelEdges2 = (V2,EV2)
modelEdges3 = (V3,EV3)
modelEdges4 = (V4,EV4)

V0 = AA(LIST) ([0.,2.1,4.2,6.3,8.4,10.6])


C00V = [[0]]

C01V = [[1]]

C02V = [[2]]

C03V = [[3]]

C04V = [[4]]

modelFloor0 = V0,C00V
modelFloor1 = V0,C01V
modelFloor2 = V0,C02V
modelFloor3 = V0,C03V
modelFloor4 = V0,C04V


mod1D0 = larModelProduct([modelEdges0,modelFloor0])
mod1D1 = larModelProduct([modelEdges1,modelFloor1])
mod1D2 = larModelProduct([modelEdges2,modelFloor2])
mod1D3 = larModelProduct([modelEdges3,modelFloor3])
mod1D4 = larModelProduct([modelEdges4,modelFloor4])

f0 = STRUCT(MKPOLS(mod1D0))
f1 = STRUCT(MKPOLS(mod1D1))
f2 = STRUCT(MKPOLS(mod1D2))
f3 = STRUCT(MKPOLS(mod1D3))
f4 = STRUCT(MKPOLS(mod1D4))

f3 = DIFFERENCE([f3,upstairs])
building = STRUCT([f0,f1,f2,f3,f4])

C0V = [[0,1]]
C1V = [[1,2]]
C2V = [[2,3]]
C3V = [[3,4]]

modelWall0 = V0,C0V
modelWall1 = V0,C1V
modelWall2 = V0,C2V
modelWall3 = V0,C3V

mod11D0 = larModelProduct([modelEdges0,modelWall0])
mod11D1 = larModelProduct([modelEdges1,modelWall1])
mod11D2 = larModelProduct([modelEdges2,modelWall2])
mod11D3 = larModelProduct([modelEdges3,modelWall3])

f03d = STRUCT(MKPOLS(mod11D0))
f13d = STRUCT(MKPOLS(mod11D1))
f23d= STRUCT(MKPOLS(mod11D2))
f33d = STRUCT(MKPOLS(mod11D3))

building_color = rgb2color([111,110,98])
f03d = COLOR(building_color)(f03d)
f13d = COLOR(building_color)(f13d)
f23d = COLOR(building_color)(f23d)
f33d = COLOR(building_color)(f33d)
floor0 = COLOR(building_color)(floor0)
floor1 = COLOR(building_color)(floor1)
floor2 = COLOR(building_color)(floor2)
floor3 = COLOR(building_color)(floor3)
floor3m = COLOR(building_color)(floor3m)
floor4 = COLOR(building_color)(floor4)
building = STRUCT([floor0,floor1,floor2,floor3,floor3m,floor4,f03d,f13d,f23d,f33d])
bulding = T(2)(0.8)(building)
VIEW(bulding)