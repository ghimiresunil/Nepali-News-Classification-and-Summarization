import re 
import string
import snowballstemmer 
import config as cfg

class NepaliPreprocess():
    
    def __init__(self) -> None:
        
        self.stop_word_list = []
        self.regX_cleaned = ""
        self.stemmer = snowballstemmer.NepaliStemmer()
        a_file = open(cfg.stop_words, "r" ,encoding= 'utf-8')
        for line in a_file:
            stripped_line = line.strip()
            self.stop_word_list.append(stripped_line)
        a_file.close()
           
    def Reg_and_Stemming(self ,input_str) -> str:

        article = re.sub(r'\([^)]*\)', r'', input_str)
        article = re.sub(r'\[[^\]]*\]', r'', article)
        article = re.sub(r'<[^>]*>', r'', article)
        article = re.sub(r'^https?:\/\/.*[\r\n]*', '', article)
        article = re.sub('http[s]?://\S+', '', article)
        article = re.sub(r'[a-zA-Z0-9]+', '', article)
        article = re.sub('[!+*-@,#%(&$_?.^]', '', article)
        article = re.sub(' +', ' ',article)
        article = article.replace(u'\ufeff','')
        article = article.replace(u'\xa0', u' ')
        article = article.replace('  ', ' ');
        article = article.replace(' , ', ', ');

        self.regX_cleaned = article
        
        return self.check_STEM_STOP()


    def listToString(self,s) -> str:   
        # initialize an empty string
        str1 = "" 
        # traverse in the string  
        for ele in s: 
            str1 += ele + " "  
        # return string  
        return str1 

    def sentence_tokenize(self, text) -> list:
        sentences = text.strip().split(u"।")
        sentences = [sentence.translate(str.maketrans('', '', string.punctuation)) for sentence in sentences]
        return sentences


    def check_STEM_STOP(self) -> str:
        data = self.sentence_tokenize(self.regX_cleaned)
        review_data_list = list()

        for i,line in enumerate(data):
            tokens = line.split()

            words = [w for w in tokens if not w in self.stop_word_list]
            words  = self.stemmer.stemWords(words)
            review_data_list.append(words)
        return self.listToString(review_data_list[0])
    
    
if __name__ == "__main__":
    inpuT = "घन्टाघरले कति बजायो सबै आफैभित्र पचायो"
    nPre = NepaliPreprocess()
    opt = nPre.Reg_and_Stemming(inpuT)
    print(opt)