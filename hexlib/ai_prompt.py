import os

class PromptBuilder:
    def __init__(self, template_dir="templates"):
        self.template_dir = template_dir
        self.template = ""

    def load_template(self, filename):
        path = os.path.join(self.template_dir, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Prompt file not found: {path}")
        with open(path, "r", encoding="utf-8") as file:
            self.template = file.read()
        return self

    def render(self, **kwargs):
        if not self.template:
            raise ValueError("No template loaded.")
        return self.template.format(**kwargs)
