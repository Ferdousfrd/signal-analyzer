# analyze what frequency hiding in signal
# how noisy is it
# with plot frequency break down

from scipy.fft import fft, fftfreq
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def analyze_signal(filename):
    df = pd.read_csv(filename)  # reading csv getting data

    time_array = df["time"].values      # df["time"] gives the time column as an array
    amplitude = df["amplitude"].values  # df["ammplitude"] gives the amplitude column as an array
    
    # getting steps or diff between time and getting sampling rate
    time_step = time_array[1] - time_array[0]
    sampling_rate = 1 / time_step

    # running fft
    fft_result = fft(amplitude)     # converting our signal to frequency domain
    frequencies = fftfreq(len(amplitude), time_step)    # getting values for x axis
    magnitude = np.abs(fft_result)      # complex numbers to strength

    # filter positive frequencies with numpy boolean array
    positive_mask = frequencies > 0
    frequencies = frequencies[positive_mask]
    magnitude = magnitude[positive_mask]

    # find dominant frequencies
    peak_index = np.argmax(magnitude)   # gets the index of the max magnitude value
    dominant_frequency = frequencies[peak_index]    # gets peak indexed freaquency

    # noise estimation
    noise = amplitude - np.sin(2 * np.pi * dominant_frequency * time_array)  # subtracting pure signal
    noise_level = np.std(noise)     # np.std() tells how spread out the noise is

    # plot frequency spectrum
    plt.figure(figsize=(10, 4))     # figure size a lil bigger
    plt.plot(frequencies, magnitude)
    plt.title("FFT Plot")
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.tight_layout()
    plt.grid(True, alpha=0.3)
    plt.xlim(0,150)     # restricting x values 0 to 200 since we have 50 Hz

    # add vertical line at dominant frequency
    plt.axvline(x=dominant_frequency, color='r', linestyle='--', label=f'Dominant: {dominant_frequency: .1f} Hz')
    plt.legend()

    plt.savefig("output/fft_plot.png")
    print("Plot svaed to output/fft_plot.png")

    print(f"Dominant frequency: {dominant_frequency:.1f} Hz")
    print(f"Estimated noise level: {noise_level:.4f}")
    print(f"Sampling rate: {sampling_rate: .0f} Hz")
    return dominant_frequency, noise_level
    

if __name__ == "__main__":
    analyze_signal("data/signal.csv")