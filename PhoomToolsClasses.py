import maya.cmds as mc
from maya import cmds as mc
import maya.cmds as cmds
import PhoomToolsUIDef as PU
import importlib

importlib.reload(PU)
#PUC=PU.PhoomToolsUI()

class PhoomCreation():
    ####### Controller Code ##########
    
    Square=[(1,0,-1),(1,0,1),(-1,0,1),(-1,0,-1),(1,0,-1)]
    Cube=[(1,-1,-1),(1,-1,1),(-1,-1,1),(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(-1,1,-1),(-1,1,1),(-1,-1,1),(-1,1,1),(1,1,1),(1,-1,1),(1,1,1),(1,1,-1)]
    IkCube=[(0,-1,-1),(0,1,-1),(-1,1,-1),(-1,-1,-1),(0,-1,-1),(0,-1,1),(0,1,1),(0,1,-1),(-1,1,-1),(-1,1,1),(-1,-1,1),(-1,-1,-1),(-1,-1,1),(0,-1,1),(0,1,1),(-1,1,1)]
    Pyramid = [(1,0,-1),(1,0,1),(-1,0,1),(-1,0,-1),(1,0,-1),(0,2,0),(-1,0,1),(-1,0,-1),(0,2,0),(1,0,1)]
    PoleVec = [(0,0,0), (-1, 1, -2),(-1 ,-1, -2), (1 ,-1 ,-2),(1, 1 ,-2),(-1, 1,-2),(0 ,0 ,0),(1 ,1 ,-2),(1 ,-1 ,-2),(0, 0, 0),(-1, -1 ,-2)]
    Plus = [(0,0,2),(1,0,2),(1,0,1),(2,0,1),(2,0,-1),(1,0,-1),(1,0,-2),(-1,0,-2),(-1,0,-1),(-2,0,-1),(-2,0,1),(-1,0,1),(-1,0,2),(0,0,2)]
    IKFoot = [(1,-1,-1),(1,-1,2),(-1,-1,2),(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(-1,1,-1),(-1,0,2),(-1,-1,2),(1,-1,2),(1,0,2),(-1,0,2),(1,0,2),(1,1,-1)]
    ArrowH = [(-0,-0, 0.99),(-0.19, 0.18, 0.96),(-0.37,0.36,0.9),(-0.56, 0.52 ,0.8),(-0.37, 0.52, 0.8),(-0.19, 0.52, 0.8),(-0.19, 0.66, 0.68),(-0.19, 0.77, 0.53),(-0.19, 0.86, 0.36),(-0.19, 0.91, 0.19),(-0.19, 0.92, 0),(-0.19, 0.91, -0.19),(-0.19, 0.86, -0.36),(-0.19, 0.77, -0.53),(-0.19, 0.66, -0.68),(-0.19, 0.52, -0.8),(-0.37, 0.52, -0.8),(-0.56, 0.52, -0.8),(-0.37, 0.36, -0.9),(-0.19, 0.18, -0.96),(-0, -0 ,-0.99),(0.19, 0.18, -0.96),(0.37, 0.36, -0.9),(0.56, 0.52, -0.8),(0.37, 0.52, -0.8),(0.19, 0.52, -0.8),(0.19, 0.66, -0.68),(0.19, 0.77, -0.53),(0.19, 0.86, -0.36),(0.19, 0.91, -0.19),( 0.19, 0.92, 0),(0.19, 0.91, 0.19),(0.19, 0.86, 0.36),(0.19, 0.77, 0.53),(0.19, 0.66, 0.68),(0.19, 0.52, 0.8),(0.37, 0.52, 0.8),(0.56, 0.52, 0.8),( 0.37, 0.36, 0.9),(0.19, 0.18, 0.96), (-0, -0, 0.99) ]    

    def Empty(self):
        deleteThat=cmds.circle(n='Delete')
        cmds.delete(deleteThat)

    def PrintName(self):
        sl = cmds.ls(sl=1, o=1)
        a = []
        for s in sl:
            print ("'"+s+"',")
            this = str(s)
            a.append(this)
    
        print (str(a))

    def FindAndDelete(self,OBJName):
        if cmds.objExists(OBJName):
            cmds.select(OBJName)
            cmds.Delete(OBJName)
        else:
            pass

    def LockHideAttr(self,CtrlName,T,TX,TY,TZ,R,RX,RY,RZ,S,SX,SY,SZ,Vis):
        if T==True:
            cmds.setAttr(CtrlName+'.t',keyable=False,l=True,channelBox=False)
        else:
            if TX==True:
                cmds.setAttr(CtrlName+'.tx',keyable=False,l=True,channelBox=False)
            if TY==True:
                cmds.setAttr(CtrlName+'.ty',keyable=False,l=True,channelBox=False)
            if TZ==True:
                cmds.setAttr(CtrlName+'.tz',keyable=False,l=True,channelBox=False)
        if R==True:
            cmds.setAttr(CtrlName+'.r',keyable=False,l=True,channelBox=False)
        else:
            if RX==True:
                cmds.setAttr(CtrlName+'.rx',keyable=False,l=True,channelBox=False)
            if RY==True:
                cmds.setAttr(CtrlName+'.ry',keyable=False,l=True,channelBox=False)
            if RZ==True:
                cmds.setAttr(CtrlName+'.rz',keyable=False,l=True,channelBox=False)
        if S==True:
            cmds.setAttr(CtrlName+'.s',keyable=False,l=True,channelBox=False)
        else:
            if SX==True:
                cmds.setAttr(CtrlName+'.sx',keyable=False,l=True,channelBox=False)
            if SY==True:
                cmds.setAttr(CtrlName+'.sy',keyable=False,l=True,channelBox=False)
            if SZ==True:
                cmds.setAttr(CtrlName+'.sz',keyable=False,l=True,channelBox=False)

        if Vis==True:
            cmds.setAttr(CtrlName+'.v',keyable=False,l=True,channelBox=False)

    def BringBackAttr(self,CtrlName):
        cmds.setAttr(CtrlName+'.tx',l=False,channelBox=True,keyable=True)
        cmds.setAttr(CtrlName+'.ty',keyable=True,l=False,channelBox=True)
        cmds.setAttr(CtrlName+'.tz',keyable=True,l=False,channelBox=True)
        cmds.setAttr(CtrlName+'.rx',keyable=True,l=False,channelBox=True)
        cmds.setAttr(CtrlName+'.ry',keyable=True,l=False,channelBox=True)
        cmds.setAttr(CtrlName+'.rz',keyable=True,l=False,channelBox=True)
        cmds.setAttr(CtrlName+'.sx',keyable=True,l=False,channelBox=True)
        cmds.setAttr(CtrlName+'.sy',keyable=True,l=False,channelBox=True)
        cmds.setAttr(CtrlName+'.sz',keyable=True,l=False,channelBox=True)
        cmds.setAttr(CtrlName+'.v',keyable=True,l=False,channelBox=True)

    def NewScene (self):
        mc.file(new=1,f=1)

    def ImportModel (self,Direct):
            mc.file("D:\JustArm.fbx",i=1)

    def ImportJoint (self,Direct):
            mc.file("D:\JustJoint.fbx",i=1)

    def ImportWeight (self,Direct):
            mc.file("D:\Arm_SW.xml",i=1)

    def FKIKLocate (self,CtrlSizeArmInput):
        self.Empty()
        cmds.spaceLocator( p=(0, 0, 0), name='FKIKBlend_Locator')
        cmds.scale( CtrlSizeArmInput, CtrlSizeArmInput, CtrlSizeArmInput )

    def red(self):
        mc.textField('ColorInputArm',e = True,tx='red')
        mc.textField('ColorInputLeg',e = True,tx='red')
    def violet(self):
        mc.textField('ColorInputArm',e = True,tx='violet')
        mc.textField('ColorInputLeg',e = True,tx='violet')
    def yellow(self):
        cmds.textField('ColorInputArm',e = True,tx='yellow')
        mc.textField('ColorInputLeg',e = True,tx='yellow')
    def blue(self):
        cmds.textField('ColorInputArm',e = True,tx='blue')
        mc.textField('ColorInputLeg',e = True,tx='blue')
    def green(self):
        cmds.textField('ColorInputArm',e = True,tx='green')
        mc.textField('ColorInputLeg',e = True,tx='green')

    def ArmSample(self,Name,LRInput,XYZInput,AimCheck,UpJntInput,UpCheck,WorldUpJntInput,WorldCheck,CtrlSizeArmInput):
        self.Empty()
        self.FKIKLocate(CtrlSizeArmInput=CtrlSizeArmInput)
        self.Empty()
        cmds.setAttr('FKIKBlend_Locator.ty',2*CtrlSizeArmInput)

        if LRInput == 'Left':
            LR='l'
        if LRInput == 'Right':
            LR='r'
        
        D1=cmds.joint(n=LR+'_'+Name+'1_jnt')
        D2=cmds.joint(n=LR+'_'+Name+'2_jnt')
        cmds.setAttr(D2+'.t',3,0,0)
        cmds.setAttr(D2+'.r',0,-35,0)
        cmds.setAttr(D2+'.preferredAngleY',-1)
        D3=cmds.joint(n=LR+'_'+Name+'3_jnt')
        cmds.setAttr(D3+'.t',2.8,0,0)
        #cmds.setAttr(D1+'.r',0,12,-24.8)
        #cmds.setAttr(D1+'.t',2.5,7.5,0)

        if LR=='r':
            cmds.mirrorJoint(D1,mirrorBehavior=True,myz=True,searchReplace=('l_', 'r_')) 
            cmds.delete(D1)

        cmds.pointConstraint(D1,'FKIKBlend_Locator',mo=True,n='DeletePCon')

    def executeArm (self,Name,LRInput,XYZInput,AimCheck,UpJntInput,UpCheck,WorldUpJntInput,WorldCheck,CtrlSizeArmInput,InGrpCheck,EndjntCheck,AutoCheck,PoleVectorDis,floatStretchAmp):
        mc.select(hi=True) #Select hiracraccy after click
        selBack=mc.ls(sl=True)
        self.FindAndDelete(OBJName='DeletePCon')
        cmds.select(selBack)

        #Name Input
        ###############Name=mc.textField('NameArmInput', q = True, tx = True)
        #LR Input
        if LRInput == 'Left':
            LR='L_'
        if LRInput == 'Right':
            LR='R_'
        
        #XYZ Input
        ################XYZInput= mc.radioCollection(XYZArmRadio, q = True, sl = True)
        if XYZInput == 'X':
            AimJnt = 'X'
        if XYZInput == 'Y':
            AimJnt = 'Y'
        if XYZInput == 'Z':
            AimJnt = 'Z'
        
        ###############AimCheck=mc.checkBox('RevXYZArm', query=True, value = True)
        if AimCheck == True:
            AimMinus = -1
        if AimCheck == False:
            AimMinus = 1
                
        ###############UpJntInput = mc.radioCollection(UpJntArmRadio, q = True, sl = True)
        if UpJntInput == 'X':
            UpJnt = 'X'
        if UpJntInput == 'Y':
            UpJnt = 'Y'
        if UpJntInput == 'Z':
            UpJnt = 'Z'
        
        ###############UpCheck=mc.checkBox('RevUpJntArm', query=True, value = True)
        if UpCheck == True:
            UpMinus = -1
        if UpCheck == False:
            UpMinus = 1
        
        ###############WorldUpJntInput = mc.radioCollection(WorldUpArmJntRadio, q = True, sl = True)
        if WorldUpJntInput == 'X':
            WorldUp = 'X'
        if WorldUpJntInput == 'Y':
            WorldUp = 'Y'
        if WorldUpJntInput == 'Z':
            WorldUp = 'Z'
        ###############WorldCheck=mc.checkBox('RevWorldUpArm', query=True, value = True)
        if WorldCheck == True:
            WorldUpMinus = -1
        if WorldCheck == False:
            WorldUpMinus = 1
        
        #CtrlSizeArmInput = float(mc.floatField(CtrlSizeArmInput, q = True, v = True))
        if InGrpCheck == True:
            InGrp = 1
        if InGrpCheck == False:
            InGrp = 2
        
        ###############EndjntCheck=mc.checkBox('EndGrpArmRadio', query=True, value = True)
        if EndjntCheck == True:
            Endjnt = 1
        if EndjntCheck == False:
            Endjnt = 0
            
        ###############AutoCheck=mc.checkBox('AutoStrechArmRadio', query=True, value = True)
        if AutoCheck == True:
            AutoEnable = 1
        if AutoCheck == False:
            AutoEnable = 0    
        
        ###############PoleVectorDis=mc.floatField(PoleVectorDisArmInput, q = True, v = True)
        ###############floatStretchAmp=mc.floatField(AmpArmInput, q = True, v = True)
        
        
        FkList=[]
        IkList = []
        Color = []
        index = 1

        if LR=='L_':
            Color = (1 , 0 , 0 )
        if LR=='R_':
            Color = (0 , 0 , 1 )

        def ArmFKIK ():
        
            index = 1

            mc.select() #Select hiracraccy after click
            selBack=mc.ls(sl=True)

            #cmds.parent(selBack,world=True)
            #self.FindAndDelete(OBJName='COG'+Name+'Ctrl')
            #cmds.select(selBack)


            mc.select(hi=True) #Select hiracraccy after click
            BJointList=mc.ls(sl=True) #Select hilight as list
            #print BJointList

            FkJnt=cmds.duplicate(n = 'FK')
            IkJnt=cmds.duplicate(n = 'IK')
                    
            for b in range (len(BJointList)):
                convertindex = str(index)
                cmds.select( FkJnt[b], r=True )
                cmds.rename( LR+'FK_'+Name+convertindex+'_jnt' )
                FkList.append( LR+'FK_'+Name+convertindex+'_jnt' )
                cmds.select( IkJnt[b], r=True )
                cmds.rename( LR+'IK_'+Name+convertindex+'_jnt' )
                IkList.append( LR+'IK_'+Name+convertindex+'_jnt' )
                index+=1
            
            WristAimJnt=cmds.joint(name=LR+'IK_'+Name+'WristAim_jnt')
            cmds.matchTransform(WristAimJnt, IkList[2])
            if AimMinus == 1:
                cmds.setAttr( WristAimJnt+'.translate'+AimJnt, 3 )
            if AimMinus == -1:
                cmds.setAttr( WristAimJnt+'.translate'+AimJnt, -3 )
            IkList.append( WristAimJnt )
        
            def FK ():

                E= len(FkList)-Endjnt
        
        
                for i in range (E):
                    FkCtrl = cmds.circle( name=LR+'FK_'+Name+str(i+1)+'_ctrl', r=2)
                    cmds.color( FkCtrl , rgb = Color )
                    cmds.rotate( 0, 90, 0, r=True )
                    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                    cmds.scale( CtrlSizeArmInput, CtrlSizeArmInput, CtrlSizeArmInput )
                    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                    FkoffsetGrp=cmds.group(FkCtrl,name=LR+'FK_'+Name+str(i+1)+'_offset')
                    cmds.group(FkCtrl,name=LR+'FK_'+Name+str(i+1)+'_zero')
                    cmds.matchTransform(FkoffsetGrp,FkList[i])
            
                    if i > 0:
                        cmds.parent(LR+'FK_'+Name+str(i+1)+'_offset',LR+'FK_'+Name+str(i)+'_ctrl')
                    else:
                        pass
            
                    if InGrp == 1:
                        cmds.parent( FkList[i],FkCtrl)
                        cmds.group(LR+'FK_'+Name+'1_offset',name=LR+'FK_'+Name+'_grp')
                
                    elif InGrp == 2:
                        cmds.parentConstraint(FkCtrl, FkList[i],mo=1)
                        cmds.group(LR+'FK_'+Name+'1_offset',LR+'FK_'+Name+'1_jnt',name=LR+'FK_'+Name+'_grp')

                    
                    else:
                        pass
                    
        
            FK ()
            def IK ():
        
                #shoulder
                IKSho=cmds.curve(p=self.Cube,d=1,n=LR+'IK_'+Name+'1_ctrl')
                cmds.color( IKSho , rgb = Color )
                cmds.rotate( 0, 0, 0, r=True )
                cmds.scale(0.5,1,1)
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                cmds.scale( CtrlSizeArmInput, CtrlSizeArmInput, CtrlSizeArmInput )
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                offsetGrpSho=cmds.group(IKSho,name=LR+'IK_'+Name+'1_offset')
                cmds.group(IKSho,name=LR+'IK_'+Name+'1_zero')
                cmds.matchTransform(offsetGrpSho, IkList[0])
                cmds.parentConstraint(IKSho,IkList[0],mo=1)
        
                #IKH
                ArmIKH=cmds.ikHandle( n=LR+Name+'_ikh', sj=IkList[0], ee=IkList[2], sol='ikRPsolver')
                HandIKH=cmds.ikHandle( n=LR+Name+'2_ikh', sj=IkList[2], ee=IkList[3], sol='ikSCsolver' )
                cmds.group(LR+Name+'_ikh',LR+Name+'2_ikh',name=LR+'IK_'+Name+'IKH_grp')
        
                #Wrist
                #IKWrist=cmds.circle( name=LR+'IK_'+Name+'3_ctrl', r=2)
                IKWrist=cmds.curve(p=self.Cube,d=1,n=LR+'IK_'+Name+'3_ctrl')
                cmds.color( IKWrist , rgb = Color )
                cmds.rotate( 0, 0, 0, r=True )
                cmds.scale(0.5,1,1)
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                cmds.scale( CtrlSizeArmInput, CtrlSizeArmInput, CtrlSizeArmInput )
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                offsetGrpWrist=cmds.group(IKWrist,name=LR+'IK_'+Name+'3_offset')
                cmds.group(IKWrist,name=LR+'IK_'+Name+'3_zero')
                cmds.matchTransform(offsetGrpWrist, IkList[2])
                cmds.parentConstraint(IKWrist, LR+Name+'_ikh',mo=1)
                cmds.parentConstraint(IKWrist, LR+Name+'2_ikh',mo=1)
        
                #Polevector
                IKPole=cmds.curve(p=self.PoleVec,d=1,n=LR+'IK_'+Name+'2_ctrl')
                cmds.color( IKPole , rgb = Color )
                cmds.scale( CtrlSizeArmInput, CtrlSizeArmInput, CtrlSizeArmInput )
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                offsetGrpPole=cmds.group( IKPole,name=LR+'IK_'+Name+'2_offset')
                zeroGrpPole=cmds.group( IKPole,name=LR+'IK_'+Name+'2_zero')
                cmds.matchTransform(offsetGrpPole, IkList[1],position=1)
            
                IkPoleDis=cmds.getAttr(offsetGrpPole+'.translateZ')
                IkPoleDisMinus= (IkPoleDis+PoleVectorDis)
                cmds.setAttr(offsetGrpPole+'.translateZ',IkPoleDisMinus)
                if AimMinus == -1:
                    cmds.setAttr(offsetGrpPole+'.rotateY',180)
                Ikorient=cmds.orientConstraint(IkList[1],offsetGrpPole,maintainOffset=0,skip="y")
                cmds.delete(Ikorient)
                
                cmds.poleVectorConstraint( IKPole, LR+Name+'_ikh' )
                FollowAttr=cmds.addAttr(IKPole,ln=LR+Name+'_Follow',minValue=0,maxValue=1,k=True)
                cmds.setAttr(IKPole+'.'+LR+Name+'_Follow',1)


                
                #FollowLocal
                def FollowLocal ():
                    PoleAim=cmds.group(em=True,name=LR+'IK_Pole'+Name+'Aim')
                    PoleFollow=cmds.group(em=True,name=LR+'IK_Pole'+Name+'Follow')
                    LocalFol=cmds.group(em=True,name=LR+'IK_Local'+Name+'Follow')
                    LocalAim=cmds.group(em=True,name=LR+'Local'+Name+'Aim')
                
                    cmds.matchTransform(PoleAim, IKSho)
                    cmds.matchTransform(PoleFollow, IKPole)
                    cmds.matchTransform(LocalFol, IKPole)
                    cmds.matchTransform(LocalAim, IKWrist)
                    
                    AimV = []
                    UpV = []
                    WorldV = []
        
                    if AimMinus == 1:
                        if AimJnt == 'X':
                            AimV = [AimMinus,0,0]
                        if AimJnt == 'Y':
                            AimV = [0,AimMinus,0]
                        if AimJnt == 'Z':
                            AimV = [0,0,AimMinus]

                    if AimMinus == -1:
                        if AimJnt == 'X':
                            AimV = [AimMinus,0,0]
                        if AimJnt == 'Y':
                            AimV = [0,AimMinus,0]
                        if AimJnt == 'Z':
                            AimV = [0,0,AimMinus]
                            
                    if UpMinus == 1:       
                        if UpJnt == 'X':
                            UpV = [AimMinus,0,0]
                        if UpJnt == 'Y':
                            UpV = [0,AimMinus,0]
                        if UpJnt == 'Z':
                            UpV = [0,0,AimMinus]
                            
                    if UpMinus == -1:       
                        if UpJnt == 'X':
                            UpV = [AimMinus,0,0]
                        if UpJnt == 'Y':
                            UpV = [0,AimMinus,0]
                        if UpJnt == 'Z':
                            UpV = [0,0,AimMinus]

                    if WorldUpMinus == 1:
                        if WorldUp == 'X':
                            WorldV = [WorldUpMinus,0,0]
                        if WorldUp == 'Y':
                            WorldV = [0,WorldUpMinus,0]
                        if WorldUp == 'Z':
                            WorldV = [0,0,WorldUpMinus]
                            
                    if WorldUpMinus == -1:
                        if WorldUp == 'X':
                            WorldV = [WorldUpMinus,0,0]
                        if WorldUp == 'Y':
                            WorldV = [0,WorldUpMinus,0]
                        if WorldUp == 'Z':
                            WorldV = [0,0,WorldUpMinus]
                
                    cmds.parentConstraint(IKWrist,LocalAim,maintainOffset =1)
                    cmds.pointConstraint(IKSho, PoleAim)
                    cmds.aimConstraint(IKWrist, PoleAim, aimVector = AimV,upVector = UpV , worldUpType = 'objectrotation',worldUpVector=WorldV , worldUpObject= LocalAim )######
                    cmds.parentConstraint(PoleAim, PoleFollow,maintainOffset =1)
                    cmds.parentConstraint(PoleFollow, LocalFol,zeroGrpPole,maintainOffset =1)
                    
                    #group,name = FollowParent
                    PoleFollowGrp=cmds.group(PoleAim,PoleFollow,LocalFol,LocalAim,n=LR+'IK_'+Name+'PoleFollow_grp')
                    zeroIkGrp=cmds.group(LR+'IK_'+Name+'1_offset',LR+'IK_'+Name+'2_offset',LR+'IK_'+Name+'3_offset',LR+'IK_'+Name+'IKH_grp',LR+'IK_'+Name+'1_jnt',PoleFollowGrp,name=LR+'IK_'+Name+'_zero')
                    cmds.group(zeroIkGrp,n=LR+'IK_'+Name+'_grp')
                    
                    
                    reverseFol=cmds.createNode('reverse', n=LR+Name+'reverseFol')
                    cmds.connectAttr(IKPole+'.'+LR+Name+'_Follow',reverseFol+'.input.inputX')
                    
                    #print FollowParent+'.'+LR+'IK_Local'+Name+'FollowW1'
                    
                    cmds.connectAttr(LR+Name+'reverseFol.output.outputX',LR+'IK_'+Name+'2_zero_parentConstraint1.'+LR+'IK_Local'+Name+'FollowW1')
                    
                    cmds.connectAttr(IKPole+'.'+LR+Name+'_Follow',LR+'IK_'+Name+'2_zero_parentConstraint1.'+LR+'IK_Pole'+Name+'FollowW0')

                FollowLocal ()
            IK ()
            def SwitchFKIK ():
                
                bjMinus = (len(BJointList)) 
                XYZ = ['X','Y','Z']
        
                #ParentConstraint
                for p in range (bjMinus):
                    cmds.parentConstraint(FkList[p],IkList[p],BJointList[p], maintainOffset=1)
                    
                #Create FKIKSwitch
                FKIKSwitch = cmds.curve(p=self.Plus,d=1,n=LR+Name+'FkIk_Switch')
                cmds.rotate( 90, 0, 0, r=True )
                cmds.scale( 0.25, 0.25, 0.25 )
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                cmds.scale( (CtrlSizeArmInput/0.5),(CtrlSizeArmInput/0.5), (CtrlSizeArmInput/0.5) )
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                cmds.color( FKIKSwitch , rgb = Color )
                cmds.addAttr(FKIKSwitch,ln=LR+Name+'Fk_IK_Blend',minValue=0,maxValue=10,k=True)
                cmds.setAttr(FKIKSwitch+'.t',keyable=False,l=True,channelBox=False)
                cmds.setAttr(FKIKSwitch+'.r',keyable=False,l=True,channelBox=False)
                cmds.setAttr(FKIKSwitch+'.s',keyable=False,l=True,channelBox=False)
                cmds.group(FKIKSwitch,name=LR+Name+'FK_IK_Switch_zero')
                SwitchoffsetGrp=cmds.group(LR+Name+'FK_IK_Switch_zero',name=LR+Name+'FK_IK_Switch_offset')
                
                cmds.matchTransform(LR+Name+'FK_IK_Switch_offset', 'FKIKBlend_Locator')
                cmds.delete('FKIKBlend_Locator')
                
                uniCon1=cmds.createNode('unitConversion', n=LR+Name+'_uniCon1')
                cmds.connectAttr(FKIKSwitch+'.'+LR+Name+'Fk_IK_Blend',LR+Name+'_uniCon1.input')
                cmds.setAttr( LR+Name+'_uniCon1.conversionFactor', 0.1 )
                
                cmds.createNode('reverse', n=LR+Name+'reverse1')
                cmds.connectAttr(LR+Name+'_uniCon1.output',LR+Name+'reverse1.input.inputX')
                cmds.connectAttr(LR+Name+'_uniCon1.output',LR+Name+'reverse1.input.inputY')
                cmds.connectAttr(LR+Name+'_uniCon1.output',LR+Name+'reverse1.input.inputZ')
                
                for z in range (bjMinus):
                    print (BJointList[z])
                    print (LR)
                    print (Name+str(z+1))
                    cmds.connectAttr(LR+Name+'reverse1.output.output'+XYZ[z], BJointList[z]+'_parentConstraint1.'+LR+'FK_'+Name+str(z+1)+'_jntW0')
                    cmds.connectAttr(LR+Name+'_uniCon1.output',BJointList[z]+'_parentConstraint1.'+LR+'IK_'+Name+str(z+1)+'_jntW1')
                
                #Vis
                cmds.createNode('reverse', n=LR+Name+'reverse2')
                cmds.connectAttr(LR+Name+'_uniCon1.output',LR+Name+'reverse2.input.inputX')    
                cmds.connectAttr(LR+Name+'reverse2.output.outputX', LR+'FK_'+Name+'1_zero.visibility')
                cmds.connectAttr(LR+Name+'_uniCon1.output', LR+'IK_'+Name+'_zero.visibility')
                
                cmds.hide(LR+'FK_'+Name+'1_jnt')
                cmds.hide(LR+'IK_'+Name+'1_jnt')
                cmds.hide(LR+'IK_'+Name+'IKH_grp')
            
            SwitchFKIK()
            
            def AutoSwitch():
                if AutoEnable == 1:
                    #Ruler
                    ruler1=cmds.circle(n='Locator1')
                    cmds.matchTransform('Locator1',BJointList[0])
                    joint1X = cmds.getAttr('Locator1.translateX')
                    joint1Y = cmds.getAttr('Locator1.translateY')
                    joint1Z = cmds.getAttr('Locator1.translateZ')
                    
                    ruler2=cmds.circle(n='Locator2')
                    cmds.matchTransform('Locator2',BJointList[1])
                    joint2X = cmds.getAttr('Locator2.translateX')
                    joint2Y = cmds.getAttr('Locator2.translateY')
                    joint2Z = cmds.getAttr('Locator2.translateZ')
                    
                    ruler3=cmds.circle(n='Locator3')
                    cmds.matchTransform('Locator3',BJointList[2])
                    joint3X = cmds.getAttr('Locator3.translateX')
                    joint3Y = cmds.getAttr('Locator3.translateY')
                    joint3Z = cmds.getAttr('Locator3.translateZ')

                    joint1Location = (joint1X,joint1Y,joint1Z)
                    joint2Location = (joint2X,joint2Y,joint2Z)
                    joint3Location = (joint3X,joint3Y,joint3Z)

                    DistanDimen1=cmds.distanceDimension( sp=joint1Location, ep=joint2Location )
                    DistanDimen2=cmds.distanceDimension( sp=joint2Location, ep=joint3Location )
                    DistanDimen3=cmds.distanceDimension( sp=joint1Location, ep=joint3Location )
                    
                    #Vaule
                    
                    floatDistanceUp=cmds.getAttr(DistanDimen1+'.distance')
                    floatDistanceDown=cmds.getAttr(DistanDimen2+'.distance')
                    floatDistanceAll=cmds.getAttr(DistanDimen3+'.distance')
                    
                    RulerGrp=cmds.group(ruler1,ruler2,ruler3,DistanDimen1,DistanDimen2,DistanDimen3,'locator1','locator2','locator3',name='ruler_grp')
                    cmds.delete(RulerGrp)
                    
                    index =[]
                    CtrlIK = LR+'IK_'+Name+'3_ctrl'
                    CtrlPole = LR+'IK_'+Name+'2_ctrl'
                    DistanceUp = LR+'IK_'+Name+'1_ctrl'
                    DistanceDown = LR+'IK_'+Name+'3_ctrl' 
                    DistancePole = LR+'IK_'+Name+'2_ctrl'
                    JointStretch1 = LR+'IK_'+Name+'2_jnt'
                    JointStretch2 = LR+'IK_'+Name+'3_jnt'
                    
                    oneDividedTop = 1/floatDistanceUp
                    oneDividedDown = 1/floatDistanceDown
                    
            
                    TopGrpName = LR+Name+'_AutoUp_grp'
                    DownGrpName = LR+Name+'_AutoDown_grp'
                    PoleGrpName = LR+Name+'_AutoPole_grp'
                    
                    #AddAttr
                    cmds.addAttr(CtrlIK,ln='Auto',attributeType='enum',k=True,enumName='---------------')
                    cmds.setAttr(CtrlIK+'.Auto',lock=True)
                    cmds.addAttr(CtrlIK,ln='St_Up',k=True,at='float')
                    cmds.addAttr(CtrlIK,ln='St_Down',k=True,at='float')
                    cmds.addAttr(CtrlIK,ln='Auto_Stretch',k=True,at='float',minValue=0,maxValue=10)
                    cmds.addAttr(CtrlPole,ln='PoleVector_Lock',minValue=0,maxValue=10,k=True)
                    
                    #MultAmpTop
                    MultAmpTop1=cmds.createNode('multDoubleLinear')
                    cmds.addAttr(MultAmpTop1,ln='Amp',k=True)
                    cmds.setAttr( MultAmpTop1+'.Amp', floatStretchAmp )
                    cmds.connectAttr(MultAmpTop1+'.Amp',MultAmpTop1+'.input1') 
                    cmds.connectAttr(CtrlIK+'.St_Up',MultAmpTop1+'.input2')
                    
                    #MultTop
                    MultTop=cmds.createNode('multDoubleLinear')
                    cmds.setAttr( MultTop+'.input2', floatDistanceUp)
                    cmds.connectAttr(MultAmpTop1+'.output',MultTop+'.input1')
                
                    #MultAmpBot
                    MultAmpBot1=cmds.createNode('multDoubleLinear')
                    cmds.addAttr(MultAmpBot1,ln='Amp',k=True)
                    cmds.setAttr( MultAmpBot1+'.Amp', floatStretchAmp )
                    cmds.connectAttr(MultAmpBot1+'.Amp',MultAmpBot1+'.input1')
                    
                    cmds.connectAttr(CtrlIK+'.St_Down',MultAmpBot1+'.input2')
                    
                    #MultBot
                    MultBot=cmds.createNode('multDoubleLinear')
                    cmds.setAttr( MultBot+'.input2', floatDistanceDown)
                    cmds.connectAttr(MultAmpBot1+'.output',MultBot+'.input1')
                    
                    #DistanTopDown
                    UpGrp=cmds.group( em=True, name=TopGrpName)
                    DownGrp=cmds.group( em=True, name=DownGrpName)
                    
                    cmds.pointConstraint(DistanceUp,UpGrp)
                    cmds.pointConstraint(CtrlIK,DownGrp)      
                    
                    DisUpDown=cmds.createNode('distanceBetween')
                    cmds.connectAttr(UpGrp+'.t',DisUpDown+'.point1')
                    cmds.connectAttr(DownGrp+'.t',DisUpDown+'.point2')
                    
                    MultTotalTD=cmds.createNode('multDoubleLinear')
                    cmds.connectAttr(DisUpDown+'.distance',MultTotalTD+'.input2')
                    DisupDownDi=cmds.getAttr(MultTotalTD+'.input2')
                    cmds.setAttr(MultTotalTD+'.input1',1/DisupDownDi)
                    
                    #Condition
                    Condi=cmds.createNode('condition')
                    cmds.connectAttr(MultTotalTD+'.output',Condi+'.colorIfTrue.colorIfTrueR')
                    cmds.connectAttr(DisUpDown+'.distance',Condi+'.firstTerm')
                    cmds.setAttr(Condi+".secondTerm",floatDistanceAll)
                    cmds.setAttr(Condi+".operation",2)
                    
                    #ConOut MultTop
                    MultConTop=cmds.createNode('multDoubleLinear')
                    cmds.connectAttr(Condi+'.outColor.outColorR',MultConTop+'.input1')
                    cmds.setAttr(MultConTop+".input2",floatDistanceUp)
                    
                    #BlendTop
                    BlendMultTop=cmds.createNode('blendTwoAttr')
                    cmds.addAttr(BlendMultTop,ln='DEF',k=True)
                    cmds.setAttr(BlendMultTop+".DEF",floatDistanceUp)
                    cmds.connectAttr(BlendMultTop+'.DEF',BlendMultTop+'.input[0]')
                    cmds.connectAttr(MultConTop+'.output',BlendMultTop+'.input[1]')
    
                    #ConOut MultDown
                    MultConDown=cmds.createNode('multDoubleLinear')
                    cmds.connectAttr(Condi+'.outColor.outColorR',MultConDown+'.input1')
                    cmds.setAttr(MultConDown+".input2",floatDistanceDown)
                    
                    #BlendDown
                    BlendMultDown=cmds.createNode('blendTwoAttr')
                    cmds.addAttr(BlendMultDown,ln='DEF',k=True)
                    cmds.setAttr(BlendMultDown+".DEF",floatDistanceDown)
                    cmds.connectAttr(BlendMultDown+'.DEF',BlendMultDown+'.input[0]')
                    cmds.connectAttr(MultConDown+'.output',BlendMultDown+'.input[1]')
                    
                    #UniConverAuto
                    UniConAuto=cmds.createNode('unitConversion')
                    cmds.setAttr(UniConAuto+".conversionFactor",0.1)
                    cmds.connectAttr(CtrlIK+'.Auto_Stretch',UniConAuto+'.input')
                    cmds.connectAttr(UniConAuto+'.output', BlendMultTop+'.attributesBlender')
                    cmds.connectAttr(UniConAuto+'.output',BlendMultDown+'.attributesBlender')
                    
                    #addDoubleLinear
                    DoubTop=cmds.createNode('addDoubleLinear')
                    cmds.connectAttr( BlendMultTop+'.output', DoubTop+'.input1')
                    cmds.connectAttr(MultTop+'.output',DoubTop+'.input2')
                    
                    DoubDown=cmds.createNode('addDoubleLinear')     
                    cmds.connectAttr(BlendMultDown+'.output',DoubDown+'.input1')
                    cmds.connectAttr(MultBot+'.output',DoubDown+'.input2')
                    
                    #PolevectorStart
                    PoleGrp=cmds.group( em=True, name=PoleGrpName)
                    cmds.pointConstraint(CtrlPole,PoleGrp)
                    
                    #Polevector+Top
                    DisUpPole=cmds.createNode('distanceBetween')
                    cmds.connectAttr(PoleGrp+'.t',DisUpPole+'.point1')
                    cmds.connectAttr( UpGrp+'.t',DisUpPole+'.point2')
                    
                    MultDiviTop=cmds.createNode('multDoubleLinear')
                    cmds.connectAttr(DisUpPole+'.distance',MultDiviTop+'.input1')
                    cmds.setAttr(MultDiviTop+".input2",oneDividedTop)
                    
                    MultLinTop=cmds.createNode('multDoubleLinear')
                    cmds.connectAttr(MultDiviTop+'.output',MultLinTop+'.input1')
                    cmds.setAttr(MultLinTop+".input2",floatDistanceUp)
                    
                    #Polevector+Down
                    DisDownPole=cmds.createNode('distanceBetween')
                    cmds.connectAttr(PoleGrp+'.t',DisDownPole+'.point1')
                    cmds.connectAttr(DownGrp+'.t',DisDownPole+'.point2')
                    
                    MultDiviDown=cmds.createNode('multDoubleLinear')
                    cmds.connectAttr(DisDownPole+'.distance',MultDiviDown+'.input1')
                    cmds.setAttr(MultDiviDown+".input2",oneDividedDown)
                    
                    MultLinDown=cmds.createNode('multDoubleLinear')
                    cmds.connectAttr(MultDiviDown+'.output',MultLinDown+'.input1')
                    cmds.setAttr(MultLinDown+".input2",floatDistanceDown)
                    
                    #LastBlendtwoAttr
                    BlendAttrTop=cmds.createNode('blendTwoAttr')
                    cmds.connectAttr(DoubTop+'.output',BlendAttrTop+'.input[0]')
                    cmds.connectAttr(MultLinTop+'.output',BlendAttrTop+'.input[1]')
                    
                    BlendAttrDown=cmds.createNode('blendTwoAttr')
                    cmds.connectAttr(DoubDown+'.output',BlendAttrDown+'.input[0]')
                    cmds.connectAttr(MultLinDown+'.output',BlendAttrDown+'.input[1]')
                    
                    ConPoleBlend=cmds.createNode('unitConversion', n='unitConversion')
                    cmds.connectAttr(CtrlPole+'.PoleVector_Lock',ConPoleBlend+'.input')
                    cmds.setAttr(ConPoleBlend+'.conversionFactor',0.1)
                    
                    cmds.connectAttr(ConPoleBlend+'.output',BlendAttrTop+'.attributesBlender')
                    cmds.connectAttr(ConPoleBlend+'.output',BlendAttrDown+'.attributesBlender')
                    
                    if AimMinus == 1:
                        cmds.connectAttr(BlendAttrTop+'.output',JointStretch1+'.translate'+AimJnt)
                        cmds.connectAttr(BlendAttrDown+'.output',JointStretch2+'.translate'+AimJnt)
                        
                    elif AimMinus == -1:
                        
                        NegaMult1=cmds.createNode('multDoubleLinear')
                        cmds.setAttr(NegaMult1+".input2",-1)
                        cmds.connectAttr(BlendAttrTop+'.output',NegaMult1+'.input1')
                        cmds.connectAttr(NegaMult1+'.output',JointStretch1+'.translate'+AimJnt)
                        
                        NegaMult2=cmds.createNode('multDoubleLinear')
                        cmds.setAttr(NegaMult2+".input2",-1)
                        cmds.connectAttr(BlendAttrDown+'.output',NegaMult2+'.input1')
                        cmds.connectAttr(NegaMult2+'.output',JointStretch2+'.translate'+AimJnt)
                        
                    else:
                        print ('error')
                        
                    cmds.group(UpGrp,DownGrp,PoleGrp,name=LR+Name+'IKAuto_grp')
                    cmds.parent(LR+Name+'IKAuto_grp',LR+'IK_'+Name+'_zero')
                else:
                    pass
            
            AutoSwitch()      
        ArmFKIK()

    def SelectOBjLeg (self):
        selection = mc.ls(sl = True)[0]
        mc.textField('NameLegInput',e = True, tx=selection)

    def LocatorLeg(self,CtrlSizeLegInput):
        self.Empty()
        J1=cmds.joint(name='FootIn_Locator')
        cmds.setAttr( 'FootIn_Locator.translateX',-1 )
        cmds.scale( CtrlSizeLegInput, CtrlSizeLegInput, CtrlSizeLegInput )
        Deletedis=cmds.circle( name='Delete', r=2)
        cmds.delete(Deletedis)
        J2=cmds.joint(name='FootOut_Locator')
        cmds.setAttr( 'FootOut_Locator.translateX',1 )
        cmds.scale( CtrlSizeLegInput, CtrlSizeLegInput, CtrlSizeLegInput )
        Deletedis=cmds.circle( name='Delete', r=2)
        cmds.delete(Deletedis)
        J3=cmds.joint(name='Heel_Locator')
        cmds.setAttr( 'Heel_Locator.translateZ',-1 )
        cmds.scale( CtrlSizeLegInput, CtrlSizeLegInput, CtrlSizeLegInput )
        Circle=cmds.circle( name='LocaterRoot', r=2)
        cmds.rotate( 90, 0, 0, r=True )
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        cmds.parent(J1,J2,J3,Circle)

    def LocatorFKIKLeg(self,CtrlSizeLegInput):
        self.Empty()
        LCS = CtrlSizeLegInput
        cmds.spaceLocator( p=(0, 0, 0), name='FootFKIK_Locator')
        #print (LCS)
        cmds.scale( LCS, LCS, LCS )

    def LegSample(self,Name,LRInput,XYZInput,AimCheck,UpJntInput,UpCheck,WorldUpJntInput,WorldCheck,CtrlSizeLegInput):
        
        self.LocatorLeg(CtrlSizeLegInput=CtrlSizeLegInput)
        self.LocatorFKIKLeg(CtrlSizeLegInput=CtrlSizeLegInput)
        
        Name=Name
        AimV=XYZInput
        UpV=UpJntInput
        WorldV=WorldUpJntInput

        print (Name)
        print (XYZInput)
        print (UpJntInput)
        print (WorldUpJntInput)

        #LR Input
        if LRInput == 'Left':
            LR='L_'
        if LRInput == 'Right':
            LR='R_'  
        #XYZ Input
        if XYZInput == 'X':
            AimJnt = 'X'
        if XYZInput == 'Y':
            AimJnt = 'Y'
        if XYZInput == 'Z':
            AimJnt = 'Z'
        #Aim-
        if AimCheck == True:
            AimMinus = -1
        if AimCheck == False:
            AimMinus = 1
        #UpJnt      
        if UpJntInput == 'X':
            UpJnt = 'X'
        if UpJntInput == 'Y':
            UpJnt = 'Y'
        if UpJntInput == 'Z':
            UpJnt = 'Z'
        #UpCheck
        if UpCheck == True:
            UpMinus = -1
        if UpCheck == False:
            UpMinus = 1
        #WorldUp
        if WorldUpJntInput == 'X':
            WorldUp = 'X'
        if WorldUpJntInput == 'Y':
            WorldUp = 'Y'
        if WorldUpJntInput == 'Z':
            WorldUp = 'Z'
        #WorldCheck
        if WorldCheck == True:
            WorldUpMinus = -1
        if WorldCheck == False:
            WorldUpMinus = 1

        if LRInput == 'Left':
            LR='L_'
        if LRInput == 'Right':
            LR='R_'

        if LR=='L_':
            lr='l'
        if LR=='R_':
            lr='r'

        AimV = ()
        UpV = ()
        WorldV = ()

        if AimMinus == 1:
            if AimJnt == 'X':
                AimV = (AimMinus,0,0)
            if AimJnt == 'Y':
                AimV = (0,AimMinus,0)
            if AimJnt == 'Z':
                AimV = (0,0,AimMinus)

        if AimMinus == -1:
            if AimJnt == 'X':
                AimV = (AimMinus,0,0)
            if AimJnt == 'Y':
                AimV = (0,AimMinus,0)
            if AimJnt == 'Z':
                AimV = (0,0,AimMinus)
                
        if UpMinus == 1:       
            if UpJnt == 'X':
                UpV = (AimMinus,0,0)
            if UpJnt == 'Y':
                UpV = (0,AimMinus,0)
            if UpJnt == 'Z':
                UpV = (0,0,AimMinus)
                
        if UpMinus == -1:       
            if UpJnt == 'X':
                UpV = (AimMinus,0,0)
            if UpJnt == 'Y':
                UpV = (0,AimMinus,0)
            if UpJnt == 'Z':
                UpV = (0,0,AimMinus)

        if WorldUpMinus == 1:
            if WorldUp == 'X':
                WorldV = (WorldUpMinus,0,0)
            if WorldUp == 'Y':
                WorldV = (0,WorldUpMinus,0)
            if WorldUp == 'Z':
                WorldV = (0,0,WorldUpMinus)
                
        if WorldUpMinus == -1:
            if WorldUp == 'X':
                WorldV = (WorldUpMinus,0,0)
            if WorldUp == 'Y':
                WorldV = (0,WorldUpMinus,0)
            if WorldUp == 'Z':
                WorldV = (0,0,WorldUpMinus)

        def empty():
            That=cmds.circle()
            cmds.delete(That)
            
        def parentThat(Kid,Mom):
            cmds.parent(Kid,Mom)

        def aimCon(OBJ,TGT,AimV,UpV,WorldV):
            AC=cmds.aimConstraint(TGT,OBJ,aim=AimV,u=UpV)
            #cmds.aimConstraint('l_Demo2_Jnt','l_Demo1_Jnt',aim=(1,0,0),u=(0,1,0),wu=(0,0,1))
            cmds.delete(AC)

        D1=cmds.joint(n=lr+'_'+Name+'1_Jnt')
        cmds.setAttr(D1+'.t',0,5,0)
        empty()

        D2=cmds.joint(n=lr+'_'+Name+'2_Jnt')
        cmds.setAttr(D2+'.t',0,3,0.5)
        empty()
        aimCon(OBJ=D1,TGT=D2,AimV=AimV,UpV=UpV,WorldV=WorldV)

        D3=cmds.joint(n=lr+'_'+Name+'3_Jnt')
        cmds.setAttr(D3+'.t',0,1,0)
        empty()
        aimCon(OBJ=D2,TGT=D3,AimV=AimV,UpV=UpV,WorldV=WorldV)

        D4=cmds.joint(n=lr+'_'+Name+'4_Jnt')
        cmds.setAttr(D4+'.t',0,0,1.3)
        empty()
        aimCon(OBJ=D3,TGT=D4,AimV=AimV,UpV=UpV,WorldV=WorldV)

        D5=cmds.joint(n=lr+'_'+Name+'5_Jnt')
        cmds.setAttr(D5+'.t',0,0,3)
        empty()
        aimCon(OBJ=D4,TGT=D5,AimV=AimV,UpV=UpV,WorldV=WorldV)

        parentThat(Kid=D5,Mom=D4)
        parentThat(Kid=D4,Mom=D3)
        parentThat(Kid=D3,Mom=D2)
        parentThat(Kid=D2,Mom=D1)

        COGCtrl=cmds.circle(n='COG'+Name+'_Ctrl')
        cmds.rotate( 90, 0, 0, r=True )
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        cmds.parent(D1,COGCtrl)
        if LR=='L_':
            cmds.setAttr('FootFKIK_Locator.tx',1.7)
            cmds.setAttr('FootFKIK_Locator.ty',5)
            cmds.parent('FootFKIK_Locator',COGCtrl)
            cmds.parent('LocaterRoot',COGCtrl)
            cmds.select(COGCtrl)
            cmds.move(3,0,0)
        if LR=='R_':
            cmds.setAttr('FootFKIK_Locator.tx',-1.7)
            cmds.setAttr('FootFKIK_Locator.ty',5)
            cmds.parent('FootFKIK_Locator',COGCtrl)
            cmds.parent('LocaterRoot',COGCtrl)
            cmds.select(COGCtrl)
            cmds.move(-3,0,0)

    def executeLeg (self,Name,LRInput,XYZInput,AimCheck,UpJntInput,UpCheck,WorldUpJntInput,WorldCheck,CtrlSizeLegInput,InGrpCheck,PoleVectorDis,RollToeAmp,RollAnkleAmp,RollHeelAmp,AutoCheck,floatStretchAmp):
        #Name Input
        ####Name=mc.textField('NameLegInput', q = True, tx = True)
        #LR Input
        ####LRInput= mc.radioCollection(LeftRightLegRadio, q = True, sl = True)

        if LRInput == 'Left':
            LR='L_'
        if LRInput == 'Right':
            LR='R_'
        
        #XYZ Input
        ####XYZInput= mc.radioCollection(XYZLegRadio, q = True, sl = True)
        if XYZInput == 'X':
            AimJnt = 'X'
        if XYZInput == 'Y':
            AimJnt = 'Y'
        if XYZInput == 'Z':
            AimJnt = 'Z'
        
        ####AimCheck=mc.checkBox('RevXYZLeg', query=True, value = True)
        if AimCheck == True:
            AimMinus = -1
        if AimCheck == False:
            AimMinus = 1
                
        ####UpJntInput = mc.radioCollection(UpJntLegRadio, q = True, sl = True)
        if UpJntInput == 'X':
            UpJnt = 'X'
        if UpJntInput == 'Y':
            UpJnt = 'Y'
        if UpJntInput == 'Z':
            UpJnt = 'Z'
        
        ####UpCheck=mc.checkBox('RevUpJntLeg', query=True, value = True)
        if UpCheck == True:
            UpMinus = -1
        if UpCheck == False:
            UpMinus = 1
        
        ####WorldUpJntInput = mc.radioCollection(WorldUpLegJntRadio, q = True, sl = True)
        if WorldUpJntInput == 'X':
            WorldUp = 'X'
        if WorldUpJntInput == 'Y':
            WorldUp = 'Y'
        if WorldUpJntInput == 'Z':
            WorldUp = 'Z'
        ####WorldCheck=mc.checkBox('RevWorldUpLeg', query=True, value = True)
        if WorldCheck == True:
            WorldUpMinus = -1
        if WorldCheck == False:
            WorldUpMinus = 1
        
        LCS = CtrlSizeLegInput
        ####ColorCode = cmds.textField('ColorInputLeg', q = True,tx = True) 
        
        ####InGrpCheck =mc.checkBox('InGrpLegRadio', query=True, value = True)
        if InGrpCheck == True:
            InGrp = 1
        if InGrpCheck == False:
            InGrp = 2
        
        ####PoleVectorDis=mc.floatField(PoleVectorDisLegInput, q = True, v = True) 
        ####RollToeAmp =mc.floatField(RollToeAmpInput, q = True, v = True)
        ####RollAnkleAmp =mc.floatField(RollAnkleAmpInput, q = True, v = True) 
        ####RollHeelAmp =mc.floatField(RollHeelAmpInput, q = True, v = True)  
            
        ####AutoCheck=mc.checkBox('AutoStrechLegRadio', query=True, value = True)
        if AutoCheck == True:
            AutoEnable = 1
        if AutoCheck == False:
            AutoEnable = 0 
        
        ####floatStretchAmp=cmds.floatField(AmpLegInput, query=True, value = True)
            
        
        FkLegList=[]
        IkLegList = []
        Color = []
        index = 1
        
            ####### Color #############
            
        if LR=='L_':
            Color = (1 , 0 , 0 )
        if LR=='R_':
            Color = (0 , 0 , 1 )

        
        def FK_IK_Leg ():
            mc.select() #Select hiracraccy after click
            selBack=mc.ls(sl=True)

            #cmds.parent(selBack,world=True)
            #cmds.parent('FootFKIK_Locator',world=True)
            #cmds.parent('LocaterRoot',world=True)
            #self.FindAndDelete(OBJName='COG'+Name+'_Ctrl')
            cmds.select(selBack)
            def DuplicateJLeg ():
                
                index = 1
            
                mc.select(hi=True) #Select hiracraccy after click
                BJointList=mc.ls(sl=True) #Select hilight as list
                
                #cmds.parent(BJointList[0],)
                FkJnt=cmds.duplicate(n = 'FK')
                IkJnt=cmds.duplicate(n = 'IK')
            
                for b in range (len(BJointList)):
                    convertindex = str(index)
                    cmds.select( FkJnt[b], r=True )
                    cmds.rename( LR+'FK_'+Name+convertindex+'_jnt' )
                    FkLegList.append( LR+'FK_'+Name+convertindex+'_jnt' )
                    cmds.select( IkJnt[b], r=True )
                    cmds.rename( LR+'IK_'+Name+convertindex+'_jnt' )
                    IkLegList.append( LR+'IK_'+Name+convertindex+'_jnt' )
                    index+=1
                cmds.setAttr(LR+'FK_'+Name+'1_jnt.visibility',0)
                cmds.setAttr(LR+'IK_'+Name+'1_jnt.visibility',0)
                
                def FK ():

                    E= len(FkLegList)-1
            
            
                    for i in range (E):
                        FkCtrl = cmds.circle( name=LR+'FK_'+Name+str(i+1)+'_ctrl', r=1.5)
                        cmds.color( FkCtrl , rgb = Color )
                        cmds.rotate( 0, 90, 0, r=True )
                        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                        cmds.scale( LCS, LCS, LCS )
                        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                        FkoffsetGrp=cmds.group(FkCtrl,name=LR+'FK_'+Name+str(i+1)+'_offset')
                        cmds.group(FkCtrl,name=LR+'FK_'+Name+str(i+1)+'_zero')
                        cmds.matchTransform(FkoffsetGrp,FkLegList[i])
                
                        if i > 0:
                            cmds.parent(LR+'FK_'+Name+str(i+1)+'_offset',LR+'FK_'+Name+str(i)+'_ctrl')
                        else:
                            pass
                
                        if InGrp == 1:
                            cmds.parent( FkLegList[i],FkCtrl)
                            
                    
                        elif InGrp == 2:
                            cmds.parentConstraint(FkCtrl, FkLegList[i],mo=1)
                            
                        else:
                            pass
                            
                    if InGrp == 1:
                        cmds.group(LR+'FK_'+Name+'1_offset',name=LR+'FK_'+Name+'_grp')
                    if InGrp == 2:
                        cmds.group(LR+'FK_'+Name+'1_offset',LR+'FK_'+Name+'1_jnt',name=LR+'FK_'+Name+'_grp')

                FK ()
                
                def IK ():
                    
                    IKLegCtrl=cmds.curve(p=self.Cube,d=1,n=LR+'IK_'+Name+'Leg_ctrl')
                    cmds.color( IKLegCtrl , rgb = Color )
                    cmds.rotate( 0, 0, 0, r=True )
                    cmds.scale(0.5,1.5,1.5)
                    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                    cmds.scale( LCS, LCS, LCS )
                    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                    offsetGrpLeg=cmds.group(IKLegCtrl,name=LR+'IK_'+Name+'Leg_offset')
                    cmds.group(IKLegCtrl,name=LR+'IK_'+Name+'Leg_zero')
                    cmds.matchTransform(offsetGrpLeg, IkLegList[0])
                    cmds.parentConstraint(IKLegCtrl,IkLegList[0],mo=1)
                    
                    #IKH
                    AnkleIKH=cmds.ikHandle( n=LR+Name+'Ankle_ikh', sj=IkLegList[0], ee=IkLegList[2], sol='ikRPsolver')
                    BallIKH=cmds.ikHandle( n=LR+Name+'Ball_ikh', sj=IkLegList[2], ee=IkLegList[3], sol='ikSCsolver' )
                    ToeIKH=cmds.ikHandle( n=LR+Name+'Toe_ikh', sj=IkLegList[3], ee=IkLegList[4], sol='ikSCsolver' )
                    AnkleIKH_GRP=cmds.group(LR+Name+'Ankle_ikh',name=LR+Name+'Ankle_ikh_Extra')
                    BallIKH_GRP=cmds.group(LR+Name+'Ball_ikh',name=LR+Name+'Ball_ikh_Extra')
                    ToeIKH_GRP=cmds.group(LR+Name+'Toe_ikh',name=LR+Name+'Toe_ikh_Extra')
                    
                    IKHLeg_grp=cmds.group(AnkleIKH_GRP,BallIKH_GRP,ToeIKH_GRP,name=LR+'IK_'+Name+'IKH_grp')
                    cmds.hide(IKHLeg_grp)
                    
                    IKFeetCtrl=cmds.curve(p=self.IKFoot,d=1,n=LR+'IK_'+Name+'Foot_ctrl')
                    cmds.color(IKFeetCtrl , rgb = Color )
                    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                    cmds.scale( LCS, LCS, LCS )
                    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                    offsetGrpFoot=cmds.group(em=True,name=LR+'IK_'+Name+'Foot_offset')
                    cmds.parent(IKFeetCtrl,offsetGrpFoot)
                    cmds.group(IKFeetCtrl,name=LR+'IK_'+Name+'Foot_zero')
                    cmds.matchTransform(offsetGrpFoot,IkLegList[2], position = 1)
                    
                    KneeCtrl=cmds.curve(p=self.PoleVec,d=1,n=LR+'IK_'+Name+'Knee_ctrl')
                    cmds.color( KneeCtrl , rgb = Color )
                    cmds.rotate( 90, 0, 0, r=True )
                    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                    cmds.scale( LCS, LCS, LCS )
                    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                    offsetGrpKnee=cmds.group( KneeCtrl,name=LR+'IK_'+Name+'Knee_offset')
                    zeroGrpKnee=cmds.group( KneeCtrl,name=LR+'IK_'+Name+'Knee_zero')
                    cmds.matchTransform(offsetGrpKnee, IkLegList[1],position=1)
                    
                    IkPoleDis=cmds.getAttr(offsetGrpKnee+'.translateZ')
                    IkPoleDisMinus= (IkPoleDis+PoleVectorDis)
                    cmds.setAttr(offsetGrpKnee+'.translateZ',IkPoleDisMinus)
                    Ikorient=cmds.orientConstraint(IkLegList[1],offsetGrpKnee,maintainOffset=0,skip="y")
                    cmds.delete(Ikorient)
                    
                    cmds.poleVectorConstraint( KneeCtrl, LR+Name+'Ankle_ikh' )
                    FollowAttr=cmds.addAttr(KneeCtrl,ln=LR+Name+'_Follow',minValue=0,maxValue=1,k=True)
                    
                    def FollowLocal ():
            
                        PoleAim=cmds.group(em=True,name=LR+'IK_Pole'+Name+'Aim')
                        PoleFollow=cmds.group(em=True,name=LR+'IK_Pole'+Name+'Follow')
                        LocalFol=cmds.group(em=True,name=LR+'IK_Local'+Name+'Follow')
                        LocalAim=cmds.group(em=True,name=LR+'Local'+Name+'Aim')
                    
                        cmds.matchTransform(PoleAim, IKLegCtrl)
                        cmds.matchTransform(PoleFollow, KneeCtrl)
                        cmds.matchTransform(LocalFol, KneeCtrl)
                        cmds.matchTransform(LocalAim, IKFeetCtrl)
                    
                        cmds.parentConstraint(IKFeetCtrl,LocalAim,maintainOffset =1)
                        cmds.pointConstraint(IKLegCtrl, PoleAim)
            
                        AimV = []
                        UpV = []
                        WorldV = []
            
                        if AimMinus == 1:
                            if AimJnt == 'X':
                                AimV = [AimMinus,0,0]
                            if AimJnt == 'Y':
                                AimV = [0,AimMinus,0]
                            if AimJnt == 'Z':
                                AimV = [0,0,AimMinus]

                        if AimMinus == -1:
                            if AimJnt == 'X':
                                AimV = [AimMinus,0,0]
                            if AimJnt == 'Y':
                                AimV = [0,AimMinus,0]
                            if AimJnt == 'Z':
                                AimV = [0,0,AimMinus]
                                
                        if UpMinus == 1:       
                            if UpJnt == 'X':
                                UpV = [AimMinus,0,0]
                            if UpJnt == 'Y':
                                UpV = [0,AimMinus,0]
                            if UpJnt == 'Z':
                                UpV = [0,0,AimMinus]
                                
                        if UpMinus == -1:       
                            if UpJnt == 'X':
                                UpV = [AimMinus,0,0]
                            if UpJnt == 'Y':
                                UpV = [0,AimMinus,0]
                            if UpJnt == 'Z':
                                UpV = [0,0,AimMinus]

                        if WorldUpMinus == 1:
                            if WorldUp == 'X':
                                WorldV = [WorldUpMinus,0,0]
                            if WorldUp == 'Y':
                                WorldV = [0,WorldUpMinus,0]
                            if WorldUp == 'Z':
                                WorldV = [0,0,WorldUpMinus]
                                
                        if WorldUpMinus == -1:
                            if WorldUp == 'X':
                                WorldV = [WorldUpMinus,0,0]
                            if WorldUp == 'Y':
                                WorldV = [0,WorldUpMinus,0]
                            if WorldUp == 'Z':
                                WorldV = [0,0,WorldUpMinus]
            
            
                        cmds.aimConstraint(IKFeetCtrl, PoleAim, aimVector = AimV,upVector = UpV , worldUpType = 'objectrotation',worldUpVector=WorldV , worldUpObject= LocalAim )
                        cmds.parentConstraint(PoleAim, PoleFollow,maintainOffset =1)
                        cmds.parentConstraint(PoleFollow, LocalFol,zeroGrpKnee,maintainOffset =1)
                        
                        #group,name = FollowParent
                        PoleFollowGrp=cmds.group(PoleAim,PoleFollow,LocalFol,LocalAim,n=LR+'IK_'+Name+'PoleFollow_grp')
                        
                        reverseFol=cmds.createNode('reverse', n=LR+Name+'reverseFol')
                        cmds.connectAttr(KneeCtrl+'.'+LR+Name+'_Follow',reverseFol+'.input.inputX')
                        
                        #print FollowParent+'.'+LR+'IK_Local'+Name+'FollowW1'
                        
                        cmds.connectAttr(LR+Name+'reverseFol.output.outputX',LR+'IK_'+Name+'Knee_zero_parentConstraint1.'+LR+'IK_Local'+Name+'FollowW1')
                        
                        cmds.connectAttr(KneeCtrl+'.'+LR+Name+'_Follow',LR+'IK_'+Name+'Knee_zero_parentConstraint1.'+LR+'IK_Pole'+Name+'FollowW0')
                    
                        
                    
                    FollowLocal ()
                    
                    
                    cmds.group(offsetGrpKnee,offsetGrpFoot,LR+'IK_'+Name+'IKH_grp',offsetGrpLeg,IkLegList[0],name=LR+'IK_'+Name+'Leg_grp')
                IK()
                
                def IKFootCtrl ():
                    footname=['RollToeEnd','RollHeel','RollAnkle','Toe','FootIn','FootOut']
                    for u in range (6):
                        if u < 4 :
                            Ikfootctrl=cmds.circle( name=LR+'IK_'+Name+footname[u]+'_ctrl', r=1)
                            cmds.color( Ikfootctrl , rgb = Color )
                            cmds.rotate( 0, 90, 0, r=True )
                            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                            cmds.scale( LCS, LCS, LCS )
                            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                            cmds.group(Ikfootctrl,name=LR+'IK_'+Name+footname[u]+'_offset')
                            cmds.group(Ikfootctrl,name=LR+'IK_'+Name+footname[u]+'_zero')
                            cmds.group(Ikfootctrl,name=LR+'IK_'+Name+footname[u]+'_Blend')
                        else:
                            Ikfootctrl=cmds.curve(p=self.ArrowH , name=LR+'IK_'+Name+footname[u]+'_ctrl', d=1)
                            cmds.color( Ikfootctrl , rgb = Color )
                            cmds.scale( LCS, LCS, LCS )
                            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                            
                            cmds.group(em=True,name=LR+'IK_'+Name+footname[u]+'_zero',a=True)
                            cmds.group(em=True,name=LR+'IK_'+Name+footname[u]+'_offset',a=True)
                            cmds.parent(Ikfootctrl,LR+'IK_'+Name+footname[u]+'_zero')
                            cmds.parent(LR+'IK_'+Name+footname[u]+'_zero',LR+'IK_'+Name+footname[u]+'_offset')
                    
                    
                    cmds.matchTransform(LR+'IK_'+Name+'RollToeEnd_offset', IkLegList[4],position=1)
                    cmds.matchTransform(LR+'IK_'+Name+'RollAnkle_offset', IkLegList[3],position=1)
                    cmds.matchTransform(LR+'IK_'+Name+'Toe_offset', IkLegList[3],position=1)
                    cmds.setAttr(LR+'IK_'+Name+'Toe_ctrl.rotateY',90)
                    cmds.select( LR+'IK_'+Name+'Toe_ctrl', r=True )
                    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                    
                    
                    if LR == 'L_':
                        cmds.matchTransform(LR+'IK_'+Name+'FootIn_offset','FootIn_Locator')
                        cmds.matchTransform(LR+'IK_'+Name+'FootOut_offset','FootOut_Locator')
                        cmds.setAttr(LR+'IK_'+Name+'FootIn_ctrl.rotateY',-90)
                        cmds.setAttr(LR+'IK_'+Name+'FootIn_ctrl.rotateX',90)
                        cmds.select( LR+'IK_'+Name+'FootIn_ctrl', r=True )
                        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                        cmds.setAttr(LR+'IK_'+Name+'FootOut_ctrl.rotateY',90)
                        cmds.setAttr(LR+'IK_'+Name+'FootOut_ctrl.rotateX',90)
                        cmds.select( LR+'IK_'+Name+'FootOut_ctrl', r=True )
                        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                            
                    if LR == 'R_':
                        cmds.matchTransform(LR+'IK_'+Name+'FootIn_offset','FootIn_Locator')
                        cmds.matchTransform(LR+'IK_'+Name+'FootOut_offset','FootOut_Locator')
                        cmds.setAttr(LR+'IK_'+Name+'FootIn_ctrl.rotateY',90)
                        cmds.setAttr(LR+'IK_'+Name+'FootIn_ctrl.rotateX',90)
                        cmds.select( LR+'IK_'+Name+'FootIn_ctrl', r=True )
                        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                        cmds.setAttr(LR+'IK_'+Name+'FootOut_ctrl.rotateY',-90)
                        cmds.setAttr(LR+'IK_'+Name+'FootOut_ctrl.rotateX',90)
                        cmds.select( LR+'IK_'+Name+'FootOut_ctrl', r=True )
                        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                    
                    cmds.matchTransform(LR+'IK_'+Name+'RollHeel_offset','Heel_Locator')
                    cmds.delete('FootIn_Locator','FootOut_Locator','Heel_Locator','LocaterRoot') 
                    
                    #Parenting Grp       
                    cmds.parent(LR+'IK_'+Name+'RollAnkle_offset',LR+'IK_'+Name+'FootIn_ctrl')
                    cmds.parent(LR+'IK_'+Name+'Toe_offset',LR+'IK_'+Name+'FootIn_ctrl')
                    cmds.parent(LR+'IK_'+Name+'FootIn_offset',LR+'IK_'+Name+'FootOut_ctrl')
                    cmds.parent(LR+'IK_'+Name+'FootOut_offset',LR+'IK_'+Name+'RollHeel_ctrl')
                    cmds.parent(LR+'IK_'+Name+'RollHeel_offset',LR+'IK_'+Name+'RollToeEnd_ctrl')
                    cmds.parent(LR+'IK_'+Name+'RollToeEnd_offset',LR+'IK_'+Name+'Foot_ctrl')
                    
                    
                    #IKH_Grp
                    Ankle_grp=cmds.group(em=True,n=LR+Name+'Ankle_grp')
                    Ball_grp=cmds.group(em=True,n=LR+Name+'Ball_grp')
                    Toe_grp=cmds.group(em=True,n=LR+Name+'Toe_grp')
                    cmds.matchTransform(Ankle_grp,LR+Name+'Ankle_ikh')
                    cmds.matchTransform(Ball_grp,LR+Name+'Ball_ikh')
                    cmds.matchTransform(Toe_grp,LR+Name+'Toe_ikh')
                    cmds.parentConstraint(Ankle_grp,LR+Name+'Ankle_ikh_Extra',mo=1)
                    cmds.parentConstraint(Ball_grp,LR+Name+'Ball_ikh_Extra',mo=1)
                    cmds.parentConstraint(Toe_grp,LR+Name+'Toe_ikh_Extra',mo=1)
                    
                    cmds.parent(Ankle_grp,LR+'IK_'+Name+'RollAnkle_ctrl')
                    cmds.parent(Ball_grp,LR+'IK_'+Name+'RollAnkle_ctrl')
                    cmds.parent(Toe_grp,LR+'IK_'+Name+'Toe_ctrl')
                    
                    #Limit Trans
                    cmds.transformLimits(LR+'IK_'+Name+'FootOut_ctrl',rz=(-1,0),erz=(False,True))
                    cmds.transformLimits(LR+'IK_'+Name+'FootOut_zero',rz=(-1,0),erz=(False,True))
                    cmds.transformLimits(LR+'IK_'+Name+'FootIn_ctrl',rz=(0,0),erz=(True,False))
                    cmds.transformLimits(LR+'IK_'+Name+'FootIn_zero',rz=(0,0),erz=(True,False))
                IKFootCtrl ()  
                def FootAttr ():
                    
                    cmds.select(LR+'IK_'+Name+'Foot_ctrl')
                    cmds.addAttr(ln='Foot_Controller',attributeType='enum',k=True,enumName='---------------')
                    cmds.setAttr(LR+'IK_'+Name+'Foot_ctrl.Foot_Controller',lock=True)
                    HeelRollAttr=cmds.addAttr(ln='Heel_Roll',attributeType='float',k=True)
                    ToeRollAttr=cmds.addAttr(ln='Toe_Roll',attributeType='float',k=True)
                    BallRollAttr=cmds.addAttr(ln='Ball_Roll',attributeType='float',k=True)
                    HeelTwistAttr=cmds.addAttr(ln='Heel_Twist',attributeType='float',k=True)
                    ToeTwistAttr=cmds.addAttr(ln='Toe_Twist',attributeType='float',k=True)
                    FootRockAttr=cmds.addAttr(ln='Foot_Rock',attributeType='float',k=True)
                    ToeBlendAttr=cmds.addAttr(ln='Toe_Blend',attributeType='float',k=True)
                    FootBlendAttr=cmds.addAttr(ln='Foot_Blend',attributeType='float', minValue=-10, maxValue=10,k=True)
                    
                    
                    cmds.connectAttr( LR+'IK_'+Name+'Foot_ctrl.Heel_Roll' , LR+'IK_'+Name+'RollHeel_zero.rotate.rotate'+AimJnt)
                    #Result: Connected L_IK_LegAFoot_ctrl.Heel_Roll to L_IK_LegARollHeel_zero.rotate.rotateX.
                    cmds.connectAttr( LR+'IK_'+Name+'Foot_ctrl.Toe_Roll' , LR+'IK_'+Name+'RollToeEnd_zero.rotate.rotate'+AimJnt)
                    #Result: Connected L_IK_LegAFoot_ctrl.Toe_Roll to L_IK_LegARollToeEnd_zero.rotate.rotateX. //
                    cmds.connectAttr( LR+'IK_'+Name+'Foot_ctrl.Ball_Roll' , LR+'IK_'+Name+'RollAnkle_zero.rotate.rotate'+AimJnt)
                    #Result: Connected L_IK_LegAFoot_ctrl.Ball_Roll to L_IK_LegARollAnkle_zero.rotate.rotateX. //
                    cmds.connectAttr( LR+'IK_'+Name+'Foot_ctrl.Heel_Twist' , LR+'IK_'+Name+'RollHeel_zero.rotate.rotate'+UpJnt)
                    #Result: Connected L_IK_LegAFoot_ctrl.Heel_Twist to L_IK_LegARollHeel_zero.rotate.rotateY. //
                    cmds.connectAttr( LR+'IK_'+Name+'Foot_ctrl.Toe_Twist' , LR+'IK_'+Name+'RollToeEnd_zero.rotate.rotate'+UpJnt)
                    #Result: Connected L_IK_LegAFoot_ctrl.Toe_Twist to L_IK_LegARollToeEnd_zero.rotate.rotateY. //
                    cmds.connectAttr( LR+'IK_'+Name+'Foot_ctrl.Foot_Rock' , LR+'IK_'+Name+'FootOut_zero.rotate.rotateZ')
                    cmds.connectAttr( LR+'IK_'+Name+'Foot_ctrl.Foot_Rock' , LR+'IK_'+Name+'FootIn_zero.rotate.rotateZ')
                    #Result: Connected L_IK_LegAFoot_ctrl.Foot_Rock to L_IK_LegAFootOut_zero.rotate.rotateZ. //
                    #Result: Connected L_IK_LegAFoot_ctrl.Foot_Rock to L_IK_LegAFootIn_zero.rotate.rotateZ. //
                    cmds.connectAttr( LR+'IK_'+Name+'Foot_ctrl.Toe_Blend' , LR+'IK_'+Name+'Toe_zero.rotate.rotate'+AimJnt)
                    #Result: Connected L_IK_LegAFoot_ctrl.Toe_Twist to L_IK_LegAToe_zero.rotate.rotateX. //
                
                FootAttr ()
                def FootBlend():
                    
                    MultMinusFootBlend=cmds.createNode('multDoubleLinear')
                    cmds.setAttr(MultMinusFootBlend+'.input2',-1)
                    RangeFootBlend=cmds.createNode('setRange')
                    cmds.connectAttr( LR+'IK_'+Name+'Foot_ctrl.Foot_Blend' , RangeFootBlend+'.value.valueX')
                    cmds.connectAttr( LR+'IK_'+Name+'Foot_ctrl.Foot_Blend' , RangeFootBlend+'.value.valueY')
                    cmds.connectAttr( LR+'IK_'+Name+'Foot_ctrl.Foot_Blend' , MultMinusFootBlend+'.input1')
                    cmds.connectAttr(MultMinusFootBlend+'.output' , RangeFootBlend+'.value.valueZ')
                    
                    cmds.setAttr(RangeFootBlend+'.maxX',RollAnkleAmp)
                    cmds.setAttr(RangeFootBlend+'.oldMaxX',5)
                    cmds.setAttr(RangeFootBlend+'.maxY',RollToeAmp)
                    cmds.setAttr(RangeFootBlend+'.oldMinY',5)
                    cmds.setAttr(RangeFootBlend+'.oldMaxY',10)
                    cmds.setAttr(RangeFootBlend+'.maxZ',RollHeelAmp)
                    cmds.setAttr(RangeFootBlend+'.oldMaxZ',10)
                    
                    MultOutRange1=cmds.createNode('multDoubleLinear')
                    cmds.setAttr(MultOutRange1+'.input2',1)
                    UnitOutRange1=cmds.createNode('unitConversion')
                    cmds.setAttr(UnitOutRange1+'.conversionFactor',0.017)
                    cmds.connectAttr( RangeFootBlend+'.outValue.outValueX' , MultOutRange1+'.input1')
                    cmds.connectAttr( MultOutRange1+'.output' ,  UnitOutRange1+'.input')
                    cmds.connectAttr( UnitOutRange1+'.output' , LR+'IK_'+Name+'RollAnkle_Blend.rotate'+AimJnt)
                    
                    MultOutRange2=cmds.createNode('multDoubleLinear')
                    cmds.setAttr(MultOutRange2+'.input2',1)
                    UnitOutRange2=cmds.createNode('unitConversion')
                    cmds.setAttr(UnitOutRange2+'.conversionFactor',0.017)
                    cmds.connectAttr( RangeFootBlend+'.outValue.outValueY' , MultOutRange2+'.input1')
                    cmds.connectAttr( MultOutRange2+'.output' ,  UnitOutRange2+'.input')
                    cmds.connectAttr( UnitOutRange2+'.output' , LR+'IK_'+Name+'RollToeEnd_Blend.rotate'+AimJnt)
                    
                    MultOutRange3=cmds.createNode('multDoubleLinear')
                    cmds.setAttr(MultOutRange3+'.input2',-1)
                    UnitOutRange3=cmds.createNode('unitConversion')
                    cmds.setAttr(UnitOutRange3+'.conversionFactor',0.017)
                    cmds.connectAttr( RangeFootBlend+'.outValue.outValueZ' , MultOutRange3+'.input1')
                    cmds.connectAttr( MultOutRange3+'.output' ,  UnitOutRange3+'.input')
                    cmds.connectAttr( UnitOutRange3+'.output' , LR+'IK_'+Name+'RollHeel_Blend.rotate'+AimJnt)
                FootBlend()
                
                def FKIK_Switch ():
                    
                    for t in range (len(BJointList)):
                        cmds.parentConstraint(FkLegList[t],IkLegList[t],BJointList[t],mo=1)
                    
                    
                    FKIKSwitch = cmds.curve(p=self.Plus,d=1,n=LR+Name+'FkIk_Switch')
                    cmds.rotate( 90, 0, 0, r=True )
                    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                    cmds.scale( (CtrlSizeLegInput/2),(CtrlSizeLegInput/2), (CtrlSizeLegInput/2) )
                    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                    cmds.color( FKIKSwitch , rgb = Color )
                    cmds.addAttr(FKIKSwitch,ln=LR+Name+'Fk_IK_Blend',minValue=0,maxValue=10,k=True)
                    cmds.group(FKIKSwitch,name=LR+Name+'FK_IK_Switch_zero')
                    SwitchoffsetGrp=cmds.group(LR+Name+'FK_IK_Switch_zero',name=LR+Name+'FK_IK_Switch_offset')
                    
                    cmds.matchTransform(LR+Name+'FK_IK_Switch_offset', 'FootFKIK_Locator') 
                    cmds.delete ('FootFKIK_Locator')
                    uniConFKIKSwitch=cmds.createNode('unitConversion')
                    cmds.connectAttr(FKIKSwitch+'.'+LR+Name+'Fk_IK_Blend',uniConFKIKSwitch+'.input')
                    cmds.setAttr( uniConFKIKSwitch+'.conversionFactor', 0.1 )
                    
                    ReverFKIKSwitch1=cmds.createNode('reverse')
                    cmds.connectAttr(uniConFKIKSwitch+'.output',ReverFKIKSwitch1+'.input.inputX')
                    cmds.connectAttr(uniConFKIKSwitch+'.output',ReverFKIKSwitch1+'.input.inputY')
                    cmds.connectAttr(uniConFKIKSwitch+'.output',ReverFKIKSwitch1+'.input.inputZ')
                    
                    ReverFKIKSwitch2=cmds.createNode('reverse')
                    cmds.connectAttr(uniConFKIKSwitch+'.output',ReverFKIKSwitch2+'.input.inputX')
                    cmds.connectAttr(uniConFKIKSwitch+'.output',ReverFKIKSwitch2+'.input.inputY')
                    
                    
                    XYZXY = ['X','Y','Z','X','Y']
                    for o in range (5):
                        cmds.connectAttr(ReverFKIKSwitch1+'.output.output'+XYZXY[o], BJointList[o]+'_parentConstraint1.'+LR+'FK_'+Name+str(o+1)+'_jntW0')
                        cmds.connectAttr(uniConFKIKSwitch+'.output',BJointList[o]+'_parentConstraint1.'+LR+'IK_'+Name+str(o+1)+'_jntW1')
                    
                    revCtrlVis=cmds.createNode('reverse')
                    cmds.connectAttr(uniConFKIKSwitch+'.output',revCtrlVis+'.input.inputX')    
                    cmds.connectAttr(revCtrlVis+'.output.outputX', LR+'FK_'+Name+'_grp.visibility')
                    cmds.connectAttr(uniConFKIKSwitch+'.output', LR+'IK_'+Name+'Leg_grp.visibility')
                    
                    cmds.group(LR+'FK_'+Name+'_grp',LR+'IK_'+Name+'Leg_grp',SwitchoffsetGrp,name=LR+Name+'Leg_grp')
                    
                FKIK_Switch()

                def AutoSwitch():
                    if AutoEnable == 1:
                        #Ruler
                        ruler1=cmds.circle(n='Locator1')
                        cmds.matchTransform('Locator1',BJointList[0])
                        joint1X = cmds.getAttr('Locator1.translateX')
                        joint1Y = cmds.getAttr('Locator1.translateY')
                        joint1Z = cmds.getAttr('Locator1.translateZ')
                        
                        ruler2=cmds.circle(n='Locator2')
                        cmds.matchTransform('Locator2',BJointList[1])
                        joint2X = cmds.getAttr('Locator2.translateX')
                        joint2Y = cmds.getAttr('Locator2.translateY')
                        joint2Z = cmds.getAttr('Locator2.translateZ')
                        
                        ruler3=cmds.circle(n='Locator3')
                        cmds.matchTransform('Locator3',BJointList[2])
                        joint3X = cmds.getAttr('Locator3.translateX')
                        joint3Y = cmds.getAttr('Locator3.translateY')
                        joint3Z = cmds.getAttr('Locator3.translateZ')

                        joint1Location = (joint1X,joint1Y,joint1Z)
                        joint2Location = (joint2X,joint2Y,joint2Z)
                        joint3Location = (joint3X,joint3Y,joint3Z)

                        DistanDimen1=cmds.distanceDimension( sp=joint1Location, ep=joint2Location )
                        DistanDimen2=cmds.distanceDimension( sp=joint2Location, ep=joint3Location )
                        DistanDimen3=cmds.distanceDimension( sp=joint1Location, ep=joint3Location )
                        
                        #Vaule
                        
                        floatDistanceUp=cmds.getAttr(DistanDimen1+'.distance')
                        floatDistanceDown=cmds.getAttr(DistanDimen2+'.distance')
                        floatDistanceAll=cmds.getAttr(DistanDimen3+'.distance')
                        
                        RulerGrp=cmds.group(ruler1,ruler2,ruler3,DistanDimen1,DistanDimen2,DistanDimen3,'locator1','locator2','locator3',name='ruler_grp')
                        cmds.delete(RulerGrp)
                        
                        index =[]
                        CtrlIK = LR+'IK_'+Name+'Foot_ctrl'
                        CtrlPole = LR+'IK_'+Name+'Knee_ctrl'
                        DistanceUp = LR+'IK_'+Name+'Leg_ctrl'
                        DistanceDown = LR+'IK_'+Name+'Foot_ctrl'
                        DistancePole = LR+'IK_'+Name+'Knee_ctrl'
                        JointStretch1 = LR+'IK_'+Name+'2_jnt'
                        JointStretch2 = LR+'IK_'+Name+'3_jnt'
                        
                        oneDividedTop = 1/floatDistanceUp
                        oneDividedDown = 1/floatDistanceDown
                        
                
                        TopGrpName = LR+Name+'_AutoUp_grp'
                        DownGrpName = LR+Name+'_AutoDown_grp'
                        PoleGrpName = LR+Name+'_AutoPole_grp'
                        
                        #AddAttr
                        cmds.addAttr(CtrlIK,ln='Auto',attributeType='enum',k=True,enumName='---------------')
                        cmds.setAttr(CtrlIK+'.Auto',lock=True)
                        cmds.addAttr(CtrlIK,ln='St_Up',k=True,at='float')
                        cmds.addAttr(CtrlIK,ln='St_Down',k=True,at='float')
                        cmds.addAttr(CtrlIK,ln='Auto_Stretch',k=True,at='float',minValue=0,maxValue=10)
                        cmds.addAttr(CtrlPole,ln='PoleVector_Lock',minValue=0,maxValue=10,k=True)
                        
                        #MultAmpTop
                        MultAmpTop1=cmds.createNode('multDoubleLinear')
                        cmds.addAttr(MultAmpTop1,ln='Amp',k=True)
                        cmds.setAttr( MultAmpTop1+'.Amp', floatStretchAmp )
                        cmds.connectAttr(MultAmpTop1+'.Amp',MultAmpTop1+'.input1') 
                        cmds.connectAttr(CtrlIK+'.St_Up',MultAmpTop1+'.input2')
                        
                        #MultTop
                        MultTop=cmds.createNode('multDoubleLinear')
                        cmds.setAttr( MultTop+'.input2', floatDistanceUp)
                        cmds.connectAttr(MultAmpTop1+'.output',MultTop+'.input1')
                    
                        #MultAmpBot
                        MultAmpBot1=cmds.createNode('multDoubleLinear')
                        cmds.addAttr(MultAmpBot1,ln='Amp',k=True)
                        cmds.setAttr( MultAmpBot1+'.Amp', floatStretchAmp )
                        cmds.connectAttr(MultAmpBot1+'.Amp',MultAmpBot1+'.input1')
                        
                        cmds.connectAttr(CtrlIK+'.St_Down',MultAmpBot1+'.input2')
                        
                        #MultBot
                        MultBot=cmds.createNode('multDoubleLinear')
                        cmds.setAttr( MultBot+'.input2', floatDistanceDown)
                        cmds.connectAttr(MultAmpBot1+'.output',MultBot+'.input1')
                        
                        #DistanTopDown
                        UpGrp=cmds.group( em=True, name=TopGrpName)
                        DownGrp=cmds.group( em=True, name=DownGrpName)
                        
                        cmds.pointConstraint(DistanceUp,UpGrp)
                        cmds.pointConstraint(CtrlIK,DownGrp)      
                        
                        DisUpDown=cmds.createNode('distanceBetween')
                        cmds.connectAttr(UpGrp+'.t',DisUpDown+'.point1')
                        cmds.connectAttr(DownGrp+'.t',DisUpDown+'.point2')
                        
                        MultTotalTD=cmds.createNode('multDoubleLinear')
                        cmds.connectAttr(DisUpDown+'.distance',MultTotalTD+'.input2')
                        DisupDownDi=cmds.getAttr(MultTotalTD+'.input2')
                        cmds.setAttr(MultTotalTD+'.input1',1/DisupDownDi)
                        
                        #Condition
                        Condi=cmds.createNode('condition')
                        cmds.connectAttr(MultTotalTD+'.output',Condi+'.colorIfTrue.colorIfTrueR')
                        cmds.connectAttr(DisUpDown+'.distance',Condi+'.firstTerm')
                        cmds.setAttr(Condi+".secondTerm",floatDistanceAll)
                        cmds.setAttr(Condi+".operation",2)
                        
                        #ConOut MultTop
                        MultConTop=cmds.createNode('multDoubleLinear')
                        cmds.connectAttr(Condi+'.outColor.outColorR',MultConTop+'.input1')
                        cmds.setAttr(MultConTop+".input2",floatDistanceUp)
                        
                        #BlendTop
                        BlendMultTop=cmds.createNode('blendTwoAttr')
                        cmds.addAttr(BlendMultTop,ln='DEF',k=True)
                        cmds.setAttr(BlendMultTop+".DEF",floatDistanceUp)
                        cmds.connectAttr(BlendMultTop+'.DEF',BlendMultTop+'.input[0]')
                        cmds.connectAttr(MultConTop+'.output',BlendMultTop+'.input[1]')
        
                        #ConOut MultDown
                        MultConDown=cmds.createNode('multDoubleLinear')
                        cmds.connectAttr(Condi+'.outColor.outColorR',MultConDown+'.input1')
                        cmds.setAttr(MultConDown+".input2",floatDistanceDown)
                        
                        #BlendDown
                        BlendMultDown=cmds.createNode('blendTwoAttr')
                        cmds.addAttr(BlendMultDown,ln='DEF',k=True)
                        cmds.setAttr(BlendMultDown+".DEF",floatDistanceDown)
                        cmds.connectAttr(BlendMultDown+'.DEF',BlendMultDown+'.input[0]')
                        cmds.connectAttr(MultConDown+'.output',BlendMultDown+'.input[1]')
                        
                        #UniConverAuto
                        UniConAuto=cmds.createNode('unitConversion')
                        cmds.setAttr(UniConAuto+".conversionFactor",0.1)
                        cmds.connectAttr(CtrlIK+'.Auto_Stretch',UniConAuto+'.input')
                        cmds.connectAttr(UniConAuto+'.output', BlendMultTop+'.attributesBlender')
                        cmds.connectAttr(UniConAuto+'.output',BlendMultDown+'.attributesBlender')
                        
                        #addDoubleLinear
                        DoubTop=cmds.createNode('addDoubleLinear')
                        cmds.connectAttr( BlendMultTop+'.output', DoubTop+'.input1')
                        cmds.connectAttr(MultTop+'.output',DoubTop+'.input2')
                        
                        DoubDown=cmds.createNode('addDoubleLinear')     
                        cmds.connectAttr(BlendMultDown+'.output',DoubDown+'.input1')
                        cmds.connectAttr(MultBot+'.output',DoubDown+'.input2')
                        
                        #PolevectorStart
                        PoleGrp=cmds.group( em=True, name=PoleGrpName)
                        cmds.pointConstraint(CtrlPole,PoleGrp)
                        
                        #Polevector+Top
                        DisUpPole=cmds.createNode('distanceBetween')
                        cmds.connectAttr(PoleGrp+'.t',DisUpPole+'.point1')
                        cmds.connectAttr( UpGrp+'.t',DisUpPole+'.point2')
                        
                        MultDiviTop=cmds.createNode('multDoubleLinear')
                        cmds.connectAttr(DisUpPole+'.distance',MultDiviTop+'.input1')
                        cmds.setAttr(MultDiviTop+".input2",oneDividedTop)
                        
                        MultLinTop=cmds.createNode('multDoubleLinear')
                        cmds.connectAttr(MultDiviTop+'.output',MultLinTop+'.input1')
                        cmds.setAttr(MultLinTop+".input2",floatDistanceUp)
                        
                        #Polevector+Down
                        DisDownPole=cmds.createNode('distanceBetween')
                        cmds.connectAttr(PoleGrp+'.t',DisDownPole+'.point1')
                        cmds.connectAttr(DownGrp+'.t',DisDownPole+'.point2')
                        
                        MultDiviDown=cmds.createNode('multDoubleLinear')
                        cmds.connectAttr(DisDownPole+'.distance',MultDiviDown+'.input1')
                        cmds.setAttr(MultDiviDown+".input2",oneDividedDown)
                        
                        MultLinDown=cmds.createNode('multDoubleLinear')
                        cmds.connectAttr(MultDiviDown+'.output',MultLinDown+'.input1')
                        cmds.setAttr(MultLinDown+".input2",floatDistanceDown)
                        
                        #LastBlendtwoAttr
                        BlendAttrTop=cmds.createNode('blendTwoAttr')
                        cmds.connectAttr(DoubTop+'.output',BlendAttrTop+'.input[0]')
                        cmds.connectAttr(MultLinTop+'.output',BlendAttrTop+'.input[1]')
                        
                        BlendAttrDown=cmds.createNode('blendTwoAttr')
                        cmds.connectAttr(DoubDown+'.output',BlendAttrDown+'.input[0]')
                        cmds.connectAttr(MultLinDown+'.output',BlendAttrDown+'.input[1]')
                        
                        ConPoleBlend=cmds.createNode('unitConversion', n='unitConversion')
                        cmds.connectAttr(CtrlPole+'.PoleVector_Lock',ConPoleBlend+'.input')
                        cmds.setAttr(ConPoleBlend+'.conversionFactor',0.1)
                        
                        cmds.connectAttr(ConPoleBlend+'.output',BlendAttrTop+'.attributesBlender')
                        cmds.connectAttr(ConPoleBlend+'.output',BlendAttrDown+'.attributesBlender')
                        
                        if AimMinus == 1:
                            cmds.connectAttr(BlendAttrTop+'.output',JointStretch1+'.translate'+AimJnt)
                            cmds.connectAttr(BlendAttrDown+'.output',JointStretch2+'.translate'+AimJnt)
                            
                        elif AimMinus == -1:
                            
                            NegaMult1=cmds.createNode('multDoubleLinear')
                            cmds.setAttr(NegaMult1+".input2",-1)
                            cmds.connectAttr(BlendAttrTop+'.output',NegaMult1+'.input1')
                            cmds.connectAttr(NegaMult1+'.output',JointStretch1+'.translate'+AimJnt)
                            
                            NegaMult2=cmds.createNode('multDoubleLinear')
                            cmds.setAttr(NegaMult2+".input2",-1)
                            cmds.connectAttr(BlendAttrDown+'.output',NegaMult2+'.input1')
                            cmds.connectAttr(NegaMult2+'.output',JointStretch2+'.translate'+AimJnt)
                            
                        else:
                            print ('error')
                            
                        cmds.group(UpGrp,DownGrp,PoleGrp,name=LR+Name+'IKAuto_grp')
                        cmds.parent(LR+Name+'IKAuto_grp',LR+'IK_'+Name+'Leg_grp')
                    else:
                        pass
                
                AutoSwitch()    
            DuplicateJLeg ()  
        FK_IK_Leg ()

