# Bryan Carter - c03697673 
# Advanced Security Lab 3.
# desecb.py
# Encryption and decryption with DES in ECB mode.

#!/usr/bin/env python3

from Crypto.Cipher import DES									# import DES from the Crypto.Cipher library.
import codecs													# import codecs to handle string encoding.

the_following = 'AAAABBBBAAAABBBB'								# silly variable name chosen for message.
key = '12345678'												# set the key value to "12345678".
des = DES.new(key, DES.MODE_ECB)								# make a DES object, pass it the key and set the mode to ECB.

cyphertext = des.encrypt(the_following)							# cyphertext value set to result of encryption function call.
print("Cyphertext: ", codecs.getencoder('hex')(cyphertext)[0])	# print cyphertext.

plaintext = des.decrypt(cyphertext)								# plaintext value set to result of decryption function call.
print("Plaintext: ", plaintext)									# print plaintext.
