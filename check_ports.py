import serial
import serial.tools.list_ports

def get_ports():
    ports = serial.tools.list_ports.comports()
    ports2=[]
    for port, desc, hwid in sorted(ports):
        ports2.append(port)
    return ports2


