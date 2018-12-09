from random import choice

def generate():
    motions = ['up', 'right', 'left', 'down']
    maze = []
    maze.append("up ")
    f = open('maze.txt', 'w')
    for i in range(1672):
        new = choice(motions)
        old = maze[i].replace(' ', '')
        print(old, new)
        if (new == 'up' and old == 'down') or (new == 'down' and old == 'up'):
            maze.append(choice(['left', 'right']) + ' ')
        elif (new == 'left' and old=="right") or (new=='right' and old=='left'):
            maze.append(choice(['up', 'down']) + ' ')
        elif (new == 'left' and old == 'left') or (new == 'right' and old == 'right'):
            maze.append(choice(['up', 'down']) + ' ')
        else:
            maze.append(new + ' ')
    f.writelines(maze)
    f.close()
generate()
