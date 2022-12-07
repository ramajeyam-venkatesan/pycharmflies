filename = ["1.raw.txt", "2.db.text", "3.raa.txt"]

for filename in filename :
    filename = filename.replace(".", "-", 1)
    print(filename)
