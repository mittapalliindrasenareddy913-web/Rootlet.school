import os, glob
from PIL import Image

uploaded_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551\.user_uploaded'
files = sorted(glob.glob(os.path.join(uploaded_dir, '*.*')), key=os.path.getmtime, reverse=True)

logo_path = files[0]
print(f"Analyzing logo screenshot: {os.path.basename(logo_path)}")

img = Image.open(logo_path).convert('RGB')
w, h = img.size

# Sample pixels from leaf (green), name (coral), tagline (olive)
# Green leaf is on left (x ~ 0.1 * w, y ~ 0.3 * h)
leaf_rgb = img.getpixel((int(w * 0.08), int(h * 0.3)))
# Coral name is in middle (x ~ 0.4 * w, y ~ 0.3 * h)
name_rgb = img.getpixel((int(w * 0.4), int(h * 0.3)))
# Tagline is on bottom right (x ~ 0.7 * w, y ~ 0.88 * h)
tagline_rgb = img.getpixel((int(w * 0.7), int(h * 0.88)))

print(f"Leaf Green RGB: {leaf_rgb} -> #{leaf_rgb[0]:02x}{leaf_rgb[1]:02x}{leaf_rgb[2]:02x}")
print(f"Name Coral RGB: {name_rgb} -> #{name_rgb[0]:02x}{name_rgb[1]:02x}{name_rgb[2]:02x}")
print(f"Tagline Olive RGB: {tagline_rgb} -> #{tagline_rgb[0]:02x}{tagline_rgb[1]:02x}{tagline_rgb[2]:02x}")
