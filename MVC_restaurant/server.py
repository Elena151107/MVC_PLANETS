""" Задача 2:
Управление заказами в ресторане

Задача: Разработать систему для управления заказами в ресторане, где администраторы могут отслеживать заказы, а пользователи
(клиенты) могут добавлять блюда в заказ и оформлять его.
Детали реализации:
• Model (Модели): Модели для блюд (с ценой и описанием), модели для заказов, а также модели для пользователей с возможностью
хранения информации о текущем заказе.
• View (Представление): Страница ресторана с меню, где можно выбрать блюда, страница оформления заказа с возможностью
выбора количества и добавления в корзину.
• Controller (Контроллер): Логика для добавления блюда в заказ, изменения количества, оформление заказа и генерация счета.
Шаблон HTML:
• Страница меню с блюдами, картинками и ценами.
• Корзина с заказом, где можно редактировать количество и оформлять заказ.
• Страница администратора с текущими заказами и их статусами (в процессе, готовится, доставлен)."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

# класс обработчик
class RestaurantHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/static/'):
            file_path = self.path[1:]   # убрали первый слэш в static/
            if os.path.exists(file_path):
                self.send_response(200)
                content_type = 'text/css' if file_path.endswith('.css') else 'application/javascript'
                self.send_header('Content-type', content_type)
                self.end_headers()
                with open(file_path, 'r') as file:
                    self.wfile.write(file.read().encode())
            else:
                self.send_response(404)
                self.end_headers()
        elif self.path == '/':
            self._serve_html('templates/menu.html')
        elif self.path == '/api/menu':
            self._serve_json('data.json', 'dishes')

    def _serve_html(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(file.read().encode())
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()

    def _serve_json(self, file_path, key):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data[key]).encode())
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RestaurantHandler)
    print('server started on http://localhost:8000')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
