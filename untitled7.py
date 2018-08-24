# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:34:30 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
w=Minecraft.create()
x,y,z= w.player.getTilePos()



w.setSign(x,y,z,63,0,"030","@@","QAQ","0.0")