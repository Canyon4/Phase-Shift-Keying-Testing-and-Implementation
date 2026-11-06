# Canyon Sorrel
# 11/5/26
# The purpose of this program is to take in an image file, convert it to bit data, then save that data to a txt

with open("image.png", "rb") as f:
  binaryData = "".join(f"{byte:08b}" for byte in f.read())
  
  
BitIn = open("BitInput.txt", "w")

for i in binaryData:
    BitIn.write(str(i))



