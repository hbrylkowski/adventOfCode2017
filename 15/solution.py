a = 65
b = 8921

def gen(value, multiplier, modulo):
    while True:
        value = (value * multiplier) % 2147483647
        while not value % modulo == 0:
            value = (value * multiplier) % 2147483647
        yield value

gen_a = gen(a, 16807, 1)
gen_b = gen(b, 48271, 1)

points = 0
for i in range(40000000):
    if bin(next(gen_a))[-16:] == bin(next(gen_a))[-16:]:
        points += 1

print(points)

gen_a = gen(a, 16807, 4)
gen_b = gen(b, 48271, 8)

points = 0
for i in range(5000000):
    if bin(next(gen_a))[-16:] == bin(next(gen_a))[-16:]:
        points += 1

print(points)
