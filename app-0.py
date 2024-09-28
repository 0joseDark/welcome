# Importamos os módulos necessários para construir o servidor HTTP
import http.server
import socketserver

# Definimos a porta onde o servidor irá funcionar (porta 8000 neste caso)
PORT = 8000

# Classe para lidar com as requisições HTTP
# Usamos SimpleHTTPRequestHandler que já está pronta para servir arquivos HTML
Handler = http.server.SimpleHTTPRequestHandler

# Criamos o servidor, utilizando o protocolo HTTP, associando-o à porta escolhida
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor HTTP a funcionar na porta {PORT}")
    
    # O servidor ficará ativo até ser interrompido (Ctrl + C para parar)
    httpd.serve_forever()
