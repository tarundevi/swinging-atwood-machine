import numpy as np
g = 9.8  
dt = 0.01 
n_steps = 10000  
delta = 1e-5
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
    distances = []

    for _ in range(n_steps):
        v, r, omega, theta, R, t = update(r, theta, v, omega, t, mu, L, d)
        v1, r1, omega1, theta1, R1, t1 = update(r1, theta1, v1, omega1, t1, mu, L, d)
        distance = np.sqrt((r * np.cos(theta) - r1 * np.cos(theta1))**2 + (r * np.sin(theta) - r1 * np.sin(theta1))**2)
        if distance == float("inf"):
            break
        distances.append(distance)
    print(distances)

    log_distances = np.log(distances)
    lyapunov_exponent = np.mean(log_distances) / dt

    return lyapunov_exponent

print(calculate_lyapunov(3,np.pi/2))