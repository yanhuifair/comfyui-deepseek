import os
import string
from openai import OpenAI


class DeepSeekNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key": ("STRING", {}),
                "model": (["deepseek-chat", "deepseek-reasoner"], {"default": "deepseek-chat"}),
                "prompt": ("STRING", {"multiline": True, "placeholder": "Type your prompt here"}),
            }
        }

    RETURN_TYPES = (
        "STRING",
        "STRING",
    )
    RETURN_NAMES = ["message", "total_tokens"]
    CATEGORY = "Fair/deepseek"

    FUNCTION = "node_function"
    OUTPUT_NODE = True

    def node_function(self, api_key, model, prompt):
        client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
            stream=False,
        )

        print(response)
        out_string = response.choices[0].message.content
        total_tokens = response.usage.total_tokens
        return (
            out_string,
            total_tokens,
        )
