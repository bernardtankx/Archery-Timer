import time
import pygame
import threading


class Timer (threading.Thread):
    def __init__(self, minutes, stop):
        threading.Thread.__init__(self)
        self.daemon = True

        pygame.mixer.init()

        self.minutes = minutes
        self.seconds = 0
        self.stop = stop

    def run(self):
        if self.minutes == 2:
            self.seconds = 122.5
            while self.seconds >= 0.0 and not self.stop.is_set():
                # ----------- STARTING PHASE ------------------
                if self.seconds == 122.5 or self.seconds == 122.0 or self.seconds == 120.0:
                    pygame.mixer.music.load("whistle.ogg")
                    pygame.mixer.music.play()  # BEEP 1/2/3
                # ------------ COMMENCE SHOOTING ---------------
                if self.seconds == 60.0:
                    pygame.mixer.music.load("oneminuteremaining.ogg")
                    pygame.mixer.music.play()  # 1 MINUTE REMAINING

                if self.seconds == 0.0:
                    pygame.mixer.music.load("whistle.ogg")
                    pygame.mixer.music.play()  # 0 MINUTE REMAINING
                # --------------- END SHOOTING ---------------
                time.sleep(0.5)
                self.seconds -= 0.5

        elif self.minutes == 3:
            self.seconds = 182.5
            while self.seconds >= 0.0 and not self.stop.is_set():
                # ----------- STARTING PHASE ------------------
                if self.seconds == 182.5 or self.seconds == 182.0 or self.seconds == 180.0:
                    pygame.mixer.music.load("whistle.ogg")
                    pygame.mixer.music.play()  # BEEP 1/2/3
                # ------------ COMMENCE SHOOTING ---------------
                if self.seconds == 60.0:
                    pygame.mixer.music.load("oneminuteremaining.ogg")
                    pygame.mixer.music.play()  # 1 MINUTE REMAINING

                if self.seconds == 0.0:
                    pygame.mixer.music.load("whistle.ogg")
                    pygame.mixer.music.play()  # 0 MINUTE REMAINING
                # --------------- END SHOOTING ---------------
                time.sleep(0.5)
                self.seconds -= 0.5

        elif self.minutes == 4:
            self.seconds = 242.5
            while self.seconds >= 0.0 and not self.stop.is_set():
                # ----------- STARTING PHASE ------------------
                if self.seconds == 242.5 or self.seconds == 242.0 or self.seconds == 240.0:
                    pygame.mixer.music.load("whistle.ogg")
                    pygame.mixer.music.play()  # BEEP 1/2/3
                # ------------ COMMENCE SHOOTING ---------------
                if self.seconds == 120.0:
                    pygame.mixer.music.load("twominutesremaining.ogg")
                    pygame.mixer.music.play()  # 2 MINUTE REMAINING

                if self.seconds == 60.0:
                    pygame.mixer.music.load("oneminuteremaining.ogg")
                    pygame.mixer.music.play()  # 1 MINUTE REMAINING

                if self.seconds == 0.0:
                    pygame.mixer.music.load("whistle.ogg")
                    pygame.mixer.music.play()  # 0 MINUTE REMAINING
                # --------------- END SHOOTING ---------------
                time.sleep(0.5)
                self.seconds -= 0.5
