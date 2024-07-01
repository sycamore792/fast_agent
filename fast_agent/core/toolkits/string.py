class StringUtils:
    @staticmethod
    def is_empty(string: str) -> bool:
        return string is None or string == ""

    @staticmethod
    def is_blank(string: str) -> bool:
        return string is None or string.isspace()

