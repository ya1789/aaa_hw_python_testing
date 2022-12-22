import pytest
from one_hot_encoder import fit_transform


def test_fit_transform():
    actual = fit_transform(['котики', 'собачки', 'попугайчики', 'поросята', 'поросята', 'котики'])
    expected = [('котики', [0, 0, 0, 1]),
                ('собачки', [0, 0, 1, 0]),
                ('попугайчики', [0, 1, 0, 0]),
                ('поросята', [1, 0, 0, 0]),
                ('поросята', [1, 0, 0, 0]),
                ('котики', [0, 0, 0, 1])]

    assert (actual == expected)


def test_fit_transform_one_arg():
    assert fit_transform('a') == [('a', [1])]


def test_fit_transform_no_argument():
    with pytest.raises(TypeError) as e:
        fit_transform()
    assert 'expected at least 1 arguments, got 0' == e.value.args[0]


def test_fit_transform_incorrect_type():
    with pytest.raises(TypeError) as e:
        fit_transform(0)


if __name__ == '__main__':
    pytest.main()
