# Return string: password
import time

def menu_password() -> str:
    print("=============================")
    print("\tMENU PASSWORD")
    print("=============================")
    password = str(input("Masukkan Password : "))
    print("=============================")
    print("Progress:  10%"); time.sleep(0.2)
    print(" Progress:  30%"); time.sleep(0.2)
    print(" Progress:  50%"); time.sleep(0.2)
    print(" Progress:  70%"); time.sleep(0.2)
    print(" Progress:  90%"); time.sleep(0.5)
    print(" Progress: 100% "); time.sleep(0.2)
    print("=============================")
    print("\t  SUCCESS ")
    print("=============================")

    return password

# RETURN PASSWORD JANGAN SAMPAI KETINGGALAN