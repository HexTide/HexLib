from hexlib.ai_prompt import PromptBuilder
from hexlib.session import SessionManager
from hexlib.filetools import write_text, read_text
from hexlib.utils import random_string, now_string
from hexlib.config import TEMPLATE_DIR

# 1. Prompt kullanımı
prompt = PromptBuilder(template_dir=TEMPLATE_DIR)
prompt.load_template("demo.txt")
result = prompt.render(name="Aytuğ", tool="HexLib")

# 2. Session örneği
session = SessionManager()
session.save("user_123", {"last_run": now_string()})
data = session.load("user_123")

# 3. Dosya kaydetme
write_text("result.txt", result)
loaded = read_text("result.txt")

# 4. Ekrana yazdır
print("Generated Prompt:", loaded)
print("Session Data:", data)
print("Random ID:", random_string())
