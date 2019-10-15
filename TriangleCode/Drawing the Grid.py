import random
import pygame

HEIGHT = 0
WIDTH = 0
WHITE = (255,255,255)
BLACK = (0,0,0)

n =30#Xnumber DONT USE ODD NUMBERS FOR X VALUE
m= 15#Ynumber
Rotation = 0
ArrX = []
ArrY = []

Rndm = [[[0] * 3 for j in range(n)] for i in range(m)]
RndmTriangle = [[0] * n for i in range(m)]
Check = [[[0] * 3 for j in range(n)] for i in range(m)]
Solved = [[0] * n for i in range(m)]


pygame.init()
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Triangles?")


GAME_FONT = pygame.font.SysFont("Calibri",40)
Congrats = pygame.font.SysFont("Calibri",60)
Timer = GAME_FONT.render(("Time: 00"),False,WHITE)
Triangle_list = pygame.sprite.Group()
Touching = pygame.sprite.Group()

#-----------------------------------------------------------------Classes------------------------------------------------------------------------------------------------------------------
class Rotate(pygame.sprite.Sprite):
    def __init__(self,ClassTriangle,i,j,x,y):
        super().__init__()
        
        Triangle = pygame.image.load(ClassTriangle)
        self.image = pygame.transform.scale(Triangle,(100,100)).convert()
        
        if (i%2 == 0 and j%2 == 0) or (i%2 != 0 and j%2 != 0) :
            self.image = pygame.transform.flip(self.image,False,True)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect() #rect value is required for draw value and cannot be used as a hitbox
        self.rect.x = x
        self.rect.y = y
        self.hitbox =(x+30,y+30, 40,40)     #deals with miss alignment (pygame counts from top left corner)
        

        
    def clicked(self,ClassTriangle,i,j,pos): #DOESNT ASSIGN SELF.RECT
        super().__init__()
        if self.hitbox[0] < pos[0] <(self.hitbox[0]+self.hitbox[2]) and self.hitbox[1] < pos[1] <(self.hitbox[1]+self.hitbox[3]): #error checking with accurate hitbox
            Triangle = pygame.image.load(ClassTriangle)
            self.image = pygame.transform.scale(Triangle,(100,100)).convert()
            
            if (i%2 == 0 and j%2 == 0) or (i%2 != 0 and j%2 != 0) :
                self.image = pygame.transform.flip(self.image,False,True)
            self.image.set_colorkey(BLACK)
            

        
        
class Mouse(pygame.sprite.Sprite):
   def __init__(self):
        super().__init__()
        self.image = pygame.Surface([0,0])
        self.rect = self.image.get_rect()


#-----------------------------------------------------------Functions-----------------------------------------------------------------------------------------------------------
def formGrid(Rndm,RndmTriangle,Solved):

    for i in range(m):  # column
        for j in range(n):  # row
            for k in range(3):

                                                                # 0 = Left 1 = Right 2 = Top/Bottom
                if Rndm[i][j][k] == 0:
                    Rndm[i][j][k] = random.randint(1, 3)

            if j < n - 1:
                Rndm[i][j + 1][0] = Rndm[i][j][1]  # always pass left value to right value of next triangle

            if i < m - 1 and (i+j) %2!=0:
                Rndm[i + 1][j][2] = Rndm[i][j][2]  # always pass down if triangle requires so
            Rotation = random.randint(-1,1)
            Rotation = 0  
            if Rotation == 0:
                RndmTriangle[i][j] = ("Triangle%s%s%s" % (Rndm[i][j][0], Rndm[i][j][1], Rndm[i][j][2])) #no rotation
                Solved[i][j] = True
            elif Rotation == 1:
                RndmTriangle[i][j] = ("Triangle%s%s%s" % (Rndm[i][j][2], Rndm[i][j][0], Rndm[i][j][1])) # rotate clockwise
                Solved[i][j] = False
            else:
                RndmTriangle[i][j] = ("Triangle%s%s%s" % (Rndm[i][j][1], Rndm[i][j][2], Rndm[i][j][0])) # rotate counter-clockwise
                Solved[i][j] == False
            for L in range(3):
                 Rndm[i][j][L] = (RndmTriangle[i][j])[8+L:9+L]
                
            RndmTriangle[i][j] = ("Triangle%s%s%s" % (Rndm[i][j][0], Rndm[i][j][1], Rndm[i][j][2]))
        
    return Rndm, RndmTriangle, Solved

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def displayGrid(RndmTriangle,Triangle_list,ArrX,ArrY):
    x = 50
    y= 50
    
    for i in range(m): #column
        for j in range(n): #row
            TriangleType ="%s.png" %RndmTriangle[i][j]                                      #assigns Random Triangle to file format
            Triangle = pygame.image.load(TriangleType)
           


            #THIS CAN BE REMOVED LATER
            TrianglePrint = pygame.transform.scale(Triangle,(100,100))                       
            if (i%2 == 0 and j%2 == 0) or (i%2 != 0 and j%2 != 0) :
                TrianglePrint = pygame.transform.flip(TrianglePrint,False,True)
              
                                                                                            #ROW ALLIGNMENT
            if j ==0:
                if i%2 != 0:
                    y-=40
                    x+=20   
                else:
                    x+=20
             
            if (i%2 == 0 and j%2 !=0) or (i%2 != 0 and j%2 == 0):                           #checks if both are odd
                y+= 20                                                                      #deals with centre issue
            else:
                y-=20                                                                       # cancels out for alternate shapes
            
            window.blit(TrianglePrint, (x, y))#CAN REMOVE EVENTUALLY
            pygame.display.update()
            
            if i == 0:
                ArrX.append(x+50) #puts Logic hitboxes over triangles
              
            
            create= Rotate(TriangleType,i,j,x,y)
            Triangle_list.add(create)
            x+= 42
        ArrY.append(y+50)#puts Logic hitboxes over triangles
        x=50
        y+= 88
  
    
    return
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def binarySearch(arr, i, length, pos,Yval): #THIS IS FOR SQA PURPOSES ONLY
  
    # Check base case 
    if length >= i: 
  
        mid = i + round((length - i)/2) #deals with odd array numbers
    
        # If element is present at the middle itself 
        if -(20+Yval)<= (arr[mid] - pos) <= (20+Yval): 
            return mid 
          
        # If element is smaller than mid, then it can only be present in left subarray
    
        elif arr[mid] > pos: 
            return binarySearch(arr, i, mid-1, pos,Yval) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binarySearch(arr, mid+1, length, pos,Yval) 
  
    else: 
        # Element is not present in the array 
        return -1

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def EndGame(Finished,RndmTriangle,Rndm,a,b):
    End = False
    Solved[a][b] = False                        # ensures that rotated triangles are always checked and the related triangles incase they become unsolved
    if b > 0:                                   #ensures that b-1 is on the grid
        Solved[a][b-1] = False
    if b < n-1 :                                # ensures that b+1 is on the grid
        Solved[a][b+1] = False
    if  a < m - 1 and (a+b)%2 != 0:             #passes down from all the flipped triangles not in the bottom row
        Solved[a+1][b] = False
    Solved[a][b] = CheckFunction(Rndm,a,b)
    
    if Solved[a][b] == True: #Only runs following code if actually required
        if End == False:
            for i in range(m):  # column
                for j in range(n):  # row
                    if Solved[i][j] == False:
                        Solved[i][j] = CheckFunction(Rndm,i,j)
                        if Solved[i][j] == False:
                            End = True
            if End == False:
                Finished = True                         #This is only assinged if no values in the loop return false and therefore the game is done
    return Finished

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def CheckFunction(Rndm,i,j):
    
    XTest = False
#CHECKING HORIZONTAL ALLIGNMENT
    if j > 0 and j < n-1:
        if(Rndm[i][j][0] == Rndm[i][j-1][1]) and (Rndm[i][j][1] == Rndm[i][j+1][0]): #Checks left matches previous right value then if right value matches next left value
            XTest = True
    elif j == 0:
        if Rndm[i][j][1] == Rndm[i][j+1][0]: #only checks right value against next left value
            XTest = True
    elif j == n-1: #only checks left value against previous right value
        if Rndm[i][j][0] == Rndm[i][j-1][1]:
            XTest = True

#CHECKING VERTICAL ALLIGNMENT IF HORIZONTAL IS OK                
    if XTest == True:
        if i < m - 1 and (i+j)%2 != 0:
            if ( Rndm[i + 1][j][2] == Rndm[i][j][2]): #check if TB values match if required 
                    Solved[i][j] = True
            else:
                Solved[i][j] = False
        else:
            Solved[i][j] = True
    else:Solved[i][j] = False


    return Solved[i][j]



             
Rndm,RndmTriangle,Solved = formGrid(Rndm,RndmTriangle,Solved)
displayGrid(RndmTriangle,Triangle_list,ArrX,ArrY)



#----------------------------------------------------MAIN PROGRAM-------------------------------------------------------------------------------------------------------------------
player = Mouse()
done = False
pressed = True
stop = False
start_time = pygame.time.get_ticks() 
clock = pygame.time.Clock()
a = 0                                           #MAIN LOOP VARIABLES
b = 0
Moves = 0
count = 0

AdjustName = ""
Finished = False
counting_minutes = 0
counting_seconds = 0


while not done:
    while stop == False:
        counting_time = pygame.time.get_ticks() - start_time #TIMER TIME
        
        counting_seconds = str(round((counting_time%60000)/1000 )).zfill(2)
        count+=1
        counting_string = "%s:%s" % (counting_minutes, counting_seconds)

            
        if count%60 ==0:
                
            if counting_minutes == 0:
                print(counting_seconds)
                Timer = GAME_FONT.render(("Time: %s"%counting_seconds),False,WHITE)
            else:
                print(counting_string)
                Timer= GAME_FONT.render(("Time: %s"%counting_string),False,WHITE)
            
        window.blit(Timer, (0, HEIGHT - 50))
        
                
                
        if count == 3600: #60fps * 60 seconds
            counting_minutes+=1
            count = 0
                 
        clock.tick(60) 
                
            
        for event in pygame.event.get():
            
            
            
            if event.type == pygame.QUIT:
                done = True
                stop = True
            if event.type == pygame.MOUSEBUTTONUP:
                pressed = True
        # Clear the screen
        
            if event.type == pygame.MOUSEBUTTONDOWN and pressed == True:
                
                pos = pygame.mouse.get_pos()
                player.rect.x = pos[0]                                                          #sets mouse position to detection object
                player.rect.y = pos[1]
                
                
                Touching = pygame.sprite.spritecollide(player, Triangle_list, False)
                
                
                a = binarySearch(ArrY, 0, (len(ArrY)-1), pos[1],20)                             #Yval
                b = binarySearch(ArrX, 0, (len(ArrX)-1), pos[0],0)                              #we can check for if both of the values are true and this will give better hitboxes
                
                if a!= -1 and b!= -1:                                                           #-1 is returned if the position is not within a hitbox
                    Moves += 1
                    CounterDisplay = GAME_FONT.render(("Moves: %s"%Moves),False,WHITE)

                    
                    Temp=[]
                    for i in range (3):
                        
                        Temp.append((RndmTriangle[a][b])[8+i:9+i])
                    if (a%2 == 0 and b%2 == 0) or (a%2 != 0 and b%2 != 0) :
                        AdjustName = ("Triangle%s%s%s.png"%(Temp[1], Temp[2],Temp[0]))
                    else:
                        AdjustName = ("Triangle%s%s%s.png"%(Temp[2], Temp[0],Temp[1]))

                    RndmTriangle[a][b] = AdjustName
                    for i in range(3):
                        Rndm[a][b][i] = (RndmTriangle[a][b])[8+i:9+i]
                        
                    
                    for create in Touching:
                        create.clicked(AdjustName,a,b,pos)                                      #pass y value first as it becomes i and j
                    
                    window.fill(BLACK) # wipes screen    
                    Triangle_list.draw(window)
                    window.blit(CounterDisplay, (WIDTH - 180, HEIGHT - 50))
                    Finished = EndGame(Finished,RndmTriangle,Rndm,a,b)
                

                    
                    if Finished == True:
                        print("congratulations")
                        Congratulate = Congrats.render("Congratulations",False,WHITE)
                        window.blit(Congratulate, (80, 30))
                        stop = True
                    
                pressed = False
                
                pygame.display.flip()
            
        
pygame.quit()

                          
        
    



'''checklist:
its phase 4 time 
FIX MOVE COUNTER AND THAT BITCH ASS TIMER
red red blue & yellow yellow blue triangles
pick x random numbers between 0 and (m*n -1)
add mystery triangles to make more difficult
add gold outline to areas which are solved for more feedback

love to see that with everything i take off this list i add something new'''
