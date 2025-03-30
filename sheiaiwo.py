def add(a, b):
    """计算两个数的和"""
    return a + b

def subtract(a, b):
    """计算两个数的差"""
    return a - b

def multiply(a, b):
    """计算两个数的积"""
    return a * b

def divide(a, b):
    """计算两个数的商"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

# 示例用法
if __name__ == "__main__":
    x = 10
    y = 5
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {subtract(x, y)}")
    print(f"{x} * {y} = {multiply(x, y)}")
    print(f"{x} / {y} = {divide(x, y)}")