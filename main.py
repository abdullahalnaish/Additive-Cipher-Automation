import os
import time

KEY = 3
INPUT_DIR = "./input"
OUTPUT_DIR = "./output"

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def encrypt(text, key):
    res = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            res += chr((ord(c) - base + key) % 26 + base)
        else:
            res += c
    return res

print("Service started. Drop .txt files in './input' folder...")

try:
    while True:
        for file in os.listdir(INPUT_DIR):
            if file.endswith(".txt"):
                in_path = os.path.join(INPUT_DIR, file)
                out_path = os.path.join(OUTPUT_DIR, file)
                
                try:
                    with open(in_path, 'r', encoding='utf-8') as f:
                        data = f.read()
                    
                    with open(out_path, 'w', encoding='utf-8') as f:
                        f.write(encrypt(data, KEY))
                    
                    os.remove(in_path)
                    print(f"Encrypted: {file}")
                except Exception as e:
                    print(f"Error processing {file}: {e}")
        time.sleep(2)
except KeyboardInterrupt:
    print("Stopped.")
