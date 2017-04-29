#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#@FileName:creatShelves
#
#@Version: 0.1
#@Author: PanYu
#@Contact: blood-vampire@foxmail.com
#@Created on 9/6/2016 8:59 PM


import os
import re
import pymel.core as pm
class NCGTool(object):
    def __init__(self):
        mayaScriptPath = pm.env.envVars['MAYA_SCRIPT_PATH']
        scriptPathPatterm = re.compile(r'[A-Z]\:([^:.])*/NCGTool/scripts')
        self.toolScriptPath = scriptPathPatterm.search(mayaScriptPath).group()

        iocnsPath = pm.env.envVars['XBMLANGPATH']
        iocnsPathpatterm = re.compile(r'[A-Z]\:([^:.])*/NCGTool/icons')
        toolIocnsPath = iocnsPathpatterm.search(iocnsPath).group()
        self.iconBaseName = [os.path.splitext(icon)[0] for icon in os.listdir(toolIocnsPath)]

    def creatShevlesBtn(self,shevlesCommand,parentLayout):

        shevlesCommandfn = 'import %s\n' % shevlesCommand
        shevlesCommandfn += 'reload(%s)\n' % shevlesCommand
        shevlesCommandfn += 'from %s import %s\n' % (shevlesCommand,shevlesCommand)
        shevlesCommandfn += 'reload(%s)\n' % shevlesCommand
        shevlesCommandfn += '%s.main()\n' % shevlesCommand

        if shevlesCommand in self.iconBaseName:
            iconName = shevlesCommand
        else:
            iconName = 'pythonFamily'

        pm.shelfButton(
            align = "center" ,
            label = shevlesCommand ,
            font = "plainLabelFont" ,
            imageOverlayLabel = shevlesCommand ,
            overlayLabelColor = (1,0,0) ,
            overlayLabelBackColor = (0,0,0,0.5) ,
            image = "%s.png" % iconName,
            image1 = "%s.png" % iconName,
            style = "iconOnly" ,
            command = shevlesCommandfn,
            sourceType = "python" ,
            parent = parentLayout
        )

    def creatShevlesFn(self):

        modFiles = [f for f in os.listdir(self.toolScriptPath) if os.path.isdir(os.path.join(self.toolScriptPath, f))]
        parentShelfLayout = [shelfPrLayout for shelfPrLayout in pm.lsUI(type = 'tabLayout')
                             if shelfPrLayout.shortName() == 'ShelfLayout'][-1]
        NCGToolshevl = pm.shelfLayout('NCGTool',parent = parentShelfLayout)
        for modFile in modFiles:
            self.creatShevlesBtn(modFile,NCGToolshevl)

def main():
    doit = NCGTool()
    doit.creatShevlesFn()

if __name__ == '__main__':
    main()