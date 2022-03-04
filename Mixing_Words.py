class Mix_word:
    def __init__(self):
        self.User_word = ""
        self.words = []
        self.new_word = ""
        self.list_letters = []
        self.list_word_count = []
        self.list_sorted_letters = []
        self.letter_average = 0
        self.Finally_word = ""
        self.Receive_words_from_the_user()

    def Receive_words_from_the_user(self):
        self.User_word = input("Enter your word: ")
        while self.User_word:
            self.words.append(self.User_word)
            self.User_word = input("Enter your word: ")
        self.Paste_words_together()

    def Paste_words_together(self):
        if len(self.words) >= 2:
            for self.word in self.words:
                self.new_word += self.word
            self.Recognize_the_letters_of_words()
            self.Count_the_number_of_letters()
            self.Mark_the_number_of_letters()
            self.Convert_marked_numbers_to_their_letters()
            self.Determine_the_average_letters_in_words()
            self.Make_a_new_word()
        else:
            print("At least two word must be entered!")

    def Recognize_the_letters_of_words(self):
        for i in self.new_word:
            if i not in self.list_letters:
                self.list_letters.append(i)
                self.list_word_count.append(0)

    def Count_the_number_of_letters(self):
        for count in self.new_word:
            for i in range(len(self.list_letters)):
                if count == self.list_letters[i].upper() or count == self.list_letters[i]:
                    self.list_word_count[i] += 1

    def Mark_the_number_of_letters(self):
        for i in range(len(self.list_letters)):
            self.list_word_count[i] = float(str(self.list_word_count[i]) + f".{i + 1}1")
        self.list_word_count.sort(reverse=True)

    def Convert_marked_numbers_to_their_letters(self):
        for i in range(len(self.list_letters)):
            self.list_word_count[i] = str(self.list_word_count[i])
            x = self.list_word_count[i].index(".")
            self.list_sorted_letters.append(self.list_letters[int(self.list_word_count[i][x + 1:-1]) - 1])

    def Determine_the_average_letters_in_words(self):
        for i in range(len(self.words)):
            self.letter_average += len(self.words[i])
        self.letter_average = round(self.letter_average / len(self.words))

    def Make_a_new_word(self):
        if self.letter_average < len(self.list_letters):
            for i in range(self.letter_average):
                self.Finally_word += self.list_sorted_letters[i]
        else:
            for i in range(len(self.list_letters)):
                self.Finally_word += self.list_sorted_letters[i]
        print(f"The result is: ( {self.Finally_word.capitalize()} )")
Mix_word()

input("\nPress enter to exit...")
