def UnicodeConversion(a):
    print(ord(a),"%c前面的为："%a,chr(ord(a)-1),"%c2后面的为："%a,chr(ord(a)+1))
a=input("请输入一个字符：")
UnicodeConversion(a)