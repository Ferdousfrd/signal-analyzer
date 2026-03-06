# In a real scenario, the signal data would come from actual hardware — antennas, 
# network equipment recording real wireless signals.
# But we don't have that hardware. So signal_generator.py is our fake hardware — 
# generating realistic looking signal data and saves it as CSV.

import numpy as np

# function to generate signal 
def generate_signal(frequency, duration, sampling_rate, noise_level):
    time_array = np.linspace(0,duration, int(sampling_rate * duration))     # creates evenly split points between given range
    clean_signal = np.sin(2 * np.pi * frequency * time_array)    # The formula is: signal = A * sin(2π * f * t), here np.sin(2 * np.pi * frequency * time_array)
    random_noise = np.random.normal(0, noise_level, len(time_array))    # making random noise values same points as time array
    noisy_signal = clean_signal + random_noise      # adding noses in clean signal to make impure noisy signal
    return time_array, noisy_signal

# function to write result in a csv file
def save_signal(time_array, signal, filename):
    data = np.column_stack((time_array, signal))    # stacikng time and signal side by side into a column table
    np.savetxt(f"data/{filename}", data, delimiter=",", header="time,amplitude", comments="")

    print(f"Signal saved to data/{filename}")

if __name__ == "__main__":
    time_array, noisy_signal = generate_signal(50,1,1000,0.1)
    save_signal(time_array, noisy_signal, 'signal.csv')