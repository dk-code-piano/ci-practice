def parse_line(line: str) -> dict | None:
    """Parse 'email:password' into a dict. Return None if invalid."""
    line = line.strip()
    if ":" not in line:
        return None
    email, password = line.split(":", 1)
    if "@" not in email or not password:
        return None
    return {"email": email.lower(), "password": password}