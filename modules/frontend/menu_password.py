# Return string: password
import time

hijau = "\033[92m"
biru = "\033[94m"
reset = "\033[0m"

def menu_password() -> str:
    print("=============================")
    print("\tMENU PASSWORD")
    print("=============================")
    password = str(input("Masukkan Password : "))
    print("=============================")
    print(biru + " Progress:  10%"); time.sleep(0.2)
    print(" Progress:  30%"); time.sleep(0.2)
    print(" Progress:  50%"); time.sleep(0.2)
    print(" Progress:  70%"); time.sleep(0.2)
    print(" Progress:  90%"); time.sleep(0.5)
    print(" Progress: 100% " + reset); time.sleep(0.2)
    print("=============================")
    print(hijau + "\t  SUCCESS " + reset)
    print("=============================")

    return password

# RETURN PASSWORD JANGAN SAMPAI KETINGGALAN