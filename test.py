from main import loop
import unittest
from unittest.mock import Mock


class InputHandler(unittest.TestCase):

    def setUp(self):
        self.mock = Mock()
        self.mock.return_value = [5, 10, 20, 30, 50]
        self.waiting = [120, 3628800, 2432902008176640000, 265252859812191058636308480000000,
                   30414093201713378043612608166064768844377641568960512000000000000]
        self.mock.side_effect = lambda n: f"Был вызван мок номер {n}!"

    def test_loop(self):
        for n in range(0, 5):
            a = loop(self.mock.return_value[n])
            b = self.waiting[n]
            self.assertEqual(a, b)
            print(self.mock.side_effect(n + 1))
