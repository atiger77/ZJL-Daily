# coding:utf-8  
import os,sys,string
import jieba
import jieba.posseg as pseg
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
reload(sys)
sys.setdefaultencoding('utf8')

def fenci():
    corpus = ["社工的不错",
    "真不是吹牛逼，我的刀功真的没话说，是真的烂",
    "家里有白板就是好，1.0版本暂时就这样，反正我说了算",
    "之前玩过一个FPS游戏Centos装桌面环境编译下包可以直接玩，那个游戏是linux下的cs直接和老外对打",
    "Docker里用脏牛的EXP跳出容器有表哥测试过的嘛"]
    for i in corpus:
        cut_list = jieba.cut(i,cut_all=True)
        #cut_list = jieba.cut(i,cut_all=False)
        f = open("/Users/Atiger77/Project/ZJL-Daily/TF-IDF/1.txt",'a')
        f.write(" ".join(cut_list))
        f.close()

def TFIDF():
    path = "/Users/Atiger77/Project/ZJL-Daily/TF-IDF/1.txt"
    corpus = []
    f = open(path,'r+')
    content = f.read()
    corpus.append(content)
    f.close()
    
    vectorizer = CountVectorizer()	
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()
    #print vectorizer.vocabulary_
    for i in range(len(weight)):
        for j in range(len(word)):
            z = word[j]+":"+str(weight[i][j])+"\n"
            f = open("/Users/Atiger77/Project/ZJL-Daily/TF-IDF/2.txt",'a')
            f.write(z)
            f.close()


if __name__ == "__main__" : 
    fenci()
    TFIDF()
