
with open('input') as f:
    steps = f.read()


dancers = [chr(i) for i in range(ord('a'), ord('p')+1)]


def dance(d):
    dancers = [x for x in d]
    for s in steps.split(","):
        if s[0] == "s":
            to_move = int(s[1:])
            dancers = dancers[-to_move:] + dancers[:-to_move]
        elif s[0] == "x":
            a = int(s[s.index("x") + 1:s.index("/")])
            b = int(s[s.index("/") + 1:])
            dancers[a], dancers[b] = dancers[b], dancers[a]
        elif s[0] == "p":
            a = int(dancers.index(s[1]))
            b = int(dancers.index(s[3]))
            dancers[a], dancers[b] = dancers[b], dancers[a]
    return dancers


print("".join(dance(dancers)))

dances_history = []
while "".join(dancers) not in dances_history:
    dances_history.append("".join(dancers))
    dancers = dance(dancers)

print("".join(dances_history[1000000000 % len(dances_history)]))
