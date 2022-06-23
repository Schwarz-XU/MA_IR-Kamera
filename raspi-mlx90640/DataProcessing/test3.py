import random
from datetime import datetime

now1 = datetime.now()
i = random.random()

#y1 = i * 1.067 - 3.221
y1 = pow(i, 4) * 1.234 - pow(i, 3) * 0.979 + pow(i, 2) * 900 - i + 100
now2 = datetime.now()
print(y1)
print(now2-now1)
x1 = 44.5
y3 = pow(10, -7) * (-5) * pow(x1, 6) + 8 * pow(10, -5) * pow(x1, 5) - 0.0059 * pow(x1, 4) + 0.2199 * pow(x1, 3) - 4.5318 * pow(x1, 2) + 50.076 * x1 - 220.86
print(y3)
