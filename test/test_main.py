import unittest
from main import Example

class ExampleTest(unittest.TestCase):
  def test_set_description(self):
    example = Example()
    example.set_description('Hi There!')
    self.assertEqual(example.get_description(), 'Hi There!')

if __name__ == '__main__':
  unittest.main()