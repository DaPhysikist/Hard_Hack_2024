# Hard_Hack_2024
This is a project designed to keep a user awake. It makes use of computer vision to detect the user's drowsiness, and if the user is falling asleep, it will try to wake up the user in a variety of ways. It will first trigger a buzzer that does not turn off until the user exercises their arm enough to satisfy the program (muscular movements measured using the EMG), which will get their blood flowing and body heated to help them wake up. In addition, it will also switch on the thermostat to lower the room temperature so that the user is not as comfortable falling asleep at their desk. Finally, there is an AI voice assistant that converses with the user to keep them thinking and talking (awake through brain activity). 

Dependencies: 
pip install pygame watchdog SpeechRecognition google-generativeai pyaudio python-dotenv pyserial
