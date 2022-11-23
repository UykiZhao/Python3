path = 'data721.txt'
with open(path,'r') as fp:
    content = fp.read()
    content_new = content[::-1]
with open('data721_new.txt','w',encoding='utf-8') as text:
    text.write(content_new)