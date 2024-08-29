from Encryption import *
from Decryption import *
import os

choice =""

while(choice != "3"):
    print("\n")
    os.system("figlet -c -f slant 'WELCOME !' ")
    choice = input("[1] Encrypt \t [2] Decrypt \t [3] Exit \n\n ==> ")
    
    match choice:

        case "1":
            choice_2 = input("[1] Encrypt File \t [2] Encrypt Text Input \n\n ==>")

            match choice_2:
                case "1":
                    File_name = input("Enter The Full File Name (e.g:test.txt): ")
                    if os.path.exists(File_name):
                        File_Encryption(File_name)
                        print("\nFile Has Been Encrypted")

                        with open(f"keys/encrypted_{File_name}.key","r") as key:
                            print("The File Key is : ",key.read())
                    else:
                        print("The File Not Exist")
                case "2":
                    text_input = input("Enter Something to Encrypt: ")
                    Input_Encryption(text_input)
                    print("\nText Has Been Encrypted")

                    with open(f"keys/encrypted_{text_input}.key","r") as key:
                            print("The File Key is : ",key.read())

        case "2":
            File_name = input("Enter The Full File Name (e.g:test.txt): ")
            if os.path.exists(File_name):
                Key = input("Enter The Key : ")
                File_Decryption(File_name,Key)

                print("File Has Been Decrypted")

            else:
                print("The File Not Exist")

        case "3":
            os.system("figlet -c -f slant 'See You Later !' ")
            break