import csv

with open("songs.csv", encoding = "utf-8") as file:
    data = list(csv.reader(file, delimiter = ";"))[1:]
    artistsR = set()
    artistsF = set()
    for e in range(len(data)):
        flag = False
        for i in data[e][1]:
            if i in "йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ":
                artistsR.add(data[e][1])
                flag = True
                break
        if not flag:
            artistsF.add(data[e][1])

artistsR = list(artistsR)
artistsF = list(artistsF)

with open("russian_artists.txt", 'w') as file:
    for i in range(len(artistsR)):
        file.writelines(artistsR[i] + "\n")
with open("foreign_artists.txt", 'w') as file:
    for i in range(len(artistsF)):
        file.writelines(artistsF[i] + "\n")