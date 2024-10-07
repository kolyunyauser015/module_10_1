from threading import Thread
from datetime import datetime
import time


def write_words(word_count, file_name):
    with open(file_name, 'w+', encoding='utf-8') as file:
        for i in range(1, word_count+1):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start_time = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
stop_time = datetime.now()
print(f'Работа потоков {stop_time - start_time}')

start_time = datetime.now()
first_ww = Thread(target=write_words, args=(10, 'example5.txt'))
second_ww = Thread(target=write_words, args=(30, 'example6.txt'))
third_ww = Thread(target=write_words, args=(200, 'example7.txt'))
four_ww = Thread(target=write_words, args=(100, 'example8.txt'))

first_ww.start()
second_ww.start()
third_ww.start()
four_ww.start()

first_ww.join()
second_ww.join()
third_ww.join()
four_ww.join()

stop_time = datetime.now()
print(f'Работа потоков {stop_time - start_time}')
