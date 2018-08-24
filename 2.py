# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 15:31:22 2018

@author: NTPU
"""

import time
from mcpi.minecraft import Minecraft
w=Minecraft.create
time.sleep(7)


x,y,z= w.player.getTilpos()
c=1
while c<100:
    w.postToChat("str(x)str(y)str(z)")
    time.sleep(1)
    c=c+1