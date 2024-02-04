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

