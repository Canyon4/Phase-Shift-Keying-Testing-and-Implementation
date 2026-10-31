import numpy as np
from scipy.io import wavfile

sampleFreq, bitsArray = wavefile.read("BPSK.wav")
bitsArray = bitsArray / 32768.0

carrierFreq = 4000
bitRate = 500
samplesPerSecond = sampleFreq // bitRate


