"""
作者：Shuaiyu Li
日期：2022年01月13日
"""
print('i love math.\ni love chinese')  #\n 表示换行

print('"life is short,you need Python"')
print('\"life is short,you need Python\"')  #\' or \" 转义符号

#动动手 1
dpy=365
hpd=24
mph=60
spm=60
spy=dpy*hpd*mph*spm
print(spy)
#动动手 2
name=input("请输入你的名字：")
print("你好", name, sep="，", end="！")  #sep  是分割各个元素之间的参数默认是一个空格
print('nihao')  #end 是print 里面的元素全部打印完成后 会默认打印一次 end ，默认的end='\n'
# 为换行符 这就是print 为什么会自动帮我们换行的主要原因

print("D:\three\two\one")   #\和一些字符搭配有别的意思，不能放在末尾，表示事情没有结束
print("D:\\three\\two\\one")  #原始字符串的两种方法
print(r"D:\three\two\one")  #r表示原始字符串

print(520+1314)
print("520"+"1314")  #字符串的加法=拼接
print("i love you\n"*3000)

fishc=r"""
      ___                     ___          ___          ___     
     /\  \         ___       /\  \        /\__\        /\  \    
    /::\  \       /\  \     /::\  \      /:/  /       /::\  \   
   /:/\:\  \      \:\  \   /:/\ \  \    /:/__/       /:/\:\  \  
  /::\~\:\  \     /::\__\ _\:\~\ \  \  /::\  \ ___  /:/  \:\  \ 
 /:/\:\ \:\__\ __/:/\/__//\ \:\ \ \__\/:/\:\  /\__\/:/__/ \:\__\
 \/__\:\ \/__//\/:/  /   \:\ \:\ \/__/\/__\:\/:/  /\:\  \  \/__/
      \:\__\  \::/__/     \:\ \:\__\       \::/  /  \:\  \      
       \/__/   \:\__\      \:\/:/  /       /:/  /    \:\  \     
                \/__/       \::/  /       /:/  /      \:\__\    
                             \/__/        \/__/        \/__/
"""
print(fishc)  #r,原始字符串，否则\容易产生误会

for i in range(1,10):
    for j in range(1,i+1):
        print(i, "x", j, "=", i * j, end=' ')
    print("\n")

###如果在 IDLE 的交互模式中使用 help(obj) 函数，可以查看到 obj 对应的说明文档