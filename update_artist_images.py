import os
import json
import re

def parse_filename(filename):
    """Parse artwork details from filename."""
    # Remove file extension
    name = filename.replace('.jpg', '').replace('.jpeg', '').replace('.png', '')
    
    # Extract year (4-digit number)
    year_match = re.search(r'\b(19|20)\d{2}\b', name)
    year = year_match.group(0) if year_match else "Unknown"
    
    # Common medium patterns
    mediums = [
        "Oil, Acrylic and Flower on Canvas",
        "Oil and Acrylic on Canvas",
        "Acrylic and Gold Leaf on Canvas",
        "Oil on Canvas",
        "Acrylic on Canvas",
        "Mixed Media on Canvas",
        "Watercolor and ink on silk",
        "Watercolor",
        "Sculpture",
        "Photography",
        "Installation",
        "Collage",
        "Resin，Acrylic on Wood Panel",
        "Mixed media"
    ]
    
    medium = "Mixed media"
    for med in mediums:
        if med in name:
            medium = med
            break
    
    # Extract dimensions (pattern: XX_ x YY_)
    dim_match = re.search(r'(\d+)_?\s*x\s*(\d+)_?', name)
    if dim_match:
        dimensions = f"{dim_match.group(1)} x {dim_match.group(2)} inches"
    else:
        dimensions = "Variable"
    
    # Title is everything before medium or year (whichever comes first)
    title_parts = name.split(medium)[0] if medium in name else name
    title_parts = title_parts.split(str(year))[0] if year in title_parts else title_parts
    title = title_parts.strip()
    
    return {
        "title": title,
        "year": year,
        "medium": medium,
        "dimensions": dimensions
    }

def update_artist_portfolio(artist_folder, artist_id):
    """Update an artist's portfolio in artists.json."""
    
    # Read current artists.json
    with open('data/artists.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Get list of images in artist folder
    images = sorted([f for f in os.listdir(artist_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
    
    # Find the artist in JSON
    artist_index = None
    for i, artist in enumerate(data['artists']):
        if artist['id'] == artist_id:
            artist_index = i
            break
    
    if artist_index is None:
        print(f"❌ Artist '{artist_id}' not found in artists.json")
        return
    
    artist_name = data['artists'][artist_index]['name']
    print(f"\n📸 Updating portfolio for: {artist_name}")
    print(f"📁 Folder: {artist_folder}")
    print(f"🖼️  Found {len(images)} images")
    
    # Update thumbnail (use first image)
    if images:
        data['artists'][artist_index]['thumbnailImage'] = f"{artist_folder}/{images[0]}"
        print(f"🎨 Thumbnail: {images[0]}")
    
    # Update artworks
    artworks = []
    for i, img in enumerate(images, 1):
        details = parse_filename(img)
        artworks.append({
            "title": details['title'],
            "year": details['year'],
            "medium": details['medium'],
            "dimensions": details['dimensions'],
            "image": f"{artist_folder}/{img}"
        })
        print(f"  {i}. {details['title']} ({details['year']})")
    
    data['artists'][artist_index]['artworks'] = artworks
    
    # Save updated JSON
    with open('data/artists.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Successfully updated {len(artworks)} artworks for {artist_name}")
    print(f"📝 Please review data/artists.json before committing\n")

def list_artists():
    """List all artists in the JSON file."""
    with open('data/artists.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print("\n📋 Available Artists:")
    print("-" * 50)
    for artist in data['artists']:
        print(f"  ID: {artist['id']}")
        print(f"  Name: {artist['name']}")
        print(f"  Artworks: {len(artist.get('artworks', []))}")
        print()

def list_folders():
    """List all artist folders in the project."""
    print("\n📁 Artist Folders:")
    print("-" * 50)
    folders = [f for f in os.listdir('.') if os.path.isdir(f) and not f.startswith('.') and f not in ['css', 'js', 'data', 'Images', 'Videos', 'Artists _ White Cube_files']]
    for folder in sorted(folders):
        image_count = len([f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
        print(f"  {folder} ({image_count} images)")

# Example usage
if __name__ == "__main__":
    import sys
    
    print("=" * 60)
    print("   Oro & Aquae - Artist Portfolio Update Tool")
    print("=" * 60)
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "list-artists":
            list_artists()
        elif command == "list-folders":
            list_folders()
        elif command == "update" and len(sys.argv) == 4:
            folder = sys.argv[2]
            artist_id = sys.argv[3]
            update_artist_portfolio(folder, artist_id)
        else:
            print("Invalid command!")
            print("\nUsage:")
            print("  python update_artist_images.py list-artists")
            print("  python update_artist_images.py list-folders")
            print("  python update_artist_images.py update <folder-name> <artist-id>")
            print("\nExample:")
            print("  python update_artist_images.py update 'Susan G. Scott' susan-g-scott")
    else:
        print("\n🚀 Quick Start:")
        print("-" * 60)
        print("1. List all artists:  python update_artist_images.py list-artists")
        print("2. List all folders:  python update_artist_images.py list-folders")
        print("3. Update portfolio:  python update_artist_images.py update <folder> <id>")
        print("\n💡 Example:")
        print("  python update_artist_images.py update 'Susan G. Scott' susan-g-scott")
        print()
