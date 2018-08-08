import pygame, sys, time, random, math
from PIL import Image

displayWidth = 1280
displayHeight = 720


def Quit():
    pygame.quit()
    quit()


##name = input('Enter your name(3-letter): ')
##with open('Score.txt','a') as scoree:
##    scoree.write('\n')
##    scoree.write(name)

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

# gameDisplay = pygame.display.set_mode((displayWidth,displayHeight),pygame.FULLSCREEN)
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

pygame.display.set_caption('Road Fighters')
clock = pygame.time.Clock()

gameIcon = pygame.image.load('Icon.png')

pygame.display.set_icon(gameIcon)

pygame.mixer.set_num_channels(9)
voice1 = pygame.mixer.Channel(1)
voice2 = pygame.mixer.Channel(2)
voice3 = pygame.mixer.Channel(3)
voice4 = pygame.mixer.Channel(4)
voice5 = pygame.mixer.Channel(5)
voice6 = pygame.mixer.Channel(6)
voice7 = pygame.mixer.Channel(7)
voice8 = pygame.mixer.Channel(8)

dy = 0


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def LargeText(text, font, size, color, posx, posy):
    largeText = pygame.font.Font(font, size)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = ((posx), (posy))
    gameDisplay.blit(TextSurf, TextRect)


def SmallText(text, font, size, color, posx, posy):
    smallText = pygame.font.Font(font, size)
    TextSurf, TextRect = text_objects(text, smallText, color)
    TextRect.center = ((posx), (posy))
    gameDisplay.blit(TextSurf, TextRect)


def button(msg, textcolor, x, y, w, h, ic, ac, size, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    SmallText(msg, 'Super Mario Bros. NES.ttf', size, textcolor, x + (w / 2), y + (h / 2))


def text(message, colour, size, location):
    font = pygame.font.Font('Super Mario Bros. NES.ttf', size)
    h = font.render(message, 0, colour)
    gameDisplay.blit(h, location)


def textporsche(message, colour, size, location):
    font = pygame.font.Font('911porschav3bold.ttf', size)
    h = font.render(message, 0, colour)
    gameDisplay.blit(h, location)


randomm = pygame.image.load('Cars/CarRandom.png')
locked = pygame.image.load('Cars/CarLocked.png')
carImage = pygame.image.load('Cars/Car.png')
vivek = pygame.image.load('Cars/Vivek.png')
FordGT = pygame.image.load('Cars/Ford GT.png')
Zonda = pygame.image.load('Cars/Pagani Zonda R.png')
F40 = pygame.image.load('Cars/Ferrari F40.png')
CarreraGT = pygame.image.load('Cars/Porsche Carrera GT.png')
dulaj = pygame.image.load('Cars/dulaj.png')
car2 = pygame.image.load('Cars/Mclaren MP44.png')
thareen = pygame.image.load('Cars/Thareen.png')
janith = pygame.image.load('Cars/Janith.png')
jai = pygame.image.load('Cars/Jai.png')
sandeep = pygame.image.load('Cars/Sandeep.png')
peshala = pygame.image.load('Cars/Peshala.png')
enemy = pygame.image.load('Cars/enemy7.png')
enemy2 = pygame.image.load('Cars/enemy2.png')
vinuja = pygame.image.load('Cars/Vinuja.png')

carImageSpecs = pygame.image.load('Messages/carImageSpecs.png')
sandeepSpecs = pygame.image.load('Messages/SuppermanSpecs.png')
vivekSpecs = pygame.image.load('Messages/RoosterSpecs.png')
thareenSpecs = pygame.image.load('Messages/MoonTurtleSpecs.png')
vinujaSpecs = pygame.image.load('Messages/MalySpecs.png')
car2Specs = pygame.image.load('Messages/MclarenSpecs.png')
janithSpecs = pygame.image.load('Messages/JanithSpecs.png')
dulajSpecs = pygame.image.load('Messages/GreyhoundSpecs.png')
jaiSpecs = pygame.image.load('Messages/JaicycleSpecs.png')
peshalaSpecs = pygame.image.load('Messages/RedlineSpecs.png')
ZondaSpecs = pygame.image.load('Messages/ZondaSpecs.png')
FordGTSpecs = pygame.image.load('Messages/GT40Specs.png')
F40Specs = pygame.image.load('Messages/F40Specs.png')
CarreraGTSpecs = pygame.image.load('Messages/CarreraGTSpecs.png')
randomSpecs = pygame.image.load('Messages/RandomBase.png')
savemessage = pygame.image.load('Messages/SpecsBase.png')
InfoIcon = pygame.image.load('Messages/InfoIcon.png')
InfoBox = pygame.image.load('Messages/InfoBox.png')

accelerate = pygame.mixer.Sound('Sounds/accelerate.wav')
decelerate = pygame.mixer.Sound('Sounds/decelerate.wav')
brake = pygame.mixer.Sound('Sounds/Brake.wav')
savecar = pygame.mixer.Sound('Sounds/Pause.wav')
crash = pygame.mixer.Sound('Sounds/Collision.wav')
blank = pygame.mixer.Sound('Sounds/blank.wav')
win = pygame.mixer.Sound('Sounds/Pass1.wav')
startMusic = pygame.mixer.Sound('Sounds/Countdown.wav')

speedo = pygame.image.load('Speedometers/Speedo2.png')
speedo3 = pygame.image.load('Speedometers/Speedo3.png')

stop = pygame.image.load('Background/stop.png')
boom = [pygame.image.load('Background/blast 1.png'), pygame.image.load('Background/blast 2.png'),
        pygame.image.load('Background/blast 3.png')]
grassLeft = pygame.image.load('Background/Grass Left.png')
grassRight = pygame.image.load('Background/Grass Right.png')
miniMap = pygame.image.load('Background/Progress.png')
miniCar = pygame.image.load('Background/Small Car.png')
road = pygame.image.load('Background/Road.png')
blankk = pygame.image.load('Background/blankk.png')
start = pygame.image.load('Background/start.png')
blankpic = pygame.image.load('Background/IntroSnap.png')
bg = pygame.image.load('Background/RoadBg.png')

timing = 250
color = (255, 255, 255)

sounding = blank

jigg = 0
placey = 650
placeyy = 400
something = True
Flag = 1
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

s = -720

source = open('money.txt', 'r')
Money = int(source.read())
# Money = 0

source = open('car.txt', 'r')
Locked = str(source.read())


# print(Locked[0])
# print(Locked[2])
# print(Locked[4])

def randomcar():
    Lock = 'L'
    while Lock == 'L':
        number = random.randrange(0, 13)
        Lock = Locked[2 * number]
    if number == 0:
        return vinuja
    elif number == 1:
        return vivek
    elif number == 2:
        return thareen
    elif number == 3:
        return car2
    elif number == 4:
        return janith
    elif number == 5:
        return dulaj
    elif number == 6:
        return jai
    elif number == 7:
        return sandeep
    elif number == 8:
        return peshala
    elif number == 9:
        return carImage
    elif number == 10:
        return FordGT
    elif number == 11:
        return Zonda
    elif number == 12:
        return F40
    elif number == 13:
        return CarreraGT


def save(r):
    global Locked

    pygame.mixer.Sound.play(savecar)

    source = open('car.txt', 'w')
    for i in range(0, 14):
        if r == 2 * i:
            source.write('U' + ' ')
        else:
            source.write(Locked[2 * i] + ' ')

    source = open('car.txt', 'r')
    Locked = str(source.read())
    # print(Money)


def frame(t):
    f = t * 60
    return f


def rotate(angle):
    tatras = Image.open('GT Rotated.png')
    rotated = tatras.rotate(angle)
    rotated.save('rotated.png')


def intro():
    x1 = (displayWidth / 6) - (37 / 2)
    x2 = (3 * displayWidth / 6) - (37 / 2)
    x3 = (5 * displayWidth / 6) - (37 / 2)
    y = displayHeight - 40
    pos1 = 1280
    pos2 = 235
    pos3 = -235

    time = 0
    angle = 0

    startt = False

    while not startt:
        time += (1 / 60)
        if time < 3:
            gameDisplay.blit(bg, (0, 0))
            car(carImage, x1, y)
            car(carImage, x2, y)
            car(carImage, x3, y)
            y -= 4.8
            pygame.draw.line(gameDisplay, black, (0, 0), (0, 720), 16)
            pygame.draw.line(gameDisplay, black, (0, 0), (1280, 0), 16)
            pygame.draw.line(gameDisplay, black, (0, 720), (1280, 720), 16)
            pygame.draw.line(gameDisplay, black, (1280, 0), (1280, 720), 16)
            pygame.draw.line(gameDisplay, black, ((1256 / 3), 0), ((1256 / 3), 720), 16)
            pygame.draw.line(gameDisplay, black, ((2536 / 3), 0), ((2536 / 3), 720), 16)

            # print(time)
            if time < 0 or time > 1.5:
                pygame.draw.rect(gameDisplay, black, (0, 0, (1220 / 3) + 20, 720))
            if time < 0.5 or time > 1.5 + (1 / 3):
                pygame.draw.rect(gameDisplay, black, ((1316 / 3) - 40, 0, (1220 / 3) + 40, 720))
            if time < 1 or time > 1.5 + (2 / 3):
                pygame.draw.rect(gameDisplay, black, ((2575 / 3) - 20, 0, (1220 / 3) + 40, 720))

        if time >= 2.5:
            gameDisplay.blit(bg, (0, 0))
            rotate(angle)
            wheel = pygame.image.load('rotated.png')
            angle += 15
            gameDisplay.blit(wheel, ((displayWidth / 2) - 86, 120 - 86))
            gameDisplay.blit(wheel, ((displayWidth / 2) - 86, 360 - 86))
            # gameDisplay.blit(wheel,((displayWidth/2)-86,595-86))

            pygame.draw.line(gameDisplay, black, (0, 0), (0, 720), 16)
            pygame.draw.line(gameDisplay, black, (0, 0), (1280, 0), 16)
            pygame.draw.line(gameDisplay, black, (0, 720), (1280, 720), 16)
            pygame.draw.line(gameDisplay, black, (1280, 0), (1280, 720), 16)
            pygame.draw.line(gameDisplay, black, (0, 235), (1280, 235), 16)
            pygame.draw.line(gameDisplay, black, (0, 470), (1280, 470), 16)

            if time >= 2.5 and time <= 2.5 + 0.75:
                pygame.draw.rect(gameDisplay, black, (0, 235, pos1, 235))
                pos1 -= (1280 / 45)

                pygame.draw.rect(gameDisplay, black, (0, 235, 1280, pos2))
                pos2 -= (235 / 45)

                pygame.draw.rect(gameDisplay, black, (0, 235, 1280, pos3))
                pos3 += (235 / 45)

            if time >= 2.5 + 1.25:
                pygame.draw.rect(gameDisplay, black, (1280, 235, pos1, 235))
                pos1 -= (1280 / 45)

                pygame.draw.rect(gameDisplay, black, (0, 235, 1280, pos2))
                pos2 -= (235 / 45)

                pygame.draw.rect(gameDisplay, black, (0, 235, 1280, pos3))
                pos3 += (235 / 45)

            # if time

            if time < 2.5:
                pygame.draw.rect(gameDisplay, black, (0, 235, 1280, 235))
                pygame.draw.rect(gameDisplay, black, (0, 0, 1280, 235))
                pygame.draw.rect(gameDisplay, black, (0, 470, 1280, 250))

        if time > 5:
            startt = True

        pygame.display.update()
        clock.tick(60)


def gameIntro():
    global accelerate
    global decelerate
    global crash
    global Money
    global Flag
    d = -2698
    intro = True

    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    while intro:
        gameDisplay.blit(bg, (0, 0))
        gameDisplay.blit(grassLeft, (0, 0))
        gameDisplay.blit(grassRight, (displayWidth - 195, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return Quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    pos = pygame.mouse.get_pos()
                    if 669.5 >= pos[0] >= 621.5 and 407.5 >= pos[1] >= 352.5 and Locked[2] == 'L' and Money >= 1000:
                        Money = Money - 1000
                        save(2)
                    elif 978.5 >= pos[0] >= 941.5 and 390.5 >= pos[1] >= 353.5 and Locked[6] == 'L' and Money >= 1000:
                        Money = Money - 1000
                        save(6)
                    elif 514.5 >= pos[0] >= 460.5 and 392 >= pos[1] >= 353 and Locked[0] == 'L' and Money >= 1000:
                        Money = Money - 1000
                        save(0)
                    elif 837.5 >= pos[0] >= 781.5 and 392 >= pos[1] >= 353 and Locked[4] == 'L' and Money >= 1000:
                        Money = Money - 1000
                        save(4)
                    elif 514.5 >= pos[0] >= 460.5 and 487 >= pos[1] >= 450 and Locked[8] == 'L' and Money >= 1000:
                        Money = Money - 1000
                        save(8)
                    elif 837.5 >= pos[0] >= 781.5 and 487 >= pos[1] >= 450 and Locked[12] == 'L' and Money >= 1000:
                        Money = Money - 1000
                        save(12)
                    elif 675.5 >= pos[0] >= 621.5 and 487 >= pos[1] >= 450 and Locked[10] == 'L' and Money >= 1000:
                        Money = Money - 1000
                        save(10)
                    elif 514.5 >= pos[0] >= 460.5 and 582 >= pos[1] >= 545 and Locked[14] == 'L' and Money >= 1000:
                        Money = Money - 1000
                        save(14)
                    elif 675.5 >= pos[0] >= 621.5 and 582 >= pos[1] >= 545 and Locked[16] == 'L' and Money >= 1000:
                        Money = Money - 1000
                        save(16)
                    elif 354.5 >= pos[0] >= 301.5 and 582 >= pos[1] >= 545 and Locked[20] == 'L' and Money >= 1000:
                        Money = Money - 1000
                        save(20)
                    elif 978.5 >= pos[0] >= 941.5 and 487 >= pos[1] >= 450 and Locked[22] == 'L' and Money >= 1000:
                        Money = Money - 1000
                        save(22)
                    elif 837.5 >= pos[0] >= 781.5 and 582 >= pos[1] >= 545 and Locked[24] == 'L' and Money >= 1000:
                        Money = Money - 1000
                        save(24)
                    elif 978.5 >= pos[0] >= 941.5 and 582 >= pos[1] >= 545 and Locked[26] == 'L' and Money >= 1000:
                        Money = Money - 1000
                        save(26)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 354.5 >= pos[0] >= 301.5 and 390.5 >= pos[1] >= 353.5:
                    carSelect = carImage
                elif 669.5 >= pos[0] >= 621.5 and 407.5 >= pos[1] >= 352.5 and Locked[2] != 'L':
                    carSelect = vivek
                elif 978.5 >= pos[0] >= 941.5 and 390.5 >= pos[1] >= 353.5 and Locked[6] != 'L':
                    carSelect = car2
                elif 514.5 >= pos[0] >= 460.5 and 392 >= pos[1] >= 353 and Locked[0] != 'L':
                    carSelect = vinuja
                elif 837.5 >= pos[0] >= 781.5 and 392 >= pos[1] >= 353 and Locked[4] != 'L':
                    carSelect = thareen
                elif 514.5 >= pos[0] >= 460.5 and 487 >= pos[1] >= 450 and Locked[8] != 'L':
                    carSelect = janith
                elif 837.5 >= pos[0] >= 781.5 and 487 >= pos[1] >= 450 and Locked[12] != 'L':
                    carSelect = jai
                elif 675.5 >= pos[0] >= 621.5 and 487 >= pos[1] >= 450 and Locked[10] != 'L':
                    carSelect = dulaj
                elif 514.5 >= pos[0] >= 460.5 and 582 >= pos[1] >= 545 and Locked[14] != 'L':
                    carSelect = sandeep
                elif 675.5 >= pos[0] >= 621.5 and 582 >= pos[1] >= 545 and Locked[16] != 'L':
                    carSelect = peshala
                elif 354.5 >= pos[0] >= 301.5 and 582 >= pos[1] >= 545 and Locked[18] != 'L':
                    carSelect = FordGT
                elif 978.5 >= pos[0] >= 941.5 and 487 >= pos[1] >= 450 and Locked[20] != 'L':
                    carSelect = Zonda
                elif 837.5 >= pos[0] >= 781.5 and 582 >= pos[1] >= 545 and Locked[22] != 'L':
                    carSelect = F40
                elif 978.5 >= pos[0] >= 941.5 and 582 >= pos[1] >= 545 and Locked[24] != 'L':
                    carSelect = CarreraGT
                elif 354.5 >= pos[0] >= 301.5 and 487 >= pos[1] >= 450:
                    carSelect = randomcar()

                # elif (displayWidth >= pos[0] >= displayWidth-59 and 130+42 >= pos[1] >= 130) or Flag == 1:
                # gameDisplay.blit(InfoBox,(displayWidth-525,130))
                # Flag = 1

                ## time.sleep(3000)
        ##      text(message,colour,size,location)
        text('Road', (0, 0, 255), 60, (530, 100))
        text('Fighters', (255, 0, 0), 60, (415, 170))
        pygame.draw.rect(gameDisplay, (255, 255, 255), (displayWidth - 260, 90, 210, 40))
        text(format(Money, '09d'), (0, 0, 0), 20, (displayWidth - 250, 100))
        gameDisplay.blit(InfoIcon, (displayWidth - 59, 130))

        pos = pygame.mouse.get_pos()
        if (displayWidth >= pos[0] >= displayWidth - 59 and 130 + 42 >= pos[1] >= 130):
            gameDisplay.blit(InfoBox, (displayWidth - 525, 130))
        elif 354.5 >= pos[0] >= 301.5 and 390.5 >= pos[1] >= 353.5:
            gameDisplay.blit(carImageSpecs, (377.5, 50))
        elif 669.5 >= pos[0] >= 621.5 and 407.5 >= pos[1] >= 352.5:
            gameDisplay.blit(vivekSpecs, (377.5, 50))
        elif 978.5 >= pos[0] >= 941.5 and 390.5 >= pos[1] >= 353.5:
            gameDisplay.blit(car2Specs, (377.5, 50))
        elif 514.5 >= pos[0] >= 460.5 and 392 >= pos[1] >= 353:
            gameDisplay.blit(vinujaSpecs, (377.5, 50))
        elif 837.5 >= pos[0] >= 781.5 and 392 >= pos[1] >= 353:
            gameDisplay.blit(thareenSpecs, (377.5, 50))
        elif 514.5 >= pos[0] >= 460.5 and 487 >= pos[1] >= 450:
            gameDisplay.blit(janithSpecs, (377.5, 50))
        elif 837.5 >= pos[0] >= 781.5 and 487 >= pos[1] >= 450:
            gameDisplay.blit(jaiSpecs, (377.5, 50))
        elif 675.5 >= pos[0] >= 621.5 and 487 >= pos[1] >= 450:
            gameDisplay.blit(dulajSpecs, (377.5, 50))
        elif 514.5 >= pos[0] >= 460.5 and 582 >= pos[1] >= 545:
            gameDisplay.blit(sandeepSpecs, (377.5, 50))
        elif 675.5 >= pos[0] >= 621.5 and 582 >= pos[1] >= 545:
            gameDisplay.blit(peshalaSpecs, (377.5, 50))
        elif 354.5 >= pos[0] >= 301.5 and 582 >= pos[1] >= 545:
            gameDisplay.blit(FordGTSpecs, (377.5, 50))
        elif 978.5 >= pos[0] >= 941.5 and 487 >= pos[1] >= 450:
            gameDisplay.blit(ZondaSpecs, (377.5, 50))
        elif 837.5 >= pos[0] >= 781.5 and 582 >= pos[1] >= 545:
            gameDisplay.blit(F40Specs, (377.5, 50))
        elif 978.5 >= pos[0] >= 941.5 and 582 >= pos[1] >= 545:
            gameDisplay.blit(CarreraGTSpecs, (377.5, 50))
        elif 354.5 >= pos[0] >= 301.5 and 487 >= pos[1] >= 450:
            gameDisplay.blit(randomSpecs, (377.5, 50))

        gameDisplay.blit(randomm, (301.5, 450))
        gameDisplay.blit(carImage, (301.5, 353.5))
        if Locked[0] == 'L':
            gameDisplay.blit(locked, (460.5, 353))
        else:
            gameDisplay.blit(vinuja, (460.5, 353))

        if Locked[2] == 'L':
            gameDisplay.blit(locked, (621.5, 352.5))
        else:
            gameDisplay.blit(vivek, (621.5, 352.5))

        if Locked[4] == 'L':
            gameDisplay.blit(locked, (781.5, 353.5))
        else:
            gameDisplay.blit(thareen, (781.5, 353.5))

        if Locked[6] == 'L':
            gameDisplay.blit(locked, (941.5, 353.5))
        else:
            gameDisplay.blit(car2, (941.5, 353.5))

        if Locked[8] == 'L':
            gameDisplay.blit(locked, (460.5, 450))
        else:
            gameDisplay.blit(janith, (460.5, 450))

        if Locked[10] == 'L':
            gameDisplay.blit(locked, (621.5, 450))
        else:
            gameDisplay.blit(dulaj, (621.5, 450))

        if Locked[12] == 'L':
            gameDisplay.blit(locked, (781.5, 450))
        else:
            gameDisplay.blit(jai, (781.5, 450))

        if Locked[14] == 'L':
            gameDisplay.blit(locked, (460.5, 545))
        else:
            gameDisplay.blit(sandeep, (460.5, 545))

        if Locked[16] == 'L':
            gameDisplay.blit(locked, (621.5, 545))
        else:
            gameDisplay.blit(peshala, (621.5, 545))

        if Locked[20] == 'L':
            gameDisplay.blit(locked, (301.5, 545))
        else:
            gameDisplay.blit(FordGT, (301.5, 545))

        if Locked[22] == 'L':
            gameDisplay.blit(locked, (941.5, 450))
        else:
            gameDisplay.blit(Zonda, (941.5, 450))

        if Locked[24] == 'L':
            gameDisplay.blit(locked, (781.5, 545))
        else:
            gameDisplay.blit(F40, (781.5, 545))

        if Locked[26] == 'L':
            gameDisplay.blit(locked, (941.5, 545))
        else:
            gameDisplay.blit(CarreraGT, (941.5, 545))

        pygame.display.update()
        clock.tick(60)
        try:
            if carSelect == carImage or carSelect == CarreraGT or carSelect == F40 or carSelect == Zonda or carSelect == FordGT or carSelect == vivek or carSelect == car2 or carSelect == peshala or carSelect == dulaj or carSelect == vinuja or carSelect == thareen or carSelect == janith or carSelect == jai or carSelect == sandeep:
                if carSelect == sandeep:
                    accelerate = pygame.mixer.Sound('Sounds/swoosh.wav')
                    decelerate = pygame.mixer.Sound('Sounds/Blank.wav')
                    crash = pygame.mixer.Sound('Sounds/ouch.wav')
                if carSelect == thareen:
                    crash = pygame.mixer.Sound('Sounds/thareenFail.wav')
                if carSelect == peshala:
                    accelerate = pygame.mixer.Sound('Sounds/pAccelerate.wav')
                    decelerate = pygame.mixer.Sound('Sounds/pDecelerate.wav')
                break
        except:
            continue
    return carSelect
    # play video, blit images:choose car, car, creator image


def car(image, x, y):
    gameDisplay.blit(image, (x, y))


def score(jig):
    global jigg
    text('score', (255, 255, 255), 20, (50, 260))
    jigg += round(jig)
    text(format(jigg, '010d'), (255, 255, 255), 20, (50, 290))


def timer():
    global something
    global timing
    global color
    if not voice6.get_busy(): voice6.play(sounding)
    text('time', (255, 255, 255), 20, (50, 360))
    text(str(int(timing)), color, 20, (50, 390))
    timing -= 0.15
    if timing <= 15:
        color = (255, 0, 0)


def progression(integer):
    global dy
    global placey
    global placeyy
    global color
    color = (255, 255, 255)
    gameDisplay.blit(miniCar, (455, placey))
    placey -= integer / 100

    if placey <= 700:
        gameDisplay.blit(start, (673, placeyy))
        placeyy += integer


def Crash(x, y):
    global accelerate
    global decelerate
    global crash
    global timing
    global sounding
    global placey
    global jigg
    global placeyy
    global something
    global Money
    global s
    # print(jigg)
    accelerate = pygame.mixer.Sound('Sounds/accelerate.wav')
    decelerate = pygame.mixer.Sound('Sounds/decelerate.wav')
    voice1.stop()
    voice2.stop()
    voice3.stop()
    voice4.stop()
    voice5.stop()
    voice6.stop()
    voice7.stop()
    something = True
    sounding = pygame.mixer.Sound('Sounds/blank.wav')
    Money = Money + round(jigg / 100)
    source = open('money.txt', 'w')
    source.write(str(Money))
    source = open('money.txt', 'r')
    Money = int(source.read())
    # print(Money)
    placey = 650
    placeyy = 400
    color = (255, 255, 255)
    voice4.play(crash)
    crash = pygame.mixer.Sound('Sounds/Collision.wav')
    ##    with open('Score.txt','a') as scoree:
    ##        scoree.write('      ')
    ##        scoree.write(str(int(jigg+timing)))
    timing = 250
    jigg = 0
    for _ in range(6):
        for f in range(len(boom)):
            gameDisplay.blit(boom[f], (x, y))
            time.sleep(0.15)
            pygame.display.flip()
    gameDisplay.blit(blankpic, (0, s))
    s = s + 12
    jigg = 0
    gameloop(gameIntro())


def obstacle(c, speed):
    gameDisplay.blit(enemy, (c, speed))


def obstacle2(c, speed):
    gameDisplay.blit(enemy2, (c, speed))


def gameloop(carGraphic):
    global timing
    global dy
    ##    pygame.mixer.pre_init(44100, -16, 1, 512)
    ##    pygame.init()
    gameDisplay.fill((0, 0, 0))
    stopPos = -60000
    x = 834.2
    t = random.randrange(int(x - 100), int(x + 100))
    while t < 673 or t + 37 > 1074:
        t = random.randrange(int(x - 100), int(x + 100))
    s = random.randrange(673, 1019)
    y = 600
    dx = 0
    dy = 0
    a = random.randrange(0, 3)
    if a <= 1:
        grassLeft = pygame.image.load('Background/Canyon Left.png')
        grassRight = pygame.image.load('Background/Canyon Right.png')
    else:
        grassLeft = pygame.image.load('Background/Grass Left.png')
        grassRight = pygame.image.load('Background/Grass Right.png')
    grassSpeed = -382
    speed = -314.666666667
    enemySpeed = -63
    enemySpeed2 = -126
    voice5.play(startMusic)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -0.20 * dy
                elif event.key == pygame.K_RIGHT:
                    dx = 0.20 * dy
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    dx += 0.20 * dy
                elif event.key == pygame.K_RIGHT:
                    dx += -0.20 * dy
                if event.key == pygame.K_UP:

                    if dy != 0: dy -= 5
                elif event.key == pygame.K_DOWN:
                    if dy != 0: dy += 5

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 1005 >= pos[0] >= 742:
                    swipestart = pos

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if 1005 >= pos[0] >= 742:
                    swipestop = pos
                    if swipestart[1] - swipestop[1] >= 125:
                        print('swipe up')
                    elif swipestart[1] - swipestop[1] <= 125:
                        print('swipe down')

        gameDisplay.blit(blankk, (0, 0))

        r = 230 + (dy * 25 / 50.4)
        g = 184 - (dy * 184 / 50.4)
        b = 92 - (dy * 92 / 50.4)
        if carGraphic == janith or carGraphic == car2:
            S = ((((180 * dy) / 50.4)) * math.pi) / 180
            speedreadout = str(format(round(dy * 10), '03d'))
            gameDisplay.blit(speedo3, (200 - 125, 550 - 150 / 4))
            if dy <= 0:
                pygame.draw.arc(gameDisplay, (r, g, b), (200 - 90, 550, 180, 180), math.pi - 0.01, math.pi, 7)
            else:
                pygame.draw.arc(gameDisplay, (r, g, b), (200 - 90, 550, 180, 180), math.pi - S, math.pi, 7)
            textporsche(speedreadout, white, 25, (150, 600))
        elif carGraphic == sandeep:
            c1 = (100 + (dy * 50) / 50.4, 650 - (dy * 150) / 50.4)
            c2 = (100 + 55, 650 - (dy * 150) / 50.4)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    c3 = (180, 500)
                    c4 = (220, 500)
                    cc = (200, 500)
                elif event.key == pygame.K_DOWN:
                    c3 = (180, 650)
                    c4 = (220, 650)
                    cc = (200, 500)
            else:
                c3 = (180, 575)
                c4 = (220, 575)
                cc = (200, 500)

            c5 = (300 - 55, 650 - (dy * 150) / 50.4)
            c6 = (300 - (dy * 50) / 50.4, 650 - (dy * 150) / 50.4)
            pygame.draw.line(gameDisplay, red, (100, 650), (150, 500), 2)
            pygame.draw.line(gameDisplay, red, (300, 650), (250, 500), 2)
            pygame.draw.line(gameDisplay, green, (100 - 3, 650), (150 - 3, 500), 2)
            pygame.draw.line(gameDisplay, green, (300 + 3, 650), (250 + 3, 500), 2)
            pygame.draw.line(gameDisplay, blue, (200, 650), (200, 500), 2)
            pygame.draw.line(gameDisplay, white, c1, c2, 2)
            pygame.draw.line(gameDisplay, white, c2, c3, 2)
            pygame.draw.line(gameDisplay, white, c3, c4, 2)
            pygame.draw.line(gameDisplay, white, c4, c5, 2)
            pygame.draw.line(gameDisplay, white, c5, c6, 2)
            textporsche('0', white, 20, (100 - 30, 650))
            textporsche('1', white, 20, (110 - 30, 650 - 30))
            textporsche('2', white, 20, (120 - 30, 650 - 60))
            textporsche('3', white, 20, (130 - 30, 650 - 90))
            textporsche('4', white, 20, (140 - 30, 650 - 120))
            textporsche('5', white, 20, (150 - 30, 650 - 150))
            textporsche('0', white, 20, (300 + 30, 650))
            textporsche('1', white, 20, (290 + 30, 650 - 30))
            textporsche('2', white, 20, (280 + 30, 650 - 60))
            textporsche('3', white, 20, (270 + 30, 650 - 90))
            textporsche('4', white, 20, (260 + 30, 650 - 120))
            textporsche('5', white, 20, (250 + 30, 650 - 150))
            text('Mach', white, 10, (160 - 30, 650 - 180))
            # pygame.draw.circle(gameDisplay,white,cc,10,2)

        else:
            # redline.speedo(1,dy)
            R = ((((225 * dy) / 50.4) - 45) * math.pi) / 180
            gameDisplay.blit(speedo, (200 - 95, 550 - 95))
            pygame.draw.line(gameDisplay, (r, g, b), (200, 550), (200 - 90 * math.cos(R), 550 - 90 * math.sin(R)), 5)

        if timing <= 0: Crash(x, y)
        L = pygame.key.get_pressed()
        if not voice5.get_busy():
            timer()
        if L[pygame.K_UP] and not voice5.get_busy():
            if voice2.get_busy: voice2.stop()
            voice1.set_volume(500)
            voice3.set_volume(0)
            if voice3.get_busy: voice3.play(decelerate)
            if dy <= 50: dy += 0.6
        if L[pygame.K_DOWN] and not voice5.get_busy():
            if dy > 0: dy -= 1
            if voice1.get_busy: voice1.stop()
            voice2.set_volume(500)
        if not L[pygame.K_UP] and not voice5.get_busy():
            voice3.set_volume(500)
            voice1.set_volume(0)
            if voice1.get_busy:
                voice1.play(accelerate)
            if dy > 5: dy -= 0.1
        if not L[pygame.K_DOWN] and not voice5.get_busy():
            voice2.set_volume(0)
            if voice2.get_busy and dy >= 35:
                voice3.set_volume(500)
                voice2.play(brake)
            else:
                voice2.stop()
        if 673.5 < x < 1030:
            x += dx
        else:
            Crash(x, y)
        if (y + 71 > enemySpeed and y < enemySpeed + 71) and (x > s and x < s + 46 or x + 46 > s and x + 46 < s + 46):
            Crash(x, y)
        if (y + 71 > enemySpeed2 and y < enemySpeed2 + 71) and (x > t and x < t + 46 or x + 46 > t and x + 46 < t + 46):
            Crash(x, y)
        if stopPos >= 600:
            global sounding
            global placey
            global jigg
            global placeyy
            global something
            something = True
            timing = 250
            jigg = 0
            sounding = pygame.mixer.Sound('Sounds/blank.wav')
            placey = 650
            placeyy = 400
            color = (255, 255, 255)
            voice1.stop()
            voice2.stop()
            voice3.stop()
            voice4.stop()
            voice5.stop()
            voice6.stop()
            voice7.stop()
            voice8.play(win)
            Money = Money + jigg
            source = open('money.txt', 'w')
            source.write(str(Money))
            source = open('money.txt', 'r')
            Money = int(source.read())
            time.sleep(6)
            ##            with open('Score.txt','a') as scoree:
            ##                scoree.write('      ')
            ##                scoree.write(str(int(jigg+timing)))
            gameloop(gameIntro())
            break
        if grassSpeed <= 0:
            grassSpeed += dy
            gameDisplay.blit(grassLeft, (478, grassSpeed))
            gameDisplay.blit(grassRight, (1074, grassSpeed))
        else:
            grassSpeed = -582
        if speed <= -55:
            speed += dy
            gameDisplay.blit(road, (673, speed))
        else:
            speed = -314.6666666667
        if enemySpeed <= 720:
            enemySpeed += -5 + dy / 1.5
            obstacle(s, enemySpeed)
        else:
            s = random.randrange(673, 1019)
            enemySpeed = -46
        if enemySpeed2 <= 720:
            enemySpeed2 += -5 + dy / 1.5
            obstacle2(t, enemySpeed2)
        else:
            t = random.randrange(int(x - 100), int(x + 100))
            while t < 673 or t + 37 > 1074:
                t = random.randrange(int(x - 100), int(x + 100))
            enemySpeed2 = -92
        gameDisplay.blit(miniMap, (447, 0))
        gameDisplay.blit(stop, (673, stopPos))
        stopPos += dy
        score(dy)
        progression(dy)
        car(carGraphic, x, y)
        pygame.display.flip()
        clock.tick(100)


# intro()
gameloop(gameIntro())
