from division import make_division

def test_division_by_1():
	result = make_division(5, 1)
	assert "INFO" in result


def test_division_by_0():
	result = make_division(5, 0)
	assert "FEHLER" in result
