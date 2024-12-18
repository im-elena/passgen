import random
import argparse

parser = argparse.ArgumentParser(
    prog='PassGen',
    description='Generates password with provided condition',
    epilog='Default settings: --capital 1 --small 3 --digits 4 --length 8')
parser.add_argument('-c', '--capital', default=1, help='Minimal amount of capital letters', type=int)
parser.add_argument('-s', '--small', default=3, help='Minimal amount of small letters', type=int)
parser.add_argument('-d', '--digits', default=4, help='Minimal amount of digits', type=int)
parser.add_argument('-l', '--length', default=8, help='Total length', type=int)
parser.add_argument('-i', '--iterations', default=1, help='How many passwords to generate', type=int)
parser.add_argument('--seed', help='Random seed', type=int)
parser.add_argument('-o', '--omit', help='Omit header and numbering', action='store_true')
parser.add_argument('--special', help='Use special characters', action='store_true')

args = parser.parse_args()

capitals = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]
small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
special = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
heap = []
heap.extend(capitals)
heap.extend(small)
heap.extend(digits)

if args.seed is not None:
    if not args.omit: print ("Generating password using provided seed {}".format(args.seed))
    random.seed(args.seed)
else:
    random.seed()

if (args.capital + args.small + args.digits) != args.length:
    if args.length < (args.capital + args.small + args.digits):
        args.length = args.capital + args.small + args.digits
        if not args.omit: print("Maximum length redefined to {}".format(args.length))
    else: args.small = args.length - (args.capital + args.digits)

if not args.omit: print(f"Will be generated {args.iterations} passwords with {args.capital} capitals, {args.small} small, {args.digits} digits and {args.length} total length")

for iteration in range(args.iterations):
    #initializing counters
    cap_count = args.capital
    sm_count = args.small
    dig_count = args.digits
    pos = 0
    passw = '' #reset password
    spec_added = False

    while pos < args.length:
        if args.special and not spec_added: val = random.randint(0, len(heap)*2)
        else: val = random.randint(0, len(heap) - 1)
        if val >= len(heap):
            passw = passw + special[random.randint(0, len(special)-1)]
            pos += 1
            val = random.randint(0, len(heap) - 1)
            spec_added = True
        if capitals.count(heap[val]) > 0 and cap_count > 0:
            passw = passw + (heap[val])
            cap_count -= 1
            pos += 1
        elif small.count(heap[val]) > 0 and sm_count > 0:
            passw = passw + (heap[val])
            sm_count -= 1
            pos += 1
        elif digits.count(heap[val]) > 0 and dig_count > 0:
            passw = passw + (heap[val])
            dig_count -= 1
            pos += 1

    if args.omit: print(passw)
    else: print("{:>2}. {}".format(iteration + 1, passw))
