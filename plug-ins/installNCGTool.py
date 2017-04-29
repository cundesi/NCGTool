#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#@FileName:installCAS
#
#@Version: 0.1
#@Author: PanYu
#@Contact: blood-vampire@foxmail.com
#@Created on 2016/8/9 22:00

import maya.cmds as cm
import maya.mel as mel
import creatShelves
reload(creatShelves)


def installCAS():
    CasShelf = [cas for cas in cm.lsUI(type = 'shelfLayout') if cas.split('|')[-1] == "NCGTool"]
    if CasShelf:
        cm.deleteUI(CasShelf[-1])
    creatShelves.main()
    
def uninstallCAS():
    CasShelf = [cas for cas in cm.lsUI(type = 'shelfLayout') if cas.split('|')[-1] == "NCGTool"]
    if CasShelf:
        cm.deleteUI(CasShelf[-1])
    
def initializePlugin(mobject):
    installCAS()

def uninitializePlugin(mobject):
    uninstallCAS()
