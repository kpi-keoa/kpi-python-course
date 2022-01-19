import sys

def get_differs(line_one: str, line_two: str) -> str:
    return ','.join(set(line_one) - set(line_two))

trim = True

with open('1.txt') as f1, open('2.txt') as f2:
    pairs = list(zip(f1.readlines(), f2.readlines()))
    byte = 0
    for pair in pairs:
        line1 = pair[0].rstrip()
        line2 = pair[1].rstrip()
        if line1 != line2:
            if(~trim):
                byte += sys.getsizeof(get_differs(line1, line2))
            else:
                length = len(line1)
                byte += sys.getsizeof(get_differs(line1, line2[:length + 1]))
print(f"In this files {byte} different bytes.")
