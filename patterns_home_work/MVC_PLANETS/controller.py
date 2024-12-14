from model import Planet
from view import PlanetView
from math import cos
from math import sin

class ControllerPlanets:
    def __init__(self):
        self.planets = {}
        self.view = PlanetView()

    def create_planet(self, name, radius, speed, mass):  # 2. Добавить планету
        if name in self.planets:
            self.view.show_mess('Планета с таким именем уже существует')
        else:
            self.planets[name] = Planet(name)
            self.planets[name] = {
                'radius': self.planets[name].set_radius(radius),
                'speed': self.planets[name].set_speed(speed),
                'mass': self.planets[name].set_mass(mass)
            }
            self.view.show_mess(f'Планета {name} создана')
            return self.planets[name]

    def remove_planet(self, name):    # 3. Удалить  планету
        if name not in self.planets:
            self.view.show_mess('Планета с таким именем не найдена')
        else:
            del self.planets[name]
            self.view.show_mess(f'Планета {name} удалена')

    def info_by_all_planets(self, indent=0):   # 1. Показать планеты
        print('***  ПЛАНЕТЫ:  ***')
        for num, planet in enumerate(self.planets, 1):
            print(f'{num}. Планета {planet}:\n\t\tРадиус орбиты: {self.planets[planet]['radius']}.\n\t\tСкорость вращения вокруг звезды: {self.planets[planet]['speed']}.\n\t\tМасса: {self.planets[planet]['mass']}')

    def move_planet(self, name, step_move, time_step):   #  4. Запустить симуляцию
        if name not in self.planets:
            self.view.show_mess('Планета с таким именем не найдена')
        else:
            for num, _ in enumerate(range(1, step_move+1), 1):
                u = self.planets[name]['speed'] / self.planets[name]['radius']
                w = u * num * time_step
                x = self.planets[name]['radius'] * cos(w)
                y = self.planets[name]['radius'] * sin(w)
                print(f'Шаг {num}: Планета {name} на позиции x={x: .2f}, y={y: .2f}')
                self.view.display_move_planet(name)

