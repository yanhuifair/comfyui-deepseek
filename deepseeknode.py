import os
from openai import OpenAI


class DeepSeekChatNode:
    def __init__(self):
        current_file_path = os.path.abspath(__file__)
        current_dir = os.path.dirname(os.path.abspath(current_file_path))
        api_key_file_path = os.path.join(current_dir, "api_key.txt")
        with open(api_key_file_path, "r") as file:
            self.api_key = file.read()

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "placeholder": "Type your prompt here"}),
                "max_tokens": ("INT", {"default": "4096", "min": 1, "max": 8192}),
                "temperature": ("FLOAT", {"default": "1", "min": 0, "max": 2, "tooltip": "创造性（越大越有创意，越小越严谨）"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("content",)
    CATEGORY = "Fair/deepseek"

    FUNCTION = "node_function"

    def node_function(self, prompt, max_tokens, temperature):
        client = OpenAI(api_key=self.api_key, base_url="https://api.deepseek.com")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
            stream=False,
            max_tokens=max_tokens,
            temperature=temperature,
        )

        content = response.choices[0].message.content
        return (content,)


class DeepSeekReasonerNode:
    def __init__(self):
        current_file_path = os.path.abspath(__file__)
        current_dir = os.path.dirname(os.path.abspath(current_file_path))
        api_key_file_path = os.path.join(current_dir, "api_key.txt")
        with open(api_key_file_path, "r") as file:
            self.api_key = file.read()

        self.history_content = []

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "placeholder": "Type your prompt here"}),
                "clear_history_content": ("BOOLEAN", {"default": False}),
                "max_tokens": ("INT", {"default": "4096", "min": 1, "max": 8192}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("reasoning_content", "content")
    CATEGORY = "Fair/deepseek"

    FUNCTION = "node_function"

    def node_function(self, prompt, clear_history_content, max_tokens):
        if clear_history_content:
            self.history_content = []

        self.history_content.append({"role": "user", "content": prompt})

        client = OpenAI(api_key=self.api_key, base_url="https://api.deepseek.com")
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=self.history_content,
            stream=False,
            max_tokens=max_tokens,
        )

        reasoning_content = response.choices[0].message.reasoning_content
        content = response.choices[0].message.content

        self.history_content.append({"role": "assistant", "content": content})

        return (reasoning_content, content)
