row = 1

while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d" % (col, row, row * col), end="\t\t")
        col += 1
    print("")
    row += 1

# P233

