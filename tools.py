import jieba


def preprocess_chinese_text(text):
    # 分词
    words = jieba.cut(text)
    
    # 去除停用词
    with open("baidu_stopwords.txt", 'r') as f:
        stop_words = f.read()
    stop_words = set(stop_words)
    words = [word for word in words if word not in stop_words]
    
    return ' '.join(words)

