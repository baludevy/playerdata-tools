import uuid
import hashlib


def generate_name_uuid(name: str) -> uuid.UUID:
    # name to bytes
    name_bytes = f"OfflinePlayer:{name}".encode("utf-8")

    # md5 hashing
    hash = hashlib.md5(name_bytes).digest()

    return uuid.UUID(bytes=hash[:16], version=3)


def file_format(uuid: str) -> str:
    return f"{uuid}.dat"
