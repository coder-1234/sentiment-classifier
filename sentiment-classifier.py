TwitterFile = open("files/project_twitter_data.csv","r")
resultFile = open("files/resulting_data.csv","w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
pos_file =  open("files/positive_words.txt"):
    for lin in pos_file:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
def get_pos(s):
    s = strip_punctuation(s)
    lstStr= s.split()
    
    count=0
    for word in lstStr:
        if word in positive_words: 
                count+=1
    return count

negative_words = []
neg_file = open("files/negative_words.txt"):
    for lin in neg_file:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

            
def get_neg(s):
    s = strip_punctuation(s)
    lstStr= s.split()
    
    count=0
    for word in lstStr:
        if word in negative_words:
        	count+=1
    return count

    
def strip_punctuation(strWord):
    for charPunct in punctuation_chars:
        strWord = strWord.replace(charPunct, "")
    return strWord


def writeData(resultFile):
    resultFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultFile.write("\n")

    tweets =  TwitterFile.readlines()
    header = tweets.pop(0)
    for lin in tweets:
        listTD = lin.strip().split(',')
        pos_score = get_pos(listTD[0])
        neg_score = get_neg(listTD[0])
        resultFile.write("{}, {}, {}, {}, {}".format(listTD[1], listTD[2], pos_score, neg_score, pos_score-neg_score))    
        resultFile.write("\n")


writeData(resultFile)
TwitterFile.close()
resultFile.close()