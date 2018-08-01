#Mouse Roration Script

import bge;
import math;
controller = bge.logic.getCurrentController();
spaceShip = controller.owner;

mouse = controller.sensors["Mouse"];
width = bge.render.getWindowWidth();
width = width/2;
height = bge.render.getWindowHeight();
height = height/2;


posX = (bge.render.getWindowWidth() / 2 - mouse.position[0]) * 0.2;
posY = (bge.render.getWindowHeight() / 2 - mouse.position[1]) * 0.1;





#print(posX);
#print(height);

xyz = spaceShip.localOrientation.to_euler();
xyz[2] = math.radians(posX);    #Rotate spaceShip around Z axes
xyz[0] = math.radians(posY);    #Rotate spaceShip around X axes

spaceShip.localOrientation = xyz.to_matrix()



