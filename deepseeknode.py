import os
import string
from openai import OpenAI


class DeepSeekChatNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {}),
                "api_key": ("STRING", {}),
                "max_tokens": ("INT", {"default": "4096", "min": 1, "max": 8192}),
                "temperature": ("INT", {"default": "1", "min": 0, "max": 2}),
                "prompt": ("STRING", {"multiline": True, "placeholder": "Type your prompt here"}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ["content", "total_tokens"]
    CATEGORY = "Fair/deepseek"

    FUNCTION = "node_function"
    OUTPUT_NODE = True

    def node_function(self, image, api_key, max_tokens, temperature, prompt):
        client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

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
        total_tokens = response.usage.total_tokens
        return (
            content,
            total_tokens,
        )


class DeepSeekReasonerNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {}),
                "api_key": ("STRING", {}),
                "max_tokens": ("INT", {"default": "4096", "min": 1, "max": 8192}),
                "prompt": ("STRING", {"multiline": True, "placeholder": "Type your prompt here"}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ["reasoning_content", "content", "total_tokens"]
    CATEGORY = "Fair/deepseek"

    FUNCTION = "node_function"
    OUTPUT_NODE = True

    def node_function(self, image, api_key, max_tokens, temperature, prompt):
        client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
            stream=False,
            max_tokens=max_tokens,
        )

        reasoning_content = response.choices[0].reasoning_content
        content = response.choices[0].message.content
        total_tokens = response.usage.total_tokens
        return (
            reasoning_content,
            content,
            total_tokens,
        )
