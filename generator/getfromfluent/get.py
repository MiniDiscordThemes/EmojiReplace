# Get emoji images from FluentUI-Emoji folder
# In this folder `git clone https://github.com/microsoft/fluentui-emoji.git`

import os
import os.path
import shutil
import glob
from datetime import datetime

thisDir = os.path.dirname(__file__)
assets = os.path.join("fluentui-emoji", "assets")
designs = ["3D", "Color", "Flat", "High Contrast"]
tones = {"Dark", "Medium-Dark", "Medium", "Medium-Light", "Light", "Default"}
assetsPath = os.path.join(thisDir, assets)
emojiPaths = glob.glob(os.path.join(assetsPath, "**"))
time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
errorsPath = os.path.join(thisDir, "errors.txt")

def logError(message):
    with open(errorsPath, "a", encoding="utf8") as errorFile:
        errorFile.write(f"Error: {message}.\n")

def getFileName(emojiPath, design):
    try:
        fileNames = os.listdir(os.path.join(emojiPath, design))
        if len(fileNames) != 1:
            raise Exception(f"Not one file in folder {fileNames}")
        return fileNames[0]
    except FileNotFoundError:
        logError(f"Error: No folder {design} in {emojiPath}")
        return None
    except Exception as error:
        logError(f"Error: {error}.")
        return None

def copyFiles(emojiPath, designs):
    for design in designs:
        fileName = getFileName(emojiPath, design)
        if fileName == None:
            continue
        else:
            origFilePath = os.path.join(emojiPath, design, fileName)
            newFilePath = os.path.join(thisDir, "extracted", design, fileName)
            os.makedirs(os.path.dirname(newFilePath), exist_ok=True)
            shutil.copyfile(origFilePath, newFilePath)

def main():
    with open(errorsPath, "w", encoding="utf8") as errorFile:
        errorFile.write(f"{time}\n")

    for emojiPath in emojiPaths:
        # Check if emoji folder has tone variants
        subpaths = {dir for dir in os.listdir(emojiPath) if dir != "metadata.json"}
        if subpaths == tones:
            for tone in tones:
                emojiPathWithTone = os.path.join(emojiPath, tone)
                # Non-default tones do not have high contrast version
                if tone == "Default":
                    copyFiles(emojiPathWithTone, designs)
                else:
                    copyFiles(emojiPathWithTone, [design for design in designs if design != "High Contrast"])
        else:
            copyFiles(emojiPath, designs)

    print("Done.")

main()