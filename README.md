# cipher_py
We encrypt and decrypt

Студенты, наставники и ревьюеры Практикума в общем чате перебрасываются мемами, анекдотами и шутками. Студенты решили шифровать анекдоты и шутки про ревьюеров и наставников, а не публиковать их в открытом виде: как бы чего не вышло.

Ваша задача — написать шифрующий/дешифрующий класс CipherMaster с методами cipher() (англ. «шифровать») и decipher() (англ. «расшифровать»).

Для шифрования строки студент 

  - создаёт объект класса CipherMaster,
  - вызывает у этого объекта метод cipher()
  - и передаёт в него строку, которую надо зашифровать;

метод возвращает строку в зашифрованном виде.

Аналогично работает и дешифровка, только надо вызывать метод decipher() и передать в него зашифрованную строку.
Шифрование и дешифровку нужно выполнять по «методу Цезаря»: любая буква в тексте заменяется на другую — со сдвигом по алфавиту вперёд или назад на определённое количество символов.
