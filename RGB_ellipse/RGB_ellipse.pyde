x=0
g=0
def setup():
    size(1000,1000)
    background(255)
    frameRate(1200)
def draw():
    global x, g
    background(255)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(x,g,50,50)
    x+=1
    g+=1
    
