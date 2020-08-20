import unittest
from Rover import executeCommand
from Util import (initiate_robot,turn_robot,move_robot)

class TestRover(unittest.TestCase):

    def test_execute_command(self):
        robot = initiate_robot()
        self.assertEqual(robot.get_position(),{'x':0,'y':0})
        robot = executeCommand(robot,'L')
        self.assertEqual(robot.get_direction(),0)
        robot = executeCommand(robot,'M')
        self.assertEqual(robot.get_direction(),0)
        self.assertEqual(robot.get_position(),{'x':0,'y':1})
        robot = executeCommand(robot,'L')
        self.assertEqual(robot.get_direction(),3)
        robot = executeCommand(robot,'M')
        self.assertEqual(robot.get_position(),{'x':-1,'y':1})
        robot = executeCommand(robot,'R')
        self.assertEqual(robot.get_direction(),0)
        robot = executeCommand(robot,'M')
        self.assertEqual(robot.get_position(),{'x':-1,'y':2})


if __name__ == '__main__':
	unittest.main()    