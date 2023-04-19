import numpy as np
import matplotlib.pyplot as plt

# Define the time range
t = np.arange(0, 1, 0.001)

# Generate a sine wave with frequency 1Hz and amplitude 1
sine_wave = np.sin(2 * np.pi * 1 * t)
    
# Plot the sine wave
plt.plot(t, sine_wave)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

# Define the time range
t = np.arange(0, 1, 0.001)

# Generate a cosine wave with frequency 2Hz and amplitude 0.5
cosine_wave = 0.5 * np.cos(2 * np.pi * 2 * t)

# Plot the cosine wave
plt.plot(t, cosine_wave)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

# Define the time range
t = np.arange(0, 10, 0.1)

# Generate an exponential signal with decay constant 0.1 and initial value 1
exp_signal = np.exp(-0.1 * t)

# Plot the exponential signal
plt.plot(t, exp_signal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()


# Define the time range
t = np.arange(0, 10, 0.1)

# Generate a ramp signal with slope 2 and intercept 1
ramp_signal = 2 * t + 1

# Plot the ramp signal
plt.plot(t, ramp_signal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()


# Define the time range
t = np.arange(-5, 5, 0.1)

# Generate the unit step signal
unit_step = np.heaviside(t, 1)

# Plot the unit step signal
plt.plot(t, unit_step)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()
