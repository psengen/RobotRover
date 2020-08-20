import sys
from Util import (print_instructions,initiate_robot,turn_robot,move_robot)

def executeCommand(robot, command):
    if command == '?':
        print_instructions()
    elif command == 'L' or command == 'R':
        robot = turn_robot(robot,command)
    elif command == 'M':
        robot = move_robot(robot)
    else:
        print('Command is not applicable')
    return robot


def commandMode(robot):
    try:
        command = input().strip()
        while command[0] != 'Q':
            robot = executeCommand(robot, command)
            command = input().strip()
    except Exception as e:
        print(e)


def fileReaderMode(robot, fileName):
    try:
        with open(fileName) as file:
            commands = file.readlines()
            for command in commands:
                robot = executeCommand(robot, command.replace('\n', '').strip())
    except Exception as e:
        print(e)


def main():
    robot = initiate_robot()
    if len(sys.argv) > 1:
        fileReaderMode(robot, sys.argv[1])
    else:
        commandMode(robot)


if __name__ == '__main__':
    main()
