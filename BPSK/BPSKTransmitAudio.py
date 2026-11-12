import pyaudio
import numpy as np
from scipy.io import wavfile
import sys

# sets max number of digits to 10 million to avoid error due to large bit data
sys.set_int_max_str_digits(10000000)

# input of generated bit file
BitInput = open("BitInput.txt", "r")
bitsList = BitInput.read().splitlines()
bitsArray = np.array([int(c) for line in bitsList for c in line if c in "01"], dtype = int)

# sets frequency and carrier info
sampleFreq = 48000
carrierFreq = 4000
bitRate = 500
samplesPerBit = sampleFreq / bitRate

# sets baseband to a 1 or -1 depending on bit info
baseband = np.repeat(2*bitsArray - 1, samplesPerBit)

# creates array of sample positions
t = np.arange(len(baseband)) / sampleFreq

phaseOffset = 0.75

# modulates bit info in baseband to carrier frequency
tx = baseband * np.cos(2*np.pi*carrierFreq*t + phaseOffset)

# scales down amplitude to avoid clipping
sig = tx * 0.9

# writes signal to a .wav file
wavfile.write("BPSK.wav", sampleFreq, (sig*32767).astype(np.int16))

