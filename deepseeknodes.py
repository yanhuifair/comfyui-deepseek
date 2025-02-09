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
                "max_tokens": ("INT", {"default": "4096", "min": 1, "max": 8192, "tooltip": "Integer between 1 and 8192. The maximum number of tokens that can be generated in the chat completion. The total length of input tokens and generated tokens is limited by the model's context length. If max_tokens is not specified, the default value 4096 is used."}),
                "temperature": ("FLOAT", {"default": "1", "min": 0, "max": 2, "tooltip": "What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or top_p but not both."}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("content",)
    CATEGORY = "Fair/deepseek"

    FUNCTION = "node_function"

    def node_function(
        self,
        prompt,
        max_tokens,
        temperature,
    ):
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


class DeepSeekChatProNode:
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
                "frequency_penalty": ("FLOAT", {"default": "0", "min": -2, "max": 2, "tooltip": "Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim."}),
                "max_tokens": ("INT", {"default": "4096", "min": 1, "max": 8192, "tooltip": "Integer between 1 and 8192. The maximum number of tokens that can be generated in the chat completion. The total length of input tokens and generated tokens is limited by the model's context length. If max_tokens is not specified, the default value 4096 is used."}),
                "presence_penalty": ("FLOAT", {"default": "0", "min": -2, "max": 2, "tooltip": "Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics."}),
                "temperature": ("FLOAT", {"default": "1", "min": 0, "max": 2, "tooltip": "What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or top_p but not both."}),
                "top_p": ("FLOAT", {"default": "1", "min": 0, "max": 2, "tooltip": "An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or temperature but not both."}),
                "logprobs": ("BOOLEAN", {"default": True, "tooltip": "Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the content of message."}),
                "top_logprobs": ("INT", {"default": "0", "min": 0, "max": 20, "tooltip": "An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. logprobs must be set to true if this parameter is used."}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("content",)
    CATEGORY = "Fair/deepseek"

    FUNCTION = "node_function"

    def node_function(self, prompt, frequency_penalty, max_tokens, presence_penalty, temperature, top_p, logprobs, top_logprobs):
        client = OpenAI(api_key=self.api_key, base_url="https://api.deepseek.com")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
            stream=False,
            frequency_penalty=frequency_penalty,
            max_tokens=max_tokens,
            presence_penalty=presence_penalty,
            temperature=temperature,
            top_p=top_p,
            logprobs=logprobs,
            top_logprobs=top_logprobs,
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
                "max_tokens": ("INT", {"default": "4096", "min": 1, "max": 8192, "tooltip": "The maximum length of the final response after the CoT output is completed, defaulting to 4K, with a maximum of 8K. Note that the CoT output can reach up to 32K tokens, and the parameter to control the CoT length"}),
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
