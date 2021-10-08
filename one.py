import csv

file1 = open("upload.csv", "r", encoding="cp932")
file2 = open("test.csv", "w", encoding="cp932")

zaiko = csv.reader(file1)
disp = csv.writer(file2)
cnt = 0

for row in zaiko:
	if cnt != 0:
		if row[16] == "0":
			newRow = [""] * 79
			newRow[0] = "1"
			newRow[3] = row[3]
			newRow[16] = "1"
			disp.writerow(newRow)
	else:
		disp.writerow(row)
		print(len(row))
	cnt += 1