from cryptography.fernet import Fernet

conscience = b'gAAAAABj2gTp5QkXTmb0vXSCOP0THO-VcnNhDzAU1C8j3DN3T45UAo5zndfV1AKjPp12dDWQs4K8FzhsmUB7v35Z2CCr6WQjFfB3s9tfovtDXDtgdZKpF-c='
key = b'gUqY5SQ17FDYhyP-dfmqhFxBargXXFUvzdeKyM6I5K0='
f = Fernet(key)
print(f.decrypt(conscience))





