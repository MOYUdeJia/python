# 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
import random

def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars)-1
    code = ''
    for _ in range(0,code_len):
        index = random.randint(0,last_pos)
        code += all_chars[index]
    return code

print(generate_code())

