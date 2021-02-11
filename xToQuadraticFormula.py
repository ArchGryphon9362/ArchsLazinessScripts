x1 = float(input("x1: "))
x2 = float(input("x2: "))

if int(x1) == x1:
    x1 = int(x1)

if int(x2) == x2:
    x2 = int(x2)

xPx = round(x1 + x2, 2)
xXx = round(x1 * x2, 2)

fSign = "+ "
sSign = "- "

if xPx <= 0:
    fSign = "+ "
    xPx*=-1

if xXx <= 0:
    sSign = "- "
    xXx*=-1

print("x² " + fSign + str(xPx) + "x " + sSign + str(xXx) + " = 0")
