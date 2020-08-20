import unittest
from Util import (initiate_robot,turn_robot,move_robot)

class TestUtil(unittest.TestCase):

    def test_init_robot(self):
        robot = initiate_robot()
        self.assertEqual(robot.get_direction(),1)
        self.assertEqual(robot.get_position(),{'x':0,'y':0})

    def test_turn_robot(self):
        robot = initiate_robot()
        robot = turn_robot(robot,'L')
        self.assertEqual(robot.get_direction(),0)
        robot = turn_robot(robot,'L')
        self.assertEqual(robot.get_direction(),3)
        robot = turn_robot(robot,'L')
        self.assertEqual(robot.get_direction(),2)
        robot = turn_robot(robot,'L')
        self.assertEqual(robot.get_direction(),1)
        robot = turn_robot(robot,'R')
        self.assertEqual(robot.get_direction(),2)
        robot = turn_robot(robot,'R')
        self.assertEqual(robot.get_direction(),3)
        robot = turn_robot(robot,'R')
        self.assertEqual(robot.get_direction(),0)
        robot = turn_robot(robot,'R')
        self.assertEqual(robot.get_direction(),1)


    def test_move_robot(self):
        robot = initiate_robot()
        robot = move_robot(robot)
        self.assertEqual(robot.get_position()['x'],1)


    def test_move_and_turn_robot(self):
        robot = initiate_robot()
        robot = turn_robot(robot,'L')
        robot = move_robot(robot)
        self.assertEqual(robot.get_position()['x'],0)
        self.assertEqual(robot.get_position()['y'],1)
        robot = turn_robot(robot,'L')
        robot = move_robot(robot)
        self.assertEqual(robot.get_position()['x'],-1)
        self.assertEqual(robot.get_position()['y'],1)
        robot = turn_robot(robot,'R')
        robot = move_robot(robot)
        self.assertEqual(robot.get_position()['x'],-1)
        self.assertEqual(robot.get_position()['y'],2)
        robot = turn_robot(robot,'R')
        robot = move_robot(robot)
        self.assertEqual(robot.get_position()['x'],0)
        self.assertEqual(robot.get_position()['y'],2)


if __name__ == '__main__':
	unittest.main()    