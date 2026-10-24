import pytest

from app import add, subtract, multiply, divide, main


def test_add():
    assert add(10, 5) == 15


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(10, 5) == 50


def test_divide():
    assert divide(10, 5) == 2


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_main(capsys):
    main()

    captured = capsys.readouterr()

    assert "Python CI Practice Application" in captured.out
    assert "10 + 5 = 15" in captured.out
    assert "10 - 5 = 5" in captured.out
    assert "10 * 5 = 50" in captured.out
    assert "10 / 5 = 2.0" in captured.out
