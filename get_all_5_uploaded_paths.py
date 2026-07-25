import os, glob

uploaded_dir = r'C:\Users\mitta\.gemini\antigravity\brain\7c851125-6658-48ad-9d73-fc4845748551\.user_uploaded'
files = sorted(glob.glob(os.path.join(uploaded_dir, '*.*')), key=os.path.getmtime, reverse=True)

print("Latest 5 uploaded files:")
for i, f in enumerate(files[:5]):
    print(f"Pic {i+1}: {os.path.basename(f)} ({os.path.getsize(f)} bytes)")
