# Write emojiset scss files
emojiSets = ["Apple", "Facebook", "Google", "JoyPixels", "Microsoft", "OpenMoji", "Samsung", "Toss", "WhatsApp"]

for emojiSet in emojiSets:
    with open(f"scss/{emojiSet}.scss", "w", encoding="utf8") as fileObj:
        fileObj.write(f"// {emojiSet}\n")
        fileObj.write(f'@use "./main";\n')
        fileObj.write(f'@include main.main("{emojiSet}");\n')