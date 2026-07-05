import http.server
from urllib.parse import parse_qs


class ContactsHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            with open("templates/contacts.html", "r", encoding="utf-8") as file:
                html_content = file.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html_content.encode("utf-8"))

        except FileNotFoundError:
            self.send_error(404, "Файл шаблона не найден")

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data_bytes = self.rfile.read(content_length)
        post_data_string = post_data_bytes.decode("utf-8")

        parsed_data = parse_qs(post_data_string)

        name = parsed_data.get("username", [""])[0]
        email = parsed_data.get("email", [""])[0]
        message = parsed_data.get("message", [""])[0]

        print("\n--- Получен новый POST-запрос ---")
        print(f"Имя: {name}")
        print(f"Почта: {email}")
        print(f"Сообщение: {message}")
        print(f"Сырые данные: {post_data_string}")
        print("-------------------------------\n")

        self.send_response(200)  # Код 200 OK
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        response_text = f"""
        <html>
            <head><title>Успех</title></head>
            <body>
                <h1>Спасибо, {name}!</h1>
                <p>Ваше сообщение получено.</p>
                <a href="/">Вернуться назад</a>
            </body>
        </html>
        """
        self.wfile.write(response_text.encode("utf-8"))
