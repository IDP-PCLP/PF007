#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 01:38:40 2021

@author: Fontanap
"""

from cryptography.fernet import Fernet

#FUNCOES
def GENERATE_KEY():
        key = Fernet.generate_key()
        fkey = open("file_key.txt", 'wb')
        fkey.write(key)
        cipher = Fernet(key)
        encrypted_text = cipher.encrypt
        key = Fernet.generate_key()
        fkey = open("file_key.txt", 'wb')
        fkey.write(key)
        cipher = Fernet(key)
        encrypted_text = cipher.encrypt
        #Read Key
        fkey = open("file_key.txt", 'rb')
        key = fkey.read()
        cipher = Fernet(key)
        print("""
SYMMETRIC KEY: """,key)
        input()

def ENCRYPT_FILE():
    
        filename = input('CHOOSE A FILE TO BE ENCRYPTED: ')
        
        fkey = input("INPUT YOUR KEY: ")
        # key = fkey.read()
        cipher = Fernet(fkey)
            
        with open(filename,'rb')as f:
            e_file = f.read()
        
        encrypted_file = cipher.encrypt(e_file)
        
        with open(filename + "encrypted",'wb') as ef:
            ef.write(encrypted_file)
        input('FILE ENCRYPTED') 
        
def DECRYPT_FILE():
        fileName = input('CHOOSE A FILE TO BE DECRYPTED: ')
            
        fkey = input("ENTER YOUR KEY: ")
        # key = fkey.read()
        cipher = Fernet(fkey)
        with open(fileName,'rb') as df:
                encrypted_data = df.read()
        decrypted_file = cipher.decrypt(encrypted_data)
        with open(fileName + 'decrypted','wb') as df:
            df.write(decrypted_file)
        input('FILE DECRYPTED')


print("""
 ______     __     ______   __  __     ______     ______    
/\  ___\   /\ \   /\  == \ /\ \_\ \   /\  ___\   /\  == \   
\ \ \____  \ \ \  \ \  _-/ \ \  __ \  \ \  __\   \ \  __<   
 \ \_____\  \ \_\  \ \_\    \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_____/   \/_/   \/_/     \/_/\/_/   \/_____/   \/_/ /_/ 
                                                            
  by fontanap        
  """)
input("""PRESS ENTER TO START """)

while True:  
    MainMenu = input(""" MAIN MENU
[GENERATE_KEY]
[ENCRYPT_FILE]
[DECRYPT_FILE]
[QUIT]
: """)
    if MainMenu in '':
        input("NO COMMAND SELECTED")
        continue
        
    elif MainMenu in 'GENERATE_KEY':
        GENERATE_KEY()
        
    elif MainMenu in 'ENCRYPT_FILE':
        ENCRYPT_FILE()
        
    elif MainMenu in 'DECRYPT_FILE':
        DECRYPT_FILE()     

    elif MainMenu in 'QUIT':
        input("""OPERATION ENDED""")
            
        input("""THANK YOU FOR USING CIPHER """)
        break
    else:
        input("ERROR: UNKNOWN COMMAND")



