import nltk
import wordcloud
from matplotlib.pyplot import imread
import pandas as pd

def HotwordCount(meeting_year):
    data = pd.read_csv("./collected_static/dataset/ACL.csv")
    #读取原始数据
    if meeting_year != 0:
        data = data[data['year'] == meeting_year]
    data_summary = data["abstract"].tolist() 
    TXT = ""

    #清洗数据
    for summary in data_summary:
        t1 = summary.lower()
        for ch in '!"""“”#$%&()*+,-./:;<=>?@[\\]^_''{|}~1234567890':
            t1 = t1.replace(ch, " ")
        ls = t1.split() # 分隔成由单词组成的list
        for i in range(1, len(ls)):
            word = ls[i]
            if word == 'embeddings' or word == 'networks' or word == 'languages' or word == 'models':
                ls[i] = word[:-1]
            elif word == 'nmt':
                if ls[i-1] == 'translation':
                    ls[i] = ' '
                else:
                    ls[i] = 'neural'
                    ls.insert(i+1,'machine')
                    ls.insert(i+2,'translation') 
            elif word == 'nlp':
                if ls[i-1] == 'processing':
                    ls[i] = ' '
                else:
                    ls[i] = 'natural'
                    ls.insert(i+1,'language')
                    ls.insert(i+2,'processing')          
        txt = " ".join(ls) #将单词序列合并成字符串
        TXT = TXT + txt

    tokens=nltk.wordpunct_tokenize(TXT)
    hotword_list = []

    finder=nltk.collocations.BigramCollocationFinder.from_words(tokens)
    finder.apply_word_filter(lambda x: x in ['a','e','g','s','f','an','of','to','et','on','in','be','is','are','as','we','our','and','not',
                                            'can','for','has','have','the','also','show','that','this','well','github','question','results',
                                            'previous','world','scale','with','proposed','data','art','task','tasks','which','base','based'])
    #bigram_measures=nltk.collocations.BigramAssocMeasures()
    hotword = sorted(finder.ngram_fd.items(), key=lambda t: (-t[1], t[0]))[:15] #list类型,每个元素是一个元组
    for item in hotword:
        hotword_list.append([item[0][0] + ' ' + item[0][1], item[1]])

    finder=nltk.collocations.TrigramCollocationFinder.from_words(tokens)
    finder.apply_word_filter(lambda x: x in ['a','e','g','s','f','an','of','to','et','on','in','be','is','are','as','we','our','and','not',
                                            'can','for','has','have','the','also','show','that','this','well','github','question','results',
                                            'previous','world','scale','with','proposed','data','art','task','tasks','which','base','based'])
    hotword = sorted(finder.ngram_fd.items(), key=lambda t: (-t[1], t[0]))[:10] #list类型,每个元素是一个元组
    for item in hotword:
        hotword_list.append([item[0][0] + ' ' + item[0][1] + ' ' + item[0][2], item[1]])

    #统一排序
    hotword_list = sorted(hotword_list, key=lambda x:int(x[1]), reverse=True)
    return hotword_list

hotword_list = HotwordCount(0)
#将hotword_list再转化为dataframe输出
columns = ['Hot Word','Frequency']
data = pd.DataFrame(hotword_list, index = None, columns = columns)
data.to_csv("ACL_hotword.csv", index = None)

hotword_list = HotwordCount(2013)
data = pd.DataFrame(hotword_list, index = None, columns = columns)
data.to_csv("ACL_hotword.csv", index = None, mode = 'a')

hotword_list = HotwordCount(2014)
data = pd.DataFrame(hotword_list, index = None, columns = columns)
data.to_csv("ACL_hotword.csv", index = None, mode = 'a')

hotword_list = HotwordCount(2015)
data = pd.DataFrame(hotword_list, index = None, columns = columns)
data.to_csv("ACL_hotword.csv", index = None, mode = 'a')

hotword_list = HotwordCount(2016)
data = pd.DataFrame(hotword_list, index = None, columns = columns)
data.to_csv("ACL_hotword.csv", index = None, mode = 'a')

hotword_list = HotwordCount(2017)
data = pd.DataFrame(hotword_list, index = None, columns = columns)
data.to_csv("ACL_hotword.csv", index = None, mode = 'a')

hotword_list = HotwordCount(2018)
data = pd.DataFrame(hotword_list, index = None, columns = columns)
data.to_csv("ACL_hotword.csv", index = None, mode = 'a')

hotword_list = HotwordCount(2019)
data = pd.DataFrame(hotword_list, index = None, columns = columns)
data.to_csv("ACL_hotword.csv", index = None, mode = 'a')