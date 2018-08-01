import bge;
controller = bge.logic.getCurrentController();
spaceShip = controller.owner;

decelerator = controller.sensors["Decelerator"];
accelerate = controller.sensors["W"];
decelerate = controller.sensors["S"];
topSpeed=0.60;
baseSpeed= 0.05;
speedStep = 0.025;
autoDecStep=0.01;
decelerationRatio = 0.20;

move = controller.actuators["Move"];
speed = move.dLoc[1];

if accelerate.positive:
    if speed <= topSpeed:
        speed = speed + speedStep
elif decelerate.positive:
    if speed >= (2*baseSpeed):
        speed=speed - decelerationRatio
elif decelerator.positive:
    if speed >= (2*baseSpeed):
        speed = speed - autoDecStep
    #else:
    #    speed = -0.10;

move.dLoc = [0.0, speed, 0.0];
controller.activate(move);
#print(speed);
