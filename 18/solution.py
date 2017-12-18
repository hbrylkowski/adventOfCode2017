data = """set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 316
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19"""


sent = 0


def program(p, rcv_queue, snd_queue):
    commands = data.split("\n")
    registers = {chr(i): 0 for i in range(ord('a'), ord('p')+1)}
    registers['p'] = p
    index = 0
    while True:
        i = commands[index]
        command = i[:3]
        if command == 'set':
            registers[i[4]] = int(registers.get(i[6:], i[6:]))
        elif command == 'add':
            registers[i[4]] += int(registers.get(i[6:], i[6:]))
        elif command == 'mul':
            registers[i[4]] *= int(registers.get(i[6:], i[6:]))
        elif command == 'mod':
            registers[i[4]] %= int(registers.get(i[6:], i[6:]))
        elif command == 'snd':
            snd_queue.append(int(registers.get(i[4:], i[4:])))
            if p == 1:
                global sent
                sent += 1
        elif command == 'rcv':
            try:
                registers[i[4]] = rcv_queue.pop(0)
            except Exception:
                yield 1
                continue
        elif command == 'jgz':
            if int(registers.get(i[4], i[4])) > 0:
                index += int(registers.get(i[6:], i[6:]))
                continue

        index += 1
        yield 0


queue1 = []
queue2 = []

p1 = program(0, queue1, queue2)
p2 = program(1, queue2, queue1)
while True:
    res_a = next(p1)
    res_b = next(p2)
    if res_a and res_b:
        break

print(sent)
