# inverse-kinematics-simple-solver

A simple implementation of a joint controller for an underactuated 
robotic arm -- currently a work in progress

controls:

w,a,s,d - moves the end effector by 0.5 units in the x-y plane

j,k - moves the end effector by +0.5 units and -0.5 units in the Z 
direction, respectively. The math most likely isn't correct for this function at the moment (in addition to some other parts of the code)

x - changes perspective to show the X-axis on the horizontal axis

z - changes perspective to show the y-axis on the horizontal axis

i - changes perspective to an isomorphic view

q - quits program