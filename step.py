

# steps2.py
import cv2
import numpy as np

def load_color_image(image_path):
    return cv2.imread(image_path)

def split_color_channels(image):
    return cv2.split(image)

def apply_fft(channel):
    return np.fft.fft2(channel)

def fft_shift(channel_fft):
    # Appliquer la fftshift sur le canal fft
    shifted_channel_fft = np.fft.fftshift(channel_fft)
    
    return shifted_channel_fft

def inverse_fft_shift(shifted_channel_fft):
    
    unshifted_channel_fft = np.fft.ifftshift(shifted_channel_fft)
    
    return unshifted_channel_fft




def apply_inverse_fft(channel_fft):
    
    inverse_fft_channel = np.fft.ifft2(channel_fft)
    
    return inverse_fft_channel


def combine_color_channels(channels):
    return cv2.merge(channels)

def save_steganographic_image(image, output_path):
    cv2.imwrite(output_path, image)

# message.py
def binary_to_text(binary_message):
    # Convertir le message binaire en texte
    text_message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
    return text_message

def text_to_binary(text_message):
    # Convertir le texte en message binaire
    binary_message = ''.join(format(ord(char), '08b') for char in text_message)
    return binary_message

def get_binary_message_length(message):
    # Obtenir la longueur binaire du message
    return format(len(message), '08b')


def modify_frequency_coefficients(channel_fft, binary_message):


    binary_message = str(binary_message)

    length = len(binary_message)

    for i in range(len (channel_fft[0])):
            

            a = channel_fft[0][i]

            length = len(binary_message)

  

            if length> 0 and channel_fft[0][i].real > 0 :

                bit  = binary_message[0]

                if bit == "1":

                    channel_fft[0][i] = complex (int ((channel_fft[0][i].real//2)*2 ), channel_fft[0][i].imag)
                else :

                    channel_fft[0][i] = complex (int ((channel_fft[0][i].real//2)*2 +1 ), round (channel_fft[0][i].imag))
                    

                binary_message = binary_message[1:]


                print ( "valeur avant modif :",a , "valeur après modif ", channel_fft[0][i])

               

                length +=1

            elif length <=0 : 

                break 




    return channel_fft, len (binary_message)


def binary_to_text(binary_string):
    """Convertit une chaîne binaire en texte."""
    text = ''.join([chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8)])
    return text

def text_to_binary(text):
    """Convertit un texte en une chaîne binaire."""
    binary_string = ''.join(format(ord(char), '08b') for char in text)
    return binary_string

def get_binary_message_length(binary_message):
    """Obtient la longueur du message binaire."""
    # En supposant que les 8 derniers bits représentent la longueur du message
    length_bits = binary_message[-8:]
    message_length = int(length_bits, 2)
    return message_length

