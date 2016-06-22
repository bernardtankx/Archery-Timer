import os
import sys
import time
import pygame
from PyQt5 import QtCore


class Timer (QtCore.QThread):
    def __init__(self, minutes, stop):
        QtCore.QThread.__init__(self)

        pygame.mixer.init()
        self.sfx_whistle = resource_path(os.path.join('data', 'whistle.wav'))
        self.sfx_oneminute = resource_path(os.path.join('data', 'oneminute.wav'))
        self.sfx_twominutes = resource_path(os.path.join('data', 'twominutes.wav'))

        self.minutes = minutes
        self.seconds = 0
        self.stop = stop

    def run(self):
        if self.minutes == 2:
            self.seconds = 122.5
            while self.seconds >= 0.0 and not self.stop.isAccepted():
                # ----------- STARTING PHASE ------------------
                if self.seconds == 122.5 or self.seconds == 122.0 or self.seconds == 120.0:
                    pygame.mixer.music.load(self.sfx_whistle)
                    pygame.mixer.music.play()  # BEEP 1/2/3
                # ------------ COMMENCE SHOOTING ---------------
                if self.seconds == 60.0:
                    pygame.mixer.music.load(self.sfx_oneminute)
                    pygame.mixer.music.play()  # 1 MINUTE REMAINING

                if self.seconds == 0.0:
                    pygame.mixer.music.load(self.sfx_whistle)
                    pygame.mixer.music.play()  # 0 MINUTE REMAINING
                # --------------- END SHOOTING ---------------
                time.sleep(0.5)
                self.seconds -= 0.5

        elif self.minutes == 3:
            self.seconds = 182.5
            while self.seconds >= 0.0 and not self.stop.isAccepted():
                # ----------- STARTING PHASE ------------------
                if self.seconds == 182.5 or self.seconds == 182.0 or self.seconds == 180.0:
                    pygame.mixer.music.load(self.sfx_whistle)
                    pygame.mixer.music.play()  # BEEP 1/2/3
                # ------------ COMMENCE SHOOTING ---------------
                if self.seconds == 60.0:
                    pygame.mixer.music.load(self.sfx_oneminute)
                    pygame.mixer.music.play()  # 1 MINUTE REMAINING

                if self.seconds == 0.0:
                    pygame.mixer.music.load(self.sfx_whistle)
                    pygame.mixer.music.play()  # 0 MINUTE REMAINING
                # --------------- END SHOOTING ---------------
                time.sleep(0.5)
                self.seconds -= 0.5

        elif self.minutes == 4:
            self.seconds = 242.5
            while self.seconds >= 0.0 and not self.stop.isAccepted():
                # ----------- STARTING PHASE ------------------
                if self.seconds == 242.5 or self.seconds == 242.0 or self.seconds == 240.0:
                    pygame.mixer.music.load(self.sfx_whistle)
                    pygame.mixer.music.play()  # BEEP 1/2/3
                # ------------ COMMENCE SHOOTING ---------------
                if self.seconds == 120.0:
                    pygame.mixer.music.load(self.sfx_twominutes)
                    pygame.mixer.music.play()  # 2 MINUTE REMAINING

                if self.seconds == 60.0:
                    pygame.mixer.music.load(self.sfx_oneminute)
                    pygame.mixer.music.play()  # 1 MINUTE REMAINING

                if self.seconds == 0.0:
                    pygame.mixer.music.load(self.sfx_whistle)
                    pygame.mixer.music.play()  # 0 MINUTE REMAINING
                # --------------- END SHOOTING ---------------
                time.sleep(0.5)
                self.seconds -= 0.5


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)
