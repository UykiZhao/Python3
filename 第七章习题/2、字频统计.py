path = 'data721.txt'
with open(path,'r') as text:
    # 把字符串里面的字符拆分成逐个单词并且用数组装着
    words = [word for word in text.read()]
    # 把字符数数再用字典装着
    count_dist = {index : words.count(index) for index in words}
    # 字典逐个打印
    for i in count_dist:
        print(f"{i}出现了{count_dist.get(i)}次")


