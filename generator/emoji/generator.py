files = ["activity", "flags", "food", "nature", "objects", "people", "symbols", "travel"]

# happy_face
emojiList = []
# 2342ui432o34ji2kl34j.svg
selectorList = []

for file in files:
    with open(f"generator/emoji/Apple/{file}.css", "r", encoding="utf8") as fileObj:
        lineCount = 0

        for line in fileObj:
            lineCount += 1
            # Grab comments with emoji name
            if lineCount % 21 == 1:
                emoji = line.strip("/* \n")
                # print(lineCount, emoji)
                emojiList.append(emoji)

            # Grab selectors
            elif lineCount % 21 == 2:
                selector = line[27:59]
                # print(lineCount, selector)
                selectorList.append(selector)

pairs = zip(emojiList, selectorList)

# Write pairs to new file
with open("scss/vars/_emojis.scss", "w", encoding="utf8") as fileObj:
    fileObj.write("$emojis: (\n")
    for pair in pairs:
        fileObj.write(f'"{pair[0]}": "{pair[1]}",\n')
    fileObj.write(");")
