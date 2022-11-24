# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:38:01 2022

@author: jgalb
"""

class Automobile:
    wheels = 4
    
    def __init__(self, size, color, speed):
        self.size = size
        self.color = color
        self.speed
    
    def drive(self):
        print("I'm moving!")

class Car(Automobile):
    
    def __init__(self, color, speed):
        self.size="small"
        self.color=color
        self.speed=speed
    
    def drive(self):
        super().drive()
        print("I'm really moving")
    

car = Car("red", 100)