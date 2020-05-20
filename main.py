import re

FILENAME = "ShortStory.txt"

class sentence(object):
    def __init__(self, sentence):
        self.sentence = sentence
    def __lt__(self, other):
        return priority(self.sentence,other.sentence) == 1
    def __gt__(self,other):
        return priority(self.sentence,other.sentence) == 0

def getSentences(fileName):
    with open(fileName, "r") as file:
        data = file.read()
    regex = r"([\s]*([A-Za-z\-])*[\w\s\,\'\-()\:\;]*([\?]|[\.]|[\!])[\s]*)|([\s]*([A-Za-z\-])([\w\s\,\'\-()\:\;\"]*([\w]*)[\s]*[\.][\w\s]*[\.][\w\s]*[\.][\w\s]*)|([\s]*([A-Za-z\-])([\w\s\,\'\-()\:\;\"]*([\?]|[\.]|[\!])[\s]*)))|([\s]*([A-Za-z\-])[\w\s\,\'\-()\:\;]*([\?]|[\.]|[\!])[\s]*)|([\s]*[\"]*([A-Za-z\-])[\w\s\,\'\-]*[\"][^\n]([\s]*)([A-Za-z\-])[\w\s\,\?\!\'\-]*[\s]*[\"]([A-Za-z\-])[\w\s\,\?\!\'\.\-]*[\"])|([\s]*[^\"]([\d\w\s\,\'\-][\d\w\s\,\'\-]*)([\"]*)(?:[^\"\\]|\\.)*)|([\s]*[A-Za-z\-][\w\s\,\'\"\-]*[\"]*([\?]|[\.]|[\!]|[\:])*[\s]*)|([\s]*[\"]([A-Za-z\-])[\w\s\,\?\!\'\.\-]*([\"][\n]|(([\"][\w\s\,\-\?]*(([\?]|[\.]|[\!]))|([\?\"]|[\.\"]|[\!\"])))))"
    result = re.findall(regex, data)
    for i in range(len(result)):
        result[i] = result[i][max([(len(v),j) for (j,v) in (enumerate(result[i]))])[1]]
    return result

def priority(s1,s2):
    s1 = re.sub(r'\W+', '', s1)
    s2 = re.sub(r'\W+', '', s2)
    return sorted([s1,s2])[0]==s1

def driver(fileName):
    parsedSentence = getSentences(fileName)
    sentenceList = [sentence(s) for s in parsedSentence]
    sortedSentence = [re.sub(r'[\n]', '',s.sentence).lstrip('[\-][\s]*') for s in sorted(sentenceList)]
    for (index,value) in list(enumerate(sortedSentence)):
        print(index, ':',value)
    return sortedSentence

def main():
    driver(FILENAME)
    input("Done, press any key to exit.")

if __name__ == "__main__":
    main()