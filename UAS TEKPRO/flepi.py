import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 500
screen_height = 650

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Gary')

#font
font = pygame.font.SysFont('Bauhaus 93', 50)
white = (255, 255, 255)

#game variables
ground_scroll = 0
scroll_speed = 3
terbang = False
jatuh = False
pipe_gap = 200
pipe_frequency = 1500 #ms
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False


#load images
bg = pygame.image.load(r'D:\belajar\Test\UAS TEKPRO\bg.png')
ground_img = pygame.image.load(r'D:\belajar\Test\UAS TEKPRO\ground.png')
button_img = pygame.image.load(r'D:\belajar\Test\UAS TEKPRO\restart.png')

def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))


def reset_game():
	pipe_group.empty()
	flappy.rect.x = 100
	flappy.rect.y = int(screen_height / 2)
	score = 0
	return score


class Bird(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.index = 0
		self.counter = 0
		for num in range(1, 4):
			img = pygame.image.load(f'D:/belajar/Test/UAS TEKPRO/bird{num}.png')
			self.images.append(img)
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.vel = 0
		self.clicked = False

	def update(self):

		#GRAVITY BOY
		if terbang == True :
			self.vel += 0.5
			if self.vel > 8:
				self.vel = 8
			if self.rect.bottom < 600:
				self.rect.y += int(self.vel)

		if jatuh == False:
			#TERBANG CUY
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False :
				self.clicked = True
				self.vel = -7
			if pygame.mouse.get_pressed()[0] == 0 :
				self.clicked = False

			#anuin animasinya burung
			self.counter += 1
			flap_cooldown = 5

			if self.counter > flap_cooldown:
				self.counter = 0
				self.index += 1
				if self.index >= len(self.images):
					self.index = 0
			self.image = self.images[self.index]

			#burung jatuh
			self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
		else:
			self.image = pygame.transform.rotate(self.images[self.index], -90)


			
class Pipe(pygame.sprite.Sprite):
	def __init__(self, x, y, position):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(r'D:\belajar\Test\UAS TEKPRO\pipe.png')
		self.rect = self.image.get_rect()
		#posisi 1 atas, -1 bawah
		if position == 1 :
			self.image = pygame.transform.flip(self.image, False, True)
			self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
		if position == -1:
			self.rect.topleft = [x, y + int(pipe_gap / 2)] 

	def update(self):
		self.rect.x -= scroll_speed
		if self.rect.right < 0:
			self.kill()


class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

	def draw(self):

		action = False
		
		#baca posisi mouse
		pos = pygame.mouse.get_pos()

		#cek mouse diatas restart
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				action = True

		#muncul tombol
		screen.blit(self.image, (self.rect.x, self.rect.y))
		
		return action

bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))

bird_group.add(flappy)

#instansi restart
button = Button(screen_width // 2 - 50, screen_height // 2 - 100, button_img)

run = True
while run:

	clock.tick(fps)

	#draw background
	screen.blit(bg, (0,0))

	bird_group.draw(screen)
	bird_group.update()
	pipe_group.draw(screen)

	#animasi tanah
	screen.blit(ground_img, (ground_scroll, 600))

	#cek score
	if len(pipe_group) > 0:
		if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
			and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
			and pass_pipe == False:
			pass_pipe = True
		if pass_pipe == True:
			if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
				score += 1
				pass_pipe = False



	draw_text(str(score), font, white, int(screen_width / 2), 20)

	#nabrak
	if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
		jatuh = True

	#burung jatuh
	if flappy.rect.bottom >= 600:
		jatuh = True
		terbang = False

	if jatuh == False and terbang == True:

		#pipa baru
		time_now = pygame.time.get_ticks()
		if time_now - last_pipe > pipe_frequency:
			pipe_height = random.randint(-100, 100)
			btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
			top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1)
			pipe_group.add(btm_pipe)
			pipe_group.add(top_pipe)
			last_pipe = time_now

		#tanah
		ground_scroll -= scroll_speed
		if abs(ground_scroll) > 35:
			ground_scroll = 0

		pipe_group.update()



	#cek jatuh apa tak
	if jatuh == True:
		if button.draw() == True:
			jatuh = False
			score = reset_game()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN and terbang == False and jatuh == False:
			terbang = True

	pygame.display.update()

pygame.quit()