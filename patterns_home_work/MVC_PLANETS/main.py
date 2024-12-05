from controller import ControllerPlanets

def main():
    controller = ControllerPlanets()
    while True:
        controller.view.display_menu()
        choice = int(controller.view.get_input('Выберите действие: '))
        if choice == 5:
            break
        elif choice == 1:
            controller.info_by_all_planets()
        elif choice == 2:
            name = controller.view.get_input('Введите имя планеты: ').upper().strip()
            radius = float(controller.view.get_input('Введите радиус орбиты: '))
            speed = float(controller.view.get_input('Введите скорость вращения: '))
            mass = float(controller.view.get_input('Введите массу планеты: '))
            controller.create_planet(name, radius, speed, mass)
        elif choice == 3:
            name = controller.view.get_input('Введите имя планеты: ').upper().strip()
            controller.remove_planet(name)
        elif choice == 4:
            name = controller.view.get_input('Введите имя планеты: ').upper().strip()
            step_move = int(controller.view.get_input('Введите количество шагов симуляции: '))
            time_step = int(controller.view.get_input('Введите временной шаг: '))
            controller.move_planet(name, step_move, time_step)
        else:
            controller.view.show_mess('Mistake')

if __name__ == '__main__':
    main()

