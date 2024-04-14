from sleepy import trigger_sleepy as buzzer_on
from thermostat import trigger_thermostat as thermostat_on
from chatbot import trigger_sleepy as prompt_bot
import threading

buzzer_on()
thermostat_on(22.0)
prompt_bot()