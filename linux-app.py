from flask import Flask, render_template

# Criação da aplicação Flask
app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota para a página 'Sobre'
@app.route('/about')
def about():
    return render_template('about.html')

# Rota para a página 'Contato'
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Executa o servidor Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
