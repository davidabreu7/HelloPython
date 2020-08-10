import maximo


def test_primo1():
    assert maximo.maior_primo(1) == 1


def test_primo2():
    assert maximo.maior_primo(2) == 1


def test_primo3():
    assert maximo.maior_primo(3) == 3


def test_primo4():
    assert maximo.maior_primo(10) == 7


def test_primo5():
    assert maximo.maior_primo(100) == 97
