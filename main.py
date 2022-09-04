metai = int(input("Iveskite metus: "))
print(metai)
if (metai % 4 == 0) or (metai % 100 == 0 and metai % 400 ==0):
    print("metai yra keliamieji")
else:
    print("metai yra nekeliamieji")
