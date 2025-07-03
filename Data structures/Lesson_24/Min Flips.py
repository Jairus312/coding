a = [0, 1, 1, 0, 0, 0, 0, 1]
zeroflip = 0
oneflip = 0
for i in range(len(a)):
  if a[i] == 0:
    zeroflip += 1
  if a[i] == 1:
    oneflip += 1
print("It wil take,", zeroflip,
      "flips to change all values to one\n It will take", oneflip,
      "flips to change all values to zero")
