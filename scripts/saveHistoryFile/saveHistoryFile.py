#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# FileName: saveHistoryFile
#
# Version: 0.1
# Author : PanYu
# Contact: blood-vampire@foxmail.com
# Created on 2017/1/11 17:45


import os
import sys
import time
import shutil

import pymel.core as pm

class SaveHistoryFile(object):
    def __init__(self):
        super(SaveHistoryFile, self).__init__()
    def removeUnknownPlugin(self):
        unPlugin = pm.unknownPlugin(q=True, l=True)
        if unPlugin:
            for i in unPlugin:
                try:
                    pm.unknownPlugin(i, remove=True)
                except:
                    pass

    def saveHistoryFile(self):
        fileDirPath,baseFileName = os.path.split(pm.sceneName())
        fileNowTime = time.strftime("%Y-%m-%d-%H-%M-%S")
        historyDir = os.path.join(fileDirPath, 'history')
        if not os.path.isdir(historyDir):
            os.mkdir(historyDir)
        fileNowTimeDir = os.path.join(historyDir, fileNowTime)
        os.makedirs(fileNowTimeDir)
        newFilePath = os.path.join(fileNowTimeDir, baseFileName)
        shutil.copy(sceneName(), newFilePath)
        saveFile(force=True)

def main():
    doit = SaveHistoryFile()
    doit.saveHistoryFile()

if __name__ == '__main__':
    main()