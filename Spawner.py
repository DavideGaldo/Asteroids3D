import bge
import random


asteroidsNumber = 30
generationMinRadius = 50
generationMaxRadius = 90
asteroidsLife = 0



scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
own=cont.owner;

#Get the player position
player = scene.objects['Spaceship']
playerPosX=player.worldPosition[0]
playerPosY=player.worldPosition[1]
playerPosZ=player.worldPosition[2]



#list of the inactive object from secondary level
list = scene.objectsInactive


for y in range(0,asteroidsNumber):
    rx = random.uniform(generationMinRadius, generationMaxRadius) * random.choice([-1,1])
    ry = random.uniform(generationMinRadius, generationMaxRadius) * random.choice([-1,1])
    rz = random.uniform(generationMinRadius, generationMaxRadius) * random.choice([-1,1])
    randomPosition = [rx,ry,rz]
    #Pick random object from inactive list
    choice = random.choice(list)
    #Move the spowner around the player before spawn
    own.worldPosition = [playerPosX + rx, playerPosY + ry, playerPosZ + rz] 
    print(own.position) 
    #Generation of the new object 
    object = scene.addObject(choice, own, asteroidsLife)
    
    
    
    
    #for x in range(-4,4):
    #    g=random.random()
    #    for z in range (-10,10):
    #        b=random.random()
    #        choice = random.choice(list)
    #        #instanzio oggetto scelto prima con vita 600frame dalla posizione dello spawner
    #        object = scene.addObject(choice, own, 600)
    #        object.worldPosition = [2*x*r,2*y*g,2*z*b] 
            