from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None
    )

with open("hello/git/firmware.bin", "rb") as file:
    firmware_data = file.read()

signature = private_key.sign(
    firmware_data,
    padding.PKCS1v15(),
    hashes.SHA256()
)

with open("signature.sig", "wb") as sig_file:
    sig_file.write(signature)

print("Firmware signed successfully!")