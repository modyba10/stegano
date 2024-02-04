# stegano.py
import cv2
from PIL import Image
import numpy as np
from step import load_color_image, split_color_channels, apply_fft, fft_shift,  modify_frequency_coefficients, inverse_fft_shift, apply_inverse_fft, combine_color_channels, save_steganographic_image
from step import binary_to_text, text_to_binary, get_binary_message_length



import matplotlib.pyplot as plt

def encode(image_path, message, output_path='test.jpg'):
    
    original_image = load_color_image(image_path)

    channels = split_color_channels(original_image)
    
    binary_message = text_to_binary(message) + "11111111"
    
    message_length = len(binary_message)

    fft_channels = [apply_fft(channel) for channel in channels]

    fft_shifted_channels = [fft_shift(channel_fft)for channel_fft in fft_channels]

    """for i in range (72) :
        
        if fft_shifted_channels[0][0][i].real >0 :

           print ("nombre orginal : ", (fft_shifted_channels[0][0][i]))"""


     # Modifier les coefficients de fréquence avec les bits du message
    fft_shifted_channels[0], binary_message = modify_frequency_coefficients(fft_shifted_channels[0], binary_message)

    """for i in range (72) :
        
        if fft_shifted_channels[0][0][i].real >0 :

           print ("nombre orginal : ", (fft_shifted_channels[0][0][i]))"""





    inverse_fft_unshifted_channels = [inverse_fft_shift(channel_fft) for channel_fft in fft_shifted_channels]
    
    
    
    

    inverse_fft_channels = [apply_inverse_fft(channel_fft_shifted) for channel_fft_shifted in inverse_fft_unshifted_channels]
    channels = [np.real(channel) + np.round (2* (np.real(channel)-np.round(np.real(channel))))  for channel in inverse_fft_channels]
    

    steganographic_image = cv2.merge(channels)

    
   

    """print( "Deuxième phase")

    channels1 = split_color_channels(steganographic_image)
    fft_channels1 = [apply_fft(channel) for channel in channels1]


    fft_shifted_channels1 = [fft_shift(channel_fft) for channel_fft in fft_channels1]

    for i in range (72) :

        if fft_shifted_channels1[0][0][i].real > 0 :

        

            print ("nombre orginal : ", (fft_shifted_channels1[0][0][i]))"""


    
    save_steganographic_image(steganographic_image, output_path)



def decode(steganographic_image_path, orginal_image_path):

    steganographic_image = load_color_image(steganographic_image_path)
    bit =""
    channels = split_color_channels(steganographic_image)

    fft_channels = [apply_fft(channel) for channel in channels]

    fft_shifted_channels = [fft_shift(channel_fft) for channel_fft in fft_channels]

    """original_image = load_color_image(orginal_image_path)

    channels_orig = split_color_channels(original_image)

    fft_channels_orig = [apply_fft(channel) for channel in channels_orig]

    fft_shifted_channels_orig = [fft_shift(channel_fft) for channel_fft in fft_channels_orig]"""




    for j in range (100) :
            
            if  fft_shifted_channels[0][0][j].real  >0 : 
            
                 print ("valeur décodage", fft_shifted_channels[0][0][j] )
            
                

    

    return 0








# Exemple d'utilisation
image_path = "PHOTO_BA.jpg"

message = "AAA"
#decode("stego_image.jpg")





stego_image_path = "stego_image.png"

    
encode(image_path, message, output_path=stego_image_path)

a =decode ("stego_image.png","PHOTO_BA.jpg")









