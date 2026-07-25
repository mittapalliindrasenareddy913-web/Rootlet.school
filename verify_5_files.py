import os, glob
from PIL import Image

uploaded_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551\.user_uploaded'

files = [
    'media__1784987423483.jpg',
    'media__1784987772804.jpg',
    'media__1784987795387.jpg',
    'media__1784987807100.jpg',
    'media__1784987832221.jpg'
]

for idx, f in enumerate(files):
    path = os.path.join(uploaded_dir, f)
    if os.path.exists(path):
        im = Image.open(path)
        print(f"Index {idx+1}: {f} size={im.size}")
    else:
        print(f"Missing {f}")
