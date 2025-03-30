# 🕵️‍♂️ Telegram Leaked Bot

Bot de Telegram en Python para monitorear posibles filtraciones de información asociadas a un dominio y tecnologías específicas, utilizando Google Dorks, foros de filtraciones y fuentes desconocidas.

> ⚙️ Ideal para ejecutarse en una máquina local o una Raspberry Pi 24/7.

## 🚀 Características

- Configuración dinámica desde Telegram:
  - `/setdomain tudomionio.com`
  - `/settech WordPress, Apache`
- Búsquedas automáticas una vez al día
- Detección de posibles leaks con:
  - Google Dorks vía API
  - Foros públicos como BreachForums (cuando están disponibles)
  - Fuentes .onion (via red Tor)
- Alertas directas a tu chat de Telegram
- Evita alertas duplicadas

## 🔧 Requisitos

- Python 3.8 o superior
- Token de un bot de Telegram (desde [@BotFather](https://t.me/BotFather))
- (Opcional) Raspberry Pi con Tor instalado para búsquedas en .onion

## 🧪 Instalación rápida

```bash
git clone https://github.com/MrR0b0t19/leaked-bot
cd leak-watcher-bot
pip install -r requirements.txt
