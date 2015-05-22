from larcc import *
from pyplasm import *
import exercise1
def rgb2color(rgb):
	r,g,b = rgb
	nr = float(r)/255
	nb = float(b)/255
	ng = float(g)/255
	return [nr,nb,nb]
wall_color = rgb2color([149,143,140])
door_color = rgb2color([39,40,34])
glass = [0.1,0.2,0.47,1,  0,0,0,0.48,  2,2,2,1, 0,0,0,1, 50]
#East-base
VeastBase = [[0,0],[4,0],[0,6.25],[3.2,6.25],[4,6.25],[3.2,8.7],[4,8.7]]
FVeastBase = [[0,1,4,2,0],[3,4,5,6,3]]

eastBase = STRUCT(MKPOLS([VeastBase,FVeastBase]))
eastBase = COLOR(wall_color)(eastBase)
eastBase = (PROD([eastBase, Q(0.3)]))
windowBaseS = CUBOID([0.75,1.9,0.3])
windowBaseS = T([1,2])([1.625,2.2])(windowBaseS)
windowBaseS = MATERIAL(glass)(windowBaseS)

lineX1b = CUBOID([3.7,0.1])
lineX1b = T([1,2])([0.3,5.4])(lineX1b)
lineX2b = CUBOID([0.5,0.1])
lineX2b = T([1,2])([3.5,6.25])(lineX2b)
lineY1b = CUBOID([0.1,1.85])
lineY1b = T([1,2])([2,4.35])(lineY1b)

windowBaseS1 = CUBOID([3.8,1.75,0.3])
windowBaseS1 = T([1,2])([0.25,4.5])(windowBaseS1)
windowBaseS1 = MATERIAL(glass)(windowBaseS1)

windowBaseS2 = CUBOID([0.86,2.05,0.3])
windowBaseS2 = T([1,2])([3.2,6.25])(windowBaseS2)
windowBaseS2 = MATERIAL(glass)(windowBaseS2)
door = CUBOID([0.75,1.9,0.3])
door = T([1,2])([1.625,0.1])(door)
door = COLOR(door_color)(door)
eastBase = DIFFERENCE([eastBase,door,windowBaseS,windowBaseS1,windowBaseS2])
eastBase = STRUCT([eastBase,windowBaseS,windowBaseS1,windowBaseS2,door,lineX1b,lineY1b,lineX2b])
#VIEW(eastBase)

#East-Cube
VeastCube = [[0,0],[4,0],[4,4.2],[0,4.2]]
FVeastCube = [[0,1,2,3,0]]
windowCubeS = CUBOID([3.65,3.65,0.3])
lineX = CUBOID([0.1,3.6])
lineX = T([1,2])([2,0.3])(lineX)
lineY = CUBOID([3.6,0.1])
lineY = T([1,2])([0.3,2])(lineY)
windowCubeS = T([1,2])([0.25,0.25])(windowCubeS)
windowCubeS = MATERIAL(glass)(windowCubeS)
eastCube = STRUCT(MKPOLS([VeastCube,FVeastCube]))
eastCube = COLOR(wall_color)(eastCube)
eastCube = (PROD([eastCube, Q(0.3)]))

eastCube = DIFFERENCE([eastCube,windowCubeS])
eastCube = STRUCT([eastCube,windowCubeS,lineX,lineY])
#VIEW(eastCube)

#viewEast
eastBase = T(1)(0.8)(eastBase)
eastCube = T(2)(6.25)(eastCube)
east = STRUCT([eastBase,eastCube])
#VIEW(east)


#North-base
VnorthBase = [[0,0],[4,0],[4,8.7],[0,8.7]]
FVnorthBase = [[0,1,2,3,0]]

northBase = STRUCT(MKPOLS([VnorthBase,FVnorthBase]))
northBase = PROD([northBase, Q(0.3)])
windowBaseS = CUBOID([0.3,1.8,0.3])
windowBaseS = T([1,2])([0.25,1.25])(windowBaseS)
windowBaseS = MATERIAL(glass)(windowBaseS)
windowsBaseS = STRUCT(NN(3)([windowBaseS,T(2)(1.85)]))

windowBaseSmall = CUBOID([0.3,0.85,0.3])
windowBaseSmall = T([1,2])([0.25,0.1])(windowBaseSmall)
windowBaseSmall = MATERIAL(glass)(windowBaseSmall)

windowBaseSCube = CUBOID([0.3,0.3,0.3])
windowBaseSCube = T([1,2])([3.2,0.3])(windowBaseSCube)
windowBaseSCube = MATERIAL(glass)(windowBaseSCube)
windowsBaseScube = STRUCT(NN(3)([windowBaseSCube,T(2)(2.45)]))#
#VIEW(windowsBaseScube)
northBase = DIFFERENCE([northBase,windowBaseSmall,windowBaseSCube,windowsBaseS])
northBase = STRUCT([northBase,windowBaseSmall,windowBaseSCube,windowsBaseS])
#VIEW(northBase)

#East-Cube
VnorthCube = [[0,0],[4,0],[4,4.2],[0,4.2]]
FVnorthCube = [[0,1,2,3,0]]
diff = CUBOID([3.3,2,0.3])
northCube = STRUCT(MKPOLS([VnorthCube,FVnorthCube]))
northCube = PROD([northCube, Q(0.3)])
northCube = DIFFERENCE([northCube,diff])

#VIEW(nordCube)

#viewNord
northCube = T(2)(6.25)(northCube)
north = STRUCT([northBase])
#VIEW(north)


#West-base
VWestBase = [[0,0],[4,0],[4,8.7],[0,8.7]]
FVWestBase = [[0,1,2,3,0]]
windowBaseS3W = CUBOID([0.67,1.05,0.3])
windowBaseS3W = T([1,2])([1.625,4.85])(windowBaseS3W)
windowBaseS3W = MATERIAL(glass)(windowBaseS3W)
westBase = STRUCT(MKPOLS([VWestBase,FVWestBase]))
westBase = (PROD([westBase, Q(0.3)]))
westBase = DIFFERENCE([westBase,door,windowBaseS3W])
westBase = STRUCT([westBase,door,windowBaseS3W])
#VIEW(westBase)

#West-Cube

windowBaseS1 = CUBOID([3.5,1.55,0.3])
windowBaseS1 = T([1,2])([0.25,2.45])(windowBaseS1)
windowBaseS1 = MATERIAL(glass)(windowBaseS1)

windowBaseS2 = CUBOID([3.4,2.1,0.3])
windowBaseS2 = T([1,2])([0.25,0.25])(windowBaseS2)
windowBaseS2 = MATERIAL(glass)(windowBaseS2)


VWestCube = [[0,4],[4,4],[0,2.45],[4,2.45],[3.2,2.45],[3.2,0],[4,0]]
FVWestCube = [[0,1,2,3,0],[3,4,5,6,3]]

westCube = STRUCT(MKPOLS([VWestCube,FVWestCube]))
lineX = CUBOID([3.5,0.1])
lineX = T([1,2])([0.25,2.45])(lineX)
lineX2 = CUBOID([3.5,0.1])
lineX2 = T([1,2])([0.25,3.78])(lineX2)
lineY = CUBOID([0.1,1.5])
lineY = T([1,2])([2,2.35])(lineY)
lineY2 = CUBOID([0.1,1.4])
lineY2 = T([1,2])([0.25,2.45])(lineY2)
lineY3 = CUBOID([0.1,1.4])
lineY3 = T([1,2])([3.65,2.45])(lineY3)
westCube = (PROD([westCube, Q(0.3)]))
westCube = DIFFERENCE([westCube,windowBaseS1,windowBaseS2])
westCube = STRUCT([westCube,windowBaseS1,windowBaseS2,lineX,lineX2,lineY,lineY2,lineY3])
#VIEW(westCube)

#viewWest
westCube = T(2)(6.25)(westCube)
westCube = T(1)(0.8)(westCube)
west = STRUCT([westCube,westBase])
#VIEW(west)


#South-base
windowsBaseE = CUBOID([0.8,0.8,0.3])
windowsBaseE = T([1,2])([1.8,2.9])(windowsBaseE)
windowsBaseE = MATERIAL(glass)(windowsBaseE)
windowsBaseE = STRUCT(NN(2)([windowsBaseE,T(2)(1.6)]))
windowDownBase = CUBOID([0.5,1.45,0.3])
windowDownBase = T([1,2])([3.2,0.5])(windowDownBase)
windowDownBase = MATERIAL(glass)(windowDownBase)
VSouthBase = [[0,0],[4,0],[4,6.25],[0,6.25],[0.8,6.25],[0.8,8.7],[0,8.7]]
FVSouthBase = [[0,1,2,3,0],[3,4,5,6,3]]
southBase = STRUCT(MKPOLS([VSouthBase,FVSouthBase]))
southBase = (PROD([southBase, Q(0.3)]))
southBase = DIFFERENCE([southBase,windowsBaseE,windowDownBase])
southBase = STRUCT([southBase,windowsBaseE,windowDownBase])
#VIEW(southBase)
windowCubeE = CUBOID([0.8,0.8,0.3])
windowCubeE = T([1,2])([1.65,1.65])(windowCubeE)
windowCubeE = MATERIAL(glass)(windowCubeE)
VSouthCube = [[0,0],[4,0],[4,4.2],[0,4.2]]
FVSouthCube = [[0,1,2,3,0]]
southCube = STRUCT(MKPOLS([VSouthCube,FVSouthCube]))
southCube = (PROD([southCube, Q(0.3)]))
southCube = DIFFERENCE([southCube,windowCubeE])
southCube = STRUCT([southCube,windowCubeE])
#VIEW(southCube)

southCube = T(2)(6.25)(southCube)
southCube = T(1)(0.8)(southCube)

south = STRUCT([southBase,southCube])
#VIEW(south)


#Rotazione piani
eastBase = R([2,3])(PI/2)(eastBase)
eastBase = R([1,2])(PI/2)(eastBase)
eastBase = T([1,2])([-4,-4.8])(eastBase)
eastBase = R([1,2])(PI)(eastBase)

eastCube = R([2,3])(PI/2)(eastCube)
eastCube = R([1,2])(PI/2)(eastCube)
eastCube = T([1,2])([-4.8,-4.8])(eastCube)
eastCube = R([1,2])(PI)(eastCube)

westBase = R([2,3])(PI/2)(westBase)
westBase = R([1,2])(PI/2)(westBase)
westCube = R([2,3])(PI/2)(westCube)
westCube = R([1,2])(PI/2)(westCube)
westCube = T(1)(0.8)(westCube)

southBase = R([2,3])(PI/2)(southBase)
southBase = T(2)(4)(southBase)

southCube = R([2,3])(PI/2)(southCube)
southCube = T(2)(4.8)(southCube)

northBase = R([2,3])(PI/2)(northBase)
northCube = R([2,3])(PI/2)(northCube)
northCube = T([1,2])([0.8,0.8])(northCube)
NORTH = STRUCT([westBase,westCube])
SOUTH = STRUCT([eastBase,eastCube])
EAST = STRUCT([southBase,southCube])
WEST = STRUCT([northBase,northCube])
b = exercise1.building
b = R([1,2])(PI/2)(b)
b = T(1)(4)(b)

building_color = rgb2color([111,110,98])
NORTH = COLOR(building_color)(NORTH)
SOUTH = COLOR(building_color)(SOUTH)
EAST = COLOR(building_color)(EAST)
WEST = COLOR(building_color)(WEST)
building = STRUCT([b,SOUTH,NORTH,EAST,WEST])
VIEW(building)