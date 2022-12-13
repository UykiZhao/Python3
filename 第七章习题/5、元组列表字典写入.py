s = (1, 2, 3, 4, 5)
l = [6, 7, 8, 9, 10]
d = {'cookie': 'ID1024', 'session': 'ID2048'}
with open('write.txt', 'w', encoding='utf-8') as fp:
   fp.writelines(str(s)+'\n')
   fp.writelines(str(l)+'\n')
   fp.writelines(str(d)+'\n')

content = open('write.txt','r')
print(content.read())