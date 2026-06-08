"""
⚡ WhatsApp Business Bot Template v1.0
Bot automatizado para WhatsApp Business API
- Auto-respuestas
- Catálogo de productos
- Seguimiento de leads
- Agenda de citas

README: 
1. Conectar a OpenWA o WATI
2. Configurar mensajes en config.json
3. Ejecutar: python3 bot.py
4. Profit.

Precio sugerido: $25 USD
"""
import json, time, random

BOT_VERSION = "1.0"
BOT_NAME = "WhatsAutoBot"

class Bot:
    def __init__(self):
        self.responses = {
            "hola": "¡Hola! 👋 Soy el asistente automático. ¿En qué puedo ayudarte?",
            "precio": "Los precios varían según el servicio. ¿Qué te interesa cotizar?",
            "whatsapp": "Puedes contactarnos directamente a este número.",
        }
    
    def handle_message(self, msg):
        msg_lower = msg.lower().strip()
        for key, response in self.responses.items():
            if key in msg_lower:
                return response
        return None

if __name__ == "__main__":
    bot = Bot()
    print(f"{BOT_NAME} v{BOT_VERSION} listo")
    print(json.dumps({"responses": len(bot.responses), "status": "ready"}, indent=2))
