# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:47:57 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
w=Minecraft.create
x,y,z= w.player.getTilePos()

a=w.getBlock(x+1,y,z)
b=w.getBlock(x-1,y,z)
c=w.getBlock(x,y,z+1)
d=w.getBlock(x,y,z-1)
if a==8 or a==9 or b==8 or b==9 or c==8 or c==9 or d==8 or d==9:
    w.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,11)





