import csv
import datetime

with open("songs.csv", encoding = "utf-8") as file:
    data = list(csv.reader(file, delimiter = ";"))[1:]
    for e in range(len(data)):
        if data[e][1] == "unknown" or data[e][2] == "unknown":
            continue
        else:
            if data[e][0] == "0":
                dates = list(data[e][-1].split("."))
                d = (datetime.date(2023,5,12) - datetime.date(int(dates[-1]), int(dates[-2]), int(dates[-3]))).days
                streams = round(abs(d / (len(data[e][1]) + len(data[e][2]))) * 10000)
                data[e][0] = str(streams)
with open("songs_new.csv", "w", encoding = "utf-8", newline = "") as file:
    w = csv.writer(file, delimiter = ";", quotechar = "'")
    w.writerow(["streams","artist_name","track_name","date"])
    w.writerows(data)