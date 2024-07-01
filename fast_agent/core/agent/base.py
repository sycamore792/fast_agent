from typing import Dict


class Agent:
    """
    Agent
    """

    def __init__(self, base_info: Dict[str, str]):
        """
        base_info: 智能体基础信息
        action_logs_base: 智能体行为日志存储
        """
        self.base_info = base_info
        self.action_logs_base = None
