import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import sys

def clean_cos(cos_angle):
    return min(1,max(cos_angle,-1))

try:
    import tty, termios
except ImportError:
    # Probably Windows.
    try:
        import msvcrt
    except ImportError:
        # FIXME what to do on other platforms?
        # Just give up here.
        raise ImportError('getch not available')
    else:
        getch = msvcrt.getch
else:
    def getch():
        """getch() -> key character

        Read a single keypress from stdin and return the resulting character. 
        Nothing is echoed to the console. This call will block if a keypress 
        is not already available, but will not wait for Enter to be pressed. 

        If the pressed key was a modifier key, nothing will be detected; if
        it were a special function key, it may return the first character of
        of an escape sequence, leaving additional characters in the buffer.
        """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def dist(x,y,z):
	return math.sqrt(math.pow(x,2) + math.pow(y,2) + math.pow(z,2))


p0x = 0
p0y = 0
p0z = 0

l1 = 3
l2 = 2
l3 = 0.6

x2 = 2
y2 = 3
z2 = 0

ta2 = math.pi/2

X = True
Z = False
# used to delete windows more than 2 plots old
# one older plot is kept to make the 'animation' look more fluid
tmp = 1

while True:
	
	A = math.acos(((math.pow(x2,2) + math.pow(y2,2)) + 
	(math.pow(l1,2)) - math.pow(l2,2)) / 
	(2 * l1 * math.sqrt(math.pow(x2,2) + math.pow(y2,2))))

	B = math.acos(x2/math.sqrt(math.pow(x2,2) + math.pow(y2,2)))

	t0 = A + B

	t1 = math.acos( (math.pow(l2,2) + math.pow(l1,2) - 
		(math.pow(x2,2) + math.pow(y2,2))) / (2 * l1 * (l2)))

	if y2 < 0:
		c = math.sqrt(math.pow(l1,2) + math.pow(l2,2) - 2*l1*l2*math.cos(t1))
		ta = math.acos((math.pow(l1,2) + math.pow(c,2) - math.pow(l2,2)) / (2*l1*c))
		t0 = 2*ta - t0


	x3 = l1*math.cos(t0)
	y3 = l1*math.sin(t0)

	l4 = math.sqrt(math.pow(x2-x3,2) + math.pow(y2-y3,2))

	t2 = - ta2 - t0 - t1

	a = math.sqrt(math.pow(l1,2) 
		+ math.pow(l2,2) - 2*l1*(l2)*math.cos(t1))
	if y2 > a:
		tv = math.pi/2
	else:
		tv = math.asin(y2/a)
	lp = a*math.cos(tv)

	t3 = math.asin(clean_cos(z2/lp))
	

	p1x = l1*math.cos(t0)
	p1y = l1*math.sin(t0)
	p1z = p1x*math.sin(t3)

	p2x = p1x + l2*math.cos(- (math.pi - t1 - t0))
	p2y = p1y + l2*math.sin(- (math.pi - t1 - t0))
	p2z = p2x*math.sin(t3)

	p3x = p2x + l3*math.cos( (math.pi - t2 - t1 - t0))
	p3y = p2y + l3*math.sin( (math.pi - t2 - t1 - t0))
	p3z = p3x*math.sin(t3)

	plt.ion()
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.set_xlim(-5,5)
	ax.set_xlabel('z')
	ax.set_ylim(-5,5)
	ax.set_ylabel('x')
	ax.set_zlim(0,5)
	ax.set_zlabel('y')
	if X == True:
		ax.set_autoscale_on(False)
		ax.autoscale_view(False,False,False)
		ax.view_init(elev=0., azim=0)
	elif Z == True:
		ax.set_autoscale_on(False)
		ax.autoscale_view(False,False,False)
		ax.view_init(elev=0., azim=-90)


	ax.scatter([p0z],[p0x],[p0y],color="g",s=100)
	ax.scatter([p1z],[p1x],[p1y],color="g",s=100)
	ax.scatter([p2z],[p2x],[p2y],color="g",s=100)
	ax.scatter([p3z],[p3x],[p3y],color="r",s=100)

	ax.plot([p0z,p1z,p2z,p3z],[p0x,p1x,p2x,p3x],[p0y,p1y,p2y,p3y],color="b")
	fig.canvas.draw()
	
	c = getch()

	maxDist = l1+l2

	if c == 'q':
		break;q

	elif(c == 'w'):
		y2 = y2+0.5
		if dist(x2,y2,z2) > maxDist or dist(x2,y2,z2) < l1-(l2) :
			print "impossible coordinates!"
			y2 = y2-0.5
	elif(c == 's'):
		y2 = y2-0.5
		if dist(x2,y2,z2) > maxDist or dist(x2,y2,z2) < l1-(l2) :
			print "impossible coordinates!"
			y2 = y2+0.5
	elif(c == 'a'):
		x2 = x2-0.5
		if dist(x2,y2,z2) > maxDist or dist(x2,y2,z2) < l1-(l2) :
			print "impossible coordinates!"
			x2 = x2+0.5
	elif(c == 'd'):
		x2 = x2+0.5
		if dist(x2,y2,z2) > maxDist or dist(x2,y2,z2) < l1-(l2) :
			print "impossible coordinates!"
			x2 = x2-0.5
	elif(c == 'j'):
		z2 = z2-0.5
		if dist(x2,y2,z2) > maxDist or dist(x2,y2,z2) < l1-(l2) :
			print "impossible coordinates!"
			z2 = z2+0.5
	elif(c == 'k'):
		z2 = z2+0.5
		if dist(x2,y2,z2) > maxDist or dist(x2,y2,z2) < l1-(l2) :
			print "impossible coordinates!"
			z2 = z2-0.5
	elif(c == 'r'):
		ta2 = ta2 + 0.3
	elif(c == 'f'):
		ta2 = ta2 - 0.3
	elif(c == 'x'):
		X = True
		Z = False
	elif(c == "z"):
		Z = True
		X = False
	elif(c == 'i'):
		Z = False
		X = False
	if(tmp > 1):
		plt.close(tmp-1)
	tmp = tmp+1
