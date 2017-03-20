# Bryan Carter - c03697673 
# Advanced Security Lab 3.
# despadding.py
# Encryption and decryption with DES in ECB mode with padding.

#!/usr/bin/env python3

from Crypto.Cipher import DES									# import DES from the Crypto.Cipher library.
import codecs													# import codecs to handle string encoding.

def pad_text(target_data, padding_data)
# function to pad passed text data with passed padding data.
	if(padding_data == o):										
	# if no padding data is required...		
		return target_data										# just return the text.
	else:														
	#otherwise...
		empty_space = padding_data-2							# empty space remaining to be filled reduced by 2.
		for x in range(0, empty_space):
		# for all values of x between 0 and the emptry space...
			target_data = target_data + "\x00"					# append "\xoo" to the text.
		if (empty_space == 1)
		# if the empty space is exactly 1...
			target_data = target_data + str(padding_data)		# just convert the padding data to a string and directly append it.
		else:
		# otherwise...
			target_data = target_data + "0"						# append a "0" to the target data.
			target_data = target_data + str(padding_data)		# then append the padding data directly to the target data.
		return target_data										# return the target data.

def unpad_text(target_data, padding_data)
# function to remove the padding from data.
	target_data = target_data[:-padding_data]					# remove padding data from target data.
	return target_data											# return the target data.
	
def differentiate(text_length_in)
# a function to get the required padding length.
	temp_length = text_length									# set a temp value.
	difference = 0												# initial difference is zero.
	control = 0													# boolean control because I am bad at Python...
	while control == 0:
	# while the control value is zero...
		temp_length = temp_length - 8							# deduct a byte from the length.
		if (temp_length <= 8):
		# if the length is now under a byte...
			control = 1											# set control to 1.
			difference = 8 - temp_length						# the difference is 8 minus the remaining length, ie: a byte minus some bits.
	return difference											# return the difference.


the_following = 'AAAABBBBAAAABBBB'								# silly variable name chosen for message.
key = '12345678'												# set the key value to "12345678".
des = DES.new(key, DES.MODE_ECB)								# make a DES object, pass it the key and set the mode to ECB.
text_length = differentiate(the_following)						# get the length of the text to be padded.
padding_length = diff(text_length)								# get the pading
message = pad_text(the_following, padding_length)				# pad the message.


cyphertext = des.encrypt(message)								# cyphertext value set to result of encryption function call.
print("Cyphertext: ", codecs.getencoder('hex')(cyphertext)[0])	# print the cyphertext as hex data.

padded_plaintext = des.decrypt(cyphertext)						# padded plaintext value set to result of decryption function call.
print("Padded laintext: ", padded_plaintext)					# print padded plaintext.

plaintext = unpad_text(padded_plaintext, padding_length)		# plaintext value set to result unpadding function call.
print("Plaintext: ", plaintext)									# print plaintext.
