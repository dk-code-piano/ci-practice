from combo_parser import parse_line


def test_valid_line():
    assert parse_line("User@Example.com:hunter2") == {
        "email": "user@example.com", "password": "hunter2"
    }

def test_password_with_colon():
    assert parse_line("a@b.com:pa:ss")["password"] == "pa:ss"

def test_invalid_lines():
    assert parse_line("no-colon-here") is None
    assert parse_line("notanemail:pw") is None
    assert parse_line("a@b.com:") is None