class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        self.original_text = original_text
        self.shift = shift
        result = []
        lower_text = self.original_text.lower()
        for letter in lower_text:
            if letter in  self.alphabet: # здесь ваш код
                index_of_word = self.alphabet.index(letter) + self.shift
                if index_of_word > (len(self.alphabet)-1):
                    index_of_word -= (len(self.alphabet)) 
                result.append(self.alphabet[index_of_word])
            else:
                result.append(letter)  
        return ''.join(result)

    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        result = []
        self.cipher_text = cipher_text
        self.shift = shift
        result = []
        lower_text = self.cipher_text.lower()
        for letter in lower_text:
            if letter in  self.alphabet: # здесь ваш код
                index_of_word = self.alphabet.index(letter) - self.shift
                if index_of_word > (len(self.alphabet)-1):
                    index_of_word -= (len(self.alphabet)) 
                result.append(self.alphabet[index_of_word])
            else:
                result.append(letter)
        
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))