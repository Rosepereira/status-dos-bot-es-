# Importa as bibliotecas Flask e SocketIO
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

# Cria a instância do Flask
app = Flask(__name__)

# Configura o SocketIO para permitir conexões de qualquer origem
socketio = SocketIO(app, cors_allowed_origins="*")

# Rota principal que serve a página HTML
@app.route('/')
def index():
    return render_template('index.html')  # Renderiza o template web/templates/index.html

# Rota para comando "pressed"
@app.route('/pressed', methods=['GET', 'POST'])
def pressed():
    print("Comando: pressed")  # Imprime no console (útil para debug)
    socketio.emit('command', {'action': 'pressed'})  # Envia comando via WebSocket
    return 'Pressed command sent', 200  # Retorna uma resposta HTTP padrão

# Rota para comando "unpressed"
@app.route('/unpressed', methods=['GET', 'POST'])
def unpressed():
    print("Comando: Unpressed")  # Imprime no console (útil para debug)
    socketio.emit('command', {'action': 'unpressed'})  # Envia comando via WebSocket
    return 'Unpressed command sent', 200  # Retorna uma resposta HTTP padrão

# Ponto de entrada principal da aplicação
if __name__ == '__main__':
    # Inicia o servidor Flask com suporte a WebSockets
    socketio.run(app, host='0.0.0.0', port=5000)
