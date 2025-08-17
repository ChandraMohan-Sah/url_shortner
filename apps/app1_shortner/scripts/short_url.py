import string
from .unique_id import get_unique_id

BASE62 = string.digits + string.ascii_letters  # 0-9, a-z, A-Z

def encode_base62(num: int) -> str:
    if num == 0:
        return BASE62[0]
    base62 = []
    while num > 0:
        num, rem = divmod(num, 62)
        base62.append(BASE62[rem])
        num //= 62
    return ''.join(reversed(base62))

def get_short_id() -> str:
    """Generate a base62 encoded unique ID."""
    unique_id = get_unique_id()
    return encode_base62(unique_id)


def get_short_url() -> str:
    """Return only the short ID (without domain)."""
    return get_short_id()