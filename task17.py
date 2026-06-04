parol = input("Parol: ")

bor = False

for belgi in parol:
    if belgi.digit():
        bor = True

print(bor)
