# inverse-kinematics-simple-solver

A simple implementation of a joint controller for an underactuated 
robotic arm -- currently a work in progress

controls: 
WASD - moves the end effector by 0.5 units in the x-y plane;
JK - moves the end effector by +0.5 units and -0.5 units in the Z direction,
	respectively. The math most likely isn't correct for this function at the
	moment (in addition to some other parts of the code)