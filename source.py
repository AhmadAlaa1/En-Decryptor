import Encryption
import Decryption

choice = input("[1] Encrypt \t [2] Decrypt \n\n : ")

match choice:
    case "1":
        File_name = input("Enter The Full FIle Name (e.g:test.txt): ")

        Encryption.File_Encryption(File_name)

        print("File Has Been Encrypted")


        with open(f"keys/encrypted_{File_name}.key","r") as key:
            print("The File Key is : ",key.read())

    case "2":
        File_name = input("Enter The Full FIle Name (e.g:test.txt): ")
        Key = input("Enter The Key : ")
        Decryption.File_Decryption_Key(File_name,Key)

        print("File Has Been Decrypted")

