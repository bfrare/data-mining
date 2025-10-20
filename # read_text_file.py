# read_text_file.py
import os

text_path = r"C:\Users\Asus\Downloads\BAFtext.txt"

if os.path.exists(text_path):
    try:
        with open(text_path, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
        print("✅ :", len(text))
        print("\nPreview :\n")
        print(text[:])
    except Exception as e:
        print(f"❌ : {e}")
else:

    print(f"⚠️ : {text_path}") 
