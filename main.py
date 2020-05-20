import re

FILENAME = "ShortStory.txt"

class sentence:
    def __init__(self, raw_sentence):
        self.raw_sentence = raw_sentence
    def __lt__(self, other):
        return self.priority(self.raw_sentence,other.raw_sentence) == 1
    def __gt__(self,other):
        return self.priority(self.raw_sentence,other.raw_sentence) == 0
    def priority(self,s1, s2):
        s1 = re.sub(r'\W+', '', s1)
        s2 = re.sub(r'\W+', '', s2)
        return sorted([s1, s2])[0] == s1 # By default Python3 will sort strings in alphanumeric order.

def getSentences(fileName : str):
    # Regex was used to compartmentalize string parsing logic from the sorting code.
    # The grammatical structure of the text turned out to be more irregular than I anticipated.
    # For a larger project, I would have wrote a tokenizer to handle string parsing.
    with open(fileName, "r") as file:
        data = file.read()
    regex = r"([\s]*([A-Za-z\-])*[\w\s\,\'\-()\:\;]*([\?]|[\.]|[\!])[\s]*)|([\s]*([A-Za-z\-])([\w\s\,\'\-()\:\;\"]*([\w]*)[\s]*[\.][\w\s]*[\.][\w\s]*[\.][\w\s]*)|([\s]*([A-Za-z\-])([\w\s\,\'\-()\:\;\"]*([\?]|[\.]|[\!])[\s]*)))|([\s]*([A-Za-z\-])[\w\s\,\'\-()\:\;]*([\?]|[\.]|[\!])[\s]*)|([\s]*[\"]*([A-Za-z\-])[\w\s\,\'\-]*[\"][^\n]([\s]*)([A-Za-z\-])[\w\s\,\?\!\'\-]*[\s]*[\"]([A-Za-z\-])[\w\s\,\?\!\'\.\-]*[\"])|([\s]*[^\"]([\d\w\s\,\'\-][\d\w\s\,\'\-]*)([\"]*)(?:[^\"\\]|\\.)*)|([\s]*[A-Za-z\-][\w\s\,\'\"\-]*[\"]*([\?]|[\.]|[\!]|[\:])*[\s]*)|([\s]*[\"]([A-Za-z\-])[\w\s\,\?\!\'\.\-]*([\"][\n]|(([\"][\w\s\,\-\?]*(([\?]|[\.]|[\!]))|([\?\"]|[\.\"]|[\!\"])))))"
    result = re.findall(regex, data)
    for i in range(len(result)):
        result[i] = result[i][max([(len(v),j) for (j,v) in (enumerate(result[i]))])[1]] # findall also returns partial matches, therefore only want the longest match
    return result

def driver(fileName : str):
    parsedSentence = getSentences(fileName)
    sentenceList = [sentence(s) for s in parsedSentence]
    sortedSentence = [re.sub(r'[\n]', '',s.raw_sentence).lstrip('[\-][\s]*') for s in sorted(sentenceList)] # Some post-processing before printing
    for (index,value) in list(enumerate(sortedSentence)):
        print(index, ':',value)
    return sortedSentence

def main():
    driver(FILENAME)
    input("Done, press enter to exit.")

if __name__ == "__main__":
    main()

# BONUS: Security Analysis
# If this was a real world application, I would also carefully consider:
# 1. Input validation (i.e checking user input on the command line).
# 2. Checking contents of the file that's being read (i.e could the program be used to circumvent an access control mechanisim?).
# 3. I used relative paths for the files but ideally an absolute path should be used (i.e another file with the same name could be placed earlier in the path).
