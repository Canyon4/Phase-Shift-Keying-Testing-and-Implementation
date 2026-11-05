import numpy as np
from scipy.io import wavfile

sampleFreq, bitsArray = wavfile.read("BPSK.wav")
bitsArray = bitsArray / 32768.0

carrierFreq = 4000
bitRate = 500
samplesPerSecond = sampleFreq // bitRate

t = np.arange(len(bitsArray)) / sampleFreq
i = bitsArray * np.cos(2 * np.pi * carrierFreq * t)
q = -bitsArray * np.sin(2 * np.pi * carrierFreq * t)

nBits = len(bitsArray) // samplesPerSecond
z = (i + 1j * q)[:nBits * samplesPerSecond].reshape(nBits, samplesPerSecond).sum(axis = 1)

phaseEst = 0.5 * np.angle(np.sum(z ** 2))
z = z * np.exp(-1j * phaseEst)


bitsHat = (z.real > 0).astype(int)

text = open("BitInput.txt").read()
bits = np.array([int(c) for c in text if c in "01"])

n = min(len(bits), len(bitsHat))
bits, bitsHat = bits[:n], bitsHat[:n]

errorsNormal = np.sum(bitsHat != bits)
errorsInverted = np.sum((1 - bitsHat) != bits)
if errorsInverted < errorsNormal:
    bitsHat = 1 - bitsHat

errors = np.sum(bitsHat != bits)
print("Bits compared: ", n)
print("Bit errors: ", errors)
print("BER:", errors / n)


