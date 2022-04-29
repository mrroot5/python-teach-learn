import unittest

from subprocess import Popen, PIPE
from os import linesep


class HelloWorldTestCase(unittest.TestCase):
    def print_hello_world(self):
        linesep_bytes = linesep.encode("utf8")
        possible_values = [
            b'hello world' + linesep_bytes,
            b'hello world!' + linesep_bytes,
            b'Hello World' + linesep_bytes,
            b'Hello World!' + linesep_bytes
        ]
        cmd = "python3 main.py"
        proc = Popen(cmd.split(' '), stdout=PIPE, stderr=PIPE)
        (output, error) = proc.communicate()
        self.assertIn(output, possible_values)


if __name__ == '__main__':
    unittest.main()
