__author__ = 'CPSC 386 Dai Kieu, Trong To, Carlos Serna'

import pygame as pg
from . import setup
from . import settings as s

class Sound(object):
    """Handles all sound for the game"""
    def __init__(self, overhead_info):
        """Initialize the class"""
        self.sfx_dict = setup.SFX
        self.music_dict = setup.MUSIC
        self.overhead_info = overhead_info
        self.game_info = overhead_info.game_info
        self.set_music_mixer()



    def set_music_mixer(self):
        """Sets music for level"""
        if self.overhead_info.state == s.LEVEL:
            pg.mixer.music.load(self.music_dict['main_theme'])
            pg.mixer.music.play()
            self.state = s.NORMAL
        elif self.overhead_info.state == s.GAME_OVER:
            pg.mixer.music.load(self.music_dict['game_over'])
            pg.mixer.music.play()
            self.state = s.GAME_OVER


    def update(self, game_info, mario):
        """Updates sound object with game info"""
        self.game_info = game_info
        self.mario = mario
        self.handle_state()

    def  handle_state(self):
        """Handles the state of the soundn object"""
        if self.state == s.NORMAL:
            if self.mario.dead:
                self.play_music('death', s.MARIO_DEAD)
            elif self.mario.invincible \
                    and self.mario.losing_invincibility == False:
                self.play_music('invincible', s.MARIO_INVINCIBLE)
            elif self.mario.state == s.FLAGPOLE:
                self.play_music('flagpole', s.FLAGPOLE)
            elif self.overhead_info.time == 100:
                self.play_music('out_of_time', s.TIME_WARNING)


        elif self.state == s.FLAGPOLE:
            if self.mario.state == s.WALKING_TO_CASTLE:
                self.play_music('stage_clear', s.STAGE_CLEAR)

        elif self.state == s.STAGE_CLEAR:
            if self.mario.in_castle:
                self.sfx_dict['count_down'].play()
                self.state = s.FAST_COUNT_DOWN

        elif self.state == s.FAST_COUNT_DOWN:
            if self.overhead_info.time == 0:
                self.sfx_dict['count_down'].stop()
                self.state = s.WORLD_CLEAR

        elif self.state == s. TIME_WARNING:
            if pg.mixer.music.get_busy() == 0:
                self.play_music('main_theme_sped_up', s.SPED_UP_NORMAL)
            elif self.mario.dead:
                self.play_music('death', s.MARIO_DEAD)

        elif self.state == s.SPED_UP_NORMAL:
            if self.mario.dead:
                self.play_music('death', s.MARIO_DEAD)
            elif self.mario.state == s.FLAGPOLE:
                self.play_music('flagpole', s.FLAGPOLE)

        elif self.state == s.MARIO_INVINCIBLE:
            if (self.mario.current_time - self.mario.invincible_start_timer) > 11000:
                self.play_music('main_theme', s.NORMAL)
            elif self.mario.dead:
                self.play_music('death', s.MARIO_DEAD)


        elif self.state == s.WORLD_CLEAR:
            pass
        elif self.state == s.MARIO_DEAD:
            pass
        elif self.state == s.GAME_OVER:
            pass

    def play_music(self, key, state):
        """Plays new music"""
        pg.mixer.music.load(self.music_dict[key])
        pg.mixer.music.play()
        self.state = state

    def stop_music(self):
        """Stops playback"""
        pg.mixer.music.stop()



