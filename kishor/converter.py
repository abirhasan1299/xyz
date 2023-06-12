from cryptography.fernet import Fernet

def Encode(request):
    key  = Fernet.generate_key()
    fernate = Fernet(key)
    encrypData = fernate.encrypt(request.encode())

    return encrypData