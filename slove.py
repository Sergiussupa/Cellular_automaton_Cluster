import random
from tabulate import tabulate

lenthArray = 10
array = [0] * 10
for i in range(lenthArray):
    array[i] = [0] * lenthArray

arrBandits = [0] * 10
for i in range(lenthArray):
    arrBandits[i] = [0] * lenthArray

for i in range(lenthArray):
    for j in range(lenthArray):
        array[i][j] = round(random.random(), 3)
print(tabulate(array))


arrEx = []

class Victor:
    def __init__(self, x=2, y=2, id=1):
        self.x = x
        self.y = y
        self.value = array[self.x][self.y]
        self.id = id
        self.stack = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
    def updatePosition(self, xx):
        self.x = self.x + xx[1]
        self.y = self.y + xx[0]
        self.stack = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]


    def compare(self):
        dd = self.stack.pop()
        print(dd)
        #print(array[self.x][self.y])

        #print(array[self.x + dd[1]][self.y + dd[0]])
        if (self.x + dd[1] < 0 or self.y + dd[0] < 0):
            pass
        elif (self.value - array[self.x + dd[1]][self.y + dd[0]] > 0.01):
            arrBandits[self.x + dd[1]][self.y + dd[0]] = self.id
            self.updatePosition(dd)
        else:
            arrEx.append(Victor(self.x + dd[1], self.y + dd[0], len(arrEx) + 1))

    def init(self):
        arrBandits[self.x][self.y] = self.id
        self.compare()

arrEx.append(Victor())
for i in range(80):
    for j in range(len(arrEx)):
        arrEx[j].init()

print(tabulate(arrBandits))
