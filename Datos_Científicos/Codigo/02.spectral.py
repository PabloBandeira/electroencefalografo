import pandas as pd
import numpy as np
import sys, select
import time
import datetime
import os
import math
import matplotlib.pyplot as plt

from scipy.fftpack import fft
from scipy.signal import firwin, remez, kaiser_atten, kaiser_beta
from scipy.signal import butter, filtfilt, buttord
from scipy.signal import butter, lfilter
from scipy.fft import rfft, rfftfreq

def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

Fs = 512.0

signals = pd.read_csv('data/TP/mentira.dat', delimiter=' ', names = ['timestamp','counter','eeg','attention','meditation','blinking'])
data = signals.values
eeg = data[:,2]
normalized_signal = eeg

N = len(normalized_signal)
x = np.linspace(0.0, int(N/Fs), N)   

y = butter_bandpass_filter(normalized_signal, 8.0, 15.0, 512.0, order=6)

plt.figure(figsize=(14,7))
plt.plot(x, y,color ='red')
plt.grid()
plt.title(r'Output filtered signal - Mentira')
plt.axis((0,15,-250,250))
plt.savefig('images/TP/spectral_mentira_signal.jpg')
plt.show()

# Fourier
yf=fft(y)
xf=x

plt.figure(figsize=(14,7))
plt.title('Frequency Spectrum - Mentira')
plt.plot(xf, np.abs(yf), color='red')
plt.xlim([0,3])
plt.ylim([0,180000])
plt.ylabel('Amplitude')
plt.xlabel('Frequency (Hertz)')
plt.savefig('images/TP/spectral_mentira_spectrum.jpg')
plt.show()

# Verdad
signals = pd.read_csv('data/TP/verdad.dat', delimiter=' ', names = ['timestamp','counter','eeg','attention','meditation','blinking'])
data = signals.values
eeg = data[:,2]
normalized_signal = eeg

N = len(normalized_signal)

x = np.linspace(0.0, int(N/Fs), N)   

# Le aplico un filtro pasabanda entre 8 y 15 Hz.  El resto se intenta planchar a cero.
y = butter_bandpass_filter(normalized_signal, 8.0, 15.0, 512.0, order=6)

# señal original habiendo aplicado el filtro espectral
plt.figure(figsize=(14,7))
plt.plot(x, y,color ='green')
plt.grid()
plt.title(r'Output filtered signal - Verdad')
plt.axis((0,15,-250,250))
plt.savefig('images/TP/spectral_verdad_signal.jpg')
plt.show()

# Fourier
yf=fft(y)
xf=x

plt.figure(figsize=(14,7))
plt.title('Frequency Spectrum - Verdad')
plt.plot(xf, np.abs(yf), color='green')
plt.xlim([0,3])
plt.ylim([0,180000])
plt.ylabel('Amplitude')
plt.xlabel('Frequency (Hertz)')
plt.savefig('images/TP/spectral_verdad_spectrum.jpg')
plt.show()

