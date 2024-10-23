class WordsFinder:
    def __init__(self,*args):
        self.list_file = list(args)

    def get_all_words(self):
        all_words = {}
        chars = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name_file in self.list_file:
            with open(name_file, encoding='utf-8') as file:
                list_lines = file.readlines()
                str_ = ''
                for line in list_lines:
                    for char in chars:
                        line = line.lower().replace(char, '')
                    str_ += line
                all_words[file.name] = str_.split()
        return all_words

    def find(self, word):
        dict_words = self.get_all_words()
        dict_coincidence = {}
        for key, value in dict_words.items():
            if word.lower() in value:
                dict_coincidence[key] = value.index(word.lower()) + 1
        return dict_coincidence

    def count(self, word):
        dict_words = self.get_all_words()
        dict_coincidence = {}
        quantity = 0
        for key, value in dict_words.items():
            if word.lower() in value:
                for item in value:
                    if item.lower() == word.lower():
                        quantity += 1
                dict_coincidence[key] = quantity
        return  dict_coincidence

if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt', 'monday’s_child.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего