import unittest
from ui import UserInterface

class MockIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def read(self, text):
        return self.inputs.pop(0)

    def printout(self, text):
        self.outputs.append(text)

class TestUserInterface(unittest.TestCase):
    def test_0_input_works(self):
        inputs = ["0"]
        io = MockIO(inputs)
        ui = UserInterface(io)
        ui.start()
        self.assertEqual(io.outputs, ui._printed_text)

    def test_1_input_works(self):
        inputs = ["1", "0"]
        io = MockIO(inputs)
        ui = UserInterface(io)
        ui.start()
        self.assertEqual(io.outputs, ui._printed_text)

    def test_2_input_works(self):
        inputs = ["2", "0"]
        io = MockIO(inputs)
        ui = UserInterface(io)
        ui.start()
        self.assertEqual(io.outputs, ui._printed_text)

    def test_false_input_works(self):
        inputs = ["3", "0"]
        io = MockIO(inputs)
        ui = UserInterface(io)
        ui.start()
        self.assertEqual(io.outputs, ui._printed_text)    

    def test_multiple_inputs_work(self):
        inputs = ["1", "1", "2", "1", "1", "0"]
        io = MockIO(inputs)
        ui = UserInterface(io)
        ui.start()
        self.assertEqual(io.outputs, ui._printed_text)