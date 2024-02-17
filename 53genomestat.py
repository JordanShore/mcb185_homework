
import sys

print(sys.argv[1:])
val = []
total = 0
for x in sys.argv[1:]:
	total += int(x)
	val.append(int(x))

print(total)

val.sort()
print(val)
if len(val) % 2 == 1:
	med = val[len(val) // 2]
else:
	med = (val[len(val) // 2] + val[len(val)//2 - 1]) / 2
print(med)