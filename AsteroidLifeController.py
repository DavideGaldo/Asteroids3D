import bge;
import random;

scene = bge.logic.getCurrentScene()
controller = bge.logic.getCurrentController();
own = controller.owner;

player = scene.objects['Spaceship']

#get the player distance
playerDistance = own.getDistanceTo(player)

#If the object is too far from player delete it
if (playerDistance > 100):
    own.endObject();