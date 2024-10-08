from cryptography.fernet import Fernet # import fernet library

def File_Encryption(name): 
    key = Fernet.generate_key()

    with open(f"keys/encrypted_{name}.key","wb") as key_file:
        key_file.write(key) # save the key in file 

    with open(f"keys/encrypted_{name}.key","rb") as key_file:
        key = key_file.read() # read the key in file 

    fern = Fernet(key) # use the generated key in the file

    with open(f"{name}","rb") as original_file:
        original = original_file.read()

    encrypted_file = fern.encrypt(original) 
    
    with open(f"encrypted_{name}","wb") as myencrypted:
     myencrypted.write(encrypted_file) # save the encrypted file


def Input_Encryption(input):
   key = Fernet.generate_key()
   with open(f"keys/encrypted_{input}.key","wb") as file_key:
        file_key.write(key)
    
   original_file = input.encode() 
   fern = Fernet(key)

   encrypted_file = fern.encrypt(original_file)

   with open(f"encrypted_{input}.txt","wb") as Encrypted_file:
       Encrypted_file.write(encrypted_file)

#===============================================
# 1- Generate Key 
# 2- Store Key 
# 3- Use This Key 
# 4- Read Original File Content 
# 5- Store it => Encrypt it 
# 6- Save The Encrypted File
#===============================================


