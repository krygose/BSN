# FOR TESTING ONLY, COMMENTED ON PURPOSE


# import importlib
# import serial
# import time
# import random
# import numpy as np
# import argparse
# import ast

# baudrate = 115200
# port = "/dev/ttyACM0"  

# def configStart():
   



#   try:
#     with serial.Serial(port=port, baudrate=baudrate) as ser:
      
#       data_to_send = bytes([0x11]) 
#       ser.write(data_to_send)
#       print("Data sent successfully!")
#   except Exception as e:
#       print(f"Error: {e}")

#   finally:
#     print("Finished")

# def configEnd():

#     try:
#       with serial.Serial(port=port, baudrate=baudrate) as ser:

#         data_to_send = bytes([0x10]) 
#         ser.write(data_to_send)
#         print("Data sent successfully!")
#     except Exception as e:
#         print(f"Error: {e}")

#     finally:
#       print("Finished")

      
# def send_data_with_variable_neuron(ser):
#   for second_byte in range(256):
#     if second_byte <138:
#       data_to_send = bytes([0x43, second_byte, 0xfe, 0x01]) 
#     else:
#       data_to_send = bytes([0x43, second_byte, 0xfe, 0x00])
#     ser.write(data_to_send)
#     print(f"Sent: {data_to_send.hex()}  (Second byte: {second_byte})")
#     time.sleep(0.01) 

# def send_data_with_variable_leak(ser):
#     for second_byte in range(138):

#       data_to_send = bytes([0x43, second_byte, 0x01, 0x02]) 

#       ser.write(data_to_send)
#       print(f"Sent: {data_to_send.hex()}  (Second byte: {second_byte})")
#       time.sleep(0.01) 


# def send_data_with_variable_threshhold(ser):
#     for second_byte in range(138):

#       data_to_send = bytes([0x42, second_byte, 0xfe, 0x02]) 

#       ser.write(data_to_send)
#       print(f"Sent: {data_to_send.hex()}  (Second byte: {second_byte})")
#       time.sleep(0.01)

# def send_data_with_variable_second_byte_neuron(ser):
#     for second_byte in range(138):

#       data_to_send = bytes([0x41, second_byte, 0xff, 0x00])

#       ser.write(data_to_send)
#       print(f"Sent: {data_to_send.hex()}  (Second byte: {second_byte})")
#       time.sleep(0.01)


# def send_data_with_variable_firts_byte_neuron(ser):
#     for second_byte in range(138):

#       data_to_send = bytes([0x40, second_byte, 0xff, 0x00])

#       ser.write(data_to_send)
#       print(f"Sent: {data_to_send.hex()}  (Second byte: {second_byte})")
#       time.sleep(0.01)
  


# def send_data_synapses(ser):

#     data = []

#     with open('neuron_weights_first', 'r') as file:
#         for line in file:
            
#             row = ast.literal_eval(line.strip())
#             data.append(row)

#     for pre in range(64):

#       for post in range(64):
        
#         packet = generate_synapse_packet(pre, post+64, data[pre][post])
#         data_to_send = bytes([packet[0], packet[1], packet[2], packet[3]])

#         ser.write(packet)
#         print(f"Sent: {data_to_send.hex()}  ")
#         time.sleep(0.01)  

# def synapses_data_send_second_layer(ser):
 
#   data2 = []

#   with open('neuron_weights_second', 'r') as file:
#       for line in file:
          
#           row = ast.literal_eval(line.strip())
#           data2.append(row)

  
#   for pre in range(64):

#     for post in range(10):
        
#       packet = generate_synapse_packet(pre+64, post+128, data2[pre][post])
#       data_to_send = bytes([packet[0], packet[1], packet[2], packet[3]]) 

#       ser.write(packet)
#       print(f"Sent: {data_to_send.hex()}  ")
#       time.sleep(0.01) 

# def AERsend(ser):
#   data_2d = []

#   with open('image_1_spikes.txt', 'r') as file:
#       for line in file:
          
#           row = ast.literal_eval(line.strip())
#           data_2d.append(row)

#   data_2d = np.array(data_2d)
#   for i in range(data_2d.shape[0]):
#         for j in range(data_2d.shape[1]):
            
#             if data_2d[i, j] == 1:
#               data_to_send = bytes([0x20, j]) 
#               ser.write(data_to_send)
#               print(f"Sent: {data_to_send.hex()}  ")

#         data_to_send = bytes([0x20, 0xFF])
#         ser.write(data_to_send)
#         print(f"Sent: {data_to_send.hex()}  ")

#   while True:
#     if ser.in_waiting > 0: 
#         message = ser.readline().decode('utf-8').strip()  
#         print("Received:", message)

# def AER():


#   try:
#       with serial.Serial(port=port, baudrate=baudrate) as ser:
#         AERsend(ser)


#   except Exception as e:
#       print(f"Error: {e}")

#   finally:
#       print("Finished sending data.")

# def synapses():


#   try:
#       with serial.Serial(port=port, baudrate=baudrate) as ser:
#           send_data_synapses(ser)
#           synapses_data_send_second_layer(ser)

#   except Exception as e:
#       print(f"Error: {e}")

#   finally:
#       print("Finished sending data.")


# def neuronThreshhold():


#   try:
#       with serial.Serial(port=port, baudrate=baudrate) as ser:
#           send_data_with_variable_threshhold(ser)
#           send_data_with_variable_second_byte_neuron(ser)
#           send_data_with_variable_firts_byte_neuron(ser)

#   except Exception as e:
#       print(f"Error: {e}")

#   finally:
#       print("Finished sending data.")


# def neuronLeak():

#   try:
#       with serial.Serial(port=port, baudrate=baudrate) as ser:
#           send_data_with_variable_leak(ser)

#   except Exception as e:
#       print(f"Error: {e}")

#   finally:
#       print("Finished sending data.")

# def neuronActivate():


#   try:
#       with serial.Serial(port=port, baudrate=baudrate) as ser:
#           send_data_with_variable_neuron(ser)

#   except Exception as e:
#       print(f"Error: {e}")

#   finally:
#       print("Finished sending data.")


# def generate_synapse_packet(pre_neur, post_neur, weight):
#     if not (0 <= pre_neur <= 255):
#         raise ValueError("pre_neur must be an 8-bit value (0-255).")
#     if not (0 <= post_neur <= 255):
#         raise ValueError("post_neur must be an 8-bit value (0-255).")
#     if not (-8 <= weight <= 7):
#         raise ValueError("weight must be a 4-bit signed value (-8 to 7).")

    
#     if weight < 0:
#         weight = (1 << 4) + weight  

   
#     word_addr = (pre_neur << 5) | (post_neur >> 3)

    
#     byte_addr = (post_neur >> 1) & 0b11

  
#     half_byte_select = post_neur & 0b1

    
#     command_byte = (1 << 7) | (byte_addr << 5) | ((word_addr >> 8) & 0b11111)

   
#     word_addr_byte = word_addr & 0xFF

    
#     mask_byte = 0b11110000 if not half_byte_select else 0b00001111

    
#     data_byte = weight << 4 if half_byte_select else weight

   
#     return bytes([command_byte, word_addr_byte, mask_byte, data_byte])

# def main():
#     parser = argparse.ArgumentParser(description="Wybierz funkcję do uruchomienia.")
#     parser.add_argument('-d', '--dzialanie', choices=['configstart', 'configend', 'neuronsetup','synapses','aer'], required=True,
#                         help="Wybierz, którą funkcję uruchomić: configstart lub configend lub neuronsetup lub synapses lub aer.")

#     args = parser.parse_args()

#     if args.dzialanie == 'configstart':
#         configStart()
#     elif args.dzialanie == 'configend':
#         configEnd()
#     elif args.dzialanie == 'neuronsetup':
#         neuronActivate()
#         neuronLeak()
#         neuronThreshhold()
#     elif args.dzialanie == 'synapses':
#         synapses()
#     elif args.dzialanie == 'aer':
#         AER()


# if __name__ == "__main__":
#     main()