# Tampilkan kesalahan

C_RESET = "\033[0m"
C_RED   = "\033[31m"

def menu_kesalahan(kesalahan: str) -> None:
    print(f"{C_RED}TERJADI KESALAHAN!{C_RESET}")
    print(f"{C_RED}{kesalahan}{C_RESET}")