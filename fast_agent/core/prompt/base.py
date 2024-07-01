# base_prompt
import abc

from fast_agent.core.toolkits.string import StringUtils


class Prompt(abc.ABC):

    def __init__(self, prompt_string: str = ""):
        self.prompt_string = prompt_string

    def invoke(self, input_value: dict) -> str:
        if StringUtils.is_blank(self.prompt_string):
            return ""
        _s = self.prompt_string
        for key, value in input_value.items():
            _s = _s.replace(f"{{{key}}}", str(value))
        return _s
