import re, string
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

content = []

with open("chat.txt", "r", encoding="utf8") as f:
    data = f.readlines()

for line in data:
    date = line[0:10]
    time = line[12: 17]
    name = re.findall(r"(?<=- )(.*)(?=:)", line)
    match = re.search(r"(?<=: )(.*)$", line)
    if match:
        text = match.group(0)
        if text != "<Media omitted>":
            if "youtube" not in text:
                if "spotify" not in text:
                    if "https" not in text:
                        text.translate(str.maketrans('', '', string.punctuation))
                        content.append(text.lower() + " ")


with open("cloud.txt", "w+", encoding="utf8") as f:
    for line in content:
        print(repr(line))
        f.write(line)


text = open("cloud.txt", "r", encoding="utf8").read()
wordcloud = WordCloud(width=2400, height=2000, max_font_size=250).generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

