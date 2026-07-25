import os, glob
from PIL import Image

uploaded_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551\.user_uploaded'
dst_dir = r'c:\Users\mitta\OneDrive\ROOTLET PROJECT (WEBSITE)\public\images'

files = sorted(glob.glob(os.path.join(uploaded_dir, '*.*')), key=os.path.getmtime, reverse=True)
logo_src = files[0]

img = Image.open(logo_src).convert('RGBA')

# Save official logo PNG to public/images/
out_path = os.path.join(dst_dir, 'rootlet_official_logo.png')
img.save(out_path, quality=100)
print(f"Saved official logo PNG: {out_path}")
