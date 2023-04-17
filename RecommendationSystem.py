# 推荐系统
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


# 两个向量的余弦相似度
def cosine_similarity(vertor1, vector2):
    return np.dot(vertor1, vector2) / (np.linalg.norm(vertor1) * np.linalg.norm(vector2))


# 两个向量的欧氏距离
def euclidean_distance(vector1, vector2):
    return np.sqrt(np.sum(np.power(vector1 - vector2, 2)))


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
tfidf_arr = X_tfidf.toarray()
print(tfidf_arr)
print("余弦相似度：", cosine_similarity(tfidf_arr[0], tfidf_arr[3]))
