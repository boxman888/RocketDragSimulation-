###################################################################
# Ethan Patterson
# PH211 FALL 2017	Lab#: 5v2
# November 3rd 2017
# Program finds the velocity of a falcon-9 rocket
#-----------------Algorithm----------------------------------------
# Using Newtons second law
##################################################################
from visual import *
from visual.graph import *
import math

#--Variables----------

# Time variables
t = 0 # In seconds
dt = .01 # In seconds
t_final = 137 # Final time in seconds
g = -9.80 # In meters per second

# Rocket variables
A = pi * ((3.7/2)**2)
rocketHight = 68.4
thrust = vector(0, 5885.0 * 1000,0)# In Newtons
m_int = 505846.0 # In Kg
m_final = 13150.0 # In kg

c_subD = 0.8

# Change in mass constants
slope = (m_final - m_int)/180
b = m_int

# Vectors
s = vector(0,0,0)
v = vector(0,0,0)
a = vector(0,0,0)
netForce = vector(0,0,0)
#--------------------

#----Graphs---------
gp = gdisplay(x=0, y=0, width=750, height=250,
      title='Position vs. time', xtitle='Time', ytitle='Positon',
      foreground=color.black, background=color.white,
      xmax=0, xmin=180, ymax=s.y, ymin=0)
pcurve=gcurve(color = color.blue)

gp = gdisplay(x=0, y=250, width=750, height=250,
      title='Velocity vs. time', xtitle='Time', ytitle='Velocity',
      foreground=color.black, background=color.white,
      xmax=0, xmin=180, ymax=v.y, ymin=0)
vcurve=gcurve(color = color.red)

gp = gdisplay(x=0, y=500, width=750, height=250,
      title='Acceleration vs. time', xtitle='Time', ytitle='Acceleration',
      foreground=color.black, background=color.white,
      xmax=0, xmin=180, ymax=a.y, ymin=0)
acurve=gcurve(color = color.green)

gp = gdisplay(x=750, y=0, width=750, height=250,
      title='Velocity vs. time', xtitle='Time', ytitle='Drag',
      foreground=color.black, background=color.white,
      xmax=0, xmin=180, ymax=v.y, ymin=0)
dcurve=gcurve(color = color.red)
#------------------

#----Functions------
# Finds the rho at a given height
def Rho(h):
	p = (0.289 * exp(1.73 - 0.000157 * h))
	return p
# Finds the linear change in mass
def newMass(slope, b, t):
	mass = slope * t + b
	return mass
#-------------------

scence = display(title='SpaceX rocket', x=0,y=0,width=600,
		height=600, range=vector(10,10,10),
		center=s)

#Make a 3D rocket, but not actially a rocket, but a partical pretending to be a rocket lolz
ball = sphere(pos=s, radius=1, color=color.blue)
balllabel = label(pos=ball.pos, text='Vy=%1.2f' %v.y,
                  xoffset=-100, yoffset=0)
balllabel2 = label(pos=ball.pos, text='Distance Fallen = %1.2f' %s.y,
                  xoffset=100, yoffset=0)
scaleIt = 50# Used to keep ball in frame
drag = vector(0,0,0)
while t <= t_final:
	rate(1000)


	drag.y = ((0.5 * c_subD * A * (v.y**2) * Rho(s.y + rocketHight)))
	# Finds the net force of all forces
	# Multiply my drag by -1 to change the derection of the vector
	netForce.y = -1 * drag.y + (g * newMass(slope,b,t)) + thrust.y
	a.y = netForce.y / newMass(slope,b,t) # Newtons second equation for finding acceleration
	v.y = v.y + a.y * dt # Change in velocity
	s.y = s.y + v.y * dt # Change in position

	#UPDATE PRATICAL ROCKET Div by 50 to keep the ball withing view range
	ball.pos = s/scaleIt
	balllabel.pos = s/scaleIt
	balllabel.text = 'v=%1.2f m/s' %v.y
	balllabel2.text = 'Vertical Position = %1.1f m' %(s.y)
	scence.center=ball.pos

	#UPDATE GRAPH
	pcurve.plot(pos=(t,s.y))
	vcurve.plot(pos=(t,v.y))
	acurve.plot(pos=(t,a.y))
	dcurve.plot(pos=(t,drag.y))

	t = t + dt # Updates time
	#print s.y, v.y,  a.y, t
print "The speed at " + str(t) + " seconds is " + str(round(v.y,2)) + "m/s"
print "END"
