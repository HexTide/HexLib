
<p align="center">
  <img src="https://github.com/HexTide.png" width="100" alt="Hex Logo"/>
</p>

<h1 align="center">HexLib – Universal Library for HEX Bots</h1>
<p align="center"><strong>Write. Share. Reuse.</strong></p>
<p align="center">
Prompt Engine • Session Manager • JSON Tools • Automation Backbone
</p>
<p align="center">
Built by <a href="https://github.com/HexTide">HexTide</a>
</p>

---

## 🧠 What is HexLib?

**HexLib** is the core utility library used by all HEX modules.  
It powers prompt templating, session handling, file operations, and configuration logic across the entire HEX ecosystem.

- 🔁 Reusable utilities  
- 🧠 Prompt engine for AI interactions  
- 📄 Session-aware automation state tracking  
- 💾 File and JSON helpers  
- ✅ Designed for both Lite and Pro modules

---

## 📁 Included Modules

| File | Description |
|------|-------------|
| `ai_prompt.py` | AI prompt builder & templating |
| `session.py`   | User session & context tracker |
| `filetools.py` | Read/write utilities (JSON, TXT) |
| `utils.py`     | Random string, time, encoding |
| `config.py`    | Default values & constants |

---

## 🧪 Usage Example

```python
# Example usage of PromptBuilder from HexLib
from hexlib.ai_prompt import PromptBuilder

builder = PromptBuilder()
builder.load_template("pitch.txt")
prompt = builder.render(product="SmartBot", goal="boost conversions")
```

---

## 🔐 License

This library is licensed and bound to HEX system modules.  
It may only be used in official HEX bots.  
See LICENSE.txt for usage rules.

<p align="center">
  <strong>© HEX Automation • All Rights Reserved</strong><br/>
  Created by <a href="https://github.com/HexTide">HexTide</a> – Build once. Use everywhere.
</p>
