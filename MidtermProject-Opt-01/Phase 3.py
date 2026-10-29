

def setup():
    size(1000, 1000)

def draw():
    background(175)
    
    
    drawObject(250, 350, 0.4) #First Pikachu 40%
    drawObject(700, 550, 0.6) #Second Pikachu 60%
#

def drawObject(x, y, s): #reusable function to draw differnet Pikachus on differnt sizes and positions 
    push() #save current transformations
    translate(x, y) #set the new position
    scale(s) #adjust the size
    translate(-500, -500) #Shift the original reference point
    
  

    # Left ear: 3 curved lines 
    fill(255, 230, 0) #Yellow

    begin_shape()
    vertex(230, 95) #Left top starting point
    bezier_vertex(280, 130, 340, 220, 390, 380) #Right side curve
    bezier_vertex(345, 345, 330, 360, 320, 380) #Low curve
    bezier_vertex(270, 300, 240, 180, 230, 95) #Left side curve
    end_shape()
    
    # Left ear black tip: 2 curved lines and a straight line to connect them
    fill(0) #Black

    begin_shape()
    vertex(230, 95) #Left top starting point
    bezier_vertex(250, 110, 285, 155, 300, 185) #Right side curve
    vertex(260, 220) #Straight Line
    bezier_vertex(245, 165, 235, 120, 230, 95) #Left side curve
    end_shape()
    
    # Right ear
    fill(255, 230, 0)

    begin_shape()
    vertex(770, 95)
    bezier_vertex(720, 130, 640, 250, 610, 380)
    bezier_vertex(630, 400, 660, 420, 680, 430)
    bezier_vertex(730, 300, 760, 180, 770, 95)
    end_shape()
    
    fill(0)
    begin_shape()
    vertex(290, 185)
    end_shape()
    
    # Right ear black tip
    fill(0)

    begin_shape()
    vertex(770, 95)
    bezier_vertex(750, 110, 715, 155, 700, 185)
    vertex(740, 220)
    bezier_vertex(755, 165, 765, 120, 770, 95)
    end_shape()
    
    
    #Face   
    fill(255, 230, 0)
    ellipse(500, 550, 510, 510)
    
    # Eyes
    fill(0)
    ellipse(390, 470, 70, 70) #Left 
    ellipse(610, 470, 70, 70) #Right

    # Eye highlights
    fill(255)

    ellipse(402, 465, 32, 32)
    ellipse(598, 465, 32, 32) 
    
    # Red cheeks
    fill(255, 50, 50)

    ellipse(330, 590, 105, 85)
    ellipse(670, 590, 105, 85)
    
    # Nose
    fill(0)
    triangle(485, 550, 515, 550, 500, 570)
    

    # Mouth: 4 curved lines 
    fill(95, 35, 40) #Dark Brown

    begin_shape()
    vertex(430, 590) #Left Corner starting point
    bezier_vertex(460, 615, 480, 615, 500, 590) #Left upper
    bezier_vertex(520, 615, 540, 615, 570, 590) #Right upper
    bezier_vertex(560, 670, 530, 700, 500, 700) #Right lower
    bezier_vertex(470, 700, 440, 670, 430, 590) #Left lower
    end_shape()
    
    #Tongue
    fill(255, 125, 150) #Pink
    ellipse(500, 670, 85, 35) #oval
    
    
    # Left lightning: 7 vertices and connected them with straight lines and closed
    fill(0, 220, 255) #Cyan

    begin_shape()
    vertex(330, 590) #1 Starting point
    vertex(260, 550) #2 Left upper
    vertex(285, 590) #3 Inner
    vertex(180, 570) #4 Left most
    vertex(250, 620) #5 Lower Inner
    vertex(205, 650) #6 Botton Left
    vertex(330, 610) #7 Ending point
    end_shape(CLOSE) #Connects the points and turns into a shape
    
    # Right lightning
    fill(0, 220, 255)

    begin_shape()
    vertex(670, 590)
    vertex(740, 550)
    vertex(715, 590)
    vertex(820, 570)
    vertex(750, 620)
    vertex(795, 650)
    vertex(670, 610)
    end_shape(CLOSE)


    pop()


    
    
    
    
    