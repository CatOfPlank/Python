# 推荐系统
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# 创建一个文本集合
corpus = [
    'This is the first document.',
    'This is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]

# 使用CountVectorizer将文本转换为词袋向量
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print(X.toarray())

# 使用TfidfVectorizer将文本转换为TF-IDF向量
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(corpus)
print(X_tfidf.toarray())