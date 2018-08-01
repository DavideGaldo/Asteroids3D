import bge;
import random;

controller = bge.logic.getCurrentController();
asteroid = controller.owner;
r=random.random();

move = controller.actuators["Move"];

# set force 
if r < 0.4:
    move.force  = [ 1.5, 0.0, 0.0];
elif r > 0.4 and r < 0.7:
    move.force  = [ 0, 0.0, 1.5];
elif r > 0.7:
    move.force  = [ 0.0, -1.5, 0.0];

controller.activate(move);