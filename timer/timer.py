import time
import pygame
import threading


class Timer (threading.Thread):
    def __init__(self, minutes, stop):
        threading.Thread.__init__(self)
        self.daemon = True

        pygame.mixer.init()

        self.minutes = minutes
        self.stop = stop

    def run(self):
        if self.minutes == 2:
            seconds = 122.5
            while seconds >= 0.0 and not self.stop.is_set():
                # ----------- STARTING PHASE ------------------
                if seconds == 122.5 or seconds == 122.0 or seconds == 120.0:
                    pygame.mixer.music.load("WHISTLE.wav")
                    pygame.mixer.music.play()  # BEEP 1/2/3
                # ------------ COMMENCE SHOOTING ---------------
                if seconds == 60.0:
                    pygame.mixer.music.load("WHISTLE.wav")
                    pygame.mixer.music.play()  # 1 MINUTE REMAINING

                if seconds == 0.0:
                    pygame.mixer.music.load("WHISTLE.wav")
                    pygame.mixer.music.play()  # 0 MINUTE REMAINING
                # --------------- END SHOOTING ---------------
                seconds -= 0.5
                time.sleep(0.5)

        elif self.minutes == 3:
            seconds = 182.5
            while seconds >= 0.0 and not self.stop.is_set():
                # ----------- STARTING PHASE ------------------
                if seconds == 182.5 or seconds == 182.0 or seconds == 180.0:
                    pygame.mixer.music.load("WHISTLE.wav")
                    pygame.mixer.music.play()  # BEEP 1/2/3
                # ------------ COMMENCE SHOOTING ---------------
                if seconds == 60.0:
                    pygame.mixer.music.load("WHISTLE.wav")
                    pygame.mixer.music.play()  # 1 MINUTE REMAINING

                if seconds == 0.0:
                    pygame.mixer.music.load("WHISTLE.wav")
                    pygame.mixer.music.play()  # 0 MINUTE REMAINING
                # --------------- END SHOOTING ---------------
                seconds -= 0.5
                time.sleep(0.5)

        elif self.minutes == 4:
            seconds = 242.5
            while seconds >= 0.0 and not self.stop.is_set():
                # ----------- STARTING PHASE ------------------
                if seconds == 242.5 or seconds == 242.0 or seconds == 240.0:
                    pygame.mixer.music.load("WHISTLE.wav")
                    pygame.mixer.music.play()  # BEEP 1/2/3
                # ------------ COMMENCE SHOOTING ---------------
                if seconds == 120.0:
                    pygame.mixer.music.load("WHISTLE.wav")
                    pygame.mixer.music.play()  # 2 MINUTE REMAINING

                if seconds == 60.0:
                    pygame.mixer.music.load("WHISTLE.wav")
                    pygame.mixer.music.play()  # 1 MINUTE REMAINING

                if seconds == 0.0:
                    pygame.mixer.music.load("WHISTLE.wav")
                    pygame.mixer.music.play()  # 0 MINUTE REMAINING
                # --------------- END SHOOTING ---------------
                seconds -= 0.5
                time.sleep(0.5)
