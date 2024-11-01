import maya.cmds as mc
import maya.cmds as cmds
import PhoomToolsClasses as PT
import importlib

from functools import partial

'''import PhoomToolsUIDef
reload(PhoomToolsUIDef)
PhoomToolsUIDef.PhoomToolsUI().PT_UI()'''

importlib.reload(PT)
PTC=PT.PhoomCreation()

class PhoomToolsUI():
        def PhoomUI(self):
            windowExpandID = 'ExpandUi'

            windowWidth = 300
            windowHeight = 436
            cX = (windowWidth-15)/30
            cY = 32/cX

            if mc.window(windowExpandID,q = True,exists = True):
                mc.deleteUI(windowExpandID)

            windowsExpand = mc.window(windowExpandID,title = 'Phoom_Tools v.2',bgc = [(0.27),(0.27),(0.27)],width = windowWidth, height=windowHeight,rtf = True, sizeable=True)
            mc.showWindow (windowsExpand)

            MainLayout=cmds.rowColumnLayout( columnWidth=[(1, 300)])#label='CreationTools', labelWidth = 280,w=280,collapsable=True,collapse=True,p=Test2,bgc= [(0.5),(0.5),(1)])
            cmds.rowColumnLayout( p=MainLayout)
            cmds.text( label='Phoom Tools v.2',fn='obliqueLabelFont' )



            #CreationToolsTab
            conCreationLayout= cmds.formLayout(nd=100)
            conCreationColumn=cmds.columnLayout(p=conCreationLayout)



            #EditToolsTab
            conEditLayout= cmds.formLayout(nd=100)
            conEditColum=cmds.columnLayout(p=conEditLayout)

            conCreateFrameLayout= cmds.frameLayout(l='CreationTools', bgc= [(0.5),(0.5),(1)], cll=True, w=windowWidth, p=conCreationColumn,collapsable=True)
            conCreateFormLayout=cmds.formLayout(nd=100, p=conCreateFrameLayout)
            conCreateRowColumn = cmds.rowColumnLayout(p=conCreateFormLayout, bgc=[0.2, 0.2, 0.2])
            


            #importTab
            ImportTab=cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'left', 0), columnWidth=[(1, 2), (2, windowWidth-8)], p=conCreateRowColumn)
            mc.text ('')
            ImportLayoutTab=cmds.frameLayout( label='Import',collapsable=True,collapse=True,p=ImportTab,bgc= [(0.5),(0.5),(0.5)])
            ImportLayout=cmds.scrollLayout(h=150,w=200,p=ImportLayoutTab)



            #armTab
            ArmTab=cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'left', 0), columnWidth=[(1, 2), (2, windowWidth-8)], p=conCreateRowColumn)
            mc.text ('')
            ArmLayoutTab=cmds.frameLayout( label='FK/IK Arm',collapsable=True,collapse=True,p=ArmTab,bgc= [(0.5),(0.5),(0.5)])
            ArmLayout=cmds.scrollLayout(h=365,w=200,p=ArmLayoutTab)



            #legTab
            LegTab=cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'left', 0), columnWidth=[(1, 2), (2, windowWidth-8)], p=conCreateRowColumn)
            mc.text ('')
            LegLayoutTab=cmds.frameLayout( label='FK/IK Leg',collapsable=True,collapse=True,p=LegTab,bgc= [(0.5),(0.5),(0.5)])
            LegLayout=cmds.scrollLayout(h=400,w=200,p=LegLayoutTab)



            #ribbonTab
            RibbonTab=cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'left', 0), columnWidth=[(1, 2), (2, windowWidth-8)], p=conCreateRowColumn)
            mc.text ('')
            RibbonLayoutTab=cmds.frameLayout( label='Spine',collapsable=True,collapse=True,p=RibbonTab,bgc= [(0.5),(0.5),(0.5)])
            RibbonLayout=cmds.scrollLayout(h=400,w=200,p=RibbonLayoutTab)

            #CreationToolsTabEND####################

            #EditToolsTab

            conCreateFrameLayout1= cmds.frameLayout(l='EditTools', bgc= [(0.5),(0.5),(1)], cll=True, w=windowWidth, p=conEditColum,collapsable=True)
            conCreateFormLayout1=cmds.formLayout(nd=100, p=conCreateFrameLayout1)
            conCreateRowColumn1 = cmds.rowColumnLayout(p=conCreateFormLayout1, bgc=[0.2, 0.2, 0.2])



            #printNameTab
            PrintNameTab=cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'left', 0), columnWidth=[(1, 2), (2, windowWidth-8)], p=conCreateRowColumn1)
            mc.text ('')
            PrintNameLayoutFrame=cmds.frameLayout( label='Print Name',collapsable=True,collapse=True,p=PrintNameTab,bgc= [(0.5),(0.5),(0.5)])
            PrintNameLayoutTab=cmds.scrollLayout(h=50,w=200,p=PrintNameLayoutFrame)



            #HideAttrTab
            HideAttrTab=cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'left', 0), columnWidth=[(1, 2), (2, windowWidth-8)], p=conCreateRowColumn1)
            mc.text ('')
            HideAttrLayoutFrame=cmds.frameLayout( label='Hide Attribute',collapsable=True,collapse=True,p=HideAttrTab,bgc= [(0.5),(0.5),(0.5)])
            HideAttrLayoutTab=cmds.scrollLayout(h=180,w=200,p=HideAttrLayoutFrame)

            


            space=11
            ###########################################################

            #printname
            cmds.rowColumnLayout( numberOfColumns=6, columnAttach=(1, 'left', 0), columnWidth=[(1,space),(2,255)], p=PrintNameLayoutTab)
            cmds.text(l='')#Space
            cmds.text( label='Select the object and print in a blanket',fn='boldLabelFont' )

            mc.rowColumnLayout(nc = 2,columnWidth = [(1,space),(2, 250)],p=PrintNameLayoutTab) #PressButton
            cmds.text(l='')#Space
            mc.button(l = 'Print', vis = True, command =self.SentPrintName, bgc = [(0.00),(101.00),(109.00)],w=200)











            #HideAttr
            cmds.rowColumnLayout( numberOfColumns=6, columnAttach=(1, 'left', 0), columnWidth=[(1,space),(2,255)], p=HideAttrLayoutTab)
            cmds.text(l='')
            cmds.text( label='Hide Select Attribuite',fn='boldLabelFont' )
            
            cmds.rowColumnLayout( numberOfColumns=6, columnAttach=(1, 'left', 0), columnWidth=[(1,space),(2,255)], p=HideAttrLayoutTab)
            cmds.text(l='')#Space

            mc.rowColumnLayout(nc = 6, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 55),(3, 25), (4, 50),(5, 50),(6,50)],p=HideAttrLayoutTab)
            cmds.text(l='')
            cmds.text(l='Translate')
            cmds.text(l='')
            self.HideAttrTXRadio=mc.checkBox('HideAttrTXRadio',l="X",v=True)
            self.HideAttrTYRadio=mc.checkBox('HideAttrTYRadio',l="Y",v=True)
            self.HideAttrTZRadio=mc.checkBox('HideAttrTZRadio',l="Z",v=True)

            mc.rowColumnLayout(nc = 6, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 55),(3, 25), (4, 50),(5, 50),(6,50)],p=HideAttrLayoutTab)
            cmds.text(l='')
            cmds.text(l='Rotate')
            cmds.text(l='')
            self.HideAttrRXRadio=mc.checkBox('HideAttrRXRadio',l="X",v=True)
            self.HideAttrRYRadio=mc.checkBox('HideAttrRYRadio',l="Y",v=True)
            self.HideAttrRZRadio=mc.checkBox('HideAttrRZRadio',l="Z",v=True)

            mc.rowColumnLayout(nc = 6, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 55),(3, 25), (4, 50),(5, 50),(6,50)],p=HideAttrLayoutTab)
            cmds.text(l='')
            cmds.text(l='Scale')
            cmds.text(l='')
            self.HideAttrSXRadio=mc.checkBox('HideAttrSXRadio',l="X",v=True)
            self.HideAttrSYRadio=mc.checkBox('HideAttrSYRadio',l="Y",v=True)
            self.HideAttrSZRadio=mc.checkBox('HideAttrSZRadio',l="Z",v=True)

            mc.rowColumnLayout(nc = 6, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 55),(3, 25), (4, 50),(5, 50),(6,50)],p=HideAttrLayoutTab)
            cmds.text(l='')
            cmds.text(l='Visibility')
            cmds.text(l='')
            self.HideAttrVisRadio=mc.checkBox('HideAttrVisRadio',l="",v=True)

            cmds.rowColumnLayout( numberOfColumns=6, columnAttach=(1, 'left', 0), columnWidth=[(1,space),(2,255)], p=HideAttrLayoutTab)
            cmds.text(l='')#Space

            mc.rowColumnLayout(nc = 2,columnWidth = [(1,space),(2, 250)],p=HideAttrLayoutTab) #PressButton
            cmds.text(l='')#Space
            mc.button(l = 'Lock n Hide', vis = True, command =self.SendHideAttr, bgc = [(0.00),(101.00),(109.00)],w=200)

            mc.rowColumnLayout(nc = 2,columnWidth = [(1,space),(2, 250)],p=HideAttrLayoutTab) #PressButton
            cmds.text(l='')#Space
            mc.button(l = 'Bring it Back', vis = True, command =self.SendBringBackAttr, bgc = [(0.00),(101.00),(109.00)],w=200)











            #ImportOBJ
            mc.rowColumnLayout(nc = 2,columnWidth = [(1,space),(2, 250)],p=ImportLayout) #PressButton
            cmds.text(l='')#Space
            mc.button(l = 'NewScene', vis = True, command =self.SentNewScene, bgc = [(0.00),(101.00),(109.00)],w=200)

            cmds.rowColumnLayout( numberOfColumns=6, columnAttach=(1, 'left', 0), columnWidth=[(1,space),(2,255)], p=ImportLayout)
            cmds.text(l='')#Space

            cmds.rowColumnLayout( numberOfColumns=6, columnAttach=(1, 'left', 0), columnWidth=[(1,space-10),(2,40),(3,5),(4,180),(5,5),(6,25)], p=ImportLayout)#(1,40),(2,5),(3,180),(4,5),(5,25)
            cmds.text(l='')#Space
            cmds.text( label='Model:',fn='boldLabelFont' )
            cmds.text(l='')#Space
            self.OBJDirectInput = cmds.textField('OBJDirectInput',insertText='dicrectory',fn='obliqueLabelFont')
            cmds.text(l='')#Spaces
            mc.button(l = '<', vis = True, c = self.SentImportModel, bgc = [(0.9),(0.4),(0.1)],w=20)

            cmds.rowColumnLayout( numberOfColumns=6, columnAttach=(1, 'left', 0), columnWidth=[(1,space-10),(2,40),(3,5),(4,180),(5,5),(6,25)], p=ImportLayout)#(1,40),(2,5),(3,180),(4,5),(5,25)
            cmds.text(l='')#Space
            cmds.text( label='Joints:',fn='boldLabelFont' )
            cmds.text(l='')#Space
            self.JNTDirectInput = cmds.textField('JNTDirectInput',insertText='dicrectory',fn='obliqueLabelFont')
            cmds.text(l='')#Spaces
            mc.button(l = '<', vis = True, c = self.SentImportJoint, bgc = [(0.9),(0.4),(0.1)],w=20)
            
            cmds.rowColumnLayout( numberOfColumns=6, columnAttach=(1, 'left', 0), columnWidth=[(1,space-10),(2,40),(3,5),(4,180),(5,5),(6,25)], p=ImportLayout)#(1,40),(2,5),(3,180),(4,5),(5,25)
            cmds.text(l='')#Space
            cmds.text( label='SW:',fn='boldLabelFont' )
            cmds.text(l='')#Space
            self.WEIGHTDirectInput = cmds.textField('WEIGHTDirectInput',insertText='dicrectory',fn='obliqueLabelFont')
            cmds.text(l='')#Spaces
            mc.button(l = '<', vis = True, c = self.SentImportWeight, bgc = [(0.9),(0.4),(0.1)],w=20)
























            ##FKIKARM##############################################
            space=15
            #Name
            cmds.rowColumnLayout( numberOfColumns=6, columnAttach=(1, 'left', 0), columnWidth=[(1,space-10),(2,40),(3,5),(4,180),(5,5),(6,25)], p=ArmLayout)#(1,40),(2,5),(3,180),(4,5),(5,25)
            cmds.text(l='')#Space
            cmds.text( label='Name:',fn='boldLabelFont' )
            cmds.text(l='')#Space
            self.NameArmInput = cmds.textField('NameArmInput',insertText='Insert_Name',fn='obliqueLabelFont')
            cmds.text(l='')#Spaces
            mc.button(l = '<', vis = True, c = self.SelectOBjArm, bgc = [(0.9),(0.4),(0.1)],w=20)

            #L R
            mc.rowColumnLayout(nc = 4, columnAttach=(1, 'both', 1), columnWidth = [(1,space),(2, 50), (3, 100),(4, 100)],p=ArmLayout) #Tick
            self.LeftRightArmRadio = mc.radioCollection()
            cmds.text(l='')#Space
            mc.text ('LR:',fn='boldLabelFont')
            mc.radioButton("Left", sl = True)
            mc.radioButton("Right")

            #Column
            cmds.rowColumnLayout( numberOfColumns=1, columnAttach=(1, 'left', 0), columnWidth=[(1, 250)], p=ArmLayout)
            cmds.text( label='' )

            #Aim
            mc.rowColumnLayout(nc = 6, columnAttach=(1, 'both', 1), columnWidth = [(1,space),(2, 50),(3, 50), (4, 50),(5, 50),(6,50)],p=ArmLayout) #Tick
            self.XYZArmRadio = mc.radioCollection()
            cmds.text(l='')#Space
            mc.text ('AimJnt')
            mc.radioButton("X", sl = True)
            mc.radioButton("Y")
            mc.radioButton("Z")
            self.RevXYZArm=mc.checkBox("RevXYZArm",l='Rev')

            #Upjnt
            mc.rowColumnLayout(nc = 6, columnAttach=(1, 'both', 1), columnWidth = [(1,space),(2, 50),(3, 50), (4, 50),(5, 50),(6,50)],p=ArmLayout) #Tick
            self.UpJntArmRadio = mc.radioCollection()
            cmds.text(l='')#Space
            mc.text ('UpJnt')
            mc.radioButton("X")
            mc.radioButton("Y", sl = True)
            mc.radioButton("Z")
            self.RevUpJntArm=mc.checkBox("RevUpJntArm",l='Rev')

            #WorldUpjnt
            mc.rowColumnLayout(nc = 6, columnAttach=(1, 'both', 1), columnWidth = [(1,space),(2, 50),(3, 50), (4, 50),(5, 50),(6,50)],p=ArmLayout) #Tick
            self.WorldUpArmJntRadio = mc.radioCollection()
            cmds.text(l='')#Space
            mc.text ('WorldUp')
            mc.radioButton("X")
            mc.radioButton("Y", sl = True)
            mc.radioButton("Z")
            self.RevWorldUpArm=mc.checkBox("RevWorldUpArm",l='Rev')

            #Column
            cmds.rowColumnLayout( numberOfColumns=1, columnAttach=(1, 'left', 0), columnWidth=[(1, 250)], p=ArmLayout)
            cmds.text( label='' )

            #CreateSample
            mc.rowColumnLayout(nc = 2,columnWidth = [(1,space),(2, 250)],p=ArmLayout) #PressButton
            cmds.text(l='')#Space
            mc.button(l = 'Create Joint', vis = True, command =self.SendArmSample, bgc = [(0.00),(101.00),(109.00)],w=200)

            #Column
            cmds.rowColumnLayout( numberOfColumns=1, columnAttach=(1, 'left', 0), columnWidth=[(1, 250)], p=ArmLayout)
            cmds.text( label='' )

            #CtrlSize
            mc.rowColumnLayout(nc = 4, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 100),(3, 100),(4, 50)],p=ArmLayout)
            cmds.text(l='')#Space
            cmds.text( label='Controler Size:' )
            self.CtrlSizeArmInput = cmds.floatField(minValue=-10, maxValue=10,value =1)
            cmds.text( label='' )

            #Column
            cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'left', 0), columnWidth=[(1,space),(2, 250)], p=ArmLayout)
            cmds.text(l='')#Space
            cmds.text( label='---------------------------   FK  -----------------------------' ,fn='obliqueLabelFont')

            #InGrp
            #InGrpRadio = mc.radioCollection()
            mc.rowColumnLayout(nc = 2, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 200)],p=ArmLayout)
            cmds.text(l='')#Space
            InGrp = 1
            self.InGrpArmRadio=mc.checkBox('InGrpArmRadio',l="FK Joint will be in the Ctrl")

            #EndJnt

            mc.rowColumnLayout(nc = 2, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 200)],p=ArmLayout)
            cmds.text(l='')#Space
            #ParentLastRadio = mc.radioCollection()
            self.EndGrpArmRadio =mc.checkBox("EndGrpArmRadio",l="Parent FK last joint")

            #Column
            cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'left', 0), columnWidth=[(1,space),(2, 250)], p=ArmLayout)
            cmds.text(l='')#Space
            cmds.text( label='----------------------------  IK  ----------------------------',fn='obliqueLabelFont' )

            mc.rowColumnLayout(nc = 4, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 100),(3, 100),(4, 50)],p=ArmLayout)
            cmds.text(l='')#Space
            cmds.text( label='Distan Polevector:' )
            self.PoleVectorDisArmInput = cmds.floatField(minValue=-10, maxValue=10, value=-4)
            cmds.text( label='' )

            #Column
            cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'left', 0), columnWidth=[(1,space),(2, 250)], p=ArmLayout)
            cmds.text(l='')#Space
            cmds.text( label='---------------------   Auto Stretch   ---------------------' ,fn='obliqueLabelFont')

            #Enable
            mc.rowColumnLayout(nc = 2, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 250)],p=ArmLayout)
            cmds.text(l='')#Space
            self.AutoStrechArmRadio=mc.checkBox('AutoStrechArmRadio',l="Enable",v=True)

            mc.rowColumnLayout(nc = 4, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 100),(3, 100),(4, 50)],p=ArmLayout)
            cmds.text(l='')#Space
            cmds.text( label='Amp' )
            self.AmpArmInput = cmds.floatField(minValue=-10, maxValue=10, value=0.1)
            cmds.text( label='' )

            #Createlocator
            mc.rowColumnLayout(nc = 2,columnWidth = [(1,space),(2, 250)],p=ArmLayout) #PressButton
            cmds.text(l='')#Space
            mc.button(l = 'Create Locator for FK/IK Blend', vis = True, command =self.SendArmFKIKLocate, bgc = [(0.00),(101.00),(109.00)],w=200)
            #partial(SendFKIKLocate, CtrlSizeArmInput)

            #Button
            mc.rowColumnLayout(nc = 2,columnWidth = [(1,space),(2, 250)],p=ArmLayout) #PressButton
            cmds.text(l='')#Space
            ExpandBT = mc.button(l = 'O', vis = True, c = self.SendArmExecute, bgc = [(0.00),(191.191),(255.255)],w=200)




















            ##FKIKLEG##############################################
            #Name
            cmds.rowColumnLayout( numberOfColumns=6, columnAttach=(1, 'left', 0), columnWidth=[(1,space-10),(2,40),(3,5),(4,180),(5,5),(6,25)], p=LegLayout)#(1,40),(2,5),(3,180),(4,5),(5,25)
            cmds.text(l='')#Space
            cmds.text( label='Name:',fn='boldLabelFont' )
            cmds.text(l='')#Space
            self.NameLeg = cmds.textField('NameLegInput',insertText='Insert_Name',fn='obliqueLabelFont')
            mc.text ('')
            mc.button(l = '<', vis = True, c = self.SelectOBjLeg, bgc = [(0.9),(0.4),(0.1)],w=20)

            #L R
            mc.rowColumnLayout(nc = 4, columnAttach=(1, 'both', 1), columnWidth = [(1,space),(2, 50), (3, 100),(4, 100)],p=LegLayout) #Tick
            self.LeftRightLegRadio = mc.radioCollection()
            cmds.text(l='')#Space
            mc.text ('LR:',fn='boldLabelFont')
            mc.radioButton("Left", sl = True)
            mc.radioButton("Right")

            #Column
            cmds.rowColumnLayout( numberOfColumns=1, columnAttach=(1, 'left', 0), columnWidth=[(1, 250)], p=LegLayout)
            cmds.text( label='' )

            #Aim
            mc.rowColumnLayout(nc = 6, columnAttach=(1, 'both', 1), columnWidth = [(1,space),(2, 50),(3, 50), (4, 50),(5, 50),(6,50)],p=LegLayout) #Tick
            self.XYZLegRadio = mc.radioCollection()
            cmds.text(l='')#Space
            mc.text ('AimJnt')
            mc.radioButton("X", sl = True)
            mc.radioButton("Y")
            mc.radioButton("Z")
            self.RevXYZLeg=mc.checkBox("RevXYZLeg",l='Rev')

            #Upjnt
            mc.rowColumnLayout(nc = 6, columnAttach=(1, 'both', 1), columnWidth = [(1,space),(2, 50),(3, 50), (4, 50),(5, 50),(6,50)],p=LegLayout) #Tick
            self.UpJntLegRadio = mc.radioCollection()
            cmds.text(l='')#Space
            mc.text ('UpJnt')
            mc.radioButton("X")
            mc.radioButton("Y", sl = True)
            mc.radioButton("Z")
            self.RevUpJntLeg=mc.checkBox("RevUpJntLeg",l='Rev')

            #WorldUpjnt
            mc.rowColumnLayout(nc = 6, columnAttach=(1, 'both', 1), columnWidth = [(1,space),(2, 50),(3, 50), (4, 50),(5, 50),(6,50)],p=LegLayout) #Tick
            self.WorldUpLegJntRadio = mc.radioCollection()
            cmds.text(l='')#Space
            mc.text ('WorldUp')
            mc.radioButton("X")
            mc.radioButton("Y")
            mc.radioButton("Z", sl = True)
            self.RevWorldUpLeg = mc.checkBox("RevWorldUpLeg",l='Rev')

            #Column
            cmds.rowColumnLayout( numberOfColumns=1, columnAttach=(1, 'left', 0), columnWidth=[(1, 250)], p=LegLayout)
            cmds.text( label='' )
            
            #CreateSample
            mc.rowColumnLayout(nc = 2,columnWidth = [(1,space),(2, 250)],p=LegLayout) #PressButton
            cmds.text(l='')#Space
            mc.button(l = 'Create Joint', vis = True, command =self.SendLegSample, bgc = [(1),(1),(0)],w=200)

            #Column
            cmds.rowColumnLayout( numberOfColumns=1, columnAttach=(1, 'left', 0), columnWidth=[(1, 250)], p=LegLayout)
            cmds.text( label='' )
           
            #CtrlSize
            mc.rowColumnLayout(nc = 4, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 100),(3, 100),(4, 50)],p=LegLayout)
            cmds.text(l='')#Space
            cmds.text( label='Controler Size:' )
            self.CtrlSizeLegInput = cmds.floatField(minValue=-10, maxValue=10,v=1)
            cmds.text( label='' )

            #Column
            cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'left', 0), columnWidth=[(1,space),(2, 250)], p=LegLayout)
            cmds.text(l='')#Space
            cmds.text( label='---------------------------   FK  -----------------------------' ,fn='obliqueLabelFont')

            #InGrp
            #InGrpRadio = mc.radioCollection()
            mc.rowColumnLayout(nc = 2, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 200)],p=LegLayout)
            InGrp = 1
            cmds.text(l='')#Space
            self.InGrpLegRadio=mc.checkBox('InGrpLegRadio',l="FK Joint will be in the Ctrl")


            #Column
            cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'left', 0), columnWidth=[(1,space),(2, 250)], p=LegLayout)
            cmds.text(l='')#Space
            cmds.text( label='----------------------------  IK  ----------------------------',fn='obliqueLabelFont' )

            mc.rowColumnLayout(nc = 4, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 100),(3, 100),(4, 50)],p=LegLayout)
            cmds.text(l='')#Space
            cmds.text( label='Distan Polevector:' )
            self.PoleVectorDisLegInput = cmds.floatField(minValue=-10, maxValue=10, value=4)
            cmds.text( label='' )

            mc.rowColumnLayout(nc = 4, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 100),(3, 100),(4, 50)],p=LegLayout)
            cmds.text(l='')#Space
            cmds.text( label='RollToeAmp:' )
            self.RollToeAmpInput = cmds.floatField(value=30)
            cmds.text( label='' )

            mc.rowColumnLayout(nc = 4, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 100),(3, 100),(4, 50)],p=LegLayout)
            cmds.text(l='')#Space
            cmds.text( label='RollAnkleAmp:' )
            self.RollAnkleAmpInput = cmds.floatField(value=30)
            cmds.text( label='' )

            mc.rowColumnLayout(nc = 4, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 100),(3, 100),(4, 50)],p=LegLayout)
            cmds.text(l='')#Space
            cmds.text( label='RollHeelAmp:' )
            self.RollHeelAmpInput = cmds.floatField(value=30)
            cmds.text( label='' )

            #Column
            cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'left', 0), columnWidth=[(1,space),(2, 250)], p=LegLayout)
            cmds.text(l='')#Space
            cmds.text( label='---------------------   Auto Stretch   ---------------------' ,fn='obliqueLabelFont')

            #Enable
            mc.rowColumnLayout(nc = 2, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 250)],p=LegLayout)
            cmds.text(l='')#Space
            self.AutoStrechLegRadio=mc.checkBox('AutoStrechLegRadio',l="Enable",v=True)

            mc.rowColumnLayout(nc = 4, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 100),(3, 100),(4, 50)],p=LegLayout)
            cmds.text(l='')#Space
            cmds.text( label='Amp' )
            self.AmpLegInput = cmds.floatField(minValue=-10, maxValue=10, value=0.1)
            cmds.text( label='' )

            #Button
            mc.rowColumnLayout(nc = 2,columnWidth = [(1,space),(2, 250)],p=LegLayout) #PressButton
            cmds.text(l='')#Space
            ExpandBT = mc.button(l = 'Create locator for foot ctrl', vis = True, c = self.SendLocatorLeg, bgc = [(1),(1),(0)],w=200)

            #Button
            mc.rowColumnLayout(nc = 2,columnWidth = [(1,space),(2, 250)],p=LegLayout)  #PressButton
            cmds.text(l='')#Space
            ExpandBT = mc.button(l = 'FK/IK Switch locator', vis = True, c = self.SendLocatorFKIKLeg, bgc = [(1),(1),(0)],w=200)

            #Button
            mc.rowColumnLayout(nc = 2,columnWidth = [(1,space),(2, 250)],p=LegLayout)  #PressButton
            cmds.text(l='')#Space
            ExpandBT = mc.button(l = 'O', vis = True, c = self.SendexecuteLeg, bgc = [(1),(1),(0)],w=200)



















            ##Spine##############################################
            #Name
            cmds.rowColumnLayout( numberOfColumns=6, columnAttach=(1, 'left', 0), columnWidth=[(1,space-10),(2,40),(3,5),(4,180),(5,5),(6,25)], p=RibbonLayout)#(1,40),(2,5),(3,180),(4,5),(5,25)
            cmds.text(l='')#Space
            cmds.text( label='Name:',fn='boldLabelFont' )
            cmds.text(l='')#Space
            self.NameSpine = cmds.textField('NameSpineInput',insertText='Insert_Name',fn='obliqueLabelFont')
            mc.text ('')
            mc.button(l = '<', vis = True, c = self.SelectOBjSpine, bgc = [(0.9),(0.4),(0.1)],w=20)

            #Column
            cmds.rowColumnLayout( numberOfColumns=1, columnAttach=(1, 'left', 0), columnWidth=[(1, 250)], p=RibbonLayout)
            cmds.text( label='' )

            #JointNum
            mc.rowColumnLayout(nc = 4, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 100),(3, 100),(4, 50)],p=RibbonLayout)
            cmds.text(l='')#Space
            cmds.text( label='JointCount:' )
            self.SpineJointNum = cmds.floatField(minValue=0, maxValue=6,v=6)
            cmds.text( label='' )

            #Column
            cmds.rowColumnLayout( numberOfColumns=1, columnAttach=(1, 'left', 0), columnWidth=[(1, 250)], p=RibbonLayout)
            cmds.text( label='' )

            #Aim
            mc.rowColumnLayout(nc = 6, columnAttach=(1, 'both', 1), columnWidth = [(1,space),(2, 50),(3, 50), (4, 50),(5, 50),(6,50)],p=RibbonLayout) #Tick
            self.XYZSpineRadio = mc.radioCollection()
            cmds.text(l='')#Space
            mc.text ('AimJnt')
            mc.radioButton("X", sl = True)
            mc.radioButton("Y")
            mc.radioButton("Z")
            self.RevXYZSpine=mc.checkBox("RevXYZSpine",l='Rev')

            #Upjnt
            mc.rowColumnLayout(nc = 6, columnAttach=(1, 'both', 1), columnWidth = [(1,space),(2, 50),(3, 50), (4, 50),(5, 50),(6,50)],p=RibbonLayout) #Tick
            self.UpJntSpineRadio = mc.radioCollection()
            cmds.text(l='')#Space
            mc.text ('UpJnt')
            mc.radioButton("X")
            mc.radioButton("Y", sl = True)
            mc.radioButton("Z")
            self.RevUpJntSpine=mc.checkBox("RevUpJntSpine",l='Rev')

            #WorldUpjnt
            mc.rowColumnLayout(nc = 6, columnAttach=(1, 'both', 1), columnWidth = [(1,space),(2, 50),(3, 50), (4, 50),(5, 50),(6,50)],p=RibbonLayout) #Tick
            self.WorldUpSpineJntRadio = mc.radioCollection()
            cmds.text(l='')#Space
            mc.text ('WorldUp')
            mc.radioButton("X")
            mc.radioButton("Y")
            mc.radioButton("Z", sl = True)
            self.RevWorldUpSpine = mc.checkBox("RevWorldUpSpine",l='Rev')

            #Column
            cmds.rowColumnLayout( numberOfColumns=1, columnAttach=(1, 'left', 0), columnWidth=[(1, 250)], p=RibbonLayout)
            cmds.text( label='' )
            
            #CreateSample
            mc.rowColumnLayout(nc = 2,columnWidth = [(1,space),(2, 250)],p=RibbonLayout) #PressButton
            cmds.text(l='')#Space
            mc.button(l = 'Create Joint', vis = True, command =self.SendSpineSample, bgc = [(1),(1),(0)],w=200)

            #Column
            cmds.rowColumnLayout( numberOfColumns=1, columnAttach=(1, 'left', 0), columnWidth=[(1, 250)], p=RibbonLayout)
            cmds.text( label='' )
           
            #CtrlSize
            mc.rowColumnLayout(nc = 4, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 100),(3, 100),(4, 50)],p=RibbonLayout)
            cmds.text(l='')#Space
            cmds.text( label='Controler Size:' )
            self.CtrlSizeSpineInput = cmds.floatField(minValue=-10, maxValue=10,v=1)
            cmds.text( label='' )

            #Column
            cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'left', 0), columnWidth=[(1,space),(2, 250)], p=RibbonLayout)
            cmds.text(l='')#Space
            cmds.text( label='---------------------------   FK  -----------------------------' ,fn='obliqueLabelFont')

            #FK
            #InGrpRadio = mc.radioCollection()
            mc.rowColumnLayout(nc = 2, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 200)],p=RibbonLayout)
            InGrp = 1
            cmds.text(l='')#Space
            self.FKSpineRadio=mc.checkBox('FKSpineRadio',l="FK_Enable",v=True)

            #Twist
            #InGrpRadio = mc.radioCollection()
            mc.rowColumnLayout(nc = 2, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 200)],p=RibbonLayout)
            InGrp = 1
            cmds.text(l='')#Space
            self.TwistSpineRadio=mc.checkBox('TwistSpineRadio',l="Twist")

            #Column
            cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'left', 0), columnWidth=[(1,space),(2, 250)], p=RibbonLayout)
            cmds.text(l='')#Space
            cmds.text( label='---------------------------   IK  -----------------------------' ,fn='obliqueLabelFont')

            #IK
            #InGrpRadio = mc.radioCollection()
            mc.rowColumnLayout(nc = 2, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 200)],p=RibbonLayout)
            InGrp = 1
            cmds.text(l='')#Space
            self.FKSpineRadio=mc.checkBox('IKSpineRadio',l="IK_Enable",v=True)

            #Column
            cmds.rowColumnLayout( numberOfColumns=1, columnAttach=(1, 'left', 0), columnWidth=[(1, 250)], p=RibbonLayout)
            cmds.text( label='' )
            
            #Column
            cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'left', 0), columnWidth=[(1,space),(2, 250)], p=RibbonLayout)
            cmds.text(l='')#Space
            cmds.text( label='---------------------------   Dynamic   -----------------------------' ,fn='obliqueLabelFont')
            
            #Dynamic
            mc.rowColumnLayout(nc = 5, columnAttach=(1, 'left', 1), columnWidth = [(1,space),(2, 50),(3, 50), (4, 75),(5, 75)],p=RibbonLayout) #Tick
            self.DynamicSpine = mc.radioCollection()
            cmds.text(l='')#Space
            mc.text ('Dynamic')
            mc.radioButton("Off",sl=True)
            mc.radioButton("LockStart")
            mc.radioButton("LockBoth")







        def SentNewScene(self,*args):
            PTC.NewScene()

        def SentImportWeight(self,*args):
            data=mc.textField(self.WEIGHTDirectInput, q = True, tx = True)
            PTC.ImportWeight(Direct=data)

        def SentImportJoint(self,*args):
            data=mc.textField(self.JNTDirectInput, q = True, tx = True)
            PTC.ImportJoint(Direct=data)
            
        def SentImportModel(self,*args):
            data=mc.textField(self.OBJDirectInput, q = True, tx = True)
            PTC.ImportModel(Direct=data)

        def SendBringBackAttr(self,*args):
            selected = cmds.ls(sl=True) or []
            for eachSel in selected:
             print(str(eachSel))
             SACtrlName=str(eachSel)
            PTC.BringBackAttr(CtrlName=SACtrlName)

        def SelectOBjArm (self,*args):
            selection = mc.ls(sl = True)[0]
            mc.textField(self.NameArmInput,e = True, tx=selection)

        def SentPrintName(self,*args):
            PTC.PrintName()

        def SendHideAttr(self,*args):
            selected = cmds.ls(sl=True) or []
            for eachSel in selected:
             print(str(eachSel))
             SACtrlName=str(eachSel)
            print (SACtrlName)
            SATX=mc.checkBox(self.HideAttrTXRadio, query=True, value = True)
            SATY=mc.checkBox(self.HideAttrTYRadio, query=True, value = True)
            SATZ=mc.checkBox(self.HideAttrTZRadio, query=True, value = True)
            SARX=mc.checkBox(self.HideAttrRXRadio, query=True, value = True)
            SARY=mc.checkBox(self.HideAttrRYRadio, query=True, value = True)
            SARZ=mc.checkBox(self.HideAttrRYRadio, query=True, value = True)
            SASX=mc.checkBox(self.HideAttrSXRadio, query=True, value = True)
            SASY=mc.checkBox(self.HideAttrSYRadio, query=True, value = True)
            SASZ=mc.checkBox(self.HideAttrSZRadio, query=True, value = True)
            SAV=mc.checkBox(self.HideAttrVisRadio, query=True, value = True)
            PTC.LockHideAttr(CtrlName=str(SACtrlName)
                             ,TX=SATX
                             ,TY=SATY
                             ,TZ=SATZ
                             ,RX=SARX
                             ,RY=SARY
                             ,RZ=SARZ
                             ,SX=SASX
                             ,SY=SASY
                             ,SZ=SASZ
                             ,T=False
                             ,R=False
                             ,S=False
                             ,Vis=SAV
                             )




        def SendArmFKIKLocate(self,*args):
            CtrlSizeArmInput = float(mc.floatField(self.CtrlSizeArmInput, q = True, v = True))
            PTC.FKIKLocate(CtrlSizeArmInput) 

        def SendArmExecuteTest(self,*args):
            SAName=mc.textField(self.NameArmInput, q = True, tx = True)
            SALRInput= mc.radioCollection(self.LeftRightArmRadio, q = True, sl = True)
            SAXYZInput= mc.radioCollection(self.XYZArmRadio, q = True, sl = True)
            SAAimCheck=mc.checkBox(self.RevXYZArm, query=True, value = True)
            SAUpJntInput = mc.radioCollection(self.UpJntArmRadio, q = True, sl = True)
            SAUpCheck=mc.checkBox(self.RevUpJntArm, query=True, value = True)
            SAWorldUpJntInput = mc.radioCollection(self.WorldUpArmJntRadio, q = True, sl = True)
            SAWorldCheck=mc.checkBox(self.RevWorldUpArm, query=True, value = True)
            SACtrlSizeArmInput=mc.floatField(self.CtrlSizeArmInput, q = True, v = True)
            SAInGrpCheck =mc.checkBox(self.InGrpArmRadio, query=True, value = True)
            SAEndjntCheck=mc.checkBox(self.EndGrpArmRadio, query=True, value = True)
            SAAutoCheck=mc.checkBox(self.AutoStrechArmRadio, query=True, value = True)
            SAPoleVectorDis=mc.floatField(self.PoleVectorDisArmInput, q = True, v = True)
            SAfloatStretchAmp=mc.floatField(self.AmpArmInput, q = True, v = True)
            
            return[SAName,SALRInput,SAXYZInput,SAAimCheck,SAUpJntInput,SAUpCheck,SAWorldUpJntInput,SAWorldCheck,SACtrlSizeArmInput,SAInGrpCheck,SAEndjntCheck,SAAutoCheck,SAPoleVectorDis,SAfloatStretchAmp]

        def SendArmSample(self,*args):
            SAName=mc.textField(self.NameArmInput, q = True, tx = True)
            SALRInput= mc.radioCollection(self.LeftRightArmRadio, q = True, sl = True)
            SAXYZInput= mc.radioCollection(self.XYZArmRadio, q = True, sl = True)
            SAAimCheck=mc.checkBox(self.RevXYZArm, query=True, value = True)
            SAUpJntInput = mc.radioCollection(self.UpJntArmRadio, q = True, sl = True)
            SAUpCheck=mc.checkBox(self.RevUpJntArm, query=True, value = True)
            SAWorldUpJntInput = mc.radioCollection(self.WorldUpArmJntRadio, q = True, sl = True)
            SAWorldCheck=mc.checkBox(self.RevWorldUpArm, query=True, value = True)
            SACtrlSizeArmInput=mc.floatField(self.CtrlSizeArmInput, q = True, v = True)
            PTC.ArmSample(Name=SAName
                          ,LRInput=SALRInput
                          ,XYZInput=SAXYZInput
                          ,AimCheck=SAAimCheck
                          ,UpJntInput=SAUpJntInput
                          ,UpCheck=SAUpCheck
                          ,WorldUpJntInput=SAWorldUpJntInput
                          ,WorldCheck=SAWorldCheck
                          ,CtrlSizeArmInput=SACtrlSizeArmInput
                          )

        def SendArmExecute(self,*args):
            data=self.SendArmExecuteTest(self,*args)
            PTC.executeArm (Name=data[0]
                            ,LRInput=data[1]
                            ,XYZInput=data[2]
                            ,AimCheck=data[3]
                            ,UpJntInput = data[4]
                            ,UpCheck=data[5]
                            ,WorldUpJntInput =data[6]
                            ,WorldCheck=data[7]
                            ,CtrlSizeArmInput=data[8]
                            ,InGrpCheck =data[9]
                            ,EndjntCheck=data[10]
                            ,AutoCheck=data[11]
                            ,PoleVectorDis=data[12]
                            ,floatStretchAmp=data[13]
                            )
            




        def SelectOBjLeg (self,*args):
            selection = mc.ls(sl = True)[0]
            mc.textField('NameLegInput',e = True, tx=selection)

        def SendLocatorLeg(self,*args):
            CtrlSizeLegInput = float(mc.floatField(self.CtrlSizeLegInput, q = True, v = True))
            PTC.LocatorLeg(CtrlSizeLegInput) 

        def SendLocatorFKIKLeg(self,*args):
            CtrlSizeLegInput = float(mc.floatField(self.CtrlSizeLegInput, q = True, v = True))
            PTC.LocatorFKIKLeg( CtrlSizeLegInput)

        def SendLegSample(self,*args):
            SAName=mc.textField(self.NameLeg, q = True, tx = True)
            SALRInput= mc.radioCollection(self.LeftRightLegRadio, q = True, sl = True)
            SAXYZInput= mc.radioCollection(self.XYZLegRadio, q = True, sl = True)
            SAAimCheck=mc.checkBox(self.RevXYZLeg, query=True, value = True)
            SAUpJntInput = mc.radioCollection(self.UpJntLegRadio, q = True, sl = True)
            SAUpCheck=mc.checkBox(self.RevUpJntLeg, query=True, value = True)
            SAWorldUpJntInput = mc.radioCollection(self.WorldUpLegJntRadio, q = True, sl = True)
            SAWorldCheck=mc.checkBox(self.RevWorldUpLeg, query=True, value = True)
            SACtrlSizeLegInput = float(mc.floatField(self.CtrlSizeLegInput, q = True, v = True))
            PTC.LegSample(Name=SAName
                          ,LRInput=SALRInput
                          ,XYZInput=SAXYZInput
                          ,AimCheck=SAAimCheck
                          ,UpJntInput=SAUpJntInput
                          ,UpCheck=SAUpCheck
                          ,WorldUpJntInput=SAWorldUpJntInput
                          ,WorldCheck=SAWorldCheck
                          ,CtrlSizeLegInput=SACtrlSizeLegInput
                          )

        def SendLegExecuteTest(self,*args):
            SLName=mc.textField(self.NameLeg, q = True, tx = True)
            SLLRInput= mc.radioCollection(self.LeftRightLegRadio, q = True, sl = True)
            SLXYZInput= mc.radioCollection(self.XYZLegRadio, q = True, sl = True)
            SLAimCheck=mc.checkBox(self.RevXYZLeg, query=True, value = True)
            SLUpJntInput= mc.radioCollection(self.UpJntLegRadio, q = True, sl = True)
            SLUpCheck=mc.checkBox(self.RevUpJntLeg, query=True, value = True)
            SLWorldUpJntInput= mc.radioCollection(self.WorldUpLegJntRadio, q = True, sl = True)
            SLWorldCheck=mc.checkBox(self.RevWorldUpLeg, query=True, value = True)
            SLCtrlSizeLegInput=mc.floatField(self.CtrlSizeLegInput, q = True, v = True)
            SLInGrpCheck=mc.checkBox(self.InGrpLegRadio, query=True, value = True)
            SLPoleVectorDis=mc.floatField(self.PoleVectorDisLegInput, q = True, v = True) 
            SLRollToeAmp=mc.floatField(self.RollToeAmpInput, q = True, v = True)
            SLRollAnkleAmp =mc.floatField(self.RollAnkleAmpInput, q = True, v = True)
            SLRollHeelAmp =mc.floatField(self.RollHeelAmpInput, q = True, v = True)
            SLAutoCheck=mc.checkBox(self.AutoStrechLegRadio, query=True, value = True)
            SLfloatStretchAmp=cmds.floatField(self.AmpLegInput, query=True, value = True)

            return[SLName,SLLRInput,SLXYZInput,SLAimCheck,SLUpJntInput,SLUpCheck,SLWorldUpJntInput,SLWorldCheck,SLCtrlSizeLegInput,SLInGrpCheck,SLPoleVectorDis,SLRollToeAmp,SLRollAnkleAmp,SLRollHeelAmp,SLAutoCheck,SLfloatStretchAmp]

        def SendexecuteLeg(self,*args):
            data=self.SendLegExecuteTest(self,*args)
            PTC.executeLeg(Name=data[0]
                       ,LRInput=data[1]
                       ,XYZInput=data[2]
                       ,AimCheck=data[3]
                       ,UpJntInput=data[4]
                       ,UpCheck=data[5]
                       ,WorldUpJntInput=data[6]
                       ,WorldCheck=data[7]
                       ,CtrlSizeLegInput=data[8]
                       ,InGrpCheck=data[9]
                       ,PoleVectorDis=data[10]
                       ,RollToeAmp=data[11]
                       ,RollAnkleAmp=data[12]
                       ,RollHeelAmp=data[13]
                       ,AutoCheck=data[14]
                       ,floatStretchAmp=data[15]
                       )




        def SelectOBjSpine (self,*args):
            selection = mc.ls(sl = True)[0]
            mc.textField('NameSpineInput',e = True, tx=selection)

        def SendSpineSample(self,*args):
            SAName=mc.textField(self.NameSpine, q = True, tx = True)
            SASpineJointNum = float(mc.floatField(self.SpineJointNum, q = True, v = True))
            SAXYZInput= mc.radioCollection(self.XYZSpineRadio, q = True, sl = True)
            SAAimCheck=mc.checkBox(self.RevXYZSpine, query=True, value = True)
            SAUpJntInput = mc.radioCollection(self.UpJntSpineRadio, q = True, sl = True)
            SAUpCheck=mc.checkBox(self.RevUpJntSpine, query=True, value = True)
            SAWorldUpJntInput = mc.radioCollection(self.WorldUpSpineJntRadio, q = True, sl = True)
            SAWorldCheck=mc.checkBox(self.RevWorldUpSpine, query=True, value = True)
            SACtrlSizeSpineInput = float(mc.floatField(self.CtrlSizeSpineInput, q = True, v = True))
            PTC.SpineSample(Name=SAName
                          ,JointNum=SASpineJointNum
                          ,XYZInput=SAXYZInput
                          ,AimCheck=SAAimCheck
                          ,UpJntInput=SAUpJntInput
                          ,UpCheck=SAUpCheck
                          ,WorldUpJntInput=SAWorldUpJntInput
                          ,WorldCheck=SAWorldCheck
                          ,CtrlSizeLegInput=SACtrlSizeSpineInput
                          )