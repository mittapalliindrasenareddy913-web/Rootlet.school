import os
from PIL import Image

src_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551\.user_uploaded'
dst_dir = r'c:\Users\mitta\OneDrive\ROOTLET PROJECT (WEBSITE)\public\images'

# 1. Play Group image crop (centered on toddler's face)
playgroup_src = os.path.join(src_dir, 'media__1784985650091.jpg')
im_pg = Image.open(playgroup_src).convert('RGB')

# Crop to include full head & face (from y=50 to y=650)
w, h = im_pg.size
im_pg_cropped = im_pg.crop((0, int(h * 0.05), w, int(h * 0.65)))
im_pg_cropped.save(os.path.join(dst_dir, 'playgroup.jpg'), quality=95)

# 2. LKG image (Pic 1: baby sitting in denim vest)
lkg_src = os.path.join(src_dir, 'media__1784986075368.png')
im_lkg = Image.open(lkg_src).convert('RGB')
im_lkg.save(os.path.join(dst_dir, 'lkg.jpg'), quality=95)
im_lkg.save(os.path.join(dst_dir, 'studio_fine_motor.jpg'), quality=95)

print("Play Group and LKG photos processed perfectly!")
