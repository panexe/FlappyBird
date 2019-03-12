import pygame
import random
import sys

pygame.init()





class game(object):

    def __init__(self):
        self.FPS = 30
        self.delay = int( (1/self.FPS)*1000)
        self.screenWidth = 288
        self.screenHeight = 512
        self.pipe_gap = 100
        self.SCREEN = pygame.display.set_mode((self.screenWidth,self.screenHeight))
        self.score = 0
        self.IMAGES = {}
        self.HITMASKS = {}
        self.pipe_x = self.screenWidth
        self.pipe_y = 300
        self.bird_y = self.screenHeight * 0.5
        self.bird_x = 75
        self.bird_tex_index = 0
        self.ground_y = 400
        self.running = True
        # the vertical amount the bird moves (+ for down, - for up)
        self.vert_speed = 0
        # how much the bird is elevated when 'flapped'
        self.jump_speed = -9
        # how much the bird is pulled down every frame
        self.gravity = -1

        self.jump = False

        # loading all Textures and Images
        self.IMAGES['numbers'] = (pygame.transform.scale2x(pygame.image.load('./assets/num_0.png')),
                                  pygame.transform.scale2x(pygame.image.load('./assets/num_1.png')),
                                  pygame.transform.scale2x(pygame.image.load('./assets/num_2.png')),
                                  pygame.transform.scale2x(pygame.image.load('./assets/num_3.png')),
                                  pygame.transform.scale2x(pygame.image.load('./assets/num_4.png')),
                                  pygame.transform.scale2x(pygame.image.load('./assets/num_5.png')),
                                  pygame.transform.scale2x(pygame.image.load('./assets/num_6.png')),
                                  pygame.transform.scale2x(pygame.image.load('./assets/num_7.png')),
                                  pygame.transform.scale2x(pygame.image.load('./assets/num_8.png')),
                                  pygame.transform.scale2x(pygame.image.load('./assets/num_9.png')))

        self.IMAGES["bg"] = pygame.transform.scale2x(pygame.image.load("./assets/background.png"))
        self.IMAGES["ground"] = pygame.transform.scale2x(pygame.image.load("./assets/ground.png"))

        self.IMAGES["bird"] = (pygame.transform.rotate(pygame.transform.scale2x(pygame.image.load("./assets/bird1.png")),30),
                               pygame.transform.rotate(pygame.transform.scale2x(pygame.image.load("./assets/bird2.png")),-30),
                               pygame.transform.scale2x(pygame.image.load("./assets/bird3.png")))

        self.IMAGES["pipe"] = (pygame.transform.scale2x(pygame.image.load("./assets/pipe_up.png")),
                               pygame.transform.scale2x(pygame.image.load("./assets/pipe_down.png")))

        self.IMAGES["playbutton"] = pygame.transform.scale2x(pygame.image.load("./assets/play_button.png"))



        # getting the hitmasks (hitboxes) for pipe & bird
        self.HITMASKS["pipe"] = (self.getHitmask(self.IMAGES["pipe"][0]),
                                 self.getHitmask(self.IMAGES["pipe"][1]))
        self.HITMASKS["bird"] = (self.getHitmask(self.IMAGES["bird"][0]),
                                 self.getHitmask(self.IMAGES["bird"][1]),
                                 self.getHitmask(self.IMAGES["bird"][2]))
        self.HITMASKS["ground"] = self.getHitmask(self.IMAGES["ground"])
        self.HITMASKS["ground"][1] = self.ground_y


        self.main()

    def update_hitboxes(self):
        self.HITMASKS["pipe"][0][0] = self.pipe_x
        self.HITMASKS["pipe"][0][1] = self.pipe_y
        self.HITMASKS["pipe"][1][0] = self.pipe_x
        self.HITMASKS["pipe"][1][1] = self.pipe_y -self.pipe_gap - int(self.HITMASKS["pipe"][1][3])

        self.HITMASKS["bird"][0][0] = self.bird_x
        self.HITMASKS["bird"][0][1] = self.bird_y

    def getHitmask(self,image):
    #returns a hitmask using an image's alpha.
        mask = []
        mask = image.get_rect()
        return mask


    def draw(self):
        #-------------------------------------------------------------------
        # this method draws all the objects to the screen
        # the farthest back object has to be drawn first
        #------------------------------------------------------------------
        self.SCREEN.blit(self.IMAGES["bg"],(0,0))
        self.SCREEN.blit(self.IMAGES["bird"][self.bird_tex_index], (self.bird_x,self.bird_y))

        self.SCREEN.blit(self.IMAGES["pipe"][0], (self.pipe_x,self.pipe_y))
        self.SCREEN.blit(self.IMAGES["pipe"][1], (self.pipe_x,self.pipe_y -self.pipe_gap - int(self.HITMASKS["pipe"][1][3])))

        # draw the score in numbers
        for i in range(0,len(str(self.score ))):
            self.SCREEN.blit(self.IMAGES["numbers"][int(str(self.score)[i])],(int(self.screenWidth / 2 + i *24),20))

        self.SCREEN.blit(self.IMAGES["ground"],(0,self.ground_y))
        pygame.display.update()

    def new_pipe(self):
        # update the pipe position to the right of the screen and set a new height
        self.pipe_y = random.randint(200,300)
        self.pipe_x = self.screenWidth
        self.score += 1


    def check_collision(self):
        # --------------------------------------------------------------
        # checks the collision of the bird and both of the pipes and the ground
        # returns false if collided
        #----------------------------------------------------------------
        if self.HITMASKS["bird"][0].colliderect(self.HITMASKS["pipe"][0]):
            print("HIT" + str(random.randint(0,100)))
            return False
        if self.HITMASKS["bird"][0].colliderect(self.HITMASKS["pipe"][1]):
            print("HIT" + str(random.randint(0,100)))
            return False
        if self.HITMASKS["bird"][0].colliderect(self.HITMASKS["ground"]):
            print("HIT" + str(random.randint(0,100)))
            return False

        return True


    def main(self):
        # ------------------------------------------------------------------
        # the main game loop
        # here runs the whole game
        #-------------------------------------------------------------------

        # setting the screen
        #SCREEN = pygame.display.set_mode((self.screenWidth,self.screenHeight))
        pygame.display.set_caption('Flappy Bird')

        self.draw()

        # waiting at the start of the game so the player has a chance to start
        self.wait_for_input()

        # main game loop
        while self.running:
            # fps as delay i n ms
            pygame.time.delay(self.delay)

            # player inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.vert_speed = self.jump_speed

            # drawing images to the screen
            self.draw()



            # update values
            self.pipe_x -= 10
            #print(self.pipe_x)

            if self.pipe_x + int(self.HITMASKS["pipe"][0][2]) - 5 < 0 :
                self.new_pipe()

            self.bird_y += self.vert_speed
            self.vert_speed -= self.gravity

            if self.vert_speed <= 4:
                self.bird_tex_index = 0
            else:
                self.bird_tex_index = 1

            self.update_hitboxes()
            self.running = self.check_collision()

    def wait_for_input(self):
        # ------------------------------------------------------------------
        # this method waits for a pressed space at the beginning of the game
        #-------------------------------------------------------------------
        while True:

            # getting the user inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return 0

g = game()
