#!/usr/local/bin/python3
import sys, select
print("Welcome to blind maze! You access to commands: right, left, up, down. You mission - pass a maze! Good luck!")

try:
    f = open('maze.txt', 'r').readlines()
    for elem in f:
        allow_step = elem.split()
    i, o, e = select.select( [sys.stdin], [], [], 1 )

    for elem in f:
        allow_step = elem.split()

    count = 0
    step = sys.stdin.readline().strip().rstrip()
    for i in allow_step:
        if step == i:
            count += 1
            print('yes!')
            step = sys.stdin.readline().strip().rstrip()
            if count <= 1671:
                continue
            else:
                print('You win! Flag is cupctf{1_50lv3_7h15_m4z3}')
                sys.exit(0)
        else:
            print('you loose.')
            sys.exit(0)
            break
except SystemExit:
    sys.exit(0)
except:
    sys.exit(0)
