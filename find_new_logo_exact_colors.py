import os, glob
from PIL import Image

uploaded_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551\.user_uploaded'
files = sorted(glob.glob(os.path.join(uploaded_dir, '*.*')), key=os.path.getmtime, reverse=True)

img = Image.open(files[0]).convert('RGB')
w, h = img.size

coral_pixels = []
green_pixels = []

for y in range(h):
    for x in range(w):
        r, g, b = img.getpixel((x, y))
        # Coral: R high, G medium, B low
        if r > 200 and g > 90 and b < 120:
            coral_pixels.append((r, g, b))
        # Green: G high, R medium, B low
        elif g > 150 and r < 180 and b < 120:
            green_pixels.append((r, g, b))

if coral_pixels:
    c = coral_pixels[len(coral_pixels)//2]
    print(f"Exact Coral Red HEX: #{c[0]:02x}{c[1]:02x}{c[2]:02x}")

if green_pixels:
    g = green_pixels[len(green_pixels)//2]
    print(f"Exact Leaf Green HEX: #{g[0]:02x}{g[1]:02x}{g[2]:02x}")
