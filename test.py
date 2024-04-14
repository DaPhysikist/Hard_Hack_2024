from sleepy import trigger_sleepy as buzzer_on
from thermostat import trigger_thermostat as thermostat_on
from chatbot import trigger_sleepy as prompt_bot
from chatbot import chat_loop
import threading

chat_thread = threading.Thread(target=chat_loop)
chat_thread.daemon = True
chat_thread.start()

buzzer_on()
thermostat_on(22.0)
prompt_bot()