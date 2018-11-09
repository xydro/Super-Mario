from __future__ import division


import pygame as pg
from .. import setup, tools
from .. import settings as s
from .. import game_sound
from .. components import mario
from .. components import collider
from .. components import bricks
from .. components import coin_box
from .. components import enemies
from .. components import checkpoint
from .. components import flagpole
from .. components import info
from .. components import score
from .. components import castle_flag

from .. import game_sound
from ..components import mario
from ..components import collider
from ..components import bricks
from ..components import coin_box
from ..components import enemies
from ..components import checkpoint
from ..components import flagpole
from ..components import info
from ..components import score
from ..components import castle_flag


class Level1(tools._State):
    def __init__(self):
        tools._State.__init__(self)

    def startup(self, current_time, persist):
        """Called when the State object is created"""
        self.game_info = persist
        self.persist = self.game_info
        self.game_info[s.CURRENT_TIME] = current_time
        self.game_info[s.LEVEL_STATE] = s.NOT_FROZEN
        self.game_info[s.MARIO_DEAD] = False

        self.state = s.NOT_FROZEN
        self.death_timer = 0
        self.flag_timer = 0
        self.flag_score = None
        self.flag_score_total = 0

        self.moving_score_list = []
        self.overhead_info_display = info.OverheadInfo(self.game_info, s.LEVEL)
        self.sound_manager = game_sound.Sound(self.overhead_info_display)

        self.setup_background()
        self.setup_ground()
        self.setup_pipes()
        self.setup_steps()
        self.setup_bricks()
        self.setup_coin_boxes()
        self.setup_flag_pole()
        self.setup_enemies()
        self.setup_mario()
        self.setup_checkpoints()
        self.setup_spritegroups()

    def setup_background(self):
        """Sets the background image, rect and scales it to the correct
        proportions"""
        self.background = setup.GFX['level_1']
        self.back_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                             (int(self.back_rect.width * s.BACKGROUND_MULTIPLER),
                                              int(self.back_rect.height * s.BACKGROUND_MULTIPLER)))
        self.back_rect = self.background.get_rect()
        width = self.back_rect.width
        height = self.back_rect.height

        self.level = pg.Surface((width, height)).convert()
        self.level_rect = self.level.get_rect()
        self.viewport = setup.SCREEN.get_rect(bottom=self.level_rect.bottom)
        self.viewport.x = self.game_info[s.CAMERA_START_X]

    def setup_ground(self):
        """Creates collideable, invisible rectangles over top of the ground for
        sprites to walk on"""
        # start at x, s.GROUND_HEIGHT, width, height
        ground_rect1 = collider.Collider(0, s.GROUND_HEIGHT, 2400, 60)
        ground_rect2 = collider.Collider(2760, s.GROUND_HEIGHT, 165, 60)
        ground_rect3 = collider.Collider(3050, s.GROUND_HEIGHT, 100, 60)
        ground_rect4 = collider.Collider(3800, s.GROUND_HEIGHT, 2600, 60)
        ground_rect5 = collider.Collider(6647, s.GROUND_HEIGHT, 2300, 60)

        self.ground_group = pg.sprite.Group(ground_rect1, ground_rect2,
                                            ground_rect3, ground_rect4,
                                            ground_rect5)

    def setup_pipes(self):
        """Create collideable rects for all the pipes"""
        # pipe.collider.Collider(x, y, width, height)

        pipe1 = collider.Collider(865, 452, 83, 82)  # mini pipe
        pipe2 = collider.Collider(1115, 409, 83, 140)  # medium pipe
        pipe3 = collider.Collider(1350, 366, 83, 170)  # high pipe
        pipe4 = collider.Collider(1915, 366, 83, 170)  # high pipe
        pipe5 = collider.Collider(1939, 463, 168, 78)  # high pipe
        pipe6 = collider.Collider(2498, 152, 83, 82)  # mini pipe
        pipe7 = collider.Collider(3230, 152, 83, 82)  # mini pipe
        pipe8 = collider.Collider(3490, 190, 83, 140)  # medium pipe: Horizontal
        pipe9 = collider.Collider(3783, 152, 83, 82)  # mini pipe
        pipe10 = collider.Collider(4162, 145, 83, 140)  # medium pipe
        pipe11 = collider.Collider(4584, 366, 83, 170)  # high pipe
        pipe12 = collider.Collider(5251, 366, 83, 170)  # high pipe
        pipe13 = collider.Collider(5334, 366, 490, 25)  # high pipe
        pipe14 = collider.Collider(2350, 452, 20, 82)  # mini pipe
        pipe15 = collider.Collider(4460, 489, 3, 0)  # mini pipe
        pipe16 = collider.Collider(230, 489, 83, 0)  # mini pipe





        self.pipe_group = pg.sprite.Group(pipe1, pipe2,
                                          pipe3, pipe4,
                                          pipe5, pipe6,
                                          pipe7, pipe8,
                                          pipe9, pipe10,
                                          pipe11, pipe12,
                                          pipe13, pipe14,
                                          pipe15, pipe16

                                          )

    def setup_steps(self):
        """Create collideable rects for all the steps"""
        step1 = collider.Collider(5745, 495, 40, 44)
        step2 = collider.Collider(5788, 452, 40, 44)
        step3 = collider.Collider(5831, 409, 40, 44)
        step4 = collider.Collider(5874, 366, 40, 176)

        step5 = collider.Collider(6001, 366, 40, 176)
        step6 = collider.Collider(6044, 408, 40, 40)
        step7 = collider.Collider(6087, 452, 40, 40)
        step8 = collider.Collider(6130, 495, 40, 40)

        step9 = collider.Collider(6345, 495, 40, 40)
        step10 = collider.Collider(6388, 452, 40, 40)
        step11 = collider.Collider(6431, 409, 40, 40)
        step12 = collider.Collider(6474, 366, 40, 40)
        step13 = collider.Collider(6517, 366, 40, 176)

        step14 = collider.Collider(6644, 366, 40, 176)
        step15 = collider.Collider(6687, 408, 40, 40)
        step16 = collider.Collider(6728, 452, 40, 40)
        step17 = collider.Collider(6771, 495, 40, 40)

        step18 = collider.Collider(7760, 495, 40, 40)
        step19 = collider.Collider(7803, 452, 40, 40)
        step20 = collider.Collider(7845, 409, 40, 40)
        step21 = collider.Collider(7888, 366, 40, 40)
        step22 = collider.Collider(7931, 323, 40, 40)
        step23 = collider.Collider(7974, 280, 40, 40)
        step24 = collider.Collider(8017, 237, 40, 40)
        step25 = collider.Collider(8060, 194, 40, 40)
        step26 = collider.Collider(8103, 194, 40, 360)

        step27 = collider.Collider(8488, 495, 40, 40)

        self.step_group = pg.sprite.Group(step1, step2,
                                          step3, step4,
                                          step5, step6,
                                          step7, step8,
                                          step9, step10,
                                          step11, step12,
                                          step13, step14,
                                          step15, step16,
                                          step17, step18,
                                          step19, step20,
                                          step21, step22,
                                          step23, step24,
                                          step25, step26,
                                          step27)

    def setup_bricks(self):
        """Creates all the breakable bricks for the level.  Coin and
        powerup groups are created so they can be passed to bricks."""
        self.coin_group = pg.sprite.Group()
        self.powerup_group = pg.sprite.Group()
        self.brick_pieces_group = pg.sprite.Group()

        brick1 = bricks.Brick(250, 450)
        brick2 = bricks.Brick(420, 280)
        brick3 = bricks.Brick(470, 280)
        brick4 = bricks.Brick(520, 280)
        brick5 = bricks.Brick(570, 280)
        brick6 = bricks.Brick(1600, 430)
        brick7 = bricks.Brick(1800, 430)
        brick8 = bricks.Brick(1300, 380, s.SIXCOINS, self.coin_group)
        brick9 = bricks.Brick(2175, 260)

        brick10 = bricks.Brick(2350, 490)  # 4 Vertical brick walls
        brick11 = bricks.Brick(2350, 450)
        brick12 = bricks.Brick(2350, 410)
        brick13 = bricks.Brick(2350, 370)

        brick14 = bricks.Brick(2350, 230)

        brick15 = bricks.Brick(2760, 82)
        brick16 = bricks.Brick(2810, 82)
        brick17 = bricks.Brick(2860, 82)
        brick18 = bricks.Brick(2910, 82)
        brick19 = bricks.Brick(2960, 82)
        brick20 = bricks.Brick(3010, 82)
        brick21 = bricks.Brick(3015, 280)
        brick22 = bricks.Brick(2850, 380, s.SIXCOINS, self.coin_group)
        brick23 = bricks.Brick(3100, 470)
        brick24 = bricks.Brick(3185, 240)
        brick25 = bricks.Brick(3150, 375)

        brick26 = bricks.Brick(3650, 180)
        brick27 = bricks.Brick(4000, 180)
        brick28 = bricks.Brick(5200, 480)

        brick29 = bricks.Brick(2500, 240)  # Brick that starts under the pipe
        brick30 = bricks.Brick(2540, 240)

        brick31 = bricks.Brick(3225, 240)
        brick32 = bricks.Brick(3265, 240)
        brick33 = bricks.Brick(3305, 240)

        brick34 = bricks.Brick(3495, 290)
        brick35 = bricks.Brick(3535, 290)

        brick36 = bricks.Brick(3800, 240)
        brick37 = bricks.Brick(3840, 240)

        brick38 = bricks.Brick(4200, 270)
        brick39 = bricks.Brick(4160, 270)

        brick40 = bricks.Brick(4531, 360, s.SIXCOINS, self.coin_group)
        brick41 = bricks.Brick(4450, 490)
        brick42 = bricks.Brick(5955, 490)

        brick43 = bricks.Brick(4400, 300, s.STAR, self.powerup_group)  # Star here

        self.brick_group = pg.sprite.Group(brick1, brick2,
                                           brick3, brick4,
                                           brick5, brick6,
                                           brick7, brick8,
                                           brick9, brick10,
                                           brick11, brick12,
                                           brick13, brick14,
                                           brick15, brick16,
                                           brick17, brick18,
                                           brick19, brick20,
                                           brick21, brick22,
                                           brick23, brick24,
                                           brick25, brick26,
                                           brick27, brick28,
                                           brick29, brick30,
                                           brick31, brick32,
                                           brick33, brick34,
                                           brick35, brick36,
                                           brick37, brick38,
                                           brick39, brick40,
                                           brick41, brick42,
                                           brick43
                                           )

    def setup_coin_boxes(self):
        """Creates all the coin boxes and puts them in a sprite group"""
        coin_box1 = coin_box.Coin_box(360, 380, s.COIN, self.coin_group)
        coin_box2 = coin_box.Coin_box(480, 380, s.COIN, self.coin_group)
        coin_box3 = coin_box.Coin_box(570, 150, s.MUSHROOM, self.powerup_group)
        coin_box4 = coin_box.Coin_box(2150, 370, s.COIN, self.coin_group)
        coin_box5 = coin_box.Coin_box(2200, 370, s.COIN, self.coin_group)
        coin_box6 = coin_box.Coin_box(2250, 370, s.COIN, self.coin_group)
        coin_box7 = coin_box.Coin_box(2300, 370, s.COIN, self.coin_group)

        coin_box8 = coin_box.Coin_box(4300, 380, s.MUSHROOM, self.powerup_group)

        self.coin_box_group = pg.sprite.Group(coin_box1, coin_box2,
                                              coin_box3, coin_box4,
                                              coin_box5, coin_box6,
                                              coin_box7, coin_box8,
                                              )

    def setup_flag_pole(self):
        """Creates the flag pole at the end of the level"""
        self.flag = flagpole.Flag(8505, 100)

        pole0 = flagpole.Pole(8505, 97)
        pole1 = flagpole.Pole(8505, 137)
        pole2 = flagpole.Pole(8505, 177)
        pole3 = flagpole.Pole(8505, 217)
        pole4 = flagpole.Pole(8505, 257)
        pole5 = flagpole.Pole(8505, 297)
        pole6 = flagpole.Pole(8505, 337)
        pole7 = flagpole.Pole(8505, 377)
        pole8 = flagpole.Pole(8505, 417)
        pole9 = flagpole.Pole(8505, 450)

        finial = flagpole.Finial(8507, 97)

        self.flag_pole_group = pg.sprite.Group(self.flag,
                                               finial,
                                               pole0,
                                               pole1,
                                               pole2,
                                               pole3,
                                               pole4,
                                               pole5,
                                               pole6,
                                               pole7,
                                               pole8,
                                               pole9)

    def setup_enemies(self):
        """Creates all the enemies and stores them in a list of lists."""
        '''
        goomba1 = enemies.Goomba(193)
        goomba2 = enemies.Goomba(193)
        goomba3 = enemies.Goomba(193)
        goomba4 = enemies.Goomba()
        goomba5 = enemies.Goomba()
        goomba6 = enemies.Goomba()
        goomba7 = enemies.Goomba()
        

        koopa1 = enemies.Koopa()

        goomba8 = enemies.Goomba(193)
        goomba9 = enemies.Goomba(193)
        goomba10 = enemies.Goomba(193)
        goomba11 = enemies.Goomba(193)
        goomba12 = enemies.Goomba()
        goomba13 = enemies.Goomba()
        goomba14 = enemies.Goomba(193)
        goomba15 = enemies.Goomba()
        goomba16 = enemies.Goomba(65)
        goomba17 = enemies.Goomba(300)
        goomba18 = enemies.Goomba(193)
        koopa2 = enemies.Koopa()

        goomba19 = enemies.Goomba(193)
        goomba20 = enemies.Goomba(193)
        goomba21 = enemies.Goomba(193)
        goomba22 = enemies.Goomba(193)
        goomba23 = enemies.Goomba(193)
        goomba24 = enemies.Goomba(193)
        goomba25 = enemies.Goomba(193)
        koopa3 = enemies.Koopa()

        koopa4 = enemies.Koopa(100)
        koopa5 = enemies.Koopa(100)
        koopa6 = enemies.Koopa(100)
        koopa7 = enemies.Koopa(100)
        koopa8 = enemies.Koopa(100)

        koopa9 = enemies.Koopa(100)
        koopa10 = enemies.Koopa(100)
        koopa11 = enemies.Koopa(100)

        goomba26 = enemies.Goomba(193)
        goomba27 = enemies.Goomba(193)
        goomba28 = enemies.Goomba(193)
        goomba29 = enemies.Goomba(193)
        goomba30 = enemies.Goomba(193)

        goomba31 = enemies.Goomba(105)
        goomba32 = enemies.Goomba(105)
        goomba33 = enemies.Goomba(105)
        goomba34 = enemies.Goomba(105)
        goomba35 = enemies.Goomba(105)

        enemy_group1 = pg.sprite.Group(goomba1)
        enemy_group2 = pg.sprite.Group(goomba2)
        enemy_group3 = pg.sprite.Group(goomba3)
        enemy_group4 = pg.sprite.Group(goomba4)
        enemy_group5 = pg.sprite.Group(goomba5)
        enemy_group6 = pg.sprite.Group(goomba6)
        enemy_group7 = pg.sprite.Group(goomba7)

        enemy_group8 = pg.sprite.Group(koopa1)

        enemy_group9 = pg.sprite.Group(goomba8)
        enemy_group10 = pg.sprite.Group(goomba9)
        enemy_group11 = pg.sprite.Group(goomba10)
        enemy_group12 = pg.sprite.Group(goomba11)
        enemy_group13 = pg.sprite.Group(goomba12)
        enemy_group14 = pg.sprite.Group(goomba13)
        enemy_group15 = pg.sprite.Group(goomba14)
        enemy_group16 = pg.sprite.Group(goomba15)
        enemy_group17 = pg.sprite.Group(goomba16)
        enemy_group18 = pg.sprite.Group(goomba17)
        enemy_group19 = pg.sprite.Group(goomba18)
        enemy_group20 = pg.sprite.Group(koopa2)

        enemy_group21 = pg.sprite.Group(goomba19)
        enemy_group22 = pg.sprite.Group(goomba20)
        enemy_group23 = pg.sprite.Group(goomba21)
        enemy_group24 = pg.sprite.Group(goomba22)
        enemy_group25 = pg.sprite.Group(goomba23)
        enemy_group26 = pg.sprite.Group(goomba24)
        enemy_group27 = pg.sprite.Group(goomba25)

        enemy_group28 = pg.sprite.Group(koopa3)

        enemy_group29 = pg.sprite.Group(koopa4)
        enemy_group30 = pg.sprite.Group(koopa5)
        enemy_group31 = pg.sprite.Group(koopa6)
        enemy_group32 = pg.sprite.Group(koopa7)
        enemy_group33 = pg.sprite.Group(koopa8)

        enemy_group34 = pg.sprite.Group(koopa9)
        enemy_group35 = pg.sprite.Group(koopa10)
        enemy_group36 = pg.sprite.Group(koopa11)

        enemy_group37 = pg.sprite.Group(goomba26)
        enemy_group38 = pg.sprite.Group(goomba27)
        enemy_group39 = pg.sprite.Group(goomba28)
        enemy_group40 = pg.sprite.Group(goomba29)
        enemy_group41 = pg.sprite.Group(goomba30)

        enemy_group42 = pg.sprite.Group(goomba31)
        enemy_group43 = pg.sprite.Group(goomba32)
        enemy_group44 = pg.sprite.Group(goomba33)
        enemy_group45 = pg.sprite.Group(goomba34)
        enemy_group46 = pg.sprite.Group(goomba35)
        enemy_group47 = pg.sprite.Group(evilBird1)
        enemy_group48 = pg.sprite.Group(eatingPlant1)
        enemy_group49 = pg.sprite.Group(eatingPlant2)
'''
        #evilBird1 = enemies.evilBird(140)
        #eatingPlant1 = enemies.eatingPlant(363, 1350)
        #eatingPlant2 = enemies.eatingPlant(375)
        #enemy_group47 = pg.sprite.Group(evilBird1)
        #enemy_group48 = pg.sprite.Group(eatingPlant1)
        #enemy_group49 = pg.sprite.Group(eatingPlant2)
        # enemy_group6 = pg.sprite.Group(koopa0)



        self.enemy_group_list = []

    def setup_mario(self):
        """Places Mario at the beginning of the level"""
        self.mario = mario.Mario()
        self.mario.rect.x = self.viewport.x + 110
        self.mario.rect.bottom = s.GROUND_HEIGHT

    def setup_checkpoints(self):
        """Creates invisible checkpoints that when collided will trigger
        the creation of enemies from the self.enemy_group_list"""
        check1 = checkpoint.Checkpoint(150, "1")
        check2 = checkpoint.Checkpoint(250, "2")
        check3 = checkpoint.Checkpoint(325, "3")
        check4 = checkpoint.Checkpoint(420, "4")
        check5 = checkpoint.Checkpoint(500, "5")
        # Fix this 6
        check6 = checkpoint.Checkpoint(10740, "6")
        check7 = checkpoint.Checkpoint(850, "7")
        check8 = checkpoint.Checkpoint(1350, "8")
        check9 = checkpoint.Checkpoint(1400, "9")
        check10 = checkpoint.Checkpoint(1455, "10")
        check11 = checkpoint.Checkpoint(1500, "11")
        # Fix 12
        check12 = checkpoint.Checkpoint(10600, "12")
        check13 = checkpoint.Checkpoint(1700, "13")
        check14 = checkpoint.Checkpoint(1750, "14")
        check15 = checkpoint.Checkpoint(1800, "15")
        check16 = checkpoint.Checkpoint(1900, "16")
        check17 = checkpoint.Checkpoint(2900, "17")
        check18 = checkpoint.Checkpoint(2600, "18")
        check19 = checkpoint.Checkpoint(3825, "19")
        check20 = checkpoint.Checkpoint(3800, "20")

        check21 = checkpoint.Checkpoint(4470, "21")
        check22 = checkpoint.Checkpoint(4520, "22")
        check23 = checkpoint.Checkpoint(4570, "23")
        check24 = checkpoint.Checkpoint(4620, "24")
        check25 = checkpoint.Checkpoint(4670, "25")
        check26 = checkpoint.Checkpoint(4670, "26")
        check27 = checkpoint.Checkpoint(4670, "27")
        check28 = checkpoint.Checkpoint(6000, "28")

        check29 = checkpoint.Checkpoint(7000, "29")
        check30 = checkpoint.Checkpoint(7050, "30")
        check31 = checkpoint.Checkpoint(7100, "31")
        check32 = checkpoint.Checkpoint(7150, "32")
        check33 = checkpoint.Checkpoint(7200, "33")

        check34 = checkpoint.Checkpoint(7250, "34")
        check35 = checkpoint.Checkpoint(7300, "35")
        check36 = checkpoint.Checkpoint(7350, "36")

        check37 = checkpoint.Checkpoint(7400, "37")
        check38 = checkpoint.Checkpoint(7450, "38")
        check39 = checkpoint.Checkpoint(7500, "39")
        check40 = checkpoint.Checkpoint(7550, "40")
        check41 = checkpoint.Checkpoint(7600, "41")

        check42 = checkpoint.Checkpoint(7650, "42")
        check43 = checkpoint.Checkpoint(7700, "43")
        check44 = checkpoint.Checkpoint(7750, "44")
        check45 = checkpoint.Checkpoint(7800, "45")
        check46 = checkpoint.Checkpoint(7850, "46")
        check47 = checkpoint.Checkpoint(810, "47")
        check48 = checkpoint.Checkpoint(1000, '48')
        check49 = checkpoint.Checkpoint(1580, '49')


        check50 = checkpoint.Checkpoint(8504, '50', 5, 6)
        check51 = checkpoint.Checkpoint(8775, '51')
        check52 = checkpoint.Checkpoint(2225, 'secret_mushroom', 286, 40, 12)



        self.check_point_group = pg.sprite.Group(check1, check2, check3,
                                                 check4, check5, check6,
                                                 check7, check8, check9,
                                                 check10, check11, check12,
                                                 check13, check14, check15,
                                                 check16, check17, check18,
                                                 check19, check20, check21,
                                                 check22, check23, check24,
                                                 check25, check26, check27,
                                                 check28, check29, check30,
                                                 check31, check32, check33,
                                                 check34, check35, check36,
                                                 check37, check38, check39,
                                                 check40, check41, check42,
                                                 check43, check44, check45,
                                                 check46, check47, check48,
                                                 check49, check50, check51,
                                                 check52
                                                 )

    def setup_spritegroups(self):
        """Sprite groups created for convenience"""
        self.sprites_about_to_die_group = pg.sprite.Group()
        self.shell_group = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()

        self.ground_step_pipe_group = pg.sprite.Group(self.ground_group,
                                                      self.pipe_group,
                                                      self.step_group)

        self.mario_and_enemy_group = pg.sprite.Group(self.mario,
                                                     self.enemy_group)

    def update(self, surface, keys, current_time):
        """Updates Entire level using states.  Called by the control object"""
        self.game_info[s.CURRENT_TIME] = self.current_time = current_time
        self.handle_states(keys)
        self.check_if_time_out()
        self.blit_everything(surface)
        self.sound_manager.update(self.game_info, self.mario)

    def handle_states(self, keys):
        """If the level is in a FROZEN state, only mario will update"""
        if self.state == s.FROZEN:
            self.update_during_transition_state(keys)
        elif self.state == s.NOT_FROZEN:
            self.update_all_sprites(keys)
        elif self.state == s.IN_CASTLE:
            self.update_while_in_castle()
        elif self.state == s.FLAG_AND_FIREWORKS:
            self.update_flag_and_fireworks()

    def update_during_transition_state(self, keys):
        """Updates mario in a transition state (like becoming big, small,
         or dies). Checks if he leaves the transition state or dies to
         change the level state back"""
        self.mario.update(keys, self.game_info, self.powerup_group)
        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_info)
        if self.flag_score:
            self.flag_score.update(None, self.game_info)
            self.check_to_add_flag_score()
        self.coin_box_group.update(self.game_info)
        self.flag_pole_group.update(self.game_info)
        self.check_if_mario_in_transition_state()
        self.check_flag()
        self.check_for_mario_death()
        self.overhead_info_display.update(self.game_info, self.mario)

    def check_if_mario_in_transition_state(self):
        """If mario is in a transition state, the level will be in a FREEZE
        state"""
        if self.mario.in_transition_state:
            self.game_info[s.LEVEL_STATE] = self.state = s.FROZEN
        elif self.mario.in_transition_state == False:
            if self.state == s.FROZEN:
                self.game_info[s.LEVEL_STATE] = self.state = s.NOT_FROZEN

    def update_all_sprites(self, keys):
        """Updates the location of all sprites on the screen."""
        self.mario.update(keys, self.game_info, self.powerup_group)
        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_info)
        if self.flag_score:
            self.flag_score.update(None, self.game_info)
            self.check_to_add_flag_score()
        self.flag_pole_group.update()
        self.check_points_check()
        self.enemy_group.update(self.game_info)
        self.sprites_about_to_die_group.update(self.game_info, self.viewport)
        self.shell_group.update(self.game_info)
        self.brick_group.update()
        self.coin_box_group.update(self.game_info)
        self.powerup_group.update(self.game_info, self.viewport)
        self.coin_group.update(self.game_info, self.viewport)
        self.brick_pieces_group.update()
        self.adjust_sprite_positions()
        self.check_if_mario_in_transition_state()
        self.check_for_mario_death()
        self.update_viewport()
        self.overhead_info_display.update(self.game_info, self.mario)

    def enemySpawning1(self, i):
        if i == 0:
            goomba1 = enemies.Goomba(193)
            enemy_group1 = pg.sprite.Group(goomba1)
            return enemy_group1
        elif i == 1:
            goomba2 = enemies.Goomba(193)
            enemy_group2 = pg.sprite.Group(goomba2)
            #eatingPlant1 = enemies.eatingPlant(363, 800)
            #enemy_group48 = pg.sprite.Group(eatingPlant1)
            #self.enemy_group.add(enemy_group48)
            return enemy_group2
        elif i == 2:
            goomba3 = enemies.Goomba(193)
            enemy_group3 = pg.sprite.Group(goomba3)
            return enemy_group3
        elif i == 3:
            goomba4 = enemies.Goomba()
            enemy_group4 = pg.sprite.Group(goomba4)
            return enemy_group4
        elif i == 4:
            goomba5 = enemies.Goomba()
            enemy_group5 = pg.sprite.Group(goomba5)
            return enemy_group5
        elif i == 5:
            goomba6 = enemies.Goomba()
            enemy_group6 = pg.sprite.Group(goomba6)
            return enemy_group6
        elif i == 6:
            goomba7 = enemies.Goomba()
            enemy_group7 = pg.sprite.Group(goomba7)
            return enemy_group7
        elif i == 7:
            koopa1 = enemies.Koopa()
            enemy_group8 = pg.sprite.Group(koopa1)
            return enemy_group8
        elif i == 8:
            pass
        elif i == 9:
            evilBird1 = enemies.evilBird(400)
            enemy_group47 = pg.sprite.Group(evilBird1)
            return enemy_group47
        elif i == 10:
            goomba8 = enemies.Goomba(193)
            enemy_group9 = pg.sprite.Group(goomba8)
            return enemy_group9
        elif i == 11:
            pass
            #eatingPlant2 = enemies.eatingPlant(375)
            #enemy_group49 = pg.sprite.Group(eatingPlant2)
            #return enemy_group49
        elif i == 12:
            goomba9 = enemies.Goomba(193)
            enemy_group10 = pg.sprite.Group(goomba9)
            return enemy_group10
        elif i == 13:
            goomba10 = enemies.Goomba(193)
            enemy_group11 = pg.sprite.Group(goomba10)
            return enemy_group11
        elif i == 14:
            goomba11 = enemies.Goomba(193)
            enemy_group12 = pg.sprite.Group(goomba11)
            return enemy_group12
        elif i == 15:
            goomba12 = enemies.Goomba()
            enemy_group13 = pg.sprite.Group(goomba12)
            return enemy_group13
        elif i == 16:
            goomba13 = enemies.Goomba()
            enemy_group14 = pg.sprite.Group(goomba13)
            return enemy_group14
        elif i == 17:
            goomba14 = enemies.Goomba(193)
            enemy_group15 = pg.sprite.Group(goomba14)
            return enemy_group15
        elif i == 18:
            goomba15 = enemies.Goomba()
            enemy_group16 = pg.sprite.Group(goomba15)
            return enemy_group16
        elif i == 19:
            goomba16 = enemies.Goomba(65)
            enemy_group17 = pg.sprite.Group(goomba16)
            return enemy_group17
        elif i == 20:
            goomba17 = enemies.Goomba(300)
            enemy_group18 = pg.sprite.Group(goomba17)
            return enemy_group18
        elif i == 21:
            goomba18 = enemies.Goomba(193)
            enemy_group19 = pg.sprite.Group(goomba18)
            return enemy_group19
        elif i == 22:
            koopa2 = enemies.Koopa()
            enemy_group20 = pg.sprite.Group(koopa2)
            return enemy_group20
        elif i == 23:
            goomba19 = enemies.Goomba(193)
            enemy_group21 = pg.sprite.Group(goomba19)
            return enemy_group21
        elif i == 24:
            goomba20 = enemies.Goomba(193)
            enemy_group22 = pg.sprite.Group(goomba20)
            return enemy_group22
        elif i == 25:
            goomba21 = enemies.Goomba(193)
            enemy_group23 = pg.sprite.Group(goomba21)
            return enemy_group23
        elif i == 26:
            goomba22 = enemies.Goomba(193)
            enemy_group24 = pg.sprite.Group(goomba22)
            return enemy_group24
        elif i == 27:
            goomba23 = enemies.Goomba(193)
            enemy_group25 = pg.sprite.Group(goomba23)
            return enemy_group25
        elif i == 28:
            goomba24 = enemies.Goomba(193)
            enemy_group26 = pg.sprite.Group(goomba24)
            return enemy_group26
        elif i == 29:
            goomba25 = enemies.Goomba(193)
            enemy_group27 = pg.sprite.Group(goomba25)
            return enemy_group27
        elif i == 30:
            koopa3 = enemies.Koopa()
            enemy_group28 = pg.sprite.Group(koopa3)
            return enemy_group28
        elif i == 31:
            koopa4 = enemies.Koopa(100)
            enemy_group29 = pg.sprite.Group(koopa4)
            return enemy_group29
        elif i == 32:
            koopa5 = enemies.Koopa(100)
            enemy_group30 = pg.sprite.Group(koopa5)
            return enemy_group30
        elif i == 33:
            koopa6 = enemies.Koopa(100)
            enemy_group31 = pg.sprite.Group(koopa6)
            return enemy_group31
        elif i == 34:
            koopa7 = enemies.Koopa(100)
            enemy_group32 = pg.sprite.Group(koopa7)
            return enemy_group32
        elif i == 35:
            koopa8 = enemies.Koopa(100)
            enemy_group33 = pg.sprite.Group(koopa8)
            return enemy_group33
        elif i == 36:
            koopa9 = enemies.Koopa(100)
            enemy_group34 = pg.sprite.Group(koopa9)
            return enemy_group34
        elif i == 37:
            koopa10 = enemies.Koopa(100)
            enemy_group35 = pg.sprite.Group(koopa10)
            return enemy_group35
        elif i == 38:
            koopa11 = enemies.Koopa(100)
            enemy_group36 = pg.sprite.Group(koopa11)
            return enemy_group36
        elif i == 39:
            goomba26 = enemies.Goomba(193)
            enemy_group37 = pg.sprite.Group(goomba26)
            return enemy_group37
        elif i == 40:
            goomba27 = enemies.Goomba(193)
            enemy_group38 = pg.sprite.Group(goomba27)
            return enemy_group38
        elif i == 41:
            goomba28 = enemies.Goomba(193)
            enemy_group39 = pg.sprite.Group(goomba28)
            return enemy_group39
        elif i == 42:
            goomba29 = enemies.Goomba(193)
            enemy_group40 = pg.sprite.Group(goomba29)
            return enemy_group40
        elif i == 43:
            goomba30 = enemies.Goomba(193)
            enemy_group41 = pg.sprite.Group(goomba30)
            return enemy_group41
        elif i == 44:
            goomba31 = enemies.Goomba(105)
            enemy_group42 = pg.sprite.Group(goomba31)
            return enemy_group42
        elif i == 45:
            goomba32 = enemies.Goomba(105)
            enemy_group43 = pg.sprite.Group(goomba32)
            return enemy_group43
        elif i == 46:
            goomba33 = enemies.Goomba(105)
            enemy_group44 = pg.sprite.Group(goomba33)
            return enemy_group44
        elif i == 47:
            goomba34 = enemies.Goomba(105)
            enemy_group45 = pg.sprite.Group(goomba34)
            return enemy_group45
        elif i == 48:
            goomba35 = enemies.Goomba(105)
            enemy_group46 = pg.sprite.Group(goomba35)
            return enemy_group46

    def enemySpawning2(self, i):
        if i == 0:
            goomba1 = enemies.Goomba(193)
            return goomba1
        elif i == 1:
            goomba2 = enemies.Goomba(193)
            return goomba2
        elif i == 2:
            goomba3 = enemies.Goomba(193)
            return goomba3
        elif i == 3:
            goomba4 = enemies.Goomba()
            return goomba4
        elif i == 4:
            goomba5 = enemies.Goomba()
            return goomba5
        elif i == 5:
            goomba6 = enemies.Goomba()
            return goomba6
        elif i == 6:
            goomba7 = enemies.Goomba()
            return goomba7
        elif i == 7:
            koopa1 = enemies.Koopa()
            return koopa1
        elif i == 8:
            eatingPlant1 = enemies.eatingPlant(363)
            return eatingPlant1
        elif i == 9:
            evilBird1 = enemies.evilBird(-100)
            return evilBird1
        elif i == 10:
            goomba8 = enemies.Goomba(193)
            return goomba8
        elif i == 11:
            eatingPlant2 = enemies.eatingPlant(-100, 0)
            return eatingPlant2
        elif i == 12:
            goomba9 = enemies.Goomba(193)
            return goomba9
        elif i == 13:
            goomba10 = enemies.Goomba(193)
            return goomba10
        elif i == 14:
            goomba11 = enemies.Goomba(193)
            return goomba11
        elif i == 15:
            goomba12 = enemies.Goomba()
            return goomba12
        elif i == 16:
            goomba13 = enemies.Goomba()
            return goomba13
        elif i == 17:
            goomba14 = enemies.Goomba(193)
            return goomba14
        elif i == 18:
            goomba15 = enemies.Goomba()
            return goomba15
        elif i == 19:
            goomba16 = enemies.Goomba(65)
            return goomba16
        elif i == 20:
            goomba17 = enemies.Goomba(300)
            return goomba17
        elif i == 21:
            goomba18 = enemies.Goomba(193)
            return goomba18
        elif i == 22:
            koopa2 = enemies.Koopa()
            return koopa2
        elif i == 23:
            goomba19 = enemies.Goomba(193)
            return goomba19
        elif i == 24:
            goomba20 = enemies.Goomba(193)
            return goomba20
        elif i == 25:
            goomba21 = enemies.Goomba(193)
            return goomba21
        elif i == 26:
            goomba22 = enemies.Goomba(193)
            return goomba22
        elif i == 27:
            goomba23 = enemies.Goomba(193)
            return goomba23
        elif i == 28:
            goomba24 = enemies.Goomba(193)
            return goomba24
        elif i == 29:
            goomba25 = enemies.Goomba(193)
            return goomba25
        elif i == 30:
            koopa3 = enemies.Koopa()
            return koopa3
        elif i == 31:
            koopa4 = enemies.Koopa(100)
            return koopa4
        elif i == 32:
            koopa5 = enemies.Koopa(100)
            return koopa5
        elif i == 33:
            koopa6 = enemies.Koopa(100)
            return koopa6
        elif i == 34:
            koopa7 = enemies.Koopa(100)
            return koopa7
        elif i == 35:
            koopa8 = enemies.Koopa(100)
            return koopa8
        elif i == 36:
            koopa9 = enemies.Koopa(100)
            return koopa9
        elif i == 37:
            koopa10 = enemies.Koopa(100)
            return koopa10
        elif i == 38:
            koopa11 = enemies.Koopa(100)
            return koopa11
        elif i == 39:
            goomba26 = enemies.Goomba(193)
            return goomba26
        elif i == 40:
            goomba27 = enemies.Goomba(193)
            return goomba27
        elif i == 41:
            goomba28 = enemies.Goomba(193)
            return goomba28
        elif i == 42:
            goomba29 = enemies.Goomba(193)
            return goomba29
        elif i == 43:
            goomba30 = enemies.Goomba(193)
            return goomba30
        elif i == 44:
            goomba31 = enemies.Goomba(105)
            return goomba31
        elif i == 45:
            goomba32 = enemies.Goomba(105)
            return goomba32
        elif i == 46:
            goomba33 = enemies.Goomba(105)
            return goomba33
        elif i == 47:
            goomba34 = enemies.Goomba(105)
            return goomba34
        elif i == 48:
            goomba35 = enemies.Goomba(105)
            return goomba35




    def check_points_check(self):
        """Detect if checkpoint collision occurs, delete checkpoint,
        add enemies to self.enemy_group"""
        checkpoint = pg.sprite.spritecollideany(self.mario,
                                                self.check_point_group)
        if checkpoint:
            checkpoint.kill()

            for i in range(1, 49):
                if checkpoint.name == str(i):
                    # Creates monster based on checkpoints x position
                    newEnemy = self.enemySpawning2(i)
                    newEnemy_group = pg.sprite.Group(newEnemy)
                    #self.enemy_group_list.insert((i - 1), newEnemy_group)
                    newEnemy.rect.x = self.viewport.right + (i * 60)
                    self.enemy_group.add(newEnemy_group)
                    '''
                    self.enemy_group_list.insert((i-1), self.enemySpawning((i-1)))
                    print(str(self.enemy_group_list))
                    for index, enemy in enumerate(self.enemy_group_list[i - 1]):
                        # Creates monster based on checkpoints x position
                        enemy.rect.x = self.viewport.right + (index * 60)
                        print(str(enemy.rect.x))
                        print(str(i))'''
                    '''
                    for index, enemy in enumerate(self.enemy_group_list[i - 1]):
                       # Creates monster based on checkpoints x position
                        if enemy.name is not "Eating Plant":
                            enemy.rect.x = self.viewport.right + (index * 60)
                            print(str(enemy.rect.x))

                        self.enemy_group.add(self.enemy_group_list[i - 1])
                        '''

            if checkpoint.name == '50':
                self.mario.state = s.FLAGPOLE
                self.mario.invincible = False
                self.mario.flag_pole_right = checkpoint.rect.right
                if self.mario.rect.bottom < self.flag.rect.y:
                    self.mario.rect.bottom = self.flag.rect.y
                self.flag.state = s.SLIDE_DOWN
                self.create_flag_points()

            elif checkpoint.name == '51':
                self.state = s.IN_CASTLE
                self.mario.kill()
                self.mario.state == s.STAND
                self.mario.in_castle = True
                self.overhead_info_display.state = s.FAST_COUNT_DOWN


            elif checkpoint.name == 'secret_mushroom' and self.mario.y_vel < 0:
                mushroom_box = coin_box.Coin_box(checkpoint.rect.x,
                                                 checkpoint.rect.bottom - 40,
                                                 '1up_mushroom',
                                                 self.powerup_group)
                mushroom_box.start_bump(self.moving_score_list)
                self.coin_box_group.add(mushroom_box)

                self.mario.y_vel = 7
                self.mario.rect.y = mushroom_box.rect.bottom
                self.mario.state = s.FALL

            self.mario_and_enemy_group.add(self.enemy_group)

    def create_flag_points(self):
        """Creates the points that appear when Mario touches the
        flag pole"""
        x = 8518
        y = s.GROUND_HEIGHT - 60
        mario_bottom = self.mario.rect.bottom

        if mario_bottom > (s.GROUND_HEIGHT - 40 - 40):
            self.flag_score = score.Score(x, y, 100, True)
            self.flag_score_total = 100
        elif mario_bottom > (s.GROUND_HEIGHT - 40 - 160):
            self.flag_score = score.Score(x, y, 400, True)
            self.flag_score_total = 400
        elif mario_bottom > (s.GROUND_HEIGHT - 40 - 240):
            self.flag_score = score.Score(x, y, 800, True)
            self.flag_score_total = 800
        elif mario_bottom > (s.GROUND_HEIGHT - 40 - 360):
            self.flag_score = score.Score(x, y, 2000, True)
            self.flag_score_total = 2000
        else:
            self.flag_score = score.Score(x, y, 5000, True)
            self.flag_score_total = 5000

    def adjust_sprite_positions(self):
        """Adjusts sprites by their x and y velocities and collisions"""
        self.adjust_mario_position()
        self.adjust_enemy_position()
        self.adjust_shell_position()
        self.adjust_powerup_position()

    def adjust_mario_position(self):
        """Adjusts Mario's position based on his x, y velocities and
        potential collisions"""
        self.last_x_position = self.mario.rect.right
        self.mario.rect.x += round(self.mario.x_vel)
        self.check_mario_x_collisions()

        if self.mario.in_transition_state == False:
            self.mario.rect.y += round(self.mario.y_vel)
            self.check_mario_y_collisions()

        if self.mario.rect.x < (self.viewport.x + 5):
            self.mario.rect.x = (self.viewport.x + 5)

    def check_mario_x_collisions(self):
        """Check for collisions after Mario is moved on the x axis"""
        collider = pg.sprite.spritecollideany(self.mario, self.ground_step_pipe_group)
        coin_box = pg.sprite.spritecollideany(self.mario, self.coin_box_group)
        brick = pg.sprite.spritecollideany(self.mario, self.brick_group)
        enemy = pg.sprite.spritecollideany(self.mario, self.enemy_group)
        shell = pg.sprite.spritecollideany(self.mario, self.shell_group)
        powerup = pg.sprite.spritecollideany(self.mario, self.powerup_group)

        if coin_box:
            self.adjust_mario_for_x_collisions(coin_box)

        elif brick:
            self.adjust_mario_for_x_collisions(brick)

        elif collider:
            self.adjust_mario_for_x_collisions(collider)

        elif enemy:
            if self.mario.invincible:
                setup.SFX['kick'].play()
                self.game_info[s.SCORE] += 100
                self.moving_score_list.append(
                    score.Score(self.mario.rect.right - self.viewport.x,
                                self.mario.rect.y, 100))
                enemy.kill()
                enemy.start_death_jump(s.RIGHT)
                self.sprites_about_to_die_group.add(enemy)
            elif self.mario.big:
                setup.SFX['pipe'].play()
                self.mario.fire = False
                self.mario.y_vel = -1
                self.mario.state = s.BIG_TO_SMALL
                self.convert_fireflowers_to_mushrooms()
            elif self.mario.hurt_invincible:
                pass
            #else:
                #self.mario.start_death_jump(self.game_info)
                #self.state = s.FROZEN

        elif shell:
            self.adjust_mario_for_x_shell_collisions(shell)

        elif powerup:
            if powerup.name == s.STAR:
                self.game_info[s.SCORE] += 1000

                self.moving_score_list.append(
                    score.Score(self.mario.rect.centerx - self.viewport.x,
                                self.mario.rect.y, 1000))
                self.mario.invincible = True
                self.mario.invincible_start_timer = self.current_time
            elif powerup.name == s.MUSHROOM:
                setup.SFX['powerup'].play()
                self.game_info[s.SCORE] += 1000
                self.moving_score_list.append(
                    score.Score(self.mario.rect.centerx - self.viewport.x,
                                self.mario.rect.y - 20, 1000))

                self.mario.y_vel = -1
                self.mario.state = s.SMALL_TO_BIG
                self.mario.in_transition_state = True
                self.convert_mushrooms_to_fireflowers()
            elif powerup.name == s.LIFE_MUSHROOM:
                self.moving_score_list.append(
                    score.Score(powerup.rect.right - self.viewport.x,
                                powerup.rect.y,
                                s.ONEUP))

                self.game_info[s.LIVES] += 1
                setup.SFX['one_up'].play()
            elif powerup.name == s.FIREFLOWER:
                setup.SFX['powerup'].play()
                self.game_info[s.SCORE] += 1000
                self.moving_score_list.append(
                    score.Score(self.mario.rect.centerx - self.viewport.x,
                                self.mario.rect.y, 1000))

                if self.mario.big and self.mario.fire == False:
                    self.mario.state = s.BIG_TO_FIRE
                    self.mario.in_transition_state = True
                elif self.mario.big == False:
                    self.mario.state = s.SMALL_TO_BIG
                    self.mario.in_transition_state = True
                    self.convert_mushrooms_to_fireflowers()

            if powerup.name != s.FIREBALL:
                powerup.kill()

    def convert_mushrooms_to_fireflowers(self):
        """When Mario becomees big, converts all fireflower powerups to
        mushroom powerups"""
        for brick in self.brick_group:
            if brick.contents == s.MUSHROOM:
                brick.contents = s.FIREFLOWER
        for coin_box in self.coin_box_group:
            if coin_box.contents == s.MUSHROOM:
                coin_box.contents = s.FIREFLOWER

    def convert_fireflowers_to_mushrooms(self):
        """When Mario becomes small, converts all mushroom powerups to
        fireflower powerups"""
        for brick in self.brick_group:
            if brick.contents == s.FIREFLOWER:
                brick.contents = s.MUSHROOM
        for coin_box in self.coin_box_group:
            if coin_box.contents == s.FIREFLOWER:
                coin_box.contents = s.MUSHROOM

    def adjust_mario_for_x_collisions(self, collider):
        """Puts Mario flush next to the collider after moving on the x axis"""
        if self.mario.rect.x < collider.rect.x:
            self.mario.rect.right = collider.rect.left
        else:
            self.mario.rect.left = collider.rect.right

        self.mario.x_vel = 0

    def adjust_mario_for_x_shell_collisions(self, shell):
        """Deals with Mario if he hits a shell moving on the x axis"""
        if shell.state == s.JUMPED_ON:
            if self.mario.rect.x < shell.rect.x:
                self.game_info[s.SCORE] += 400
                self.moving_score_list.append(
                    score.Score(shell.rect.centerx - self.viewport.x,
                                shell.rect.y,
                                400))
                self.mario.rect.right = shell.rect.left
                shell.direction = s.RIGHT
                shell.x_vel = 5
                shell.rect.x += 5

            else:
                self.mario.rect.left = shell.rect.right
                shell.direction = s.LEFT
                shell.x_vel = -5
                shell.rect.x += -5

            shell.state = s.SHELL_SLIDE

        elif shell.state == s.SHELL_SLIDE:
            if self.mario.big and not self.mario.invincible:
                self.mario.state = s.BIG_TO_SMALL
            elif self.mario.invincible:
                self.game_info[s.SCORE] += 200
                self.moving_score_list.append(
                    score.Score(shell.rect.right - self.viewport.x,
                                shell.rect.y, 200))
                shell.kill()
                self.sprites_about_to_die_group.add(shell)
                shell.start_death_jump(s.RIGHT)
            else:
                if not self.mario.hurt_invincible and not self.mario.invincible:
                    self.state = s.FROZEN
                    self.mario.start_death_jump(self.game_info)

    def check_mario_y_collisions(self):
        """Checks for collisions when Mario moves along the y-axis"""
        ground_step_or_pipe = pg.sprite.spritecollideany(self.mario, self.ground_step_pipe_group)
        enemy = pg.sprite.spritecollideany(self.mario, self.enemy_group)
        shell = pg.sprite.spritecollideany(self.mario, self.shell_group)
        brick = pg.sprite.spritecollideany(self.mario, self.brick_group)
        coin_box = pg.sprite.spritecollideany(self.mario, self.coin_box_group)
        powerup = pg.sprite.spritecollideany(self.mario, self.powerup_group)

        brick, coin_box = self.prevent_collision_conflict(brick, coin_box)

        if coin_box:
            self.adjust_mario_for_y_coin_box_collisions(coin_box)

        elif brick:
            self.adjust_mario_for_y_brick_collisions(brick)

        elif ground_step_or_pipe:
            self.adjust_mario_for_y_ground_pipe_collisions(ground_step_or_pipe)

        elif enemy:
            if self.mario.invincible:
                setup.SFX['kick'].play()
                enemy.kill()
                self.sprites_about_to_die_group.add(enemy)
                enemy.start_death_jump(s.RIGHT)
            else:
                self.adjust_mario_for_y_enemy_collisions(enemy)

        elif shell:
            self.adjust_mario_for_y_shell_collisions(shell)

        elif powerup:
            if powerup.name == s.STAR:
                setup.SFX['powerup'].play()
                powerup.kill()
                self.mario.invincible = True
                self.mario.invincible_start_timer = self.current_time

        self.test_if_mario_is_falling()

    def prevent_collision_conflict(self, obstacle1, obstacle2):
        """Allows collisions only for the item closest to marios centerx"""
        if obstacle1 and obstacle2:
            obstacle1_distance = self.mario.rect.centerx - obstacle1.rect.centerx
            if obstacle1_distance < 0:
                obstacle1_distance *= -1
            obstacle2_distance = self.mario.rect.centerx - obstacle2.rect.centerx
            if obstacle2_distance < 0:
                obstacle2_distance *= -1

            if obstacle1_distance < obstacle2_distance:
                obstacle2 = False
            else:
                obstacle1 = False

        return obstacle1, obstacle2

    def adjust_mario_for_y_coin_box_collisions(self, coin_box):
        """Mario collisions with coin boxes on the y-axis"""
        if self.mario.rect.y > coin_box.rect.y:
            if coin_box.state == s.RESTING:
                if coin_box.contents == s.COIN:
                    self.game_info[s.SCORE] += 200
                    coin_box.start_bump(self.moving_score_list)
                    if coin_box.contents == s.COIN:
                        self.game_info[s.COIN_TOTAL] += 1
                else:
                    coin_box.start_bump(self.moving_score_list)

            elif coin_box.state == s.OPENED:
                pass
            setup.SFX['bump'].play()
            self.mario.y_vel = 7
            self.mario.rect.y = coin_box.rect.bottom
            self.mario.state = s.FALL
        else:
            self.mario.y_vel = 0
            self.mario.rect.bottom = coin_box.rect.top
            self.mario.state = s.WALK

    def adjust_mario_for_y_brick_collisions(self, brick):
        """Mario collisions with bricks on the y-axis"""
        if self.mario.rect.y > brick.rect.y:
            if brick.state == s.RESTING:
                if self.mario.big and brick.contents is None:
                    setup.SFX['brick_smash'].play()
                    self.check_if_enemy_on_brick(brick)
                    brick.kill()
                    self.brick_pieces_group.add(
                        bricks.BrickPiece(brick.rect.x,
                                          brick.rect.y - (brick.rect.height / 2),
                                          -2, -12),
                        bricks.BrickPiece(brick.rect.right,
                                          brick.rect.y - (brick.rect.height / 2),
                                          2, -12),
                        bricks.BrickPiece(brick.rect.x,
                                          brick.rect.y,
                                          -2, -6),
                        bricks.BrickPiece(brick.rect.right,
                                          brick.rect.y,
                                          2, -6))
                else:
                    setup.SFX['bump'].play()
                    if brick.coin_total > 0:
                        self.game_info[s.COIN_TOTAL] += 1
                        self.game_info[s.SCORE] += 200
                    self.check_if_enemy_on_brick(brick)
                    brick.start_bump(self.moving_score_list)
            elif brick.state == s.OPENED:
                setup.SFX['bump'].play()
            self.mario.y_vel = 7
            self.mario.rect.y = brick.rect.bottom
            self.mario.state = s.FALL

        else:
            self.mario.y_vel = 0
            self.mario.rect.bottom = brick.rect.top
            self.mario.state = s.WALK

    def check_if_enemy_on_brick(self, brick):
        """Kills enemy if on a bumped or broken brick"""
        brick.rect.y -= 5

        enemy = pg.sprite.spritecollideany(brick, self.enemy_group)

        if enemy:
            setup.SFX['kick'].play()
            self.game_info[s.SCORE] += 100
            self.moving_score_list.append(
                score.Score(enemy.rect.centerx - self.viewport.x,
                            enemy.rect.y,
                            100))
            enemy.kill()
            self.sprites_about_to_die_group.add(enemy)
            if self.mario.rect.centerx > brick.rect.centerx:
                enemy.start_death_jump('right')
            else:
                enemy.start_death_jump('left')

        brick.rect.y += 5

    def adjust_mario_for_y_ground_pipe_collisions(self, collider):
        """Mario collisions with pipes on the y-axis"""
        if collider.rect.bottom > self.mario.rect.bottom:
            self.mario.y_vel = 0
            self.mario.rect.bottom = collider.rect.top
            if self.mario.state == s.END_OF_LEVEL_FALL:
                self.mario.state = s.WALKING_TO_CASTLE
            else:
                self.mario.state = s.WALK
        elif collider.rect.top < self.mario.rect.top:
            self.mario.y_vel = 7
            self.mario.rect.top = collider.rect.bottom
            self.mario.state = s.FALL

    def test_if_mario_is_falling(self):
        """Changes Mario to a FALL state if more than a pixel above a pipe,
        ground, step or box"""
        self.mario.rect.y += 1
        test_collide_group = pg.sprite.Group(self.ground_step_pipe_group,
                                             self.brick_group,
                                             self.coin_box_group)

        if pg.sprite.spritecollideany(self.mario, test_collide_group) is None:
            if self.mario.state != s.JUMP \
                    and self.mario.state != s.DEATH_JUMP \
                    and self.mario.state != s.SMALL_TO_BIG \
                    and self.mario.state != s.BIG_TO_FIRE \
                    and self.mario.state != s.BIG_TO_SMALL \
                    and self.mario.state != s.FLAGPOLE \
                    and self.mario.state != s.WALKING_TO_CASTLE \
                    and self.mario.state != s.END_OF_LEVEL_FALL:
                self.mario.state = s.FALL
            elif self.mario.state == s.WALKING_TO_CASTLE or \
                    self.mario.state == s.END_OF_LEVEL_FALL:
                self.mario.state = s.END_OF_LEVEL_FALL

        self.mario.rect.y -= 1

    def adjust_mario_for_y_enemy_collisions(self, enemy):
        """Mario collisions with all enemies on the y-axis"""
        if self.mario.y_vel > 0:
            setup.SFX['stomp'].play()
            self.game_info[s.SCORE] += 100
            self.moving_score_list.append(
                score.Score(enemy.rect.centerx - self.viewport.x,
                            enemy.rect.y, 100))
            enemy.state = s.JUMPED_ON
            enemy.kill()
            if enemy.name == s.GOOMBA:
                enemy.death_timer = self.current_time
                self.sprites_about_to_die_group.add(enemy)
            elif enemy.name == s.KOOPA:
                self.shell_group.add(enemy)

            self.mario.rect.bottom = enemy.rect.top
            self.mario.state = s.JUMP
            self.mario.y_vel = -7

    def adjust_mario_for_y_shell_collisions(self, shell):
        """Mario collisions with Koopas in their shells on the y axis"""
        if self.mario.y_vel > 0:
            self.game_info[s.SCORE] += 400
            self.moving_score_list.append(
                score.Score(self.mario.rect.centerx - self.viewport.x,
                            self.mario.rect.y, 400))
            if shell.state == s.JUMPED_ON:
                setup.SFX['kick'].play()
                shell.state = s.SHELL_SLIDE
                if self.mario.rect.centerx < shell.rect.centerx:
                    shell.direction = s.RIGHT
                    shell.rect.left = self.mario.rect.right + 5
                else:
                    shell.direction = s.LEFT
                    shell.rect.right = self.mario.rect.left - 5
            else:
                shell.state = s.JUMPED_ON

    def adjust_enemy_position(self):
        """Moves all enemies along the x, y axes and check for collisions"""
        for enemy in self.enemy_group:
            enemy.rect.x += enemy.x_vel
            self.check_enemy_x_collisions(enemy)

            enemy.rect.y += enemy.y_vel
            self.check_enemy_y_collisions(enemy)
            self.delete_if_off_screen(enemy)

    def check_enemy_x_collisions(self, enemy):
        """Enemy collisions along the x axis.  Removes enemy from enemy group
        in order to check against all other enemies then adds it back."""
        enemy.kill()

        collider = pg.sprite.spritecollideany(enemy, self.ground_step_pipe_group)
        enemy_collider = pg.sprite.spritecollideany(enemy, self.enemy_group)

        if collider:
            if enemy.direction == s.RIGHT:
                enemy.rect.right = collider.rect.left
                enemy.flipFrames()
                enemy.direction = s.LEFT
                enemy.x_vel = -2
            elif enemy.direction == s.LEFT:
                enemy.rect.left = collider.rect.right
                enemy.flipFrames()
                enemy.direction = s.RIGHT
                enemy.x_vel = 2



        elif enemy_collider:
            if enemy.direction == s.RIGHT:
                enemy.rect.right = enemy_collider.rect.left
                enemy.direction = s.LEFT
                enemy.flipFrames()
                enemy_collider.direction = s.RIGHT
                enemy.x_vel = -2
                enemy_collider.x_vel = 2
            elif enemy.direction == s.LEFT:
                enemy.rect.left = enemy_collider.rect.right
                enemy.direction = s.RIGHT
                enemy.flipFrames()
                enemy_collider.direction = s.LEFT
                enemy.x_vel = 2
                enemy_collider.x_vel = -2

        self.enemy_group.add(enemy)
        self.mario_and_enemy_group.add(self.enemy_group)

    def check_enemy_y_collisions(self, enemy):
        """Enemy collisions on the y axis"""
        collider = pg.sprite.spritecollideany(enemy, self.ground_step_pipe_group)
        brick = pg.sprite.spritecollideany(enemy, self.brick_group)
        coin_box = pg.sprite.spritecollideany(enemy, self.coin_box_group)

        if enemy.name == "Eating Plant":
            pass
        else:
            if collider:
                if enemy.rect.bottom > collider.rect.bottom:
                    enemy.y_vel = 7
                    enemy.rect.top = collider.rect.bottom
                    enemy.state = s.FALL
                elif enemy.rect.bottom < collider.rect.bottom:

                    enemy.y_vel = 0
                    enemy.rect.bottom = collider.rect.top
                    enemy.state = s.WALK

            elif brick:
                if brick.state == s.BUMPED:
                    enemy.kill()
                    self.sprites_about_to_die_group.add(enemy)
                    if self.mario.rect.centerx > brick.rect.centerx:
                        enemy.start_death_jump('right')
                    else:
                        enemy.start_death_jump('left')

                elif enemy.rect.x > brick.rect.x:
                    enemy.y_vel = 7
                    enemy.rect.top = brick.rect.bottom
                    enemy.state = s.FALL
                else:
                    enemy.y_vel = 0
                    enemy.rect.bottom = brick.rect.top
                    enemy.state = s.WALK

            elif coin_box:
                if coin_box.state == s.BUMPED:
                    self.game_info[s.SCORE] += 100
                    self.moving_score_list.append(
                        score.Score(enemy.rect.centerx - self.viewport.x,
                                    enemy.rect.y, 100))
                    enemy.kill()
                    self.sprites_about_to_die_group.add(enemy)
                    if self.mario.rect.centerx > coin_box.rect.centerx:
                        enemy.start_death_jump('right')
                    else:
                        enemy.start_death_jump('left')

                elif enemy.rect.x > coin_box.rect.x:
                    enemy.y_vel = 7
                    enemy.rect.top = coin_box.rect.bottom
                    enemy.state = s.FALL
                else:
                    enemy.y_vel = 0
                    enemy.rect.bottom = coin_box.rect.top
                    enemy.state = s.WALK


            else:
                enemy.rect.y += 1
                test_group = pg.sprite.Group(self.ground_step_pipe_group,
                                             self.coin_box_group,
                                             self.brick_group)
                if pg.sprite.spritecollideany(enemy, test_group) is None:
                    if enemy.state != s.JUMP:
                        enemy.state = s.FALL

                enemy.rect.y -= 1

    def adjust_shell_position(self):
        """Moves any koopa in a shell along the x, y axes and checks for
        collisions"""
        for shell in self.shell_group:
            shell.rect.x += shell.x_vel
            self.check_shell_x_collisions(shell)

            shell.rect.y += shell.y_vel
            self.check_shell_y_collisions(shell)
            self.delete_if_off_screen(shell)

    def check_shell_x_collisions(self, shell):
        """Shell collisions along the x axis"""
        collider = pg.sprite.spritecollideany(shell, self.ground_step_pipe_group)
        enemy = pg.sprite.spritecollideany(shell, self.enemy_group)

        if collider:
            setup.SFX['bump'].play()
            if shell.x_vel > 0:
                shell.direction = s.LEFT
                shell.rect.right = collider.rect.left
            else:
                shell.direction = s.RIGHT
                shell.rect.left = collider.rect.right

        if enemy:
            setup.SFX['kick'].play()
            self.game_info[s.SCORE] += 100
            self.moving_score_list.append(
                score.Score(enemy.rect.right - self.viewport.x,
                            enemy.rect.y, 100))
            enemy.kill()
            self.sprites_about_to_die_group.add(enemy)
            enemy.start_death_jump(shell.direction)

    def check_shell_y_collisions(self, shell):
        """Shell collisions along the y axis"""
        collider = pg.sprite.spritecollideany(shell, self.ground_step_pipe_group)

        if collider:
            shell.y_vel = 0
            shell.rect.bottom = collider.rect.top
            shell.state = s.SHELL_SLIDE

        else:
            shell.rect.y += 1
            if pg.sprite.spritecollideany(shell, self.ground_step_pipe_group) is None:
                shell.state = s.FALL
            shell.rect.y -= 1

    def adjust_powerup_position(self):
        """Moves mushrooms, stars and fireballs along the x, y axes"""
        for powerup in self.powerup_group:
            if powerup.name == s.MUSHROOM:
                self.adjust_mushroom_position(powerup)
            elif powerup.name == s.STAR:
                self.adjust_star_position(powerup)
            elif powerup.name == s.FIREBALL:
                self.adjust_fireball_position(powerup)
            elif powerup.name == '1up_mushroom':
                self.adjust_mushroom_position(powerup)

    def adjust_mushroom_position(self, mushroom):
        """Moves mushroom along the x, y axes."""
        if mushroom.state != s.REVEAL:
            mushroom.rect.x += mushroom.x_vel
            self.check_mushroom_x_collisions(mushroom)

            mushroom.rect.y += mushroom.y_vel
            self.check_mushroom_y_collisions(mushroom)
            self.delete_if_off_screen(mushroom)

    def check_mushroom_x_collisions(self, mushroom):
        """Mushroom collisions along the x axis"""
        collider = pg.sprite.spritecollideany(mushroom, self.ground_step_pipe_group)
        brick = pg.sprite.spritecollideany(mushroom, self.brick_group)
        coin_box = pg.sprite.spritecollideany(mushroom, self.coin_box_group)

        if collider:
            self.adjust_mushroom_for_collision_x(mushroom, collider)

        elif brick:
            self.adjust_mushroom_for_collision_x(mushroom, brick)

        elif coin_box:
            self.adjust_mushroom_for_collision_x(mushroom, coin_box)

    def check_mushroom_y_collisions(self, mushroom):
        """Mushroom collisions along the y axis"""
        collider = pg.sprite.spritecollideany(mushroom, self.ground_step_pipe_group)
        brick = pg.sprite.spritecollideany(mushroom, self.brick_group)
        coin_box = pg.sprite.spritecollideany(mushroom, self.coin_box_group)

        if collider:
            self.adjust_mushroom_for_collision_y(mushroom, collider)
        elif brick:
            self.adjust_mushroom_for_collision_y(mushroom, brick)
        elif coin_box:
            self.adjust_mushroom_for_collision_y(mushroom, coin_box)
        else:
            self.check_if_falling(mushroom, self.ground_step_pipe_group)
            self.check_if_falling(mushroom, self.brick_group)
            self.check_if_falling(mushroom, self.coin_box_group)

    def adjust_mushroom_for_collision_x(self, item, collider):
        """Changes mushroom direction if collision along x axis"""
        if item.rect.x < collider.rect.x:
            item.rect.right = collider.rect.x
            item.direction = s.LEFT
        else:
            item.rect.x = collider.rect.right
            item.direction = s.RIGHT

    def adjust_mushroom_for_collision_y(self, item, collider):
        """Changes mushroom state to SLIDE after hitting ground from fall"""
        item.rect.bottom = collider.rect.y
        item.state = s.SLIDE
        item.y_vel = 0

    def adjust_star_position(self, star):
        """Moves invincible star along x, y axes and checks for collisions"""
        if star.state == s.BOUNCE:
            star.rect.x += star.x_vel
            self.check_mushroom_x_collisions(star)
            star.rect.y += star.y_vel
            self.check_star_y_collisions(star)
            star.y_vel += star.gravity
            self.delete_if_off_screen(star)

    def check_star_y_collisions(self, star):
        """Invincible star collisions along y axis"""
        collider = pg.sprite.spritecollideany(star, self.ground_step_pipe_group)
        brick = pg.sprite.spritecollideany(star, self.brick_group)
        coin_box = pg.sprite.spritecollideany(star, self.coin_box_group)

        if collider:
            self.adjust_star_for_collision_y(star, collider)
        elif brick:
            self.adjust_star_for_collision_y(star, brick)
        elif coin_box:
            self.adjust_star_for_collision_y(star, coin_box)

    def adjust_star_for_collision_y(self, star, collider):
        """Allows for a star bounce off the ground and on the bottom of a
        box"""
        if star.rect.y > collider.rect.y:
            star.rect.y = collider.rect.bottom
            star.y_vel = 0
        else:
            star.rect.bottom = collider.rect.top
            star.start_bounce(-8)

    def adjust_fireball_position(self, fireball):
        """Moves fireball along the x, y axes and checks for collisions"""
        if fireball.state == s.FLYING:
            fireball.rect.x += fireball.x_vel
            self.check_fireball_x_collisions(fireball)
            fireball.rect.y += fireball.y_vel
            self.check_fireball_y_collisions(fireball)
        elif fireball.state == s.BOUNCING:
            fireball.rect.x += fireball.x_vel
            self.check_fireball_x_collisions(fireball)
            fireball.rect.y += fireball.y_vel
            self.check_fireball_y_collisions(fireball)
            fireball.y_vel += fireball.gravity
        self.delete_if_off_screen(fireball)

    def bounce_fireball(self, fireball):
        """Simulates fireball bounce off ground"""
        fireball.y_vel = -8
        if fireball.direction == s.RIGHT:
            fireball.x_vel = 15
        else:
            fireball.x_vel = -15

        if fireball in self.powerup_group:
            fireball.state = s.BOUNCING

    def check_fireball_x_collisions(self, fireball):
        """Fireball collisions along x axis"""
        collide_group = pg.sprite.Group(self.ground_group,
                                        self.pipe_group,
                                        self.step_group,
                                        self.coin_box_group,
                                        self.brick_group)

        collider = pg.sprite.spritecollideany(fireball, collide_group)

        if collider:
            fireball.kill()
            self.sprites_about_to_die_group.add(fireball)
            fireball.explode_transition()

    def check_fireball_y_collisions(self, fireball):
        """Fireball collisions along y axis"""
        collide_group = pg.sprite.Group(self.ground_group,
                                        self.pipe_group,
                                        self.step_group,
                                        self.coin_box_group,
                                        self.brick_group)

        collider = pg.sprite.spritecollideany(fireball, collide_group)
        enemy = pg.sprite.spritecollideany(fireball, self.enemy_group)
        shell = pg.sprite.spritecollideany(fireball, self.shell_group)

        if collider and (fireball in self.powerup_group):
            fireball.rect.bottom = collider.rect.y
            self.bounce_fireball(fireball)

        elif enemy:
            self.fireball_kill(fireball, enemy)

        elif shell:
            self.fireball_kill(fireball, shell)

    def fireball_kill(self, fireball, enemy):
        """Kills enemy if hit with fireball"""
        setup.SFX['kick'].play()
        self.game_info[s.SCORE] += 100
        self.moving_score_list.append(
            score.Score(enemy.rect.centerx - self.viewport.x,
                        enemy.rect.y, 100))
        fireball.kill()
        enemy.kill()
        self.sprites_about_to_die_group.add(enemy, fireball)
        enemy.start_death_jump(fireball.direction)
        fireball.explode_transition()

    def check_if_falling(self, sprite, sprite_group):
        """Checks if sprite should enter a falling state"""
        sprite.rect.y += 1

        if pg.sprite.spritecollideany(sprite, sprite_group) is None:
            if sprite.state != s.JUMP:
                sprite.state = s.FALL

        sprite.rect.y -= 1

    def delete_if_off_screen(self, enemy):
        """Removes enemy from sprite groups if 500 pixels left off the screen,
         underneath the bottom of the screen, or right of the screen if shell"""
        if enemy.rect.x < (self.viewport.x - 300):
            enemy.kill()

        elif enemy.rect.y > (self.viewport.bottom):
            enemy.kill()

        elif enemy.state == s.SHELL_SLIDE:
            if enemy.rect.x > (self.viewport.right + 500):
                enemy.kill()

    def check_flag(self):
        """Adjusts mario's state when the flag is at the bottom"""
        if (self.flag.state == s.BOTTOM_OF_POLE
                and self.mario.state == s.FLAGPOLE):
            self.mario.set_state_to_bottom_of_pole()

    def check_to_add_flag_score(self):
        """Adds flag score if at top"""
        if self.flag_score.y_vel == 0:
            self.game_info[s.SCORE] += self.flag_score_total
            self.flag_score_total = 0

    def check_for_mario_death(self):
        """Restarts the level if Mario is dead"""
        if self.mario.rect.y > s.SCREEN_HEIGHT and not self.mario.in_castle:
            self.mario.dead = True
            self.mario.x_vel = 0
            self.state = s.FROZEN
            self.game_info[s.MARIO_DEAD] = True

        if self.mario.dead:
            self.play_death_song()

    def play_death_song(self):
        if self.death_timer == 0:
            self.death_timer = self.current_time
        elif (self.current_time - self.death_timer) > 3000:
            self.set_game_info_values()
            self.done = True

    def set_game_info_values(self):
        """sets the new game values after a player's death"""
        if self.game_info[s.SCORE] > self.persist[s.TOP_SCORE]:
            self.persist[s.TOP_SCORE] = self.game_info[s.SCORE]
        if self.mario.dead:
            self.persist[s.LIVES] -= 1

        if self.persist[s.LIVES] == 0:
            self.next = s.GAME_OVER
            self.game_info[s.CAMERA_START_X] = 0
        elif self.mario.dead == False:
            self.next = s.MAIN_MENU
            self.game_info[s.CAMERA_START_X] = 0
        elif self.overhead_info_display.time == 0:
            self.next = s.TIME_OUT
        else:
            if self.mario.rect.x > 0 \
                    and self.game_info[s.CAMERA_START_X] == 0:
                self.game_info[s.CAMERA_START_X] = 0
            self.next = s.LOAD_SCREEN

    def check_if_time_out(self):
        """Check if time has run down to 0"""
        if self.overhead_info_display.time <= 0 \
                and not self.mario.dead \
                and not self.mario.in_castle:
            self.state = s.FROZEN
            self.mario.start_death_jump(self.game_info)

    def update_viewport(self):
        """Changes the view of the camera"""
        third = self.viewport.x + self.viewport.w // 6
        mario_center = self.mario.rect.centerx
        mario_right = self.mario.rect.right

        if self.mario.x_vel > 0 and mario_center >= third:
            mult = 0.5 if mario_right < self.viewport.centerx else 1
            new = self.viewport.x + mult * self.mario.x_vel
            highest = self.level_rect.w - self.viewport.w
            self.viewport.x = min(highest, new)

    def update_while_in_castle(self):
        """Updates while Mario is in castle at the end of the level"""
        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_info)
        self.overhead_info_display.update(self.game_info)

        if self.overhead_info_display.state == s.END_OF_LEVEL:
            self.state = s.FLAG_AND_FIREWORKS
            self.flag_pole_group.add(castle_flag.Flag(8745, 322))

    def update_flag_and_fireworks(self):
        """Updates the level for the fireworks and castle flag"""
        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_info)
        self.overhead_info_display.update(self.game_info)
        self.flag_pole_group.update()

        self.end_game()

    def end_game(self):
        """End the game"""
        if self.flag_timer == 0:
            self.flag_timer = self.current_time
        elif (self.current_time - self.flag_timer) > 2000:
            self.set_game_info_values()
            self.next = s.GAME_OVER
            self.sound_manager.stop_music()
            self.done = True

    def blit_everything(self, surface):
        """Blit all sprites to the main surface"""
        self.level.blit(self.background, self.viewport, self.viewport)
        if self.flag_score:
            self.flag_score.draw(self.level)
        self.powerup_group.draw(self.level)
        self.coin_group.draw(self.level)
        self.brick_group.draw(self.level)
        self.coin_box_group.draw(self.level)
        self.sprites_about_to_die_group.draw(self.level)
        self.shell_group.draw(self.level)
        #self.check_point_group.draw(self.level)
        self.brick_pieces_group.draw(self.level)
        self.flag_pole_group.draw(self.level)
        self.mario_and_enemy_group.draw(self.level)

        surface.blit(self.level, (0, 0), self.viewport)
        self.overhead_info_display.draw(surface)
        for score in self.moving_score_list:
            score.draw(surface)


