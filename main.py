from random import choice


class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w') as file:
            for item in data_set:
                file.write(f'{item}\n')

    return write_everything


def main():
    first = 'Мама мыла раму'
    second = 'Рамена мало было'

    print(list(map(lambda x, y: x == y, first, second)))

    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())


if __name__ == '__main__':
    main()
