from .deepseeknode import DeepSeekChatNode

NODE_CLASS_MAPPINGS = {
    "DeepSeekChatNode": DeepSeekChatNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepSeekChatNode": "DeepSeek Chat",
}


WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
