# takes in image file and writes bit info into .txt file
with open("image.png", "rb") as f:
  binaryData = "".join(f"{byte:08b}" for byte in f.read())
  
  
BitIn = open("BitInput.txt", "w")

for i in binaryData:
    BitIn.write(str(i))



