import jieba
sentence = input("请输入一段三国演义的片段")
words = jieba.lcut(sentence)
names = {"曹操", "刘备", "孙权", "诸葛亮", "孔明", "关羽", "云长", "张飞", "翼德", "赵云", "子龙", "马超", "孟起", "黄忠", "汉升", "周瑜", "公瑾","吕布","玄德", "华雄", "颜良", "文丑", "周郎", "仲谋", "许褚", "夏侯渊"}
count = {}
for word in words:
    if word in names:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
print("-" * 10)
#for w,n in count.items():
 #   print(w,":",n)



words= ['《', '凉州', '词', '》', '\n', '葡萄', '美酒', '夜光杯', ',', '欲', '饮', '琵琶', '马上', '催', '。', '\n', '醉卧', '沙场', '君莫笑', ',', '古来', '征战', '几人', '回', '？']
punctuation = ['《', '》', ',', '.', '?', '\n', ',', '。']
count = {}
for word in words:
    if word not in punctuation:
        count[word] += 1
    else:
        count[word] = 1
result = ','.join([f"{k}:{v}" for k,v in count.items()])
print(result)