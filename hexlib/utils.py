import base64
import random
import string
from datetime import datetime

def random_string(length=12):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def now_string():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def encode_b64(data: str) -> str:
    return base64.b64encode(data.encode()).decode()

def decode_b64(encoded: str) -> str:
    return base64.b64decode(encoded.encode()).decode()
