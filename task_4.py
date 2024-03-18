import csv

with open("songs.csv", encoding = "utf-8") as file:
    data = list(csv.reader(file, delimiter = ";"))[1:]
    while True:
        print("Введите имя артиста: ")
        artist = str(input())
        flag = False
        if artist == "0":
            break
        for e in range(len(data)):
            if data[e][1] == artist and data[e][2] != 'unknown':
                print(f"У {artist} найдена песня: {data[e][2]}")
                flag = True
        if not flag:
            print("К сожалению, ничего не удалось найти")