import os
from PIL import Image

user_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551\.user_uploaded'
dst_dir = r'c:\Users\mitta\OneDrive\ROOTLET PROJECT (WEBSITE)\public\images'

os.makedirs(dst_dir, exist_ok=True)

files = [
    ('media__1784990109886.jpg', 'school_building_1.jpg'),
    ('media__1784990122125.jpg', 'school_building_2.jpg'),
    ('media__1784990134415.jpg', 'school_building_3.jpg'),
    ('media__1784990146333.jpg', 'school_building_4.jpg')
]

for src_name, dst_name in files:
    src_path = os.path.join(user_dir, src_name)
    img = Image.open(src_path).convert('RGB')
    out_path = os.path.join(dst_dir, dst_name)
    img.save(out_path, quality=98)
    print(f"Saved real school building photo: {dst_name}")

print("All 4 real school building photos processed!")
