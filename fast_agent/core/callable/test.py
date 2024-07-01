from typing import Callable

from fast_agent.core.callable.base import Runnable, Input, Output

class MyCallable(Runnable[Input, Output]):
    def __init__(self, func: Callable[[Input], Output]):
        self.func = func
    def run(self, i: Input) -> Output:
        return self.func(i)

# 示例函数
def example_func(x: int) -> str:
    return f"The number is {x}"

def test_callable():
    # 使用示例
    my_callable = MyCallable(example_func)
    result = my_callable.run(10)
    print(result)


# 定义一个具体实现类


if __name__ == "__main__":
    test_callable()
