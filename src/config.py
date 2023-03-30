import pygame
import os

from sound import Sound
from theme import Theme

class Config:

    def __init__(self):
        self.themes = []
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        self.font = pygame.font.SysFont('monospace', 18, bold=True)
        self.move_sound = Sound(
            os.path.join('assets/sounds/move.wav'))
        self.capture_sound = Sound(
            os.path.join('assets/sounds/capture.wav'))

    def change_theme(self):
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]

    def _add_themes(self):
        green = Theme((234, 235, 200), (119, 154, 88), (244, 247, 116), (172, 195, 51), '#C86464', '#C84646')
        brown = Theme((235, 209, 166), (165, 117, 80), (245, 234, 100), (209, 185, 59), '#C86464', '#C84646')
        blue = Theme((229, 228, 200), (60, 95, 135), (123, 187, 227), (43, 119, 191), '#C86464', '#C84646')
        grey = Theme((120, 119, 118), (86, 85, 84), (99, 126, 143), (82, 102, 128), '#C86464', '#C84646')
        purple = Theme((187, 143, 206), (113, 88, 152), (229, 200, 247), (165, 94, 234), '#D95C5C', '#D93636')
        pink = Theme((255, 192, 203), (240, 128, 128), (255, 182, 193), (219, 112, 147), '#FFD700', '#FFA500')
        indigo = Theme((75, 0, 130), (36, 5, 81), (138, 43, 226), (75, 0, 130), '#E32636', '#C41E3A')
        navy_blue = Theme((0, 0, 128), (0, 0, 51), (30, 30, 255), (0, 0, 128), '#FFA500', '#FF8C00')



        self.themes = [green, brown, blue, grey, purple, pink, indigo, navy_blue]