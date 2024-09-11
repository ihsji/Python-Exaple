
#基本语法：
def decorator(func):  
    def wrapper(*args, **kwargs):  
        # 在这里添加额外的功能  
        print("添加新功能代码前")  
        result = func(*args, **kwargs)  
        print("添加新功能代码后")  
        return result  
    return wrapper  
  
@decorator  
def my_function():  
    print("你好！我是新添加的功能代码。")  
  
# 调用my_function时，实际上调用的是wrapper函数  
my_function()