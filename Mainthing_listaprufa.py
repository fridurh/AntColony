from Throunloka_melli import *
from ants_and_sticks_and_rocks import *
import time
from graphics import *
import itertools 



st = 0.1        
t=0
while t < 400:
    time.sleep(st)
    for i in range(len(poddulisti) - 1):
        j = i + 1;
        for j in range(j, len(poddulisti)):
            if (poddulisti[i].posY == poddulisti[j].posY):
                if (((poddulisti[i].posX+1) > poddulisti[j].posX and poddulisti[i].posX < (poddulisti[j].posX+1)) or ((poddulisti[i].posX+1) < poddulisti[j].posX and poddulisti[i].posX > (poddulisti[j].posX+1))):
                    poddulisti[i].collision(poddulisti[j],win)

    for i in range(len(poddulisti)):
        for j in range(len(Sticklisti)):
            poddulisti[i].isFalling(Sticklisti[j])
            if (poddulisti[i].falling):
                poddulisti[i].fall()
                poddulisti[i].landing()
        poddulisti[i].hitwall(win)
        poddulisti[i].moveFwd()

    for i in range(len(MoveableRocklisti)):
        for j in range(0, len(poddulisti)):
            if (poddulisti[j].posY == (MoveableRocklisti[i].posY)-1):
                if (((poddulisti[j].posX+5) > MoveableRocklisti[i].posX and poddulisti[j].posX < (MoveableRocklisti[i].posX+5)) or ((poddulisti[j].posX+5) < MoveableRocklisti[i].posX and poddulisti[j].posX > (MoveableRocklisti[i].posX+5))):
                    MoveableRocklisti[i].rockmoves(poddulisti[j])
                    

    for i in range(len(MoveableRocklisti)):
        for j in range(0, len(poddulisti)):
            if (poddulisti[j].posY == (MoveableRocklisti[i].posY)-1):
                if (((poddulisti[j].posX+5) > MoveableRocklisti[i].posX and poddulisti[j].posX < (MoveableRocklisti[i].posX+5)) or ((poddulisti[j].posX+5) < MoveableRocklisti[i].posX and poddulisti[j].posX > (MoveableRocklisti[i].posX+5))):
                    MoveableRocklisti[i].collision(poddulisti[j],win)  

    for i in range(len(MoveableRocklisti)):
        for j in range(0, len(ladybuglisti)):
            if (ladybuglisti[j].posY == (MoveableRocklisti[i].posY)-1):
                if (((ladybuglisti[j].posX+5) > MoveableRocklisti[i].posX and ladybuglisti[j].posX < (MoveableRocklisti[i].posX+5)) or ((ladybuglisti[j].posX+5) < MoveableRocklisti[i].posX and ladybuglisti[j].posX > (MoveableRocklisti[i].posX+5))):
                    flyingbugslisti.append(ladybuglisti[i])

    for i in range(len(MoveableRocklisti)):
        for j in range(len(Sticklisti)):
            MoveableRocklisti[i].isFalling(Sticklisti[j])
            if (MoveableRocklisti[i].falling):
                MoveableRocklisti[i].fallingRock(win)
                MoveableRocklisti[i].rocklands()

    for i in range(len(ladybuglisti)):
        for j in range(len(Sticklisti)):
            ladybuglisti[i].LadyFalling(Sticklisti[j])
            if (ladybuglisti[i].LFalling and ladybuglisti[i].posX > 12 and ladybuglisti[i].posX!= 100):
                flyingbugslisti.append(ladybuglisti[i])

    for i in range(len(poddulisti)):
        for j in range(len(ladybuglisti)):
            if (poddulisti[i].posY == ladybuglisti[j].posY):
                if (((poddulisti[i].posX+1) > ladybuglisti[j].posX and poddulisti[i].posX < (ladybuglisti[j].posX+1)) or ((poddulisti[i].posX+1) < ladybuglisti[j].posX and poddulisti[i].posX > (ladybuglisti[j].posX+1))):
                    flyingbugslisti.append(ladybuglisti[j])

    for i in range(len(flyingbugslisti)):
        if flyingbugslisti[i] in ladybuglisti:
            ladybuglisti.remove(flyingbugslisti[i])
        flyingbugslisti[i].pfly(win)

    for i in range(len(ladybuglisti)):
            ladybuglisti[i].moveFwd()
            ladybuglisti[i].hitwall(win)
                               

    t = t + 1    

    
    

   




        
            
       
