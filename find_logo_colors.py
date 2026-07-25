import os, glob
from PIL import Image

uploaded_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551\.user_uploaded'
files = sorted(glob.glob(os.path.join(uploaded_dir, '*.*')), key=os.path.getmtime, reverse=True)

img = Image.open(files[0]).convert('RGB')
w, h = img.size

# Scan for green pixels (where G > R and G > B)
green_colors = []
olive_colors = []
for y in range(h):
    for x in range(w):
        r, g, b = img.getpixel((x, y))
        if g > r + 30 and g > b + 20:
            green_colors.append((r, g, b))
        elif r > 80 and g > 80 and b < 50:
            olive_colors.append((r, g, b))

if green_colors:
    avg_g = green_colors[len(green_colors)//2]
    print(f"Leaf Green Exact HEX: #{avg_g[0]:02x}{avg_g[1]:02x}{avg_g[2]:02x}")

if olive_colors:
    avg_o = olive_colors[len(olive_colors)//2]
    print(f"Tagline Olive Exact HEX: #{avg_o[0]:02x}{avg_o[1]:02x}{avg_o[2]:02x}")
