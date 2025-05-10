<div align='center' style='margin: 20px'>
  <img src='web/static/img/logo-no-background.svg' width='1000' /> 
</div>

# 📶 Pico W - Leitor de Botão via Servidor HTTP com Flask

Este projeto demonstra como utilizar um **Raspberry Pi Pico W - BitdogLab** para ler o estado de um botão físico e exibi-lo em uma interface web utilizando um **servidor Flask**. O sistema lê o botão e envia o estado atual ("Pressionado" ou "Solto") para o servidor Flask, que o apresenta via navegador.

---

## 🚀 Funcionalidades

- Leitura digital de um botão físico
- Comunicação com servidor Flask via Wi-Fi
- Exibição do estado do botão em uma página web

---

## 🔧 Hardware Utilizado

- BitDogLab - Raspberry Pi Pico W
- 1 botão push-button
- 1 resistor de pull-up interno
- LED (feedback visual)

---

## 📌 Pinagem

| Componente     | Pino GPIO |
|----------------|-----------|
| Botão          | GPIO 5    |
| LED BLUE       | GPIO 12   |
| LED RED        | GPIO 13   |
---

## ⚙️ Como Funciona

- O botão é lido continuamente pelo Pico W.
- O Pico W envia, a cada segundo, uma requisição para o servidor Flask indicando o estado do botão.
- O Flask exibe esse estado através de duas rotas: `/pressed` ou `/unpressed` acessiveis via navegador.

---

## 🛠️ Como Rodar o Projeto

1. Clone este repositório ou copie os arquivos.
2. Configure o Wi-Fi no código do Pico (`WIFI_SSID` e `WIFI_PASSWORD`).
3. Defina a pinagem da sua BitDogLab.
4. Compile e envie o código C para o Pico W utilizando o SDK da Raspberry Pi.
5. Rode o servidor Flask com:

```bash
python app.py
```

6. Acesse `http://<IP_SERVIDORFLASK>:5000/status` para ver o estado do botão.

---

## 💻 Exemplo de Código (Pico W)

```c
if (gpio_get(BUTTON_PIN) == 0) {
    path = "/pressed";
} else {
    path = "/unpressed";
}
```

---

## 💻 Exemplo de Código (Flask)

```python
from flask import Flask

app = Flask(__name__)
status = "Solto"

@app.route('/pressed')
def pressed():
    global status
    status = "Pressionado"
    return "OK"

@app.route('/unpressed')
def unpressed():
    global status
    status = "Solto"
    return "OK"

@app.route('/status')
def get_status():
    return status

if __name__ == '__main__':
    app.run(debug=True)
```

---

Feito com 💜 usando Raspberry Pi Pico W e Flask
