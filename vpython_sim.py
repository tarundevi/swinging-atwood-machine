from vpython import *


scene = canvas(background = color.black)


mu = 5
L = 60              
r = 15              
d = 35              
R = L - d - r       
theta = radians(90)


g = 9.8
v = 0  
omega = 0            
a = 0               
alpha = 0              
t = 0 
dt = 0.00001
T = 300


rope1 = cylinder(pos=vector(0,0,0), axis=vec( r*sin(theta), -r*cos(theta),0), radius=0.2, color= vec(.5,.5,.5) )
rope2 = cylinder(pos=vector(-d,0,0), axis=vector(0,R,0), radius=0.2, color= vec(.5,.5,.5) )
rope3 = cylinder(pos=rope1.pos, axis=rope2.pos, radius=0.2, color= vec(.5,.5,.5) )

pendulum = sphere(pos = rope1.axis, radius = 1.5, color = color.red, make_trail = True, trail_color = color.yellow)
block = sphere(pos = rope2.axis, radius = 2, color = color.red )

extrusion( path = [ vec(0,0,0.3) , vec(0,0,-0.3)], shape = shapes.circle(radius=1) , color= vec(1,1,1) )
extrusion( path = [ vec(-d,0,0.3) , vec(-d,0,-0.3)], shape = shapes.circle(radius=1) , color= vec(1,1,1) )


while t < T:
 rate(10/dt)
 # animating:
 X = pendulum.pos = rope1.axis = vec( r*sin(theta), -r*cos(theta),0)
 rope2.axis = vec( 0,-R,0)
 block.pos = vec(-d,-R,0)
 # updating:
 l = mag(X)                              
 a = ( l*(omega*omega) + g*(cos(theta)-mu ) )/( 1+mu )
 v += a*dt
 r += v*dt
 alpha = -( 2*(v*omega) + g*sin(theta) )/ l
 omega += alpha*dt
 theta += omega*dt 
 R = L - d -  r
 t += dt
 print([r,theta,t,R])
 
print("terminated")
