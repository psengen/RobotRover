
class Robot:
    def __init__(self,position,direction):
        print("Hello! Robot coming online.")
        print_instructions()
        self.position = position
        self.direction = direction

    def get_direction(self):
        return self.direction

    def get_position(self):
        return self.position

    def turn(self,move):
        if move=='L':
            self.direction = (self.direction + 3) % 4
        elif move=='R':
            self.direction = (self.direction + 1) % 4    

    def forward(self):
        if(self.direction==0):
            self.position["y"]=self.position["y"]+1
        elif(self.direction==1):
            self.position["x"]=self.position["x"]+1
        elif(self.direction==2):
            self.position["y"]=self.position["y"]-1
        elif(self.direction==3):
            self.position["x"]=self.position["x"]-1    


def print_instructions():
    print('Command the robot with:')
    print('L - turn left')
    print('R - turn right')
    print('M - move forward')
    print('? - print this message')
    print('Q - quit')


directions={0:"North",1:"East",2:"South",3:"West"}

def initiate_robot():
    robot = Robot({'x':0,'y':0},1)
    return robot

def turn_robot(robot,dir):
    robot.turn(dir)
    print("Robot at", robot.get_position() ,"facing", directions[robot.get_direction()])    
    return robot

def move_robot(robot):
    robot.forward()
    print("Robot at", robot.get_position() ,"facing", directions[robot.get_direction()])    
    return robot