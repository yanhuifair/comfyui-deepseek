from .deepseeknode import DeepSeekChatNode
from .deepseeknode import DeepSeekReasonerNode

NODE_CLASS_MAPPINGS = {
    "DeepSeekChatNode": DeepSeekChatNode,
    "DeepSeekReasonerNode": DeepSeekReasonerNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepSeekChatNode": "DeepSeek Chat",
    "DeepSeekReasonerNode": "DeepSeek Reasoner",
}


WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
