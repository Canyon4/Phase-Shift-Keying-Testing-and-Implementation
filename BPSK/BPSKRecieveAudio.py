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


finalBits = (z.real > 0).astype(int)

text = open("BitInput.txt").read()
bits = np.array([int(c) for c in text if c in "01"])

n = min(len(bits), len(finalBits))
bits, finalBits = bits[:n], finalBits[:n]

errorsNormal = np.sum(finalBits != bits)
errorsInverted = np.sum((1 - finalBits) != bits)
if errorsInverted < errorsNormal:
    finalBits = 1 - finalBits

errors = np.sum(finalBits != bits)
print("Bits compared: ", n)
print("Bit errors: ", errors)
print("BER:", errors / n)

inputType = input("Was the incoming data random or an image(y/n): ")

if(inputType == 'y'):
    finalBits = "".join(map(str, finalBits))

    finalBytesChunks = [finalBits[i:i + 8] for i in range(0, len(finalBits), 8)]

    finalRawBytes = bytearray(int(chunk, 2) for chunk in finalBytesChunks if chunk)

    with open("resultImage.png", "wb") as outputFile:
        outputFile.write(finalRawBytes)
    
    
