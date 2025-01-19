import serial
import serial.tools.list_ports

def get_ports():
    ports = serial.tools.list_ports.comports()
    ports2 = []
    for port, desc, hwid in sorted(ports):
        ports2.append(port)
    return ports2


def get_ports2() -> list:
    ports: list = sorted(map(lambda s: s[0], sorted(serial.tools.list_ports.comports())))
    return ports


def open_connection(step: int, angle: int) -> serial.Serial:
    uart = serial.Serial(port='COM3', baudrate=115200)
    angle_lidar = angle

    if uart.is_open:
        st = f"$LDESP,0,0,0,0,{angle_lidar},{step},0,"
        uart.write(st.encode())

    return uart