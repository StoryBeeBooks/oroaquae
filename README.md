# Oro & Aquae Art Gallery Website

A contemporary art gallery website showcasing artists and their works with elegant typography inspired by Hermès and White Cube.

## Typography System

### Font Families

**Primary Fonts:**
- **Serif:** `Crimson Text` - Used for display headings, large titles, and artistic content
- **Sans-serif:** `Inter` - Used for body text, navigation, labels, and UI elements

**Font Stack:**
```css
--font-serif: 'Crimson Text', 'Garamond', Georgia, 'Times New Roman', serif;
--font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif;
```

### Typography Hierarchy

#### Headings
- **H1 (Hero):** Crimson Text, 4.5rem (72px), weight 400, letter-spacing 0.02em
- **H2 (Sections):** Crimson Text, 3rem (48px), weight 400, letter-spacing 0.01em, line-height 1.2
- **H3 (Cards):** Inter, 1.25rem (20px), weight 400, letter-spacing 0.02em
- **H4 (Subsections):** Inter, 1rem (16px), weight 500, letter-spacing 0.02em

#### Body Text
- **Body:** Inter, 1rem (16px), weight 400, line-height 1.7, letter-spacing 0.01em
- **Small Text:** Inter, 0.875rem (14px), weight 400, letter-spacing 0.01em
- **Captions:** Inter, 0.75rem (12px), weight 400, letter-spacing 0.02em

#### Labels & Metadata
- **Uppercase Labels:** Inter, 0.75-0.875rem, weight 500, letter-spacing 0.15-0.2em, uppercase
- **Artist Names:** Inter, 1rem (16px), weight 400, letter-spacing 0.02em
- **Dates/Details:** Inter, 0.95rem (15px), weight 400, letter-spacing 0.05em

#### Navigation
- **Logo:** Inter, 0.875rem (14px), weight 500, letter-spacing 0.2em, uppercase
- **Nav Links:** Inter, 0.95rem (15px), weight 400, letter-spacing 0.08em

### Font Weights
- **Light:** 300 (used sparingly for italicized subtitles)
- **Regular:** 400 (primary weight for body and headings)
- **Medium:** 500 (navigation, labels, UI elements)
- **Semibold:** 600 (emphasis, CTAs)

### Letter Spacing
- **Tight:** 0.01em (large headings, body text)
- **Normal:** 0.02-0.05em (subheadings, artist names)
- **Loose:** 0.08-0.15em (labels, metadata)
- **Extra Loose:** 0.2em (logo, uppercase elements)

### Line Height
- **Headings:** 1.1-1.2 (tight for impact)
- **Body:** 1.7 (comfortable reading)
- **UI Elements:** 1.5 (compact but legible)

### Design Principles

1. **Hierarchy:** Clear visual distinction between content levels using size and font family
2. **Elegance:** Serif for artistic/emotional content, sans-serif for functional content
3. **Readability:** Generous line-height (1.7) and letter-spacing for body text
4. **Consistency:** All uppercase elements use Inter with increased letter-spacing
5. **Refinement:** Subtle letter-spacing adjustments enhance sophistication
6. **Balance:** Mix of serif (30%) and sans-serif (70%) creates visual interest

### Usage Guidelines

**Use Crimson Text (Serif) for:**
- Hero titles and main page headings
- Artist names in hero sections
- Exhibition titles
- Large, impactful typography
- Artistic or emotional content

**Use Inter (Sans-serif) for:**
- Body copy and paragraphs
- Navigation and menus
- Form labels and inputs
- Buttons and CTAs
- Metadata (dates, dimensions, locations)
- Card titles and descriptions
- Search and filter interfaces

### Color & Typography Pairing
- **Black text (#000000)** on white background for maximum contrast
- **Medium grey (#666666)** for secondary information and metadata
- **White text** on dark backgrounds with text-shadow for readability

## Project Structure

```
OroAquae/
├── index.html              # Homepage
├── artists.html            # Artist index page with search
├── artist.html             # Artist template page (dynamic)
├── contact.html            # Contact page
├── faq.html               # Frequently Asked Questions
├── web-accessibility.html  # Web Accessibility Statement
├── privacy-policy.html     # Privacy Policy
├── terms-of-use.html      # Terms of Use
├── cookie-policy.html     # Cookie Policy
├── css/
│   └── styles.css         # Main stylesheet
├── data/
│   └── artists.json       # Artist data (JSON format)
├── Ting Ting Gao/         # Artist artwork folder
│   ├── tingtinggao1.jpg
│   ├── tingtinggao2.jpg
│   └── ... (7 images total)
└── [Other artist folders]
```

## Features

### 1. Homepage (`index.html`)
- Hero section with featured artwork
- Current exhibitions grid
- Artist preview section
- Responsive navigation
- Footer with links to all pages

### 2. Artist Index (`artists.html`)
- Dynamic artist grid loaded from JSON
- Search functionality (filters by artist name)
- Alpine.js powered interactivity
- Responsive grid layout

### 3. Artist Page (`artist.html`)
- Template-based design using JSON data
- Dynamic content loading via URL parameter (?id=artist-id)
- Three main sections:
  - Artist hero with image and name
  - Biography section
  - Artworks grid
- Related artists section
- Scalable for 100+ artists

### 4. Footer Utility Pages
- **Web Accessibility:** WCAG compliance information
- **Privacy Policy:** Data collection and usage
- **Terms of Use:** Website usage terms
- **Cookie Policy:** Cookie usage information
- **Contact Us:** Contact form and gallery information
- **FAQ:** Common questions with accordion interface

## Technical Details

### Technologies Used
- **HTML5:** Semantic markup
- **CSS3:** Modern styling with CSS Grid and Flexbox
- **Alpine.js:** Lightweight JavaScript framework for interactivity
- **JSON:** Data storage for scalability

### Artist Data Structure (artists.json)

```json
{
  "artists": [
    {
      "id": "artist-slug",
      "name": "Artist Name",
      "birthYear": "1990",
      "biography": "<p>HTML formatted biography</p>",
      "artworks": [
        {
          "title": "Artwork Title",
          "year": "2024",
          "medium": "Medium description",
          "dimensions": "Dimensions",
          "image": "folder/image.jpg"
        }
      ]
    }
  ]
}
```

### Current Artists
1. Ting Ting Gao (with 7 artworks)
2. Susan G. Scott
3. Shelley Adler
4. Christine Reimer
5. Leonel Jules
6. Andy Dixon
7. Ben Walmsley

## Adding New Artists

### Step 1: Create Artist Folder
Create a new folder with the artist's name and add artwork images.

### Step 2: Update artists.json
Add a new artist entry to `data/artists.json`:

```json
{
  "id": "artist-name-slug",
  "name": "Artist Name",
  "birthYear": "1985",
  "biography": "<p>Artist biography in HTML</p>",
  "artworks": [
    {
      "title": "Artwork Title",
      "year": "2024",
      "medium": "Oil on canvas",
      "dimensions": "48 x 60 inches",
      "image": "Artist Name/artwork1.jpg"
    }
  ]
}
```

### Step 3: Test
- Artist will automatically appear on the artist index page
- Artist page will be accessible via `artist.html?id=artist-name-slug`

## Responsive Design

The website is fully responsive with breakpoints at:
- Mobile: < 768px
- Tablet: 768px - 1023px
- Desktop: ≥ 1024px

## Accessibility Features

- Semantic HTML5 structure
- Skip to content link
- ARIA labels and landmarks
- Keyboard navigation support
- Sufficient color contrast
- Alt text for images
- Focus indicators

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Setup and Deployment

### Local Development
1. Clone the repository
2. Open `index.html` in a web browser
3. For JSON loading, use a local server (e.g., Live Server in VS Code)

### Deployment
- Upload all files to web hosting
- Ensure proper MIME types for JSON files
- Configure HTTPS for security

## Future Enhancements

- [ ] Add exhibition pages
- [ ] Implement newsletter signup
- [ ] Add image lightbox/gallery viewer
- [ ] Create admin panel for managing artists
- [ ] Add multilingual support
- [ ] Implement e-commerce for artwork sales
- [ ] Add social media integration
- [ ] Create artist application form

## Contact

For questions or support:
- Email: info@oroaquae.com
- Phone: +1 (234) 567-890

## License

© 2024 Oro & Aquae. All rights reserved.
