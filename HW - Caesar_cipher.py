"""
@author: Augusto Fonseca and Rodrigo Dornelles
"""

# Code to create the class CaesarCipher

class CaesarCipher:

    # define an attribute key to identify the parameter that will be used to encrypt the message
    def __init__(self, key):
        self.key = key # key used to cipher the message - integer
        self.lw_dict = {chr(i+96):i for i in range(1,27)} # create a dictionary to convert lower case characters to an integer
        self.up_dict = {chr(i+64):i for i in range(1,27)} # create a dictionary to convert upper case characters to an integer

    # Method to convert the original string message in a list
    def str_to_list(self, original_str):
        return list(original_str)

    # Method to convert a list os characters in a string
    def list_to_str(self, original_list):
        converted_str = ''.join(original_list)
        return converted_str

    # receive each char to cipher and the option to encrypt "True" or decrypt "False"
    def convert_chars(self, letter, option):
        # compare to check if the char is uppercase and find it on the dictionary
        if letter.isupper():  # if it`s uppercase
            if option: coded_index = (self.up_dict[letter] + self.key) % 26 # Add the key to encrypt
            else: coded_index = (self.up_dict[letter] - self.key) % 26 # subtract the key to decrypt
            return list(self.up_dict)[coded_index-1] #return the value of the dictionary for the encrypted index

        elif letter.islower():  # compare to check if the char is lowercase and find it on the dictionary
            if option: coded_index = (self.lw_dict[letter] + self.key) % 26 # Add the key to encrypt
            else: coded_index = (self.lw_dict[letter] - self.key) % 26 # subtract the key to decrypt
            return list(self.lw_dict)[coded_index-1] #return the value of the dictionary for the encrypted index
        else:
            return letter  # Return the original char, as it`s not a letter

    #Main method to encrypt a message
    def encrypt(self, message_string): # receive a string to encrypt

        list_to_encrypt = self.str_to_list(message_string) # convert the string to a list
        encrypted_list = list() # create an empty list to receive the encrypted characters

        # call the method "convert_chars"for each character in the message
        for each_char in list_to_encrypt:
            encrypted_list += self.convert_chars(each_char, True) # parameter true to decrypt
        return self.list_to_str(encrypted_list) # return the encrypted list converted to a string

    # call the method "convert_chars"for each character in the message
    def decrypt(self, message_string): # receive a string to decrypt

        list_to_decrypt = self.str_to_list(message_string)  # convert the string to a list
        decrypted_list = list() # create an empty list to receive the decrypted characters
        for each_char in list_to_decrypt:
            decrypted_list += self.convert_chars(each_char, False) # parameter false to decrypt
        return self.list_to_str(decrypted_list) # return the encrypted list converted to a string


# Create an instance for the CaesarCipher class with a key to encrypt
cipher = CaesarCipher(5)

# Original message to encrypt
message = "THE eagle IS IN PLAY; MEET AT JOE'S"

# Print the encrypted message
coded = cipher.encrypt(message)
print("Secret: ", coded)

# Print the original message
answer = cipher.decrypt(coded)
print("Message: ", answer)