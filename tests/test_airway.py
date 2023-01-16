import arinc424.record as a424
import unittest


class TestAirway(unittest.TestCase):

    def test_file_read(self):
        with open('./tests/example_data/enroute_airway.txt') as f:
            for idx, line in enumerate(f.readlines()):
                r = a424.Record()
                self.assertEqual(r.read(line), 0)
                print()
                self.assertEqual(r.decode(), 0)


if __name__ == '__main__':
    unittest.main()
