import time
from graphics import *

class Thing:
   def __init__(self,posX,posY,name):
      self.posX = posX
      self.posY = posY
      self.name = name

   def getName(self):
     print (name)

   def isFalling(self, stick):
      if (self.posY ==  47 or self.posY == 48) and stick.posY == 45: # the ant is on level 1
        if self.posX < 45 and stick.posX < 45: #The ant is on Stick1
          if (((self.posX < stick.posX) and (self.posX >= stick.posX-2)) or ((self.posX > (stick.posX+stick.length)) and (self.posX <= (stick.posX+stick.length+2)))):
            self.falling = True
        elif self.posX > 45 and stick.posX > 45: #The ant is on Stick1
          if (((self.posX < stick.posX) and (self.posX >= stick.posX-2)) or ((self.posX > (stick.posX+stick.length)) and (self.posX <= (stick.posX+stick.length+2)))):
            self.falling = True

      if (self.posY ==  39 or self.posY == 40) and stick.posY == 37: # the ant is on level 2  
        if (((self.posX < stick.posX) and (self.posX >= stick.posX-2)) or ((self.posX > (stick.posX+stick.length)) and (self.posX <= (stick.posX+stick.length+2)))):
          self.falling = True 

      if (self.posY ==  31 or self.posY == 32) and stick.posY == 29: # the ant is on level 3
        if self.posX < 60 and stick.posX < 60: # the ant is on Stick3
          if (((self.posX < stick.posX) and (self.posX >= stick.posX-2)) or ((self.posX > (stick.posX+stick.length)) and (self.posX <= (stick.posX+stick.length+2)))):
            self.falling = True
        elif self.posX > 60 and stick.posX > 60: #The ant is on Stick33
          if (((self.posX < stick.posX) and (self.posX >= stick.posX-2)) or ((self.posX > (stick.posX+stick.length)) and (self.posX <= (stick.posX+stick.length+2)))):
            self.falling = True
              
      if (self.posY ==  23 or self.posY == 24) and stick.posY == 21: # the ant is on level 4
        if (((self.posX < stick.posX) and (self.posX >= stick.posX-2)) or ((self.posX > (stick.posX+stick.length)) and (self.posX <= (stick.posX+stick.length+2)))):
            self.falling = True
               
      if (self.posY ==  15 or self.posY == 16) and stick.posY == 13: # the ant is on level 5 
        if self.posX < 52 and stick.posX < 52: # the ant is on Stick5
          if (((self.posX < stick.posX) and (self.posX >= stick.posX-2)) or ((self.posX > (stick.posX+stick.length)) and (self.posX <= (stick.posX+stick.length+2)))):
            self.falling = True
        elif self.posX > 52 and stick.posX > 52: #The ant is on Stick55
          if (((self.posX < stick.posX) and (self.posX >= stick.posX-2)) or ((self.posX > (stick.posX+stick.length)) and (self.posX <= (stick.posX+stick.length+2)))):
            self.falling = True 

      if (self.posY ==  7 or self.posY == 48) and stick.posY == 5: # the ant is on level 6    
        if self.posX < 72 and stick.posX < 72: # the ant is on Stick6
          if (((self.posX < stick.posX) and (self.posX >= stick.posX-2)) or ((self.posX > (stick.posX+stick.length)) and (self.posX <= (stick.posX+stick.length+2)))):
            self.falling = True
        elif self.posX > 72 and stick.posX > 72: #The ant is on Stick66
          if (((self.posX < stick.posX) and (self.posX >= stick.posX-2)) or ((self.posX > (stick.posX+stick.length)) and (self.posX <= (stick.posX+stick.length+2)))):
            self.falling = True      


class Stick(Thing):
   def __init__(self,num,length):
      self.num=num
      self.length=length

   def get_length(self):
      return self.length
   def draw(self,win):
       kassa = Rectangle(Point(self.posX, self.posY), Point(self.posX+self.length,self.posY+1))
       kassa.setFill("peru")
       kassa.setOutline('Saddle Brown')
       kassa.draw(win)

class Rock(Thing):
   def __init__(self,num,picture, pic):
      self.num = num
      self.picture = picture
      self.pic = pic
   def draw(self,win):
      self.pic = Image(Point(self.posX, self.posY), self.picture)
      self.pic.draw(win)   
  
class StaticRock(Rock):
   def __init__(self,color):
      self.color = color
       

class MoveableRock(Rock):
   def __init__(self,color):
      self.color = color

   def rockmoves(self, strongAnt):
      if strongAnt.color == 'black':
        if strongAnt.direction == 'left':
          self.posX = self.posX - strongAnt.velocity
          self.pic.move(-strongAnt.velocity, 0)
        else:
          self.posX = self.posX + strongAnt.velocity
          self.pic.move(strongAnt.velocity, 0)  

   def fallingRock(self):
      self.posY = self.posY - 0.25
      self.pic.move(0,-0.25)

   def rocklands(self):
      if (self.posY == 46 or self.posY == 40 or self.posY == 30 or self.posY == 22 or self.posY == 14 or self.posY == 6):
        self.falling = False
        self.pic.undraw()
   def collision(self, antTwo, win):
         self.turnAround(win)
         antTwo.turnAround(win)
   def turnAround(self, win):
       if (self.color == "red"):
           if (self.direction == "left"):
              self.direction = "right"
              self.pic.undraw()
              self.picture = "ant-red-right.gif"
              self.draw(win)
           else:
              self.direction = "left"
              self.pic.undraw()
              self.picture = "ant-red-left.gif"
              self.draw(win)
       elif (self.color == "black"):
          if (self.direction == "left"):
             self.direction = "left"
             self.pic.undraw()
             self.picture = "ant-black-right.gif"
             self.draw(win)
          else:
             self.direction = "right"
             self.pic.undraw()
             self.picture = "ant-black-left.gif"
             self.draw(win)
       elif (self.color == "blue"):
          if (self.direction == "left"):
             self.direction = "right"
             self.pic.undraw()
             self.picture = "ant_blue_cute_left.gif"
             self.draw(win)
          else:
             self.direction = "left"
             self.pic.undraw()
             self.picture = "ant_blue_cute_left.gif"
             self.draw(win)
       elif (self.color == 'grey'):
          self.pic.undraw()
          self.picture = 'StaticRock1_angry.gif'
          self.draw(win)       
       else:
          if (self.direction == "left"):
              self.direction = "right"
              self.pic.undraw()
              self.picture = "ant-red-right.gif"
              self.draw(win)
          else:
              self.direction = "left"
              self.pic.undraw()
              self.picture = "ant-red-left.gif"
              self.draw(win)           
                  
      

class Animal(Thing):
   def __init__(self, direction, velocity, picture, pic):
      self.direction = direction
      self.velocity = velocity
      self.picture = picture
      self.pic = pic
      self.falling = False
   def moveFwd(self):
      if self.direction == "left":
         self.posX=self.posX-self.velocity
         self.pic.move(-self.velocity, 0)
      else:
         self.posX = self.posX+self.velocity
         self.pic.move(self.velocity, 0)

   def collision(self, antTwo, win):
         self.turnAround(win)
         antTwo.turnAround(win)


class Ant(Animal):
   def __init__(self,color):
      self.color=color

   def draw(self,win):
      self.pic = Image(Point(self.posX, self.posY), self.picture)
      self.pic.draw(win)

   def turnAround(self, win):
       if (self.color == "red"):
           if (self.direction == "left"):
              self.direction = "right"
              self.pic.undraw()
              self.picture = "ant-red-right.gif"
              self.draw(win)
           else:
              self.direction = "left"
              self.pic.undraw()
              self.picture = "ant-red-left.gif"
              self.draw(win)
       elif (self.color == "black"):
          if (self.direction == "left"):
             self.direction = "right"
             self.pic.undraw()
             self.picture = "ant-black-right.gif"
             self.draw(win)
          else:
             self.direction = "left"
             self.pic.undraw()
             self.picture = "ant-black-left.gif"
             self.draw(win)
       elif (self.color == "blue"):
          if (self.direction == "left"):
             self.direction = "right"
             self.pic.undraw()
             self.picture = "ant_blue_cute_left.gif"
             self.draw(win)
          else:
             self.direction = "left"
             self.pic.undraw()
             self.picture = "ant_blue_cute_left.gif"
             self.draw(win)
       elif (self.color == 'grey'):
          self.pic.undraw()
          self.picture = 'StaticRock1.gif'       
       else:
          if (self.direction == "left"):
              self.direction = "right"
              self.pic.undraw()
              self.picture = "ant-red-right.gif"
              self.draw(win)
          else:
              self.direction = "left"
              self.pic.undraw()
              self.picture = "ant-red-left.gif"
              self.draw(win)    


            
   def fall(self):
      self.posY = self.posY-0.5*self.velocity
      self.pic.move(0,-0.5*self.velocity)

   


   def landing(self):
      if (self.posY == 47 or self.posY == 39 or self.posY == 31 or self.posY == 23 or self.posY == 15 or self.posY == 7):
        self.falling = False

   def hitwall(self,win):
      if ((self.posX == 6) or (self.posX == 118)):
         self.turnAround(win)


   
class Ladybug(Animal):
   def __init__(self,color):
      self.color=color
      self.LFalling = False

   def draw(self,win):
      self.pic = Image(Point(self.posX+10, self.posY), self.picture)
      self.pic.draw(win)

   def pfly(self, win):
      self.velocity = 1.2
      if self.direction == "left":
         self.posX=self.posX-self.velocity
         self.posY=self.posY+1.2
         self.pic.undraw()
         self.picture = "Ladybug_fly.gif"
         self.draw(win)
         self.pic.move(1.2, 1.2)
         

      else:
         self.posX = self.posX+self.velocity
         self.posY=self.posY+1.2
         self.pic.undraw()
         self.picture = "Ladybug_fly.gif"
         self.draw(win)
         self.pic.move(1.2, 1.2)

   def LadyFalling(self, stick):
      if self.posY ==  47 and stick.posY == 45: # the ant is on level 1
        if self.posX < 47 and stick.posX < 47: #The ant is on Stick1
          if (((self.posX < stick.posX-6) and (self.posX >= stick.posX-8)) or ((self.posX > (stick.posX+stick.length-10)) and (self.posX <= (stick.posX+stick.length-8)))):
            self.LFalling = True
        elif self.posX > 45 and stick.posX > 45: #The ant is on Stick1
          if (((self.posX < stick.posX-6) and (self.posX >= stick.posX-8)) or ((self.posX > (stick.posX+stick.length-10)) and (self.posX <= (stick.posX+stick.length-8)))):
            self.LFalling = True

      if self.posY ==  39 and stick.posY == 37: # the ant is on level 2  
        if (((self.posX < stick.posX-6) and (self.posX >= stick.posX-8)) or ((self.posX > (stick.posX+stick.length-10)) and (self.posX <= (stick.posX+stick.length-8)))):
          self.LFalling = True 

      if self.posY ==  31 and stick.posY == 29: # the ant is on level 3
        if self.posX < 60 and stick.posX < 60: # the ant is on Stick3
          if (((self.posX < stick.posX-6) and (self.posX >= stick.posX-8)) or ((self.posX > (stick.posX+stick.length-10)) and (self.posX <= (stick.posX+stick.length-8)))):
            self.LFalling = True
        elif self.posX > 58 and stick.posX > 58: #The ant is on Stick33
          if (((self.posX < stick.posX-6) and (self.posX >= stick.posX-8)) or ((self.posX > (stick.posX+stick.length-10)) and (self.posX <= (stick.posX+stick.length-8)))):
            self.LFalling = True
              
      if self.posY ==  23 and stick.posY == 21: # the ant is on level 4
        if (((self.posX < stick.posX-6) and (self.posX >= stick.posX-8)) or ((self.posX > (stick.posX+stick.length-10)) and (self.posX <= (stick.posX+stick.length-8)))):
            self.LFalling = True
               
      if self.posY ==  15 and stick.posY == 13: # the ant is on level 5 
        if self.posX < 52 and stick.posX < 52: # the ant is on Stick5
          if (((self.posX < stick.posX-6) and (self.posX >= stick.posX-8)) or ((self.posX > (stick.posX+stick.length-10)) and (self.posX <= (stick.posX+stick.length-8)))):
            self.LFalling = True
        elif self.posX > 50 and stick.posX > 50: #The ant is on Stick55
          if (((self.posX < stick.posX-6) and (self.posX >= stick.posX-8)) or ((self.posX > (stick.posX+stick.length)-10) and (self.posX <= (stick.posX+stick.length-8)))):
            self.LFalling = True 

      if self.posY ==  7 and stick.posY == 5: # the ant is on level 6    
        if self.posX < 72 and stick.posX < 72: # the ant is on Stick6
          if (((self.posX < stick.posX-6) and (self.posX >= stick.posX-8)) or ((self.posX > (stick.posX+stick.length-10)) and (self.posX <= (stick.posX+stick.length-8)))):
            self.LFalling = True
        elif self.posX > 70 and stick.posX > 70: #The ant is on Stick66
          if (((self.posX < stick.posX-6) and (self.posX >= stick.posX-8)) or ((self.posX > (stick.posX+stick.length-10)) and (self.posX <= (stick.posX+stick.length-8)))):
            self.LFalling = True 

   def turnAround(self, win):
      if (self.direction == "left"):
         self.direction = "right"
         self.pic.undraw()
         self.picture = "ladybug_walk-right.gif"
         self.draw(win)
      else:
         self.direction = "left"
         self.pic.undraw()
         self.picture = "ladybug_walk.gif"
         self.draw(win)

   def hitwall(self,win):
      if ((self.posX < -5) or (self.posX > 105)):
         self.turnAround(win)