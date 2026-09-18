nilai = [90, 85, 78, 65, 55,30, 0,]

for variabel in nilai:
    if variabel >= 85:
        grade = "A"
    elif variabel >= 75:
        grade = "B"
    elif variabel >= 65:
        grade = "C"
    elif variabel >= 50:
        grade = "D"
    else:
        grade = "E"

    print("Nilai:", variabel, "| Grade:", grade)