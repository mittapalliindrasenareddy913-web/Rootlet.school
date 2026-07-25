import os, shutil
from PIL import Image

artifacts_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551'
dst_dir = r'c:\Users\mitta\OneDrive\ROOTLET PROJECT (WEBSITE)\public\images'

os.makedirs(dst_dir, exist_ok=True)

def process_and_copy(src_name, dst_name):
    src_path = os.path.join(artifacts_dir, src_name)
    if os.path.exists(src_path):
        img = Image.open(src_path).convert('RGB')
        target_w, target_h = 600, 400
        img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
        out_path = os.path.join(dst_dir, dst_name)
        img.save(out_path, quality=98)
        print(f"Saved Studio Real-Face Card: {dst_name}")

# 1. Fine Motor Studio
process_and_copy('studio_fine_motor_real_face_1784989910535.jpg', 'studio_fine_motor.jpg')

# 2. Gross Motor Studio
process_and_copy('studio_gross_motor_real_face_1784989934452.jpg', 'studio_gross_motor.jpg')

# 3. Sensory Exploration Studio
process_and_copy('studio_sensory_real_face_1784989958391.jpg', 'studio_sensory.jpg')

# 4. Practical Life Studio
process_and_copy('afterschool_real_face_1784989738535.jpg', 'studio_practical.jpg')

# 5. Creative Expression Studio
process_and_copy('nursery_real_face_1784989671834.jpg', 'studio_creative.jpg')

# 6. Nature & Discovery Studio
process_and_copy('ukg_real_face_1784989717485.jpg', 'studio_nature.jpg')

print("All 6 Learning Studio Real-Face Cards saved successfully!")
