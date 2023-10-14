# 设计一个函数返回给定文件名的后缀名。
def get_suffix(filename,has_dot=False):
    pos = filename.rfind('.')
    if 0<pos<len(filename)-1:
        if has_dot == False:
            index =pos + 1
        else:
            index = pos
        return filename[index:]
    else:
        return ''

print(get_suffix('yuanshen.exe',False))

