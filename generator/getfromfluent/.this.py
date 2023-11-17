import os

thisDir = os.path.dirname(__file__)
files = [file.replace(".avif", "") for file in os.listdir(thisDir) if file.endswith(".avif")]

with open(os.path.join(thisDir, ".filenames.txt"), "w") as f:
    f.write(" ".join(files))