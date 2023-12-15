infile = "input"

digits = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
]

words = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "zero",
]

codes = []

with open(infile) as f:
    for line in f:
        code = ""
        matches = []
        for match in digits + words:
            low_pos = line.find(match)
            high_pos = -1
            if low_pos > -1:
                high_pos = line.rfind(match)
                matches.append((low_pos, match))
            if high_pos > low_pos:
                matches.append((high_pos, match))
        first = min(matches)[1]
        last = max(matches)[1]
        if first in words:
            first = digits[words.index(first)]
        if last in words:
            last = digits[words.index(last)]
        codes.append(int(first + last))

print(sum(codes))
