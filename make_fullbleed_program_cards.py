import os
from PIL import Image, ImageEnhance

src_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551\.user_uploaded'
dst_dir = r'c:\Users\mitta\OneDrive\ROOTLET PROJECT (WEBSITE)\public\images'

def create_fullbleed_card(input_path, output_filename, crop_box=(0.0, 0.0, 1.0, 1.0), focal_point='center'):
    img = Image.open(input_path).convert('RGB')
    w, h = img.size

    # Apply crop box
    crop_left = int(w * crop_box[0])
    crop_top = int(h * crop_box[1])
    crop_right = int(w * crop_box[2])
    crop_bottom = int(h * crop_box[3])
    img = img.crop((crop_left, crop_top, crop_right, crop_bottom))

    # Target ratio 3:2 (600x400)
    target_w, target_h = 600, 400
    target_ratio = target_w / target_h
    cur_w, cur_h = img.size
    cur_ratio = cur_w / cur_h

    if cur_ratio > target_ratio:
        # Image is wider -> crop sides
        new_w = int(cur_h * target_ratio)
        left = (cur_w - new_w) // 2
        img = img.crop((left, 0, left + new_w, cur_h))
    else:
        # Image is taller -> crop top/bottom based on focal point
        new_h = int(cur_w / target_ratio)
        if focal_point == 'top':
            top = 0
        elif focal_point == 'top_third':
            top = int((cur_h - new_h) * 0.25)
        else:
            top = (cur_h - new_h) // 2
        img = img.crop((0, top, cur_w, top + new_h))

    # Resize to exact 600x400
    img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    img = ImageEnhance.Sharpness(img).enhance(1.3)
    img = ImageEnhance.Contrast(img).enhance(1.05)

    out_path = os.path.join(dst_dir, output_filename)
    img.save(out_path, quality=98)
    print(f"Saved fullbleed card: {output_filename}")

# 1. Toddler (Screenshot 2: media__1784988297535.jpg)
toddler_ai_path = os.path.join(src_dir, 'media__1784988297535.jpg')
create_fullbleed_card(toddler_ai_path, 'toddler_card.jpg', crop_box=(0.0, 0.05, 1.0, 0.95), focal_point='top_third')

# 2. Play Group (Boy in park with toy tractor: media__1784987772804.jpg)
playgroup_path = os.path.join(src_dir, 'media__1784987772804.jpg')
create_fullbleed_card(playgroup_path, 'playgroup_card.jpg', crop_box=(0.0, 0.1, 1.0, 0.85), focal_point='top_third')

# 3. Nursery (Boy in blue velvet suit: media__1784987795387.jpg)
nursery_path = os.path.join(src_dir, 'media__1784987795387.jpg')
create_fullbleed_card(nursery_path, 'nursery_card.jpg', crop_box=(0.0, 0.1, 1.0, 0.85), focal_point='top_third')

# 4. LKG (Boy in suspenders: media__1784987807100.jpg)
lkg_path = os.path.join(src_dir, 'media__1784987807100.jpg')
create_fullbleed_card(lkg_path, 'lkg_card.jpg', crop_box=(0.0, 0.0, 1.0, 0.85), focal_point='top_third')

# 5. UKG (Girl in yellow shirt: media__1784987832221.jpg)
ukg_path = os.path.join(src_dir, 'media__1784987832221.jpg')
create_fullbleed_card(ukg_path, 'ukg_card.jpg', crop_box=(0.0, 0.05, 1.0, 0.85), focal_point='top_third')

# 6. After School (Two kids sitting together: media__1784985660953.jpg)
afterschool_path = os.path.join(src_dir, 'media__1784985660953.jpg')
create_fullbleed_card(afterschool_path, 'afterschool_card.jpg', crop_box=(0.0, 0.0, 1.0, 1.0), focal_point='center')

print("All 6 full-bleed edge-to-edge cards created successfully!")
