

def setup():
    size(1000, 1000)

def draw():
    background(175)

    for row in range(3): #create three rows
        for col in range(4): #create four columns
            x = 125 + col * 250 #(125, 170) is the first Pikachu and space 250, 300 pixels away
            y = 170 + row * 300
            drawObject(x, y, 0.25) #Draw Pikachu 25% of its original size


def drawObject(x, y, s):
    push()
    translate(x, y)
    scale(s)
    translate(-500, -500)
    
    # Left ear
    fill(255, 230, 0)

    begin_shape()
    vertex(230, 95)
    bezier_vertex(280, 130, 340, 220, 390, 380)
    bezier_vertex(345, 345, 330, 360, 320, 380)
    bezier_vertex(270, 300, 240, 180, 230, 95)
    end_shape()
    
    # Left ear black tip
    fill(0)

    begin_shape()
    vertex(230, 95)
    bezier_vertex(250, 110, 285, 155, 300, 185)
    vertex(260, 220)
    bezier_vertex(245, 165, 235, 120, 230, 95)
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
    ellipse(390, 470, 70, 70)
    ellipse(610, 470, 70, 70)

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
    

    # Mouth
    fill(95, 35, 40)

    begin_shape()
    vertex(430, 590)
    bezier_vertex(460, 615, 480, 615, 500, 590)
    bezier_vertex(520, 615, 540, 615, 570, 590)
    bezier_vertex(560, 670, 530, 700, 500, 700)
    bezier_vertex(470, 700, 440, 670, 430, 590)
    end_shape()
    
    #Tongue
    fill(255, 125, 150)
    ellipse(500, 670, 85, 35)
    
 
    
    # Left lightning
    fill(0, 220, 255)

    begin_shape()
    vertex(330, 590)
    vertex(260, 550)
    vertex(285, 590)
    vertex(180, 570)
    vertex(250, 620)
    vertex(205, 650)
    vertex(330, 610)
    end_shape(CLOSE)
    
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
    
    
    
    
    