import bge
import sys
import nnetga
import imp
from random import random
from time import clock
from math import pi
from random import random
import plotly
from plotly.graph_objs import Scatter, Layout
import os.path
import csv

if not os.path.exists("/home/adri/Downloads/blender_cleaned/cost_function.html"): 
    plotly.offline.plot({
        "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
        "layout": Layout(title="hello world")
    }, filename ='cost_function.html', auto_open=False,)

def draw_chart(note):
    with open("scores_generation.dat", "a") as myfile:
            myfile.write(note)
    draw()

def draw():
    print("Inside draw function")
    gen = []
    score = []
    f2 = open('scores_generation.dat', 'r')
    # read the whole file into a single variable, which is a list of every row of the file.
    lines = f2.readlines()
    f2.close()
    for line in lines:
        p = line.split()
        score.append(float(p[0]))
        gen.append(float(p[1]))

    plotly.offline.plot({
        "data": [Scatter(x=gen, y=score)],
        "layout": Layout(title="Cost function")
    }, filename ='cost_function.html', auto_open=False,
    )

class Body:
    def __init__(self,scene,spawner,offset,cnsType,ShoulderXMin,ShoulderXMax,ElbowXMin,ElbowXMax):
        self.scene=scene
        self.spawner=spawner
        self.offset=offset
        self.cnsType=cnsType
        self.ShoulderXMin=ShoulderXMin
        self.ShoulderXMax=ShoulderXMax
        self.ElbowXMin=ElbowXMin
        self.ElbowXMax=ElbowXMax

    def create_joint(self,i,leg,leg_name,connection,params):
        self.spawner.worldTransform = self.scene.objectsInactive[leg_name].worldTransform
        self.spawner.worldOrientation = self.scene.objectsInactive[leg_name].worldOrientation
        self.spawner.worldPosition.x += self.offset
        leg_logic = getattr(bge.logic, leg_name)
        leg_logic[i] = self.scene.addObject(leg,self.spawner,0)
        connect_pt1 = getattr(bge.logic,connection[0])
        connect_pt2 = getattr(bge.logic,connection[1])
        physics_id_1 = connect_pt1[i].getPhysicsId()
        physics_id_2 = connect_pt2[i].getPhysicsId()
        cnsPos = self.spawner.worldPosition
        cns = bge.constraints.createConstraint(physics_id_1, physics_id_2,self.cnsType,cnsPos.x - self.offset - params[0],cnsPos.y + params[1],cnsPos.z - 1,1.0,0,0)
        cns.setParam(3, self.ShoulderXMin, self.ShoulderXMax)
        cns.setParam(4, 0.0, 0.0)
        cns.setParam(5, 0.0, 0.0)
        bge.logic.cnstrnt[i].append(cns)

def run():    
    scene = bge.logic.getCurrentScene()
#    nnetga.info() 
#    nnetga.info_pop()
    #for objs in scene.objects:
        #print(objs.name)
        
    #for objs in scene.objectsInactive:
        #print(objs.name)
    
    #obj1 = scene.objectsInactive['Cube']
    #obj2 = scene.objectsInactive['Cylinder']
    timer = scene.objects['timer']
    
    #print('step 0')
    
    if timer.localPosition.y < 0.0:
        #imp.reload(nnetga)
        print("Start------------------")
        bge.logic.agentNum = 40

#--------------------------------------------------------------        
        nnetga.add_pop(1,0.7,0.3,0.25)

        #Description:
        # nnetga.add_pop(numbers of population to add,
        #                crossover chance (0.0 to 1.0, default 0.7),
        #                mutation rate(0 to 1.0, default 0.3),
        #                mutation ratio(0.0 to 1.0, default 0.3)): 
        # Set new population with options of crossover , mutation rate and ratio.

#--------------------------------------------------------------        
        nnetga.add_agent(0,bge.logic.agentNum)

       #Description:
       #  nnetga.add_agent(population index,numbers of agent to add): 
       # Populate with agent the population with the given index.

#--------------------------------------------------------------        
        nnetga.add_net(0,30,2,24,8)

       #Description:
       # nnetga.add_net(population index,
       #                numbers of inputs,
       #                numbers of hidden layers,
       #                numbers of neurons in hidden layers,
       #                numbers of ouput): 
       # To add neural net on each agent of the given population index.

#--------------------------------------------------------------        

        bge.logic.cframe = 0
        bge.logic.body = [0] * (bge.logic.agentNum)
        bge.logic.legFR1 = [0] * (bge.logic.agentNum)
        bge.logic.legFR2 = [0] * (bge.logic.agentNum)
        bge.logic.legFL1 = [0] * (bge.logic.agentNum)
        bge.logic.legFL2 = [0] * (bge.logic.agentNum )
        bge.logic.legRR1 = [0] * (bge.logic.agentNum)
        bge.logic.legRR2 = [0] * (bge.logic.agentNum)
        bge.logic.legRL1 = [0] * (bge.logic.agentNum)
        bge.logic.legRL2 = [0] * (bge.logic.agentNum)
        #bge.logic.all.append([bge.logic.legFR1,bge.logic.legFR2,bge.logic.legFL1,bge.logic.legFL2,bge.logic.legRR1,bge.logic.legRR2,bge.logic.legRL1,bge.logic.legRL2])
        bge.logic.hiscore = 0
        bge.logic.hiaverage = 0
        bge.logic.avrgList = []
        timer.localPosition.y = 1.0
        bge.logic.cnstrnt = [0] * (bge.logic.agentNum)
        bge.logic.generation = 0
        bge.logic.alldead = -1
        timer.localPosition.y = 0.0
    
        
    #print(timer.localPosition.y)    
    if timer.localPosition.y < 1.0:
        #print("Create")
        bge.logic.scores = [0] * (bge.logic.agentNum)
        bge.logic.farPosition = [0] * (bge.logic.agentNum)
        body = scene.objectsInactive['body']
        legFL1 = scene.objectsInactive['legFL1']
        legFL2 = scene.objectsInactive['legFL2']
        legFR1 = scene.objectsInactive['legFR1']
        legFR2 = scene.objectsInactive['legFR2']
        legRL1 = scene.objectsInactive['legRL1']
        legRL2 = scene.objectsInactive['legRL2']
        legRR1 = scene.objectsInactive['legRR1']
        legRR2 = scene.objectsInactive['legRR2']
        spawner = scene.objects['spawner']


#-------------------Creat agents (quadrupedes) and put them in a line one by one--------------------------#

        for i in range(bge.logic.agentNum):

            #-------Set parameters ranges for arms------------#
            bge.logic.cnstrnt[i] = []
            offset = i * 9
            cnsType = 12  #constraint type set to 6DOF (g degree of freedom)
            ShoulderXMin = -1.0
            ShoulderXMax = 0.7
            ElbowXMin = -1.0
            ElbowXMax = 0.0

#-------------------Create body---------------------------------------------------------------------------#

            spawner.worldPosition = scene.objectsInactive['body'].worldPosition
            spawner.worldOrientation = scene.objectsInactive['body'].worldOrientation
            spawner.worldPosition.x += offset
            bge.logic.body[i] = scene.addObject(body,spawner,0)

#-------------------Create joints-------------------------------------------------------------------------#
            
            body_class = Body(scene,spawner,offset,cnsType,ShoulderXMin,ShoulderXMax,ElbowXMin,ElbowXMax)
            body_class.create_joint(i,legFL1,'legFL1',['body','legFL1'],[0,1.4])
            body_class.create_joint(i,legFL2,'legFL2',['legFL1','legFL2'],[-1.8,4.3])
            body_class.create_joint(i,legFR1,'legFR1',['body','legFR1'],[0,-1.4])
            body_class.create_joint(i,legFR2,'legFR2',['legFR1','legFR2'],[-1.8,-6.15])
            body_class.create_joint(i,legRL1,'legRL1',['body','legRL1'],[0,1.4])
            body_class.create_joint(i,legRL2,'legRL2',['legRL1','legRL2'],[1.8,4.3])
            body_class.create_joint(i,legRR1,'legRR1',['body','legRR1'],[0,-1.4])
            body_class.create_joint(i,legRR2,'legRR2',['legRR1','legRR2'],[1.8,-6.15])
    
    input = []
    for i in range(bge.logic.agentNum):
        input.append([0] * 30)
    input = [input]
    
    
    if timer.localPosition.y >= 1.0:
        for i in range(bge.logic.agentNum):
            
            
            input[0][i][0] = bge.logic.body[i].localOrientation.to_euler().x / pi
            input[0][i][1] = bge.logic.body[i].localOrientation.to_euler().y / pi
            input[0][i][2] = bge.logic.body[i].localOrientation.to_euler().z / pi
            input[0][i][3] = bge.logic.body[i].localLinearVelocity.x / 3
            input[0][i][4] = bge.logic.body[i].localLinearVelocity.y / 3
            input[0][i][5] = bge.logic.body[i].localLinearVelocity.z / 3
            
            input[0][i][6] = (bge.logic.legFL1[i].localOrientation * bge.logic.body[i].localOrientation.inverted()).to_euler().x / pi
            input[0][i][7] = (bge.logic.legFL2[i].localOrientation * bge.logic.legFL1[i].localOrientation.inverted()).to_euler().x / pi
            
            input[0][i][8] = (bge.logic.legFR1[i].localOrientation * bge.logic.body[i].localOrientation.inverted()).to_euler().x / pi
            input[0][i][9] = (bge.logic.legFR2[i].localOrientation * bge.logic.legFR1[i].localOrientation.inverted()).to_euler().x / pi
            
            input[0][i][10] = (bge.logic.legRL1[i].localOrientation * bge.logic.body[i].localOrientation.inverted()).to_euler().x / pi
            input[0][i][11] = (bge.logic.legRL2[i].localOrientation * bge.logic.legRL1[i].localOrientation.inverted()).to_euler().x / pi
            
            input[0][i][12] = (bge.logic.legRR1[i].localOrientation * bge.logic.body[i].localOrientation.inverted()).to_euler().x / pi
            input[0][i][13] = (bge.logic.legRR2[i].localOrientation * bge.logic.legRR1[i].localOrientation.inverted()).to_euler().x / pi
            
            badhits = input[0][i][14] = (bge.logic.body[i]['hit'] + bge.logic.legFL1[i]['hit'] + bge.logic.legFR1[i]['hit'] + bge.logic.legRL1[i]['hit'] + bge.logic.legRR1[i]['hit']) / 5
            input[0][i][15] = bge.logic.legFL2[i]['hit']
            input[0][i][16] = bge.logic.legFR2[i]['hit']
            input[0][i][17] = bge.logic.legRL2[i]['hit']
            input[0][i][18] = bge.logic.legRR2[i]['hit']
            
            input[0][i][19] = (bge.logic.legFL1[i].localAngularVelocity.x - bge.logic.body[i].localAngularVelocity.x) / 5
            input[0][i][20] = (bge.logic.legFL2[i].localAngularVelocity.x - bge.logic.legFL1[i].localAngularVelocity.x) / 5
            
            input[0][i][21] = (bge.logic.legFR1[i].localAngularVelocity.x - bge.logic.body[i].localAngularVelocity.x) / 5
            input[0][i][22] = (bge.logic.legFR2[i].localAngularVelocity.x - bge.logic.legFR1[i].localAngularVelocity.x) / 5
            
            input[0][i][23] = (bge.logic.legRL1[i].localAngularVelocity.x - bge.logic.body[i].localAngularVelocity.x) / 5
            input[0][i][24] = (bge.logic.legRL2[i].localAngularVelocity.x - bge.logic.legRL1[i].localAngularVelocity.x) / 5
            
            input[0][i][25] = (bge.logic.legRR1[i].localAngularVelocity.x - bge.logic.body[i].localAngularVelocity.x) / 5
            input[0][i][26] = (bge.logic.legRR2[i].localAngularVelocity.x - bge.logic.legRR1[i].localAngularVelocity.x) / 5
            
            input[0][i][27] = bge.logic.body[i].localAngularVelocity.x / 5
            input[0][i][28] = bge.logic.body[i].localAngularVelocity.y / 5
            input[0][i][29] = bge.logic.body[i].localAngularVelocity.z / 5
            
            #input[0][i][30] = 
            
            #bge.logic.legFL2[i]['test'] = (bge.logic.legFL2[i].localOrientation.to_euler().x -bge.logic.legFL1[i].localOrientation.to_euler().x)
            
            
            if badhits <= 0:
                #if bge.logic.legFL2[i]['hit'] + bge.logic.legFR2[i]['hit'] + bge.logic.legRL2[i]['hit'] + bge.logic.legRR2[i]['hit'] == 2:
                    #bge.logic.scores[i] += 0.005
                    #bge.logic.legFL2[i]['test'] += 0.005
                #bge.logic.scores[i] += 1
                if abs(bge.logic.body[i].worldPosition.y) > bge.logic.farPosition[i]:
                    #print(abs(bge.logic.body[i].worldPosition.y),bge.logic.farPosition[i])
                    bge.logic.scores[i] += abs(bge.logic.body[i].worldPosition.y) - bge.logic.farPosition[i]
                    bge.logic.farPosition[i] = abs(bge.logic.body[i].worldPosition.y)
            else:
                if abs(bge.logic.body[i].worldPosition.y) > bge.logic.farPosition[i]:
                    bge.logic.farPosition[i] = abs(bge.logic.body[i].worldPosition.y)
                    bge.logic.scores[i] = 0#bge.logic.scores[i] / 2
                
            
        #print("I:",input)
        #print("I2:",input[0][2])
        #print(min(test),max(test))
        output = []

#---------------------------------------------------------------
        output = nnetga.update(input)

        #nnetga.update(inputs array): Give inputs to all neural network of all popualtion and agents and return a array of ouputs.

#---------------------------------------------------------------


#---------------Apply outputs to quadrupeds---------------------

        #print("O:",output)
        for i in range(bge.logic.agentNum):
            torque = 3
            speed = 4
            
            #for ii in range(8):
                #print((output[0][i][ii] * 2) -1)
            xtorque = torque    
            #print((output[0][i][4] * 2) -1)
            #bge.logic.legFL2[i]['test'] = ((output[0][i][0] * 2) -1) * speed
            
            xspeed = ((output[0][i][0] * 2) -1) * speed
            #xtorque = output[0][i][1] * torque
            bge.logic.cnstrnt[i][0].setParam(9,xspeed,xtorque)
            xspeed = ((output[0][i][1] * 2) -1) * speed
            #xtorque = output[0][i][3] * torque
            bge.logic.cnstrnt[i][1].setParam(9,xspeed,xtorque)
            
            xspeed = ((output[0][i][2] * 2) -1) * speed
            #xtorque = output[0][i][5] * torque
            bge.logic.cnstrnt[i][2].setParam(9,-xspeed,xtorque)
            xspeed = ((output[0][i][3] * 2) -1) * speed
            #xtorque = output[0][i][7] * torque
            bge.logic.cnstrnt[i][3].setParam(9,xspeed,xtorque)
            
            xspeed = ((output[0][i][4] * 2) -1) * speed
            #xtorque = output[0][i][9] * torque
            bge.logic.cnstrnt[i][4].setParam(9,xspeed,xtorque)
            xspeed = ((output[0][i][5] * 2) -1) * speed
            #xtorque = output[0][i][11] * torque
            bge.logic.cnstrnt[i][5].setParam(9,xspeed,xtorque)
            
            xspeed = ((output[0][i][6] * 2) -1) * speed
            #xtorque = output[0][i][13] * torque
            bge.logic.cnstrnt[i][6].setParam(9,-xspeed,xtorque)
            xspeed = ((output[0][i][7] * 2) -1) * speed
            #xtorque = output[0][i][15] * torque
            bge.logic.cnstrnt[i][7].setParam(9,xspeed,xtorque)
            
    scene.objects['genText']['Text'] = "Generation:" + str(bge.logic.generation)

#-----------Wait for some time and observe quadrupeds--------------------------------

    if timer.localPosition.y >= 250.0: 
        print('Generation',bge.logic.generation)
        score = []
        for i in range(bge.logic.agentNum):
            #bge.logic.scores[i] = (abs(bge.logic.body[i].worldPosition.y))
            bge.logic.body[i].endObject()
            bge.logic.legFL1[i].endObject()
            bge.logic.legFL2[i].endObject()
            bge.logic.legFR1[i].endObject()
            bge.logic.legFR2[i].endObject()
            bge.logic.legRL1[i].endObject()
            bge.logic.legRL2[i].endObject()
            bge.logic.legRR1[i].endObject()
            bge.logic.legRR2[i].endObject()
            
            for ii in range(len(bge.logic.cnstrnt[i])):
                bge.constraints.removeConstraint(bge.logic.cnstrnt[i][ii].getConstraintId())
        #print("    Score list:",bge.logic.scores)
        print("   Min score:",min(bge.logic.scores)," by agent ",bge.logic.scores.index(min(bge.logic.scores)))
        print("   Avg score:",sum(bge.logic.scores)/len(bge.logic.scores))
        print("   Max score:",max(bge.logic.scores)," by agent ",bge.logic.scores.index(max(bge.logic.scores)))
        note = str(sum(bge.logic.scores)/len(bge.logic.scores)) + " " + str(bge.logic.generation) + '\n'
        draw_chart(note)

#---------------------------------------------------------------      
        nnetga.next_gen(0,bge.logic.scores,1,1,4,0)

        #nnetga.next_gen(population index,scores array,cross over option (0 or 1, default 1), mutation option (0 or 1, default 1 ),numbers of elite keep for next generation (default 4 ),numbers of worst agent removed for crossover ( default 0)): Push the given population to the next generation where crossover and mutation happen and give the new generation.

#---------------------------------------------------------------


        #a = nnetga.get_chromo(0,bge.logic.scores.index(min(bge.logic.scores)))
        #print(a)
        #for i in range(len(a)):
            #a[i] = (random() * 36) - 18
        #print(a)
        #nnetga.insert_chromo(0,bge.logic.scores.index(min(bge.logic.scores)),a)
        
        bge.logic.generation += 1
        timer.localPosition.y = -1.0
        
    frameset = [0,10,25,50,100,250,500,1000,2000,4000,8000]
    if bge.logic.generation in frameset:
        #filename = "//render/09/test." + str(bge.logic.cframe) + "."
        #bge.render.makeScreenshot(filename)
        bge.logic.cframe += 1
    
    
    timer.localPosition.y += 1
    

