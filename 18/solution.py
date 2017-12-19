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
    registers = {'p': p}
    index = 0
    while True:
        operation = commands[index].split(" ")

        command = operation[0]

        if command in ('set', 'add', 'mul', 'mod', 'rcv'):
            modified_register = operation[1]
        else:
            operand = registers.get(operation[1], 0) if operation[1].isalpha() else int(operation[1])

        if command in ('set', 'add', 'mul', 'mod', 'jgz'):
            value = registers.get(operation[2], 0) if operation[2].isalpha() else int(operation[2])

        if command == 'set':
            registers[modified_register] = value
        elif command == 'add':
            registers[modified_register] += value
        elif command == 'mul':
            registers[modified_register] *= value
        elif command == 'mod':
            registers[modified_register] %= value
        elif command == 'jgz':
            if operand > 0:
                index += value
                continue
        elif command == 'snd':
            snd_queue.append(operand)
            if p == 1:
                global sent
                sent += 1
        elif command == 'rcv':
            try:
                registers[modified_register] = rcv_queue.pop(0)
            except IndexError:
                yield 1
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
