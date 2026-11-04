from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from uv_python import python_command


class PythonCommandTests(unittest.TestCase):
    def test_it_runs_this_interpreter_through_uv(self):
        self.assertEqual(python_command('-c', 'pass'),
                         ['uv', 'run', '--no-project', '--python', sys.executable, 'python', '-c', 'pass'])

    def test_it_accepts_a_path_argument(self):
        self.assertEqual(python_command(Path('/a/b.py'), 'x')[-2:], ['/a/b.py', 'x'])


if __name__ == '__main__':
    unittest.main()
