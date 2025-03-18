students = [
    ["BSIT", ["David", "Alenere", ]],
    ["BSCS", ["Jaymar", "Emman", "Patrick"]]
]

for x in students:
    print(x[0])
    for y in x[1]:
        print("-" + y)
    print()