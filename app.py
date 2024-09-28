from flask import Flask, render_template

# Criar instância do Flask
app = Flask(__name__)

# Rota para a página principal (index)
@app.route('/')
def index():
    # Renderiza a página inicial com links para as subpáginas
    return render_template('index.html')

# Rota para a página torre_linux.html
@app.route('/torre_linux')
def torre_linux():
    # Renderiza a página torre_linux.html
    return render_template('torre_linux.html')

# Rota para a página torre_windows.html
@app.route('/torre_windows')
def torre_windows():
    # Renderiza a página torre_windows.html
    return render_template('torre_windows.html')

# Rota para a página main_torre.html
@app.route('/torre_main')
def torre_main():
    # Renderiza a página main_torre.html
    return render_template('main_torre.html')

# Iniciar o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
