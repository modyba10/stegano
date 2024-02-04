# stegano.py
import cv2
from PIL import Image
import numpy as np
from step import load_color_image, split_color_channels, apply_fft, fft_shift,  modify_frequency_coefficients, inverse_fft_shift, apply_inverse_fft, combine_color_channels, save_steganographic_image
from message import binary_to_text, text_to_binary, get_binary_message_length



import matplotlib.pyplot as plt

def encode(image_path, message, output_path='test.jpg'):
    
    original_image = load_color_image(image_path)

    channels = split_color_channels(original_image)
    
    binary_message = text_to_binary(message) + "11111111"
    
    message_length = len(binary_message)

    fft_channels = [apply_fft(channel) for channel in channels]

    fft_shifted_channels = [fft_shift(channel_fft)for channel_fft in fft_channels]

    for i in range(3): 
        for j in range(len(fft_shifted_channels)):
            
            if message_length > 0:
                # Modifier les coefficients de fréquence avec les bits du message
                fft_shifted_channels[j], message_length, binary_message = modify_frequency_coefficients(fft_shifted_channels[j], binary_message)

                
            else:
                break

        if message_length <= 0:
            break


    inverse_fft_unshifted_channels = [inverse_fft_shift(channel_fft) for channel_fft in fft_shifted_channels]
    
    
    
    

    inverse_fft_channels = [apply_inverse_fft(channel_fft_shifted) for channel_fft_shifted in inverse_fft_unshifted_channels]
    channels = [np.round (np.real(channel)) for channel in inverse_fft_channels]
    

    steganographic_image = cv2.merge(channels)

    
   

    """print( "Deuxième phase")

    channels1 = split_color_channels(steganographic_image)
    fft_channels1 = [apply_fft(channel) for channel in channels1]


    fft_shifted_channels1 = [np.real (fft_shift(channel_fft)) for channel_fft in fft_channels1]

    for i in range (72) :

        real_binary = format(int(round(fft_shifted_channels1[0][0][i].real)), '032b')

        print ("nombre orginal : ", (fft_shifted_channels1[0][0][i].real), "nombre en binaire : ",real_binary )"""


    
    save_steganographic_image(steganographic_image, output_path)



def decode(steganographic_image_path, orginal_image_path):

    steganographic_image = load_color_image(steganographic_image_path)
    bit =""
    channels = split_color_channels(steganographic_image)

    fft_channels = [apply_fft(channel) for channel in channels]

    fft_shifted_channels = [fft_shift(channel_fft) for channel_fft in fft_channels]

    original_image = load_color_image(orginal_image_path)

    channels_orig = split_color_channels(original_image)

    fft_channels_orig = [apply_fft(channel) for channel in channels_orig]

    fft_shifted_channels_orig = [fft_shift(channel_fft) for channel_fft in fft_channels_orig]




    for j in range (200) :
            
            if fft_shifted_channels_orig[0][0][j] >0 and fft_shifted_channels[0][0][j] > 0 :
            
                 print ("valeur de l'original",fft_shifted_channels_orig[0][0][j], "valeur du codé", fft_shifted_channels[0][0][j] )
            
                 bit += "1" if fft_shifted_channels_orig[0][0][j] == fft_shifted_channels[0][0][j] else "0"

    

    return bit


"""def extract_frequency_coefficients(channel):

    stop_point = 0
    binary_message = ""

    for i in range(channel.shape[0]):
        for j in range(channel.shape[1]):
            real_binary = format(int(round(channel[i][j].real)), '032b')
            bit =  real_binary[29]
            binary_message += bit

            if bit == "1":
                stop_point += 1

            if stop_point == 8:
                break

            binary_message += bit
            
            if stop_point == 8:
                break
        if stop_point == 8:
            break

    return binary_message"""












