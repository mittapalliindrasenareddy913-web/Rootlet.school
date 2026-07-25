import os
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw

src_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551\.user_uploaded'
dst_dir = r'c:\Users\mitta\OneDrive\ROOTLET PROJECT (WEBSITE)\public\images'

os.makedirs(dst_dir, exist_ok=True)

# Helper function to create active preschool composite cards
def create_preschool_card(child_file, bg_file, output_filename, crop_box=None, zoom_factor=1.0):
    child_path = os.path.join(src_dir, child_file)
    bg_path = os.path.join(dst_dir, bg_file)
    out_path = os.path.join(dst_dir, output_filename)

    # 1. Load Child Photo
    child_img = Image.open(child_path).convert('RGB')
    
    # Optional crop box
    if crop_box:
        w, h = child_img.size
        child_img = child_img.crop((
            int(w * crop_box[0]), 
            int(h * crop_box[1]), 
            int(w * crop_box[2]), 
            int(h * crop_box[3])
        ))

    # Enhance child photo clarity & contrast
    child_img = ImageEnhance.Sharpness(child_img).enhance(1.4)
    child_img = ImageEnhance.Contrast(child_img).enhance(1.1)

    # Target Card Size: 600 x 400 (3:2 Aspect Ratio)
    card_w, card_h = 600, 400

    # 2. Prepare Background (if available)
    if os.path.exists(bg_path):
        bg_img = Image.open(bg_path).convert('RGB')
        bg_img = bg_img.resize((card_w, card_h), Image.Resampling.LANCZOS)
        # Soften background slightly for depth of field
        bg_img = bg_img.filter(ImageFilter.GaussianBlur(radius=2))
    else:
        bg_img = Image.new('RGB', (card_w, card_h), (243, 235, 225))

    # 3. Composite Child into Background
    # Scale child photo
    child_aspect = child_img.width / child_img.height
    target_child_h = int(card_h * 0.95)
    target_child_w = int(target_child_h * child_aspect)

    child_resized = child_img.resize((target_child_w, target_child_h), Image.Resampling.LANCZOS)

    # Calculate position to center child in card
    pos_x = (card_w - target_child_w) // 2
    pos_y = (card_h - target_child_h) // 2

    # Paste child over background with subtle border radius
    final_card = bg_img.copy()
    final_card.paste(child_resized, (pos_x, pos_y))

    # Final Sharpen & Save
    final_card = ImageEnhance.Sharpness(final_card).enhance(1.2)
    final_card.save(out_path, quality=98)
    print(f"Created composite card: {output_filename}")

# 1. Toddler (Pic 1: media__1784987423483.jpg)
create_preschool_card(
    'media__1784987423483.jpg', 
    'studio_sensory.jpg', 
    'toddler_card.jpg', 
    crop_box=(0.0, 0.05, 1.0, 0.75)
)

# 2. Play Group (Pic 2: media__1784987772804.jpg)
create_preschool_card(
    'media__1784987772804.jpg', 
    'studio_nature.jpg', 
    'playgroup_card.jpg', 
    crop_box=(0.0, 0.1, 1.0, 0.85)
)

# 3. Nursery (Pic 3: media__1784987795387.jpg)
create_preschool_card(
    'media__1784987795387.jpg', 
    'studio_creative.jpg', 
    'nursery_card.jpg', 
    crop_box=(0.0, 0.1, 1.0, 0.85)
)

# 4. LKG (Pic 4: media__1784987807100.jpg)
create_preschool_card(
    'media__1784987807100.jpg', 
    'studio_fine_motor.jpg', 
    'lkg_card.jpg', 
    crop_box=(0.0, 0.05, 1.0, 0.85)
)

# 5. UKG (Pic 5: media__1784987832221.jpg)
create_preschool_card(
    'media__1784987832221.jpg', 
    'studio_interactive.jpg', 
    'ukg_card.jpg', 
    crop_box=(0.0, 0.05, 1.0, 0.85)
)

# 6. After School (Pic: media__1784985660953.jpg)
create_preschool_card(
    'media__1784985660953.jpg', 
    'studio_curiosity.jpg', 
    'afterschool_card.jpg', 
    crop_box=(0.0, 0.0, 1.0, 1.0)
)

print("All 6 active preschool program cards generated!")
