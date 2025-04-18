from .deepseeknodes import DeepSeekChatNode
from .deepseeknodes import DeepSeekChatProNode
from .deepseeknodes import DeepSeekReasonerNode

NODE_CLASS_MAPPINGS = {
    "DeepSeekChatNode": DeepSeekChatNode,
    "DeepSeekChatProNode": DeepSeekChatProNode,
    "DeepSeekReasonerNode": DeepSeekReasonerNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepSeekChatNode": "DeepSeek Chat",
    "DeepSeekChatProNode": "DeepSeek Chat Pro",
    "DeepSeekReasonerNode": "DeepSeek Reasoner",
}


WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
