import os
import time
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

# ---------------- BASE DIRECTORY ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------- FILE PATHS ----------------
FIRMWARE_FILE = os.path.join(BASE_DIR, "firmware.bin")
SIGNATURE_FILE = os.path.join(BASE_DIR, "signature.sig")
PUBLIC_KEY_FILE = os.path.join(BASE_DIR, "public_key.pem")
VERSION_FILE = os.path.join(BASE_DIR, "version.txt")
LOG_FILE = os.path.join(BASE_DIR, "security.log")

# ---------------- LOGGING ----------------
def log_event(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.ctime()} - {message}\n")

# ---------------- DOWNLOAD SIMULATION ----------------
def download_firmware():
    print("Downloading firmware from cloud...")
    with open(FIRMWARE_FILE, "rb") as f:
        return f.read()

# ---------------- VERSION CHECK ----------------
def get_local_version():
    with open(VERSION_FILE, "r") as f:
        return f.read().strip()

# ---------------- MAIN ----------------
def main():
    print("Edge Device Started...\n")

    # Simulated cloud version
    cloud_version = "v3.0"

    # Read local version
    local_version = get_local_version()

    print("Local Version:", local_version)
    print("Cloud Version:", cloud_version)

    if cloud_version <= local_version:
        print("Device is up to date")
        return

    print("Update available\n")

    # Download firmware
    firmware = download_firmware()

    # Load signature
    with open(SIGNATURE_FILE, "rb") as f:
        signature = f.read()

    # Load public key
    with open(PUBLIC_KEY_FILE, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    try:
        # Verify firmware signature
        public_key.verify(
            signature,
            firmware,
            padding.PKCS1v15(),
            hashes.SHA256()
        )

        print("Firmware VERIFIED")
        print("Installing update...")

        # Update version file
        with open(VERSION_FILE, "w") as f:
            f.write(cloud_version)

        log_event(f"Firmware updated successfully to {cloud_version}")

        print("Update COMPLETE")

    except Exception:
        print("SECURITY ALERT: INVALID FIRMWARE")
        print("UPDATE BLOCKED")

        log_event("Firmware verification failed")

# ---------------- RUN ----------------
if __name__ == "__main__":
    main()