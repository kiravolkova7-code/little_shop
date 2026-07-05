from src.web import *

PORT = 8000
if __name__ == "__main__":
    web_server = http.server.HTTPServer(("", PORT), ContactsHandler)
    print(f"Сервер запущен на http://localhost:{PORT}")
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass
    web_server.server_close()
