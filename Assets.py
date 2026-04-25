import os
import requests

# 1. Define the folder and images
folder_name = "assets"
images = {
    "diet.jpg": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=1000&auto=format&fit=crop",
    "exercise.jpg": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?q=80&w=1000&auto=format&fit=crop",
    "monitoring.jpg": "https://images.unsplash.com/photo-1505751172876-fa1923c5c528?q=80&w=1000&auto=format&fit=crop"
}

# 2. Create the folder if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"✅ Created folder: {folder_name}")
else:
    print(f"ℹ️ Folder '{folder_name}' already exists.")

# 3. Download the images
print("📥 Downloading health assets... please wait.")

for filename, url in images.items():
    path = os.path.join(folder_name, filename)
    try:
        # Request the image with a timeout to prevent hanging
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(path, "wb") as f:
                f.write(response.content)
            print(f"✅ Successfully saved: {filename}")
        else:
            print(f"❌ Failed to download {filename}: Status {response.status_code}")
    except Exception as e:
        print(f"❌ Error downloading {filename}: {e}")

print("\n🚀 Asset setup complete! Your app is ready to show images.")