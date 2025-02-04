import time
import numpy as np
import argparse
import ast
import serial

BAUDRATE = 115200
PORT = "/dev/ttyACM0"

def send_serial_data(port, baudrate, data):
    try:
        with serial.Serial(port, baudrate) as ser:
            ser.write(data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Operation finished.")

def config_start():
    send_serial_data(PORT, BAUDRATE, bytes([0x11]))

def config_end():
    send_serial_data(PORT, BAUDRATE, bytes([0x10]))

def send_variable_data(command, range_end, extra_bytes):
    try:
        with serial.Serial(PORT, BAUDRATE) as ser:
            for second_byte in range(range_end):
                data_to_send = bytes([command, second_byte, *extra_bytes])
                ser.write(data_to_send)
                time.sleep(0.01)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Finished sending data.")

def neuron_setup():
    send_variable_data(0x43, 256, [0x7F, 0x00])
    send_variable_data(0x43, 138, [0x7F, 0x80])
    send_variable_data(0x43, 138, [0x80, 0x01])
    send_variable_data(0x42, 138, [0x00, 0x14])
    send_variable_data(0x41, 138, [0x00, 0x00])
    send_variable_data(0x40, 138, [0x00, 0x00])

def read_weights(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            row = ast.literal_eval(line.strip())
            data.append(row)
    return data

def send_synapses(data, pre_offset=0, post_offset=64):
    try:
        with serial.Serial(PORT, BAUDRATE) as ser:
            for pre in range(len(data)):
                for post in range(len(data[pre])):
                    packet = generate_synapse_packet(pre + pre_offset, post + post_offset, data[pre][post])
                    ser.write(packet)
                    time.sleep(0.01)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Finished sending synapse data.")

def synapses():
    send_synapses(read_weights('neuron_weights_first.txt'))
    send_synapses(read_weights('neuron_weights_second.txt'), 64, 128)

def aer():
    try:
        with serial.Serial(PORT, BAUDRATE) as ser:
            data_2d = np.array(read_weights('image_1_spikes.txt'))
            for i in range(data_2d.shape[0]):
                for j in range(data_2d.shape[1]):
                    if data_2d[i, j] == 1:
                        send_serial_data(PORT, BAUDRATE, bytes([0x20, j]))
                send_serial_data(PORT, BAUDRATE, bytes([0x20, 0xFF]))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Finished AER transmission.")

def generate_synapse_packet(pre, post, weight):
    weight = (1 << 4) + weight if weight < 0 else weight
    word_addr = (pre << 5) | (post >> 3)
    byte_addr = (post >> 1) & 0b11
    half_byte_select = post & 0b1
    command_byte = (1 << 7) | (byte_addr << 5) | ((word_addr >> 8) & 0b11111)
    word_addr_byte = word_addr & 0xFF
    mask_byte = 0b11110000 if not half_byte_select else 0b00001111
    data_byte = weight << 4 if half_byte_select else weight
    return bytes([command_byte, word_addr_byte, mask_byte, data_byte])

def main():
    parser = argparse.ArgumentParser(description="Choose function to run.")
    parser.add_argument('-d', '--function', choices=['configstart', 'configend', 'neuronsetup', 'synapses', 'aer'], required=True,
                        help="Choose function to execute.")
    args = parser.parse_args()
    
    functions = {
        'configstart': config_start,
        'configend': config_end,
        'neuronsetup': neuron_setup,
        'synapses': synapses,
        'aer': aer
    }
    
    functions[args.function]()

if __name__ == "__main__":
    main()
