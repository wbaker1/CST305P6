#CST-305 Project 6 - Matthew Powers and Wesley Baker 
#This project is a display of the equtions solved for project 6

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def part_1_result_A(x):
    return 1-x+(2/6)*(x**3)-(2/24)*(x**4)

#################################################################
# plot results for part 1 A
# time points
x = np.linspace(-2,4,1000)
plt.plot(x,part_1_result_A(x),'b-', label='Part A Question 1 Y(x) line')

# label neccessary info on graph
plt.title('Question 1 Part A')
plt.xlabel('x val')
plt.ylabel('y val')
plt.legend()
# Display the graph
plt.show()
#################################################################

def part_1_result_B(x):
    return 6+(x-3)-(11/2)*((x-3)**2)-2*((x-3)**3)

#################################################################
# plot results for part 1 B
# time points
x = np.linspace(-2,6,1000)
plt.plot(x,part_1_result_B(x),'b-', label='Part B Question 1 Y(x) line')

# label neccessary info on graph
plt.title('Question 1 Part B')
plt.xlabel('x val')
plt.ylabel('y val')
plt.legend()
# Display the graph
plt.show()
#################################################################

def part_2_result(x):
    a0 = 1
    a1 = 1
    return a0 + a1*x - ((a0*(x**2))/8) - ((a1*(x**3))/24) + ((a0*(x**4))/128) + ((7*a1*(x**5))/1920) - ((13*a0*(x**6))/15360) - ((7*a1*(x**7))/15360) + ((403*a0*(x**8))/3440640) + ((301*a1*(x**9))/4423680) - ((4433*a0*(x**10))/247726080)

#################################################################
# plot results for part 2
# time points
x = np.linspace(0,10,1000)
plt.plot(x,part_2_result(x),'b-', label='Question 2 Y(x) line')

# label neccessary info on graph
plt.title('Question 2 with a0 and a1 = 1')
plt.xlabel('x val')
plt.ylabel('y val')
plt.legend()
# Display the graph
plt.show()
#################################################################

#################################################################
# plot results for part 3
# initial condition
y0 = 155

# function that returns dy/dt
def model(y, t, T):
    # k = (1/time waited)*ln((temp at end of time-room Temp)/(start temmp-room temp)) kept 74 as base temp as we were unable to simulate extreme temperatures accuratly
    k = -(1/5)*np.log((107.6-74)/(y0-74))
    dydt = -k*(y-T)
    return dydt

# time points
t = np.linspace(0,60,100)

# solve ODE for y1 with respect to k
T = 99
y1 = odeint(model,y0,t, args=(T,))

# plot result of y1
plt.plot(t,y1,'y-', label='Room Temperature = ' + str(T) + 'ºF')

# solve ODE for y2 with respect to k
T = 74
y2 = odeint(model,y0,t, args=(T,))

# plot result of y2
plt.plot(t,y2,'r-', label='Room Temperature = ' + str(T) + 'ºF')

# solve ODE for y3 with respect to k
T = 37
y3 = odeint(model,y0,t, args=(T,))

# plot result of y3
plt.plot(t,y3,'b-', label='Room Temperature = ' + str(T) + 'ºF')

# solve ODE for y4 with respect to k
T = 27
y4 = odeint(model,y0,t, args=(T,))

# plot result of y4
plt.plot(t,y4,'g-', label='Room Temperature = ' + str(T) + 'ºF')

# label neccessary info on graph
plt.title('Part 3: GPU cooling based off room temp in ºF')
plt.xlabel('Time (minutes)')
plt.ylabel('Temperature (ºF)')
plt.legend()
# Display the graph
plt.show()
#################################################################