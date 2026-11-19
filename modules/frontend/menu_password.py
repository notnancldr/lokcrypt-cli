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
    for i in range(5):
        jeda = 0.3
        if i == 3:
            jeda = 0.5
        print(f"{biru}\r Progress:  {(i+1)*20}% {reset}", end=""); time.sleep(jeda)
    print("\n=============================")

    return password
menu_password()
# RETURN PASSWORD JANGAN SAMPAI KETINGGALAN