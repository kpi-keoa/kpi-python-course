from random import choice
from string import (ascii_lowercase as low,
                    ascii_uppercase as high)

# TODO: find proper functions in random module
#       to build random sequences
#       i.e ''.join(sample(low, 5))

def gen_name(length=5):
    length = int(length)
    if length <= 0:
        raise TypeError(f'length should be > 0')
    # fast
    # s = ''.join(choice(high) if i == 0 else choice(low) for i in range(length))

    # concise
    s = ''
    for i in range(length):
        if i == 0:
            s += choice(high)
        else:
            s += choice(low)
        
    return s
