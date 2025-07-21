from machine import UART, Pin
import time

# Initialize UART0
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

def BT_send_data(data_value):
    # Send data over BLE UART
    
    uart.write(f"{data_value}\n")
    
    # Check for incoming data
    if uart.any():
        received = uart.read()
        print("Received:", received.decode('utf-8'))
    
    time.sleep(1)