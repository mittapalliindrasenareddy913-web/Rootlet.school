import os, shutil
from PIL import Image

artifacts_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551'
user_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551\.user_uploaded'
dst_dir = r'c:\Users\mitta\OneDrive\ROOTLET PROJECT (WEBSITE)\public\images'

os.makedirs(dst_dir, exist_ok=True)

# Helper function to resize and copy
def process_and_copy(src_path, dst_name):
    img = Image.open(src_path).convert('RGB')
    target_w, target_h = 600, 400
    img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    out_path = os.path.join(dst_dir, dst_name)
    img.save(out_path, quality=98)
    print(f"Copied AI generated card: {dst_name}")

# 1. Play Group AI Photo
process_and_copy(os.path.join(artifacts_dir, 'playgroup_ai_active_1784989316763.jpg'), 'playgroup_card.jpg')

# 2. Toddler AI Photo (User's Screenshot 2)
process_and_copy(os.path.join(user_dir, 'media__1784988297535.jpg'), 'toddler_card.jpg')

# 3. Nursery AI Photo
process_and_copy(os.path.join(artifacts_dir, 'nursery_ai_active_1784989337786.jpg'), 'nursery_card.jpg')

# 4. LKG AI Photo
process_and_copy(os.path.join(artifacts_dir, 'lkg_ai_active_1784989359423.jpg'), 'lkg_card.jpg')

# 5. UKG AI Photo
process_and_copy(os.path.join(artifacts_dir, 'ukg_ai_active_1784989379996.jpg'), 'ukg_card.jpg')

# 6. After School AI Photo
process_and_copy(os.path.join(artifacts_dir, 'afterschool_ai_active_1784989403312.jpg'), 'afterschool_card.jpg')

print("All 6 Nano Banana AI Active Play Cards copied successfully!")
