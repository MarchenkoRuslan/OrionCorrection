from main import loop
import unittest
from unittest.mock import Mock
import random

mock = Mock()
mock.return_value = random.randint(1, 100)
mock.side_effect = lambda: "Был вызван мок!"

print(loop(mock.return_value))
print(mock())

# class InputHandler(unittest.TestCase):
#
#     def setUp(self):
#         self.mock = Mock()
#         self.mock.return_value = random.randint(1, 100)
#         self.mock.side_effect = lambda: "Был вызван мок!"
#
#     def test_loop(self):
#         return loop(self.mock.return_value), self.mock()
