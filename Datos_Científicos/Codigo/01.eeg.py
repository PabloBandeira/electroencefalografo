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

signals = pd.read_csv('data/TP/ojosabiertos.dat', delimiter=' ', names = ['timestamp','counter','eeg','attention','meditation','blinking'])

data = signals.values
eeg = data[:,2]

print(eeg)
len(eeg)
plt.figure(figsize=(14,7))
plt.plot(eeg, label='EEG', color="violet")
plt.xlabel('t');
plt.ylabel('eeg(t)');
plt.title('EEG Signal - Ojos Abiertos')    
plt.ylim([-1500, 1500]);
plt.xlim([0,len(eeg)])
plt.savefig('images/TP/grafico_ojosabiertos.jpg')
plt.show()

signals = pd.read_csv('data/TP/ojoscerrados.dat', delimiter=' ', names = ['timestamp','counter','eeg','attention','meditation','blinking'])

data = signals.values
eeg = data[:,2]

plt.figure(figsize=(14,7))
plt.plot(eeg, label='EEG', color="orange")
plt.xlabel('t');
plt.ylabel('eeg(t)');
plt.title('EEG Signal - Ojos Cerrados')   
plt.ylim([-1500, 1500]);
plt.xlim([0,len(eeg)])
plt.savefig('images/TP/grafico_ojoscerrados.jpg')
plt.show()

signals = pd.read_csv('data/TP/pestaneos.dat', delimiter=' ', names = ['timestamp','counter','eeg','attention','meditation','blinking'])

data = signals.values
eeg = data[:,2]

plt.figure(figsize=(14,7))
plt.plot(eeg, label='EEG', color="pink")
plt.xlabel('t');
plt.ylabel('eeg(t)');
plt.title('EEG Signal - Pestañeos')    
plt.ylim([-1500, 1500]);
plt.xlim([0,len(eeg)])
plt.savefig('images/TP/grafico_pestaneos.jpg')
plt.show()

signals = pd.read_csv('data/TP/si.dat', delimiter=' ', names = ['timestamp','counter','eeg','attention','meditation','blinking'])

data = signals.values
eeg = data[:,2]

plt.figure(figsize=(14,7))
plt.plot(eeg,label='EEG',color="aquamarine")
plt.xlabel('t');
plt.ylabel('eeg(t)');
plt.title('EEG Signal - Afirmación')     
plt.ylim([-1500, 1500]);
plt.xlim([0,len(eeg)])
plt.savefig('images/TP/grafico_afirmacion.jpg')
plt.show()

signals = pd.read_csv('data/TP/no.dat', delimiter=' ', names = ['timestamp','counter','eeg','attention','meditation','blinking'])

data = signals.values
eeg = data[:,2]

plt.figure(figsize=(14,7))
plt.plot(eeg,label='EEG', color="gray")
plt.xlabel('t');
plt.ylabel('eeg(t)');
plt.title('EEG Signal - Negación')    
plt.ylim([-1500, 1500]);
plt.xlim([0,len(eeg)])
plt.savefig('images/TP/grafico_negacion.jpg')
plt.show()

signals = pd.read_csv('data/TP/mentira.dat', delimiter=' ', names = ['timestamp','counter','eeg','attention','meditation','blinking'])

data = signals.values
eeg = data[:,2]

plt.figure(figsize=(14,7))
plt.plot(eeg, label='EEG', color="red")
plt.xlabel('t');
plt.ylabel('eeg(t)');
plt.title('EEG Signal - Mentira')   
plt.ylim([-1500, 1500]);
plt.xlim([0,len(eeg)])
plt.savefig('images/TP/grafico_mentira.jpg')
plt.show()

signals = pd.read_csv('data/TP/verdad.dat', delimiter=' ', names = ['timestamp','counter','eeg','attention','meditation','blinking'])

data = signals.values
eeg = data[:,2]

plt.figure(figsize=(14,7))
plt.plot(eeg, label='EEG', color="green")
plt.xlabel('t');
plt.ylabel('eeg(t)');
plt.title('EEG Signal - Verdad')     
plt.ylim([-1500, 1500]);
plt.xlim([0,len(eeg)])
plt.savefig('images/TP/grafico_verdad.jpg')
plt.show()

signals = pd.read_csv('data/TP/meditacion.dat', delimiter=' ', names = ['timestamp','counter','eeg','attention','meditation','blinking'])

data = signals.values
eeg = data[:,2]

plt.figure(figsize=(14,7))
plt.plot(eeg, label='EEG', color="blue" )
plt.xlabel('t');
plt.ylabel('eeg(t)');
plt.title('EEG Signal - Meditacion')     
plt.ylim([-1500, 1500]);
plt.xlim([0,len(eeg)])
plt.savefig('images/TP/grafico_meditacion.jpg')
plt.show()


