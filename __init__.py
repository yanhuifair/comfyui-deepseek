from .deepseeknode import DeepSeekNode

NODE_CLASS_MAPPINGS = {
    "DeepSeekNode": DeepSeekNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepSeekNode": "DeepSeek",
}


WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
