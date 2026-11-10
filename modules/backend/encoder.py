import base64


def base64_encode(data: bytes) -> str:
    return base64.b64encode(data).decode('ascii')


def base64_decode(text: str) -> bytes:
    return base64.b64decode(text, validate=True)
