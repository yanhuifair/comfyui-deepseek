from openai import OpenAI
import os


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
                "temperature": ("FLOAT", {"default": "1", "min": 0, "max": 2}),
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

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "placeholder": "Type your prompt here"}),
                "max_tokens": ("INT", {"default": "4096", "min": 1, "max": 8192}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("reasoning_content", "content")
    CATEGORY = "Fair/deepseek"

    FUNCTION = "node_function"

    def node_function(self, prompt, max_tokens):
        client = OpenAI(api_key=self.api_key, base_url="https://api.deepseek.com")
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
            stream=False,
            max_tokens=max_tokens,
        )

        reasoning_content = response.choices[0].message.reasoning_content
        content = response.choices[0].message.content
        return (reasoning_content, content)
