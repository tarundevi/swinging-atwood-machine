import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
import math


g = 9.8  
dt = 0.01 
n_steps = 10000  
delta = 1e-5
delta1 = 1e-3
def update(r, theta, v, omega, t, mu, L, d):
    l = r
    a = (l * (omega**2) + g * (np.cos(theta) - mu)) / (1 + mu)
    v += a * dt
    r += v * dt
    alpha = -(2 * (v * omega) + g * np.sin(theta)) / l
    omega += alpha * dt
    theta += omega * dt
    R = L - d - r
    t += dt
    return v, r, omega, theta, R, t

def calculate_lyapunov(mu, theta):
    d = 35
    L = 60
    r = 15
    R = L - d - r
    R1 = L - d - r
    v = 0
    omega = 0
    t = 0
    r1 = 15
    v1 = 0
    omega1 = 0
    t1 = 0
    theta1 = theta + delta
    mu1 = mu+delta1

    distances = []

    
    for _ in range(n_steps):
        v, r, omega, theta, R, t = update(r, theta, v, omega, t, mu, L, d)
        v1, r1, omega1, theta1, R1, t1 = update(r1, theta1, v1, omega1, t1, mu1, L, d)
        distance = np.sqrt((r * np.cos(theta) - r1 * np.cos(theta1))**2 + (r * np.sin(theta) - r1 * np.sin(theta1))**2)
        if distance == float("inf") or math.isnan(distance):
            break
        distances.append(distance)

    log_distances = np.log(distances)
    lyapunov_exponent = np.mean(log_distances) / dt

    return lyapunov_exponent


theta_range = np.linspace(0.5, 120*np.pi/180, 300)  
mu_range = np.linspace(1.55, 20, 300)  

lyapunov_exponents = np.zeros((len(mu_range), len(theta_range)))
n=0
for i, mu in enumerate(mu_range):
    for j, theta in enumerate(theta_range):
        lyapunov_exponent = calculate_lyapunov(mu, theta)
        lyapunov_exponents[i, j] = lyapunov_exponent
        print(n)
        n+=1


plt.figure(figsize=(10, 8))
plt.imshow(lyapunov_exponents, extent=[mu_range[0], mu_range[-1], theta_range[0], theta_range[-1]], aspect='auto', origin='lower', cmap='hot')
plt.colorbar(label='Lyapunov Exponent')
plt.xlabel('Mass Ratio $\\mu$')
plt.ylabel('Initial Angle $\\theta$ (radians)')
plt.title('Heatmap of Lyapunov Exponents')
plt.show()
