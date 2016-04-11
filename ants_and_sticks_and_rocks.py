from Throunloka_melli import *
import time
from graphics import *
import itertools

# create window and initialize it
win = GraphWin(width=1200, height=700)     # create a window
win.setCoords(0, 0, 120, 50)               # set the coordinates "cm"
win.setBackground('Medium Sea Green')

#Prik i efstu linu
Sticklisti = [];
Stick1=Stick(1,30)
Stick1.name = "Stick1"    
Stick1.posX = 2
Stick1.posY = 45
Stick1.draw(win)
Sticklisti.append(Stick1)

Stick11=Stick(2,60)
Stick11.name = 'Stick11'
Stick11.posX = 60
Stick11.posY = 45
Stick11.draw(win)
Sticklisti.append(Stick11)

#Prik i 2. linu
Stick2=Stick(3,70)
Stick2.name = 'Stick2'
Stick2.posX = 30
Stick2.posY = 37
Stick2.draw(win)
Sticklisti.append(Stick2)

#Prik i 3. linu
Stick3=Stick(4,50)
Stick3.name = 'Stick3'
Stick3.posX = 2
Stick3.posY = 29
Stick3.draw(win)
Sticklisti.append(Stick3)

Stick33=Stick(5,60)
Stick33.name = 'Stick33'
Stick33.posX = 65
Stick33.posY = 29
Stick33.draw(win)
Sticklisti.append(Stick33)

#Prik i 4. linu
Stick4=Stick(6,50)
Stick4.name = 'Stick4'
Stick4.posX = 30
Stick4.posY = 21
Stick4.draw(win)
Sticklisti.append(Stick4)

#Prik i 5. linu
Stick5=Stick(7,40)
Stick5.name = 'Stick5'
Stick5.posX = 2
Stick5.posY = 13
Stick5.draw(win)
Sticklisti.append(Stick5)

Stick55=Stick(8,80)
Stick55.name = 'Stick55'
Stick55.posX = 60
Stick55.posY = 13
Stick55.draw(win)
Sticklisti.append(Stick55)

#Prik i 6. linu
Stick6=Stick(9,65)
Stick6.name = 'Stick6'
Stick6.posX = 2
Stick6.posY = 5
Stick6.draw(win)
Sticklisti.append(Stick6)

Stick66=Stick(9,65)
Stick66.name = 'Stick66'
Stick66.posX = 80
Stick66.posY = 5
Stick66.draw(win)
Sticklisti.append(Stick66)

poddulisti = [];

Mellibesti = Ant("green")
Mellibesti.velocity=0.5
Mellibesti.direction = "left"
Mellibesti.posX = 110
Mellibesti.posY = 47
Mellibesti.name= "Mellibesti"
Mellibesti.picture = 'ant_green_cute_left.gif'
Mellibesti.draw(win)
Mellibesti.falling = False
poddulisti.append(Mellibesti)

Thorinn = Ant("blue")
Thorinn.velocity=0.5
Thorinn.direction = "left"
Thorinn.posX = 90
Thorinn.posY = 31
Thorinn.name="Thorinn"
Thorinn.picture = 'ant_blue_cute_left.gif'
Thorinn.draw(win)
Thorinn.falling = False
poddulisti.append(Thorinn)

Melli = Ant("red")
Melli.velocity=0.5
Melli.direction = "left"
Melli.posX = 70
Melli.posY = 31
Melli.name="Melli"
Melli.picture = 'ant-red-left.gif'
Melli.draw(win)
Melli.falling = False
poddulisti.append(Melli)

Gloin = Ant("red")
Gloin.velocity=1
Gloin.direction = "right"
Gloin.posX = 70
Gloin.posY = 15
Gloin.name="Gloin"
Gloin.picture = 'ant-red-right.gif'
Gloin.draw(win)
Gloin.falling = False
poddulisti.append(Gloin)

Dwalin = Ant("black")
Dwalin.velocity=1
Dwalin.direction = "right"
Dwalin.posX = 7
Dwalin.posY = 47
Dwalin.name="Dwalin"
Dwalin.picture = 'ant-black-right.gif'
Dwalin.draw(win)
Dwalin.falling = False
poddulisti.append(Dwalin)

Balin = Ant("black")
Balin.velocity=1
Balin.direction = "right"
Balin.posX = 10
Balin.posY = 31
Balin.name="Balin"
Balin.picture = 'ant-black-right.gif'
Balin.draw(win)
Balin.falling = False
poddulisti.append(Balin)



Melli1 = Ant("red")
Melli1.velocity=1
Melli1.direction = "left"
Melli1.posX = 15
Melli1.posY = 7
Melli1.name="Melli1"
Melli1.picture = 'ant-red-left.gif'
Melli1.draw(win)
Melli1.falling = False
poddulisti.append(Melli1)

flyingbugslisti = [];
ladybuglisti = [];
Padda = Ladybug("pink")
Padda.velocity=0.8
Padda.direction = "right"
Padda.posX = 90
Padda.posY = 15
Padda.name="Padda"
Padda.picture = 'ladybug_walk-right.gif'
Padda.falling = False
Padda.draw(win)
ladybuglisti.append(Padda)

Padda2 = Ladybug("pink")
Padda2.velocity=0.8
Padda2.direction = "left"
Padda2.posX = 70
Padda2.posY = 39
Padda2.name="Padda"
Padda2.picture = 'ladybug_walk.gif'
Padda2.falling = False
Padda2.draw(win)
ladybuglisti.append(Padda2)

Dobby = Ladybug("pink")
Dobby.velocity=0.8
Dobby.direction = "right"
Dobby.posX = 15
Dobby.posY = 7
Dobby.name="Padda"
Dobby.picture = 'ladybug_walk-right.gif'
Dobby.falling = False
Dobby.draw(win)
ladybuglisti.append(Dobby)


StatickRock1 = StaticRock("grey")
StatickRock1.picture = 'StaticRock1.gif'
StatickRock1.posX = 3
StatickRock1.posY = 32
StatickRock1.draw(win)

MoveableRocklisti = [];
MoveableRock1 = MoveableRock("grey")
MoveableRock1.picture = 'StaticRock1.gif'
MoveableRock1.posX = 65
MoveableRock1.posY = 40
MoveableRock1.falling = False
MoveableRock1.draw(win)
MoveableRocklisti.append(MoveableRock1)

MoveableRock2 = MoveableRock("grey")
MoveableRock2.picture = 'StaticRock1.gif'
MoveableRock2.posX = 35
MoveableRock2.posY = 24
MoveableRock2.falling = False
MoveableRock2.draw(win)
MoveableRocklisti.append(MoveableRock2)

MoveableRock3 = MoveableRock("grey")
MoveableRock3.picture = 'StaticRock1.gif'
MoveableRock3.posX = 110
MoveableRock3.posY = 16
MoveableRock3.falling = False
MoveableRock3.draw(win)
MoveableRocklisti.append(MoveableRock3)

MoveableRock4 = MoveableRock("grey")
MoveableRock4.picture = 'StaticRock1.gif'
MoveableRock4.posX = 77
MoveableRock4.posY = 24
MoveableRock4.falling = False
MoveableRock4.draw(win)
MoveableRocklisti.append(MoveableRock4)