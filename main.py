# modules
from tkinter import *
import pygame
import os

# music player classs
class MusicPlayer:


  
 def __init__(self,root):
    self.root = root
    self.root.title("Music Player")
    self.root.geometry("1000x200+200+200")
    pygame.init()
    pygame.mixer.init()
    self.track = StringVar()
    self.status = StringVar()
