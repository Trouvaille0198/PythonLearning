from sklearn.feature_extraction.text import TfidfVectorizer
import jieba


def cut_word(text):
    # 用结巴对中文字符串进行分词
    text = " ".join(list(jieba.cut(text)))
    return text


data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
        "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
        "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]
# 将原始数据转换成分好词的形式
text_list = []
for sent in data:
    text_list.append(cut_word(sent))
print(text_list)

# 1、实例化一个转换器类
# transfer = CountVectorizer(sparse=False)
transfer = TfidfVectorizer(stop_words=['一种', '不会', '不要'])
# 2、调用fit_transform
data = transfer.fit_transform(text_list)
print("文本特征抽取的结果：\n", data.toarray())
print("返回特征名字：\n", transfer.get_feature_names())
