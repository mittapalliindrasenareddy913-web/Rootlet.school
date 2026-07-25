import os, glob
from PIL import Image

uploaded_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551\.user_uploaded'
files = sorted(glob.glob(os.path.join(uploaded_dir, '*.*')), key=os.path.getmtime, reverse=True)

logo_path = files[0]
print(f"Analyzing new logo screenshot: {os.path.basename(logo_path)}")

img = Image.open(logo_path).convert('RGB')
w, h = img.size

# Scan for leaf green (left side), brand coral (top right), tagline green (bottom right)
leaf_rgb = img.getpixel((int(w * 0.25), int(h * 0.4)))
coral_rgb = img.getpixel((int(w * 0.45), int(h * 0.3)))
tagline_rgb = img.getpixel((int(w * 0.45), int(h * 0.8)))

print(f"Leaf Green RGB: {leaf_rgb} -> #{leaf_rgb[0]:02x}{leaf_rgb[1]:02x}{leaf_rgb[2]:02x}")
print(f"Brand Coral RGB: {coral_rgb} -> #{coral_rgb[0]:02x}{coral_rgb[1]:02x}{coral_rgb[2]:02x}")
print(f"Tagline Green RGB: {tagline_rgb} -> #{tagline_rgb[0]:02x}{tagline_rgb[1]:02x}{tagline_rgb[2]:02x}")
