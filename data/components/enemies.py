__author__ = 'CPSC 386 Dai Kieu, Trong To, Carlos Serna'


import pygame as pg
from .. import setup
from .. import settings as s


class Enemy(pg.sprite.Sprite):
    """Base class for all enemies (Goombas, Koopas, ets.)"""
    def __init__(self):
        pg.sprite.Sprite.__init__(self)


    def setup_enemy(self, x, y, direction, name, setup_frames):
        """Sets up various values for enemy"""
        self.sprite_sheet = setup.GFX['smb_enemies_sheet']
        self.frames = []
        self.frame_index = 0
        self.animate_timer = 0
        self.death_timer = 0
        self.gravity = 1.5
        self.state = s.WALK

        self.name = name
        self.direction = direction
        setup_frames()

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.set_velocity()


    def set_velocity(self):
        """Sets velocity vector based on direction"""
        if self.direction == s.LEFT:
            self.x_vel = -2
        else:
            pg.transform.flip(self.frames[0], False, True)
            self.x_vel = 2

        self.y_vel = 0


    def get_image(self, x, y, width, height):
        """Get the image frames from the sprite sheet"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(s.BLACK)


        image = pg.transform.scale(image,
                                   (int(rect.width*s.SIZE_MULTIPLIER),
                                    int(rect.height*s.SIZE_MULTIPLIER)))
        return image


    def handle_state(self):
        """Enemy behavior based on state"""
        if self.state == s.WALK:
            self.walking()
        elif self.state == s.FALL:
            self.falling()
        elif self.state == s.JUMPED_ON:
            self.jumped_on()
        elif self.state == s.SHELL_SLIDE:
            self.shell_sliding()
        elif self.state == s.DEATH_JUMP:
            self.death_jumping()


    def walking(self):
        """Default state of moving sideways"""
        if (self.current_time - self.animate_timer) > 125:
            if self.frame_index == 0:
                self.frame_index += 1
            elif self.frame_index == 1:
                self.frame_index = 0

            self.animate_timer = self.current_time


    def falling(self):
        """For when it falls off a ledge"""
        if self.y_vel < 10:
            self.y_vel += self.gravity


    def jumped_on(self):
        """Placeholder for when the enemy is stomped on"""
        pass


    def death_jumping(self):
        """Death animation"""
        self.rect.y += self.y_vel
        self.rect.x += self.x_vel
        self.y_vel += self.gravity

        if self.rect.y > 600:
            self.kill()


    def start_death_jump(self, direction):
        """Transitions enemy into a DEATH JUMP state"""
        self.y_vel = -8
        if direction == s.RIGHT:
            self.x_vel = 2
        else:
            self.x_vel = -2
        self.gravity = .5
        self.frame_index = 3
        self.image = self.frames[self.frame_index]
        self.state = s.DEATH_JUMP


    def animation(self):
        """Basic animation, switching between two frames"""
        self.image = self.frames[self.frame_index]


    def update(self, game_info, *args):
        """Updates enemy behavior"""
        self.current_time = game_info[s.CURRENT_TIME]
        self.handle_state()
        self.animation()


    def flipFrames(self):
        if self.frame_index == 0 or self.frame_index == 1:
            self.frame_index = 4
        else:
            self.frame_index = 0




class Goomba(Enemy):

    def __init__(self, y=s.GROUND_HEIGHT, x=0, direction=s.LEFT, name='goomba'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)


    def setup_frames(self):
        """Put the image frames in a list to be animated"""

        self.frames.append(
            self.get_image(0, 0, 16, 20))
        self.frames.append(
            self.get_image(30, 0, 16, 20))
        self.frames.append(
            self.get_image(61, 0, 16, 20))
        self.frames.append(pg.transform.flip(self.frames[1], False, True))
        self.frames.append(pg.transform.flip(self.frames[0], True, False))
        self.frames.append(pg.transform.flip(self.frames[1], True, False))

    def jumped_on(self):
        """When Mario squishes him"""
        self.frame_index = 2

        if (self.current_time - self.death_timer) > 500:
            self.kill()


class Koopa(Enemy):

    def __init__(self, y=s.GROUND_HEIGHT, x=0, direction=s.LEFT, name='koopa'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)


    def setup_frames(self):
        """Sets frame list"""
        self.frames.append(
            self.get_image(87, 0, 16, 24))
        self.frames.append(
            self.get_image(116, 0, 16, 24))
        self.frames.append(
            self.get_image(360, 5, 16, 15))
        self.frames.append(pg.transform.flip(self.frames[2], False, True))
        # This is 4th index
        self.frames.append(pg.transform.flip(self.frames[0], True, False))
        self.frames.append(pg.transform.flip(self.frames[1], True, False))



    def jumped_on(self):
        """When Mario jumps on the Koopa and puts him in his shell"""
        self.x_vel = 0
        self.frame_index = 2
        shell_y = self.rect.bottom
        shell_x = self.rect.x
        self.rect = self.frames[self.frame_index].get_rect()
        self.rect.x = shell_x
        self.rect.bottom = shell_y


    def shell_sliding(self):
        """When the koopa is sliding along the ground in his shell"""
        if self.direction == s.RIGHT:
            self.x_vel = 10
        elif self.direction == s.LEFT:
            self.x_vel = -10

class evilBird(Enemy):

    def __init__(self, y=s.GROUND_HEIGHT, x=0, direction=s.UP, name='Evil Bird'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)


    def setup_frames(self):
        """Put the image frames in a list to be animated"""
        self.frames.append(
            self.get_image(60, 184, 15, 15))
        self.frames.append(
            self.get_image(90, 184, 15, 15))
        self.frames.append(
            self.get_image(60, 184, 15, 15))
        self.frames.append(
            self.get_image(60, 198, 15, 15))
        self.frames.append(
            self.get_image(60, 184, 15, 15))
        self.frames.append(
            self.get_image(60, 184, 15, 15))

        def flipFrames(self):
            pass

        def set_velocity(self):
            pass

        def start_death_jump(self, direction):
            pass


class eatingPlant(Enemy):
    def __init__(self, y=s.GROUND_HEIGHT, x=0, direction=s.UP, name='Eating Plant'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)

    def setup_frames(self):
        """Put the image frames in a list to be animated"""
        self.frames.append(
            self.get_image(390, 60, 15, 23))
        self.frames.append(
            self.get_image(420, 60, 15, 23))
        self.frames.append(
            self.get_image(420, 60, 15, 23))
        self.frames.append(
            self.get_image(420, 60, 15, 23))
        self.frames.append(
            self.get_image(420, 60, 15, 23))
        self.frames.append(
            self.get_image(420, 60, 15, 23))


    def flipFrames(self):
            pass

    def set_velocity(self):
            self.x_vel = 0
            self.y_vel = 0

    def start_death_jump(self, direction):
            pass





















