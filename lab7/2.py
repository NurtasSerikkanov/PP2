import pygame
pygame.init()

WIDTH, HEIGHT=400, 870
FPS=20

screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Music')

clock=pygame.time.Clock()

finished=False

playlist = list()
playlist.append ( "./music/Andro- Как не любить.mp3" )
playlist.append ( "./music/Chlara-The Nights.mp3" )
playlist.append ( "./music/Glass_Animals-Heat_Waves .mp3" )
playlist.append ( "./music/Juice Wrld and Halsey - Without Me.mp3" )
playlist.append ( "./music/Lewis Capaldi - Someone You Loved.mp3" )
playlist.append ( "./music/Ludovico Einaudi, Daniel Hope - Experience.mp3" )
playlist.append ( "./music/Monoir, Eneli - 3 to 1.mp3" )

pygame.mixer.music.load(playlist.pop()) 
# pygame.mixer.music.queue("./music/Ludovico Einaudi, Daniel Hope - Experience.mp3") 
pygame.mixer.music.set_endevent(pygame.USEREVENT)    
pygame.mixer.music.play() 

image=list()
image.append("./img2/Как не любить.jpeg")
image.append("./img2/The Nights.jpeg")
image.append("./img2/Heat Waves.jpeg")
image.append("./img2/Without me.jpeg")
image.append("./img2/Someone You Loved.jpeg")
image.append("./img2/Experience.jpeg")
image.append("./img2/3 to 1.jpeg")
          
img=pygame.image.load(image.pop())

def nextsong():
    global playlist
    playlist = playlist[1:] + [playlist[0]]
    pygame.mixer.music.load(playlist[0])
    pygame.mixer.music.play()

def prevsong():
    global playlist
    playlist = [playlist[-1]] + playlist[:-1]
    pygame.mixer.music.load(playlist[0])
    pygame.mixer.music.play()

while not finished:
    clock.tick(FPS)

    music_number=0

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            finished=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                pygame.mixer.music.stop()
                nextsong()
                image = image[1:] + [image[0]]
                img=pygame.image.load(image[0])
            if event.key==pygame.K_RIGHT:
                pygame.mixer.music.stop()
                prevsong()
                image = [image[-1]] + image[:-1]
                img=pygame.image.load(image[0])
            if event.key==pygame.K_SPACE:
                pygame.mixer.music.pause()
            if event.key==pygame.K_s:
                pygame.mixer.music.unpause()
            if event.key==pygame.K_1:
                pygame.mixer.music.set_volume(0.5)
            if event.key==pygame.K_2:
                pygame.mixer.music.set_volume(1)

        # if event.type == pygame.USEREVENT:    
        #     if len(playlist)>0:       
        #         pygame.mixer.music.queue(playlist.pop())
    
    screen.blit(img, (0, 0))
    pygame.display.flip()
pygame.quit()