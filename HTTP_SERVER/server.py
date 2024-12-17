"""    Задание: "Мини-сервер для голосования"
Создать веб-сервер на Python с использованием http.server, который предоставляет HTML-страницу для голосования.
Веб-страница должна отправлять данные на сервер через JavaScript с использованием fetch()4"""


from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class VoteHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':  # проверка запроса, по какому пути  (# ОБРАБОТКА ЗАПРОСА СТАНДАРТНАЯ )
            self.send_response(200)  # отправить ответ (код 200) - успешно
            self.send_header('Content-type', 'text/html')  # в каком формате отправляем ответ
            self.end_headers()  # закрыть отправку заголовка
            with open('vote.html', 'r', encoding='utf-8') as file:
                self.wfile.write(file.read().encode('utf-8'))
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'status:': 'success'}
            self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_POST(self):
        if self.path == '/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            print(data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'status': 'success', 'count': data}
            self.wfile.write(json.dumps(response).encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), VoteHandler)
    print('Сервер запущен - http://localhost:8000')
    server.serve_forever()
