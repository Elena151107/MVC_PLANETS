class PlanetView:
    @staticmethod
    def display_menu():
        print('Команды:')
        print('1. Показать планеты')
        print('2. Добавить планету')
        print('3. Удалить  планету')
        print('4. Запустить симуляцию')
        print('5. Выйти')

    @staticmethod
    def get_input(prompt):
        return input(prompt)

    @staticmethod
    def show_mess(mess):
        print(mess)

    @staticmethod
    def display_move_planet(name):
        print(f'Планета {name} завершила 1 полный оборот')

