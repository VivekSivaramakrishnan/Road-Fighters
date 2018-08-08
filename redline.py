import math,pygame

displayWidth = 1280
displayHeight = 720
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))

speedo = pygame.image.load('Speedo2.png')

def speedo(x,dy):
    if x==1:
        R = ((((225*dy)/50.4)-45)*math.pi)/180
        gameDisplay.blit(speedo, (200-95,550-95))
        pygame.draw.line(gameDisplay,(r,g,b), (200,550), (200-90*math.cos(R),550-90*math.sin(R)),5)
