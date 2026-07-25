import os
from PIL import Image

artifacts_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551'
user_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551\.user_uploaded'
dst_dir = r'c:\Users\mitta\OneDrive\ROOTLET PROJECT (WEBSITE)\public\images'

os.makedirs(dst_dir, exist_ok=True)

def process_and_copy(src_path, dst_name):
    img = Image.open(src_path).convert('RGB')
    target_w, target_h = 600, 400
    img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    out_path = os.path.join(dst_dir, dst_name)
    img.save(out_path, quality=98)
    print(f"Saved real-face modified card: {dst_name}")

# 1. Play Group Real Face Modified Photo
process_and_copy(os.path.join(artifacts_dir, 'playgroup_real_face_1784989652358.jpg'), 'playgroup_card.jpg')

# 2. Toddler Real Face Modified Photo (Screenshot 2)
process_and_copy(os.path.join(user_dir, 'media__1784988297535.jpg'), 'toddler_card.jpg')

# 3. Nursery Real Face Modified Photo
process_and_copy(os.path.join(artifacts_dir, 'nursery_real_face_1784989671834.jpg'), 'nursery_card.jpg')

# 4. LKG Real Face Modified Photo
process_and_copy(os.path.join(artifacts_dir, 'lkg_real_face_1784989695293.jpg'), 'lkg_card.jpg')

# 5. UKG Real Face Modified Photo
process_and_copy(os.path.join(artifacts_dir, 'ukg_real_face_1784989717485.jpg'), 'ukg_card.jpg')

# 6. After School Real Face Modified Photo
process_and_copy(os.path.join(artifacts_dir, 'afterschool_real_face_1784989738535.jpg'), 'afterschool_card.jpg')

print("All 6 Real-Face Modified Active Play Cards saved successfully!")
