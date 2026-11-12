import random

# generates random bit data and writes it into a .txt file
BitIn = open("BitInput.txt", "w")

numBits = 1000

for i in range(numBits):
    num = random.randint(0,1)
    BitIn.write(str(random.randint(0,1)))



