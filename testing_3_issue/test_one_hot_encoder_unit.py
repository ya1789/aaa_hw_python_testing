from unittest import TestCase, main
from one_hot_encoder import fit_transform


class TestOneHotEncoder(TestCase):
    def test_fit_transform(self):
        actual = fit_transform(['котики', 'собачки', 'попугайчики', 'поросята', 'поросята', 'котики'])
        expected = [('котики', [0, 0, 0, 1]),
                    ('собачки', [0, 0, 1, 0]),
                    ('попугайчики', [0, 1, 0, 0]),
                    ('поросята', [1, 0, 0, 0]),
                    ('поросята', [1, 0, 0, 0]),
                    ('котики', [0, 0, 0, 1])]

        self.assertEqual(actual, expected)

    def test_fit_transform_brief(self):
        actual = fit_transform('a', 'c', 'a', 'a', 'a', 'a')
        self.assertIn(('c', [1, 0]), actual)

    def test_fit_transform_incorrect_type(self):
        with self.assertRaises(TypeError) as e:
            fit_transform(0)

    def test_fit_transform_no_argument(self):
        with self.assertRaises(TypeError) as e:
            fit_transform()
        self.assertEqual('expected at least 1 arguments, got 0', e.exception.args[0])


if __name__ == '__main__':
    main()
