# Artist Portfolio Image Update Guide

## Overview
This guide explains how to update artist portfolio images in the Oro & Aquae gallery website. The process involves replacing old placeholder images with actual artwork images where the filename contains the artwork details.

## What Was Done for Sophia Gao

### 1. Folder Renaming
- Renamed `Ting Ting Gao` folder to `Sophia Gao`
- All 14 artwork images uploaded to GitHub

### 2. JSON Updates
- Updated `data/artists.json`:
  - Changed all image paths from `Ting Ting Gao/` to `Sophia Gao/`
  - Used actual filenames (which contain artwork details)
  - Updated thumbnail to "Unlimited No. 6 Oil on Canvas 30_ x 40_ 2016.jpg"
  - Extracted title, year, medium, and dimensions from filenames

### 3. Birth Year Removal
- Removed `birthYear` field from all 7 artists in `artists.json`
- Removed "Born in XXXX" references from all artist biographies

### 4. Index Page Updates
- Hero section: Changed to "Mist （氤氲） Series #5" image with caption
- Featured artist section: Changed to "Soul's Pilgrimage II" image with caption
- Added CSS styling for `.image-caption` class

### 5. Caption Styling Added
```css
.image-caption {
    font-family: var(--font-sans);
    font-size: 0.75rem;
    color: #888;
    text-align: center;
    margin-top: 0.5rem;
    letter-spacing: 0.02em;
    line-height: 1.4;
}
```

## How to Update Other Artists' Portfolios

### Option 1: Manual Update (Recommended for 1-2 artists)

1. **Rename the artist folder** (if needed):
   ```powershell
   Rename-Item -Path "Old Artist Name" -NewName "New Artist Name"
   ```

2. **Update `data/artists.json`**:
   - Find the artist's section
   - Update `thumbnailImage` path
   - For each artwork in the `artworks` array:
     - Extract title from filename (before first space or descriptor)
     - Extract year from filename (4-digit number)
     - Extract medium from filename (e.g., "Oil on Canvas")
     - Extract dimensions from filename (e.g., "24_ x 30_" = "24 x 30 inches")
     - Update the `image` path

3. **Example filename parsing**:
   ```
   Filename: "Coral Sea No.1 Oil, Acrylic and Flower on Canvas 24_ x 30_ 2017 SOLD.jpg"
   
   Extract:
   - Title: "Coral Sea No.1"
   - Year: "2017"
   - Medium: "Oil, Acrylic and Flower on Canvas"
   - Dimensions: "24 x 30 inches"
   - Image: "Artist Name/Coral Sea No.1 Oil, Acrylic and Flower on Canvas 24_ x 30_ 2017 SOLD.jpg"
   ```

4. **Commit and push**:
   ```powershell
   git add -A
   git commit -m "Update [Artist Name] portfolio images"
   git push
   ```

### Option 2: Python Script (For bulk updates)

Create a file `update_artist_images.py`:

```python
import os
import json
import re

def parse_filename(filename):
    """Parse artwork details from filename."""
    # Remove .jpg extension
    name = filename.replace('.jpg', '').replace('.jpeg', '').replace('.png', '')
    
    # Extract year (4-digit number)
    year_match = re.search(r'\b(19|20)\d{2}\b', name)
    year = year_match.group(0) if year_match else "Unknown"
    
    # Common medium patterns
    mediums = [
        "Oil on Canvas", "Acrylic on Canvas", "Mixed Media on Canvas",
        "Oil and Acrylic on Canvas", "Watercolor", "Sculpture",
        "Photography", "Installation", "Collage", "Resin"
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
    
    # Title is everything before medium or year
    title = name.split(medium)[0].strip() if medium in name else name.split(str(year))[0].strip()
    
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
    images = [f for f in os.listdir(artist_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    # Find the artist in JSON
    artist_index = None
    for i, artist in enumerate(data['artists']):
        if artist['id'] == artist_id:
            artist_index = i
            break
    
    if artist_index is None:
        print(f"Artist {artist_id} not found in artists.json")
        return
    
    # Update thumbnail (use first image)
    if images:
        data['artists'][artist_index]['thumbnailImage'] = f"{artist_folder}/{images[0]}"
    
    # Update artworks
    artworks = []
    for img in images:
        details = parse_filename(img)
        artworks.append({
            "title": details['title'],
            "year": details['year'],
            "medium": details['medium'],
            "dimensions": details['dimensions'],
            "image": f"{artist_folder}/{img}"
        })
    
    data['artists'][artist_index]['artworks'] = artworks
    
    # Save updated JSON
    with open('data/artists.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Updated {len(artworks)} artworks for {artist_folder}")

# Example usage:
if __name__ == "__main__":
    # Update a specific artist
    # update_artist_portfolio("Susan G. Scott", "susan-g-scott")
    
    print("Artist portfolio update script ready.")
    print("Uncomment and modify the line above to update an artist.")
```

### Running the Script

```powershell
# Navigate to project directory
cd C:\Users\Mario\OneDrive\Desktop\OroAquae

# Run the script
python update_artist_images.py

# Review changes
git diff data/artists.json

# Commit if satisfied
git add -A
git commit -m "Update artist portfolio images"
git push
```

## Important Notes

1. **Image Sizes**: Keep original sizes - they will be automatically resized by CSS
2. **Filenames**: The more descriptive the filename, the better the parsed data
3. **Special Characters**: Be careful with special characters in filenames (use URL encoding if needed)
4. **Testing**: Always test on localhost before pushing:
   ```powershell
   python -m http.server 8000
   ```
   Then visit: http://localhost:8000

## File Structure

```
Artist Name/
├── Artwork 1 Medium Dimensions Year.jpg
├── Artwork 2 Medium Dimensions Year.jpg
└── ...
```

## Caption Support

Image captions are automatically shown for:
- Hero section images (index.html)
- Featured artist section images (index.html)
- Can be added to any image by adding: `<p class="image-caption">Caption text</p>`

## GitHub URL Format

When referencing images in HTML/JSON, use:
```
https://raw.githubusercontent.com/StoryBeeBooks/oroaquae/main/Artist%20Name/filename.jpg
```

Note: Spaces become `%20` in URLs.

## Summary of Changes Made

### Files Modified:
- `data/artists.json` - Updated Sophia Gao artworks, removed all birth years
- `index.html` - Updated hero and featured artist images with captions
- `css/styles.css` - Added `.image-caption` styling
- `README.md` - Updated artist name reference

### Files Added/Renamed:
- Renamed folder: `Ting Ting Gao` → `Sophia Gao`
- Added 14 new artwork images to `Sophia Gao/` folder
- Created this documentation file

### Git Commits:
1. "Change artist name from Ting Ting Gao to Sophia Gao across all pages"
2. "Update Sophia Gao portfolio: rename folder, update all images with real artwork, remove birth years from all artists, add image captions"
