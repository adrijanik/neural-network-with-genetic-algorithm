import bge
import sys
if 'E:\\3D\\project_neuralnet\\build\\windows\\64bit' not in sys.path:
    sys.path.append('E:\\3D\\project_neuralnet\\build\\windows\\64bit')
    print(sys.path)
import nnetga
import imp
from random import random
from time import clock
from math import pi
from random import random

scene = bge.logic.getCurrentScene()

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
    nnetga.add_pop(1,0.7,0.3,0.25)
    nnetga.add_agent(0,bge.logic.agentNum)
    nnetga.add_net(0,30,2,24,8)
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
    for i in range(bge.logic.agentNum):
        bge.logic.cnstrnt[i] = []
        offset = i * 9
        cnsType = 12
        ShoulderXMin = -1.0
        ShoulderXMax = 0.7
        ElbowXMin = -1.0
        ElbowXMax = 0.0
        spawner.worldPosition = scene.objectsInactive['body'].worldPosition
        spawner.worldOrientation = scene.objectsInactive['body'].worldOrientation
        spawner.worldPosition.x += offset
        bge.logic.body[i] = scene.addObject(body,spawner,0)
        
        spawner.worldTransform = scene.objectsInactive['legFL1'].worldTransform
        spawner.worldOrientation = scene.objectsInactive['legFL1'].worldOrientation
        spawner.worldPosition.x += offset
        bge.logic.legFL1[i] = scene.addObject(legFL1,spawner,0)
        physics_id_1 = bge.logic.body[i].getPhysicsId()
        physics_id_2 = bge.logic.legFL1[i].getPhysicsId()
        cnsPos = spawner.worldPosition
        cns = bge.constraints.createConstraint(physics_id_1, physics_id_2,cnsType,cnsPos.x - offset,cnsPos.y + 1.4,cnsPos.z - 1,1.0,0,0)
        cns.setParam(3, ShoulderXMin, ShoulderXMax)
        cns.setParam(4, 0.0, 0.0)
        cns.setParam(5, 0.0, 0.0)
        bge.logic.cnstrnt[i].append(cns)

        spawner.worldTransform = scene.objectsInactive['legFL2'].worldTransform
        spawner.worldOrientation = scene.objectsInactive['legFL2'].worldOrientation
        spawner.worldPosition.x += offset
        bge.logic.legFL2[i] = scene.addObject(legFL2,spawner,0)
        physics_id_1 = bge.logic.legFL1[i].getPhysicsId()
        physics_id_2 = bge.logic.legFL2[i].getPhysicsId()
        cnsPos = spawner.worldPosition
        cns = bge.constraints.createConstraint(physics_id_1, physics_id_2,cnsType,cnsPos.x - offset - 1.8,cnsPos.y + 4.3,cnsPos.z - 1,1.0,0,0)
        cns.setParam(3, ElbowXMin, ElbowXMax)
        cns.setParam(4, 0.0, 0.0)
        cns.setParam(5, 0.0, 0.0)
        bge.logic.cnstrnt[i].append(cns)

        spawner.worldPosition = scene.objectsInactive['legFR1'].worldPosition
        spawner.worldOrientation = scene.objectsInactive['legFR1'].worldOrientation
        spawner.worldPosition.x += offset
        bge.logic.legFR1[i] = scene.addObject(legFR1,spawner,0)
        physics_id_1 = bge.logic.body[i].getPhysicsId()
        physics_id_2 = bge.logic.legFR1[i].getPhysicsId()
        cnsPos = spawner.worldPosition
        cns = bge.constraints.createConstraint(physics_id_1, physics_id_2,cnsType,cnsPos.x - offset,cnsPos.y - 1.4,cnsPos.z - 1,1.0,0,0)
        cns.setParam(3, -ShoulderXMax, -ShoulderXMin)
        cns.setParam(4, 0.0, 0.0)
        cns.setParam(5, 0.0, 0.0)
        bge.logic.cnstrnt[i].append(cns)
        
        spawner.worldPosition = scene.objectsInactive['legFR2'].worldPosition
        spawner.worldOrientation = scene.objectsInactive['legFR2'].worldOrientation
        spawner.worldPosition.x += offset
        bge.logic.legFR2[i] = scene.addObject(legFR2,spawner,0)
        physics_id_1 = bge.logic.legFR1[i].getPhysicsId()
        physics_id_2 = bge.logic.legFR2[i].getPhysicsId()
        cnsPos = spawner.worldPosition
        cns = bge.constraints.createConstraint(physics_id_1, physics_id_2,cnsType,cnsPos.x - offset - 1.8,cnsPos.y - 6.15,cnsPos.z - 1,1.0,0,0)
        cns.setParam(3, ElbowXMin, ElbowXMax)
        cns.setParam(4, 0.0, 0.0)
        cns.setParam(5, 0.0, 0.0)
        bge.logic.cnstrnt[i].append(cns)
        
        
        spawner.worldTransform = scene.objectsInactive['legRL1'].worldTransform
        spawner.worldOrientation = scene.objectsInactive['legRL1'].worldOrientation
        spawner.worldPosition.x += offset
        bge.logic.legRL1[i] = scene.addObject(legRL1,spawner,0)
        physics_id_1 = bge.logic.body[i].getPhysicsId()
        physics_id_2 = bge.logic.legRL1[i].getPhysicsId()
        cnsPos = spawner.worldPosition
        cns = bge.constraints.createConstraint(physics_id_1, physics_id_2,cnsType,cnsPos.x - offset,cnsPos.y + 1.4,cnsPos.z - 1,1.0,0,0)
        cns.setParam(3, ShoulderXMin, ShoulderXMax)
        cns.setParam(4, 0.0, 0.0)
        cns.setParam(5, 0.0, 0.0)
        bge.logic.cnstrnt[i].append(cns)
        
        spawner.worldTransform = scene.objectsInactive['legRL2'].worldTransform
        spawner.worldOrientation = scene.objectsInactive['legRL2'].worldOrientation
        spawner.worldPosition.x += offset
        bge.logic.legRL2[i] = scene.addObject(legRL2,spawner,0)
        physics_id_1 = bge.logic.legRL1[i].getPhysicsId()
        physics_id_2 = bge.logic.legRL2[i].getPhysicsId()
        cnsPos = spawner.worldPosition
        cns = bge.constraints.createConstraint(physics_id_1, physics_id_2,cnsType,cnsPos.x - offset + 1.8,cnsPos.y + 4.3,cnsPos.z - 1,1.0,0,0)
        cns.setParam(3, ElbowXMin, ElbowXMax)
        cns.setParam(4, 0.0, 0.0)
        cns.setParam(5, 0.0, 0.0)
        bge.logic.cnstrnt[i].append(cns)
        
        spawner.worldPosition = scene.objectsInactive['legRR1'].worldPosition
        spawner.worldOrientation = scene.objectsInactive['legRR1'].worldOrientation
        spawner.worldPosition.x += offset
        bge.logic.legRR1[i] = scene.addObject(legRR1,spawner,0)
        physics_id_1 = bge.logic.body[i].getPhysicsId()
        physics_id_2 = bge.logic.legRR1[i].getPhysicsId()
        cnsPos = spawner.worldPosition
        cns = bge.constraints.createConstraint(physics_id_1, physics_id_2,cnsType,cnsPos.x - offset,cnsPos.y - 1.4,cnsPos.z - 1,1.0,0,0)
        cns.setParam(3, -ShoulderXMax, -ShoulderXMin)
        cns.setParam(4, 0.0, 0.0)
        cns.setParam(5, 0.0, 0.0)
        bge.logic.cnstrnt[i].append(cns)
        
        spawner.worldPosition = scene.objectsInactive['legRR2'].worldPosition
        spawner.worldOrientation = scene.objectsInactive['legRR2'].worldOrientation
        spawner.worldPosition.x += offset
        bge.logic.legRR2[i] = scene.addObject(legRR2,spawner,0)
        physics_id_1 = bge.logic.legRR1[i].getPhysicsId()
        physics_id_2 = bge.logic.legRR2[i].getPhysicsId()
        cnsPos = spawner.worldPosition
        cns = bge.constraints.createConstraint(physics_id_1, physics_id_2,cnsType,cnsPos.x - offset + 1.8,cnsPos.y - 6.15,cnsPos.z - 1,1.0,0,0)
        cns.setParam(3, ElbowXMin, ElbowXMax)
        cns.setParam(4, 0.0, 0.0)
        cns.setParam(5, 0.0, 0.0)
        bge.logic.cnstrnt[i].append(cns)
        

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
    output = nnetga.update(input)
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
    nnetga.next_gen(0,bge.logic.scores,1,1,4,0)
    
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


