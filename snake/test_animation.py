import snakelib
import animation
from unittest import TestCase
import importlib

class TestAnimation(TestCase):

    def run_test_from_file(self, test_name):
        test_ok = True
        msg = ""
        try:
            importlib.reload(animation) # reset global variables in student file
            ui = snakelib.SnakeTestInterface(test_name)
            animation.play_animation(ui)
            test_ok = ui.test_succeeded
            if not test_ok:
                ui.raise_err("You quit before the test was over")
        except snakelib._IPyException  as err:
            msg = err.parameter
            test_ok = False

        self.assertTrue(test_ok,msg)

    def test_animation1(self):
        self.run_test_from_file("tests/animation1.txt")

    def test_animation2(self):
        self.run_test_from_file("tests/animation2.txt")

    def test_animation3(self):
        self.run_test_from_file("tests/animation3.txt")

