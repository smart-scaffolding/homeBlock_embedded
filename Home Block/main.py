import Serial

xMax = 4
yMax = 4
zMax = 4

structure = [[ ['0' for col in range(xMax)] for col in range(yMax)] for row in range(zMax)] 


ser = serial.Serial('/dev/ttyAMA0', 9600) #serial connection on port ttyAMA0 at 9600Baud

while(ser.readline() != 'hello') { #wait for block to connect
    continue
}

ser.write("home\n") #tell block it is attachted to home block

## Might want to put this in thread ##
while(1) {
    newBlock = serial.readline().split(',') #"x,y,z"
    xPos = int(newBlock[0])
    yPos = int(newBlock[1])
    zPos = int(newBlock[2])

    structure[xPos][yPos][zPos] = 1;
}
##                                  ##