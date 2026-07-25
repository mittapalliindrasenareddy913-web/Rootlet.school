import os, glob

uploaded_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551\.user_uploaded'
files = sorted(glob.glob(os.path.join(uploaded_dir, '*.*')), key=os.path.getmtime, reverse=True)

print("Latest 5 uploaded photos for Learning Studios:")
for i, f in enumerate(files[:5]):
    # Note: reverse=True means files[0] is photo 5 (latest), files[4] is photo 1 (oldest of the 5 batch)
    print(f"Index {i}: {os.path.basename(f)} ({os.path.getsize(f)} bytes)")
