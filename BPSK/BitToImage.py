
def BitToImage(finalBits):
    finalBits = "".join(map(str, finalBits))

    finalBytesChunks = [finalBits[i:i + 8] for i in range(0, len(finalBits), 8)]

    finalRawBytes = bytearray(int(chunk, 2) for chunk in finalBytesChunks if chunk)

    with open("resultImage.png", "wb") as outputFile:
        outputFile.write(finalRawBytes)

