import base64

def encode_base64(text: str):
    if text is None:
        return None
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def decode_base64(encoded_text: str) -> str:

    if encoded_text is None:
        return None
    try:
        return base64.b64decode(encoded_text).decode('utf-8')
    except Exception:
        return encoded_text  # Return as-is if decoding fails