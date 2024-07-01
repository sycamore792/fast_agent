from abc import ABC, abstractmethod


class LargeLanguageModel(ABC):
    """
    llm 顶级抽象类
    """

    @abstractmethod
    def init_clint(self):
        """
        初始化客户端
        :return:
        """
        pass

    @abstractmethod
    def llm_inference_with_stream(self):
        """
        流式推理
        :return:
        """
        pass

    @abstractmethod
    def llm_inference_without_stream(self):
        """
        非流式推理
        :return:
        """
        pass
