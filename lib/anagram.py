# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word = word
        
    def match(self, words):        
        test_word = list(self.word)
        test_word_list = list(test_word)
        test_word_list.sort()
        test_word_str = ''.join([str(elem) for elem in test_word_list])

        answer = []
        # word for word in words if test_word_list == word.sort()
        for word in words:
            index = words.index(word)
            word_list = list(word)
            word_list.sort()
            word_str = ''.join([str(elem) for elem in word_list])
                        
            if(word_str == test_word_str):
                answer.append(words[index])
            
            
        return answer
