# mypy: ignore-errors
# flake8: noqa

from functools import reduce

data = open("16-input.txt").read().strip()
bits = bin(int(data, 16))[2:]
if (4 - len(bits) % 4) != 4:
    bits = (4 - len(bits) % 4) * "0" + bits
if data[0] == "0":
    bits = "0000" + bits


def parse_literal(bits):
    literal_bits = ""
    read = 0
    for i in range(0, len(bits), 5):
        literal_bits += bits[i + 1 : i + 5]
        read += 5
        if int(bits[i], 2) == 0:
            break
    return read, int(literal_bits, 2)


def parse_operator_literals_type_0(length, bits):
    read = 0
    literals = []
    while read < length:
        literal_read, literal = parse_packet(bits[read:])
        literals.append(literal)
        read += literal_read
    return read, literals


def parse_operator_literals_type_1(packets, bits):
    read = 0
    results = []
    for _ in range(packets):
        packet_read, result = parse_packet(bits[read:])
        results.append(result)
        read += packet_read
    return read, results


def parse_operator(op_type, bits):
    length_type = int(bits[0], 2)
    if length_type == 0:
        length = int(bits[1:16], 2)
        read, results = parse_operator_literals_type_0(length, bits[16:])
        read += 16
    else:
        packets = int(bits[1:12], 2)
        read, results = parse_operator_literals_type_1(packets, bits[12:])
        read += 12

    if op_type == 0:
        return read, sum(results)
    elif op_type == 1:
        return read, reduce(lambda x, y: x * y, results, 1)
    elif op_type == 2:
        return read, min(results)
    elif op_type == 3:
        return read, max(results)
    elif op_type == 5:
        return read, 1 if results[0] > results[1] else 0
    elif op_type == 6:
        return read, 1 if results[0] < results[1] else 0
    elif op_type == 7:
        return read, 1 if results[0] == results[1] else 0

    raise NotImplementedError


def parse_packet(bits):
    _ = int(bits[:3], 2)
    packet_type = int(bits[3:6], 2)

    if packet_type == 4:
        read, result = parse_literal(bits[6:])
        return 6 + read, result
    else:
        read, result = parse_operator(packet_type, bits[6:])
        return 6 + read, result


print(parse_packet(bits)[1])
