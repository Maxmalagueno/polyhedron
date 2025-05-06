import unittest
from unittest.mock import patch, mock_open

from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0	45.0	45.0	30.0
8	4	16
-0.5	-0.5	0.5
-0.5	0.5	0.5
0.5	0.5	0.5
0.5	-0.5	0.5
-0.5	-0.5	-0.5
-0.5	0.5	-0.5
0.5	0.5	-0.5
0.5	-0.5	-0.5
4	5    6    2    1
4	3    2    6    7
4	3    7    8    4
4	1    4    8    5"""

        cube1 = """200.0 60.0 -140.0 60.0
8 6 12
-0.5 -0.5 0.5
-0.5 0.5 0.5
0.5 0.5 0.5
0.5 -0.5 0.5
-0.5 -0.5 -0.5
-0.5 0.5 -0.5
0.5 0.5 -0.5
0.5 -0.5 -0.5
4 1 2 3 4
4 5 6 2 1
4 3 2 6 7
4 3 7 8 4
4 1 4 8 5
4 5 8 7 6"""

        cube2 = """200.0 0.0 0.0 0.0
8 6 12
-0.5 -0.5 0.5
-0.5 0.5 0.5
0.5 0.5 0.5
0.5 -0.5 0.5
-0.5 -0.5 -0.5
-0.5 0.5 -0.5
0.5 0.5 -0.5
0.5 -0.5 -0.5
4 1 2 3 4
4 5 6 2 1
4 3 2 6 7
4 3 7 8 4
4 1 4 8 5
4 5 8 7 6"""

        cube3 = """200.0 0.0 0.0 0.0
8 6 12
0.0 -0.5 0.5
0.0 0.5 0.5
1.0 0.5 0.5
1.0 -0.5 0.5
0.0 -0.5 -0.5
0.0 0.5 -0.5
1.0 0.5 -0.5
1.0 -0.5 -0.5
4 1 2 3 4
4 5 6 2 1
4 3 2 6 7
4 3 7 8 4
4 1 4 8 5
4 5 8 7 6"""

        planes = """200.0 10.0 30.0 0.0
8 6 12
-1.0 -1.0 -0.5
1.0 -1.0 -0.5
1.0 1.0 -0.5
-1.0 1.0 -0.5
-1.0 -1.0 0.5
1.0 -1.0 0.5
1.0 1.0 0.5
-1.0 1.0 0.5
4 1 2 3 4
4 5 6 7 8
4 1 2 6 5
4 2 3 7 6
4 3 4 8 7
4 4 1 5 8"""

        shadow1 = """1.0 0.0 0.0 0.0
8	2	8
-5	-5	5
-5	5	5
5	5	5
5	-5	5
-0.5 -0.5 -0.5
-0.5 0.5 -0.5
0.5	0.5	-0.5
0.5	-0.5 -0.5
4 1 2 3 4
4 8 7 6 5"""

        fake_file_path1 = 'data/holey_box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path1)
            _file.assert_called_once_with(fake_file_path1)

        fake_file_path2 = 'data/cube1.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=cube1)) as _file:
            self.cube1 = Polyedr(fake_file_path2)
            _file.assert_called_once_with(fake_file_path2)

        fake_file_path3 = 'data/planes'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=planes)) as _file:
            self.planes = Polyedr(fake_file_path3)
            _file.assert_called_once_with(fake_file_path3)

        fake_file_path4 = 'data/shadow1'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=shadow1)) as _file:
            self.shadow1 = Polyedr(fake_file_path4)
            _file.assert_called_once_with(fake_file_path4)

        fake_file_path5 = 'data/cube2.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=cube2)) as _file:
            self.cube2 = Polyedr(fake_file_path5)
            _file.assert_called_once_with(fake_file_path5)

        fake_file_path6 = 'data/cube3.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=cube3)) as _file:
            self.cube3 = Polyedr(fake_file_path6)
            _file.assert_called_once_with(fake_file_path6)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 4)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 16)

    def test_calculate_edges1(self):
        self.assertAlmostEqual(
            Polyedr.calculate_good_edges(self.cube1),
            1800.0,
            places=1
        )

    def test_calculate_edges2(self):
        self.assertEqual(Polyedr.calculate_good_edges(self.planes), 0.0)

    def test_calculate_edges3(self):
        self.assertEqual(Polyedr.calculate_good_edges(self.shadow1), 0.0)

    def test_calculate_edges4(self):
        self.assertAlmostEqual(
            Polyedr.calculate_good_edges(self.cube2),
            2400.0,
            places=1
        )

    def test_calculate_edges5(self):
        self.assertAlmostEqual(
            Polyedr.calculate_good_edges(self.cube3),
            1600.0,
            places=1
        )
