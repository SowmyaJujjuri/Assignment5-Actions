import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_area(self):
        radius = 3
        self.assertEqual(28.26, task.area(radius))

    def test_lastElement(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual([1, 8], task.lastElement(arr))

        arr2 = ["hi", "what", "bye"]
        self.assertEqual(["hi", "bye"], task.lastElement(arr2))


if __name__ == '__main__':
    unittest.main()
