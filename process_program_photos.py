import os, shutil
from PIL import Image

src_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551\.user_uploaded'
dst_dir = r'c:\Users\mitta\OneDrive\ROOTLET PROJECT (WEBSITE)\public\images'
dst_public = r'c:\Users\mitta\OneDrive\ROOTLET PROJECT (WEBSITE)\public'

os.makedirs(dst_dir, exist_ok=True)

# 1. Pic 1 (Play Group)
pic1 = os.path.join(src_dir, 'media__1784985650091.jpg')
shutil.copy(pic1, os.path.join(dst_dir, 'playgroup.jpg'))
shutil.copy(pic1, os.path.join(dst_dir, 'child_card.jpg'))
shutil.copy(pic1, os.path.join(dst_public, 'playgroup.jpg'))

# 2. Pic 2 (After School)
pic2 = os.path.join(src_dir, 'media__1784985660953.jpg')
shutil.copy(pic2, os.path.join(dst_dir, 'afterschool.jpg'))
shutil.copy(pic2, os.path.join(dst_dir, 'studio_curiosity.jpg'))
shutil.copy(pic2, os.path.join(dst_public, 'afterschool.jpg'))

# 3. Pic 3 (UKG)
pic3 = os.path.join(src_dir, 'media__1784985702764.jpg')
shutil.copy(pic3, os.path.join(dst_dir, 'ukg.jpg'))
shutil.copy(pic3, os.path.join(dst_dir, 'studio_interactive.jpg'))
shutil.copy(pic3, os.path.join(dst_public, 'ukg.jpg'))

print("All 3 program photos copied successfully!")
