# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:12:39 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
w=Minecraft.create()
from random import choice
list2=[[11010100010101110110101010101010110101010101101101010101010101011011010101],[10101011011101001010101011011010110100101011010101010101010101101],[10101101001101111110100111111101100111111]]

id = w.getPlayerEntityId("P_ROOT")
x,y,z=w.entity.getTilePos(id)
starex = x
for list1 in list2:
    for i in list2:
        w.setBlock(x,y,z,i)
        x = x+1
    x= starex
    z =z+1