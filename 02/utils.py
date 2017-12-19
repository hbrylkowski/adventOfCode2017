def to_table(spreadsheet, separator):
    return [[int(v) for v in l.split(separator)] for l in spreadsheet.split("\n")]


def checksum(spreadsheet, separator):
    table = to_table(spreadsheet, separator)
    return sum([max(v) - min(v) for v in table])


def checksum_modulo(spreadsheet, separator):
    table = to_table(spreadsheet, separator)
    s = 0
    for l in table:
        for v in l:
            for d in l:
                if v != d and v % d == 0:
                    s += v // d
    return s
