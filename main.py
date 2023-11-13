# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 13:24:20 2023

@author: Ece
"""

import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import os

directory = dir_path = os.path.dirname(os.path.realpath(__file__)) 
for file in sorted(os.listdir(directory)):
    filename = os.fsdecode(file)
    if filename.endswith(".wav"):
        rate, data = wav.read(filename)
        plt.title(file)
        plt.plot(data, color='red')
        plt.show()
        fft_out = fft(data)
        plt.title(file)
        plt.xlabel("Frequency")
        plt.plot(fft_out, color='green')
        plt.show()


