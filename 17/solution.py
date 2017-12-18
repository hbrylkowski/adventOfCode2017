import progressbar

buffer = [0]
steps = 377
pos = 0

for i in range(1, 2018):
    pos += steps
    pos %= i
    pos += 1
    buffer.insert(pos, i)

print(buffer[buffer.index(2017)+1])

bar = progressbar.ProgressBar()
before_zero = 0
after_zero = 1
for i in bar(range(1, 50000000)):
    pos += steps
    pos %= i
    if pos <= before_zero:
        before_zero
    pos += 1
    if pos == before_zero + 1:
        after_zero = i

print(after_zero)
