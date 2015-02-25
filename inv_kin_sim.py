import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

l1 = 3
l2 = 2
l3 = 1

x2 = 2
y2 = 3
z2 = 4

A = math.acos(((math.pow(x2,2) + math.pow(y2,2)) + 
	(math.pow(l1,2)) - math.pow(l2+l3,2)) / 
	(2 * l1 * math.sqrt(math.pow(x2,2) + math.pow(y2,2))))

B = math.acos(x2/math.sqrt(math.pow(x2,2) + math.pow(y2,2)))

t0 = A + B


t1 = math.acos( (math.pow(l2+l3,2) + math.pow(l1,2) - 
	(math.pow(x2,2) + math.pow(y2,2))) / (2 * l1 * (l2+l3)))

x3 = l1*math.cos(t0)
y3 = l1*math.sin(t0)

l4 = math.sqrt(math.pow(x2-x3,2) + math.pow(y2-y3,2))

# print "thing: " + str((math.pow(l2,2) + math.pow(l3,2) - math.pow(l4,2)) 
# 	/ (2*l2*l3))

# t2 = math.acos( (math.pow(l2,2) + math.pow(l3,2) - math.pow(l4,2)) 
# 	/ (2*l2*l3))

t2 = math.pi

t3 = math.acos(x2/(math.sqrt(math.pow(x2,2) + math.pow(z2,2))))


print "t0: " + str(t0)
print "t1: " + str(t1)
print "t2: " + str(t2)

p0x = 0
p0y = 0
p0z = 0

p1x = l1*math.cos(t0)
p1y = l1*math.sin(t0)
p1z = p1x*math.sin(t3)
print "p1x: " + str(p1x)
print "p1y: " + str(p1y)

p2x = p1x + l2*math.cos(- (math.pi - t1 - t0))
p2y = p1y + l2*math.sin(- (math.pi - t1 - t0))
p2z = p2x*math.sin(t3)
print "p2x: " + str(p2x)
print "p2y: " + str(p2y)

# p3x = p2x + l3*math.cos(math.pi - t2 - t1)
# p3y = p2y + l3*math.sin(math.pi - t2 - t1)
p3x = p2x + l3*math.cos(-(math.pi - t1 - t0))
p3y = p2y + l3*math.sin(-(math.pi - t1 - t0))
p3z = p3x*math.sin(t3)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect("equal")
plt.plot([p0z,p1z,p2z,p3z],[p0x,p1x,p2x,p3x],[p0y,p1y,p2y,p3y],color="b")

ax.scatter([p0z],[p0x],[p0y],color="r",s=100)
ax.scatter([p1z],[p1x],[p1y],color="g",s=100)
ax.scatter([p2z],[p2x],[p2y],color="g",s=100)
ax.scatter([p3z],[p3x],[p3y],color="g",s=100)


plt.show()



