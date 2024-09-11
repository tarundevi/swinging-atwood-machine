import pygame
from math import sin, cos, pi

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SIZE)
pygame.init()
pygame.display.set_caption("Swinging Atwood's Machine")
screen.fill((255, 255, 255))
run = True

#PARAMETERS
def calculate_angularmom(m1,g,r,theta,p_theta,dt):
    z = p_theta-m1*g*r*sin(theta)*dt
    return z
def calculate_omega(p_theta,m1,r):
    z = (p_theta)/(m1*r*r)
    return z
def calculate_linearmom(p_r, p_theta,m1,r,m2,g,theta,dt):
    z =  p_r + dt*((p_theta**2)/(m1*r**3)-m2*g+m1*g*cos(theta))
    return z
def calculate_v(p_r,m1,m2):
    z =  (p_r)/(m1+m2)
    return z

def draw(v, omega, r, theta,dt,L):
    theta = theta + omega*dt
    r = r + v*dt
    pygame.draw.circle(screen, (0, 0, 0), (400, 400), 10)
    pygame.draw.circle(screen, (0, 0, 0), (600, 400), 10)
    pygame.draw.aaline(screen,(0,0,0), (400, 400), (600, 400))
    pygame.draw.line(screen,(0,0,0),(400,400),(400-r*cos(theta),400+r*sin(theta)))
    pygame.draw.circle(screen,(0,0,0),(400-r*cos(theta),400+r*sin(theta)),10)
    pygame.draw.line(screen,(0,0,0),(600,400),(600,max(400, 400+L-r)))
    pygame.draw.circle(screen,(0,0,0),(600,max(400, 400+L-r)),10)
    return(r,theta)
g=10
m1=100
m2=200
r=80
theta = 0
dt = .001
L=200
v=100
omega =200
p_theta = 1000
p_r = 1000
t=0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
    screen.fill((255,255,255))
    t+=dt
    p_theta = calculate_angularmom(m1,g,r,theta,p_theta,dt)
    p_r = calculate_linearmom(p_r,p_theta,m1,r,m2,g,theta,dt)
    omega = calculate_omega(p_theta,m1,r)
    v = calculate_v(p_r,m1,m2)
    r,theta = draw(v,omega,r,theta,dt,L)
    pygame.display.flip()




