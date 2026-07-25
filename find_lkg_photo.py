import os, glob
from PIL import Image

uploaded_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551\.user_uploaded'
files = sorted(glob.glob(os.path.join(uploaded_dir, '*.*')), key=os.path.getmtime, reverse=True)

for f in files[:10]:
    try:
        im = Image.open(f)
        print(f"{os.path.basename(f)}: format={im.format}, size={im.size}, mtime={os.path.getmtime(f)}")
    except Exception as e:
        print(f"Error {f}: {e}")
