# happy_face
emojiList = []
# 2342ui432o34ji2kl34j.svg
selectorList = []

with open(f"generator/emoji/Apple/spritesheets.css", "r", encoding="utf8") as fileObj:
    lineCount = 0

    for line in fileObj:
        lineCount += 1
        # Grab comments with emoji name
        if lineCount % 5 == 3:
            emoji = line[95:-20]
            # print(lineCount, emoji)
            emojiList.append(emoji)

        # Grab selectors
        elif lineCount % 5 == 2:
            selector = line[41:73]
            # print(lineCount, selector)
            selectorList.append(selector)

pairs = zip(emojiList, selectorList)

# Write pairs to new file
with open("scss/vars/_spritesheets.scss", "w", encoding="utf8") as fileObj:
    fileObj.write("$spritesheets: (\n")
    for pair in pairs:
        fileObj.write(f'"{pair[0]}": "{pair[1]}",\n')
    fileObj.write(");")