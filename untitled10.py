# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:39:43 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
w=Minecraft.create
x,y,z= w.player.getTilePos()


w.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,11)
w.setBlocks(x,y,z,x,y+4,z,1)