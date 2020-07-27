import os
folder = r'Redux- freeCodeCamp/React with redux'

for filename in os.listdir(folder):
    infilename = os.path.join(folder, filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.txt', '.js')
    output = os.rename(infilename, newname)
print("Complete")

