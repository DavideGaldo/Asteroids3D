import bge;
import random;

controller = bge.logic.getCurrentController();
asteroid = controller.owner;
rx=random.random();
ry=random.random();
rz=random.random();

topForce=2.50;



move = controller.actuators["Move"];

# set force 
move.force  = [ rx*topForce, ry*topForce, rz*topForce];
controller.activate(move);