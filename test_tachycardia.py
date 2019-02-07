import pytest


def test_tachycardia():
    from tachycardia import is_tachycardic

    result = is_tachycardic("tachycardia")
    expected = False

    assert result == expected


@pytest.mark.parametrize("test_string, expected", [
    (" TacHycardic", True),
    ("tachycardic!", True),
    (".Tachycardic", True),
    ("TACHYCARDIC?", True),
    ("tach y cardic", True),
])
def test_tachycardia2(test_string, expected):
    from tachycardia import is_tachycardic

    answer = is_tachycardic(test_string)
    assert answer == expected
