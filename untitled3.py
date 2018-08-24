# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:35:08 2018

@author: NTPU
"""
import random,time
from mcpi.minecraft import Minecraft
w=Minecraft.create
x,y,z= w.player.getTilePos()

r=random.randrange(1,16)
while True:
    w.setblocks(x+25,y-1,z+25,x-25,y-1,z-25,r)
    time.sleep(0.5)
#w.player.setPos(x+0.5,y,z+0.5,11)