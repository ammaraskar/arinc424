import arinc424.record as a424
import unittest


class TestVHFNavaid(unittest.TestCase):

    def test_file_read(self):
        with open('./tests/example_data/vhf_navaid.txt') as f:
            for idx, line in enumerate(f.readlines()):
                r = a424.Record()
                if idx in range(6):
                    self.assertEqual(r.read(line), None)
                else:
                    self.assertEqual(r.read(line), 0)
                    # self.assertEqual(r.decode(), 0)


if __name__ == '__main__':
    unittest.main()
