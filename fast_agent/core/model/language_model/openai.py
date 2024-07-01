from openai import OpenAI
import os
import logging

from fast_agent.core.model.language_model.base import LargeLanguageModel


class OpenAILargeLanguageModel(LargeLanguageModel):

    def __init__(self, api_key=None, base_url=None):
        self.client = self.init_clint(api_key, base_url)

    def init_clint(self, api_key=None, base_url=None):
        """
        初始化客户端
        :return:
        """
        if api_key is None and 'OPENAI_API_KEY' not in os.environ:
            raise ValueError('Please set OPENAI_API_KEY in environment')
        api_key = api_key or os.environ['OPENAI_API_KEY']
        base_url = base_url or os.environ.get('OPENAI_API_BASE', 'https://api.openai.com/v1')
        return OpenAI(api_key=api_key, base_url=base_url, max_retries=3)

    def llm_inference_with_stream(self, messages=None, model=None, temperature=None):
        """
        流式推理实现
        :return:
        """
        try:
            response = self.client.chat.completions.create(
                messages=messages,
                model=model,
                stream=True,
                temperature=temperature
            )
            for chunk in response:
                if len(chunk.choices) > 0:
                    token = chunk.choices[0].delta.content
                    if token is None:
                        continue
                    yield token
        except Exception as e:
            logging.exception(e)
            raise ValueError('LLM(Large Language Model) error, Please check your key or base_url, or network')

    def llm_inference_without_stream(self, messages=None, model=None, temperature=None):
        """
        非流式推理实现
        :return:
        """
        try:
            response = self.client.chat.completions.create(
                messages=messages,
                model=model,
                stream=False,
                temperature=temperature
            )
            result = response.choices[0].message.content
            return result
        except Exception as e:
            logging.exception(e)
            raise ValueError('LLM(Large Language Model) error, Please check your key or base_url, or network')
