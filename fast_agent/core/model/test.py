import os

from fast_agent.core.model.language_model.openai import OpenAILargeLanguageModel
from dotenv import load_dotenv

from fast_agent.core.model.language_model.token_util import string_token_count, messages_token_count

load_dotenv()


def test_openai_llm():
    llm = OpenAILargeLanguageModel()
    input_msg = [
        {
            "role": "user",
            "content": "你是谁"
        }
    ]
    inference_without_stream = llm.llm_inference_without_stream(
        messages=input_msg,
        model='gpt-4o'
    )
    print("input msg token count:", messages_token_count(input_msg))
    print("非流式输出：", inference_without_stream)
    print("output token count:", string_token_count(inference_without_stream))


if __name__ == "__main__":
    test_openai_llm()
