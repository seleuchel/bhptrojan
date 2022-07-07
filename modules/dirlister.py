import os
def run(**args):
    print("[*] Indirlister module.")
    files = os.listdir(".") # 모듈은 run 함수를 제공해야함 
    return str(files)
