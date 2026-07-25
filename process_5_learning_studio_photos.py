import os
from PIL import Image

user_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551\.user_uploaded'
dst_dir = r'c:\Users\mitta\OneDrive\ROOTLET PROJECT (WEBSITE)\public\images'

os.makedirs(dst_dir, exist_ok=True)

mappings = [
    ('media__1784993351073.jpg', 'studio_fine_motor.jpg', 'Fine Motor Studio (Photo 1)'),
    ('media__1784993358957.jpg', 'studio_gross_motor.jpg', 'Gross Motor Studio (Photo 2)'),
    ('media__1784993367958.jpg', 'studio_sensory.jpg', 'Sensory Exploration Studio (Photo 3)'),
    ('media__1784993375448.jpg', 'studio_practical.jpg', 'Practical Life Studio (Photo 4)'),
    ('media__1784993382722.png', 'studio_creative.jpg', 'Creative Expression Studio (Photo 5)')
]

for src_file, dst_file, label in mappings:
    src_path = os.path.join(user_dir, src_file)
    img = Image.open(src_path).convert('RGB')
    
    # Save high quality JPEG to public/images/
    dst_path = os.path.join(dst_dir, dst_file)
    img.save(dst_path, quality=95)
    print(f"Updated {label}: {dst_file}")

print("All 5 Learning Studio photos processed successfully!")
