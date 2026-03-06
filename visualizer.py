import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_signal(filename, frequency):   # this filename takes csv file

    # this func written below reads the given csv file and returns our data
    time_array, amplitude, clean_signal = read_csv_file(filename, frequency)    

    # making graphs for visuals

    fig, axes = plt.subplots(3 ,1)

    # 1st figre with noise signal
    axes[0].plot(time_array, amplitude, 'b-')
    axes[0].set_title("Noise Signal")
    axes[0].set_xlabel("Time (s)")
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(True, alpha=0.2)

    # 2nd figure with clean signal

    axes[1].plot(time_array, clean_signal, 'b-')
    axes[1].set_title("Clean Signal")
    axes[1].set_xlabel("Time (s)")
    axes[1].set_ylabel("Amplitude")
    axes[1].grid(True, alpha=0.2)

    # 3nd figure for only noise visual
    noise = amplitude - clean_signal

    axes[2].plot(time_array, noise, 'b-')
    axes[2].set_title("Noise Level")
    axes[2].set_xlabel("Time (s)")
    axes[2].set_ylabel("Amplitude")
    axes[2].grid(True, alpha=0.2)

    plt.tight_layout()  # stops subplots from overlapping other
    plt.savefig("output/signal_plot.png")   # saves plots in a file
    print("Plot svaed to output/signal_plot.png")


# func to read csv file and ready our plotting data
def read_csv_file(filename, frequency):

    df = pd.read_csv(filename)     # using pandas library to read csv files

    time_array = df["time"].values      # df["time"] gives the time column as an array
    amplitude = df["amplitude"].values  # df["ammplitude"] gives the amplitude column as an array
    clean_signal = np.sin(2 * np.pi * frequency * time_array)  # claen signal formula for 50hz frequency

    return time_array, amplitude, clean_signal

    # print(time_array)

if __name__ == "__main__":
    plot_signal('data/signal.csv', 50)