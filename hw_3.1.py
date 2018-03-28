

mass = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
m = [x ** 2 for x in mass if x % 3 == 0 and x % 4 == 0]
print(m)