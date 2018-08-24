# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:29:33 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
w=Minecraft.create
x,y,z= w.player.getTilePos()


while True:
    hits = w.events.pollProjectileHits()
    if len(hits)>0:
          h = hits[0]
          x,y,z = h.pos.x, h.pos.y, h.pos.z
          w.createExplosion(x,y,z,150)