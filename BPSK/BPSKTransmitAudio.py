import pyaudio
import numpy as np
from scipy.io import wavfile
import sys

sys.set_int_max_str_digits(10000000)

# input of randomly generated bit file
BitInput = open("BitInput.txt", "r")
bitsList = BitInput.read().splitlines()
bitsArray = np.array([int(c) for line in bitsList for c in line if c in "01"], dtype = int)

sampleFreq = 48000
carrierFreq = 4000
bitRate = 500
samplesPerBit = sampleFreq / bitRate #how many samples per one transmitted bit

baseband = np.repeat(2*bitsArray - 1, samplesPerBit)
print(baseband)

t = np.arange(len(baseband)) / sampleFreq

phaseOffset = 0.75

tx = baseband * np.cos(2*np.pi*carrierFreq*t + phaseOffset)

sig = tx * 0.9
wavfile.write("BPSK.wav", sampleFreq, (sig*32767).astype(np.int16))

