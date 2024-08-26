from cryptography.fernet import Fernet

def File_Decryption_Key(name,key):
    
    fern = Fernet(key) # use the key

    with open(f"{name}","rb") as encrypted_file:
        file = encrypted_file.read()
    
    Decrypted_File = fern.decrypt(file)
    
    name = name.replace("encrypted","")
    with open(f"decrypted_{name}","wb") as decrypted_file:
        decrypted_file.write(Decrypted_File) # save the decrypted file
    
# 1- Read The File Key 
# 2- Store Key 
# 3- Use This Key 
# 4- Read The Decrypted File Content 
# 5- Store it => Decrypt it 
# 6- Save The Decrypted File
