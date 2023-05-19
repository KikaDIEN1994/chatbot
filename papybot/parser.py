from papybot.stopword import stopwords
import string

class Parser:

    def __init__(self,question):
        self.question = question

    # Clean the question
    def parse(self):
        self._remove_upper_letter()
        self._remove_ponctuation()
        keywords = self._remove_stop_word()
        return keywords

    # remove all upper letter
    def _remove_upper_letter(self):
        self.question = self.question.lower()

    # remove ponctuation
    def _remove_ponctuation(self):
        self.question  = self.question .translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))).replace(' '*4, ' ').replace(' '*3, ' ').replace(' '*2, ' ').strip()

    # remove word of stopword
    def _remove_stop_word(self):
        keywords = []
        list_of_keywords = self.question.split(' ')
        for word in list_of_keywords:
            if word not in stopwords:
                keywords.append(word)
        keywords = ' '.join(keywords)
        return keywords


# parser = Parser("Bonjour, J'aimerais savoir ou se trouve la tour-eiffel.")
# parser.parse()