# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:14:19 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
w=Minecraft.create
x,y,z= w.player.getTilpos()
w.setblock(x,y-1,z,11)
w.setblock(x+1,y-1,z,11)

w.setblock(x+2,y-1,z,11)

w.setblock(x+2,y-1,z-2,11)
 
w.setblock(x+2,y-1,z-2,11)

w.setblock(x+1,y-1,z-2,11)

w.setblock(x,y-1,z-2,11)

w.setblock(x,y-1,z-1,11)
