import warnings
import serial
import serial.tools.list_ports

def trigger_sleepy():
    arduino_ports = [
        p.device
        for p in serial.tools.list_ports.comports()
        if 'USB' in p.description
    ]
    if not arduino_ports:
        raise IOError("No Arduino found")
    if len(arduino_ports) > 1:
        warnings.warn('Multiple Arduinos found - using the first')
    ser = serial.Serial(arduino_ports[0], 9600)
    i = 0
    while (i<100):
        ser.write(b'Sleepy\n')
        i+=1
    