# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:06:44 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
w=Minecraft.create
x,y,z= w.player.getTilePos()
e=10
l=6
h=5
b=1
a=0
w.setBlocks(x,y,z,x+e,y+l,z+h)
w.setBlocks(x+1,y+1,z+1,x+e-1,y+l-1,z+h-1)