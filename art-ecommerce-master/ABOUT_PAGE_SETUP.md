# About Page Setup Guide

## Overview
A professional "About Sreelekha Jayaram" page has been created with a beautiful, modern design showcasing all achievements, skills, and artwork.

## Features

### 1. **Hero Section**
- Eye-catching gradient background
- Artist name and tagline with animations
- Professional presentation

### 2. **Artist Profile Section**
- Image placeholder for artist photo
- Detailed biography
- Highlighted specializations box
- Responsive layout

### 3. **Statistics Section**
- Display of key achievements:
  - Years of artistic excellence
  - Total awards & recognitions
  - Artworks created
  - Expert art forms

### 4. **Major Achievements Cards**
Four beautifully designed cards showcasing:
- **A Grade - Kalolsavam** (2023-2024 & 2024-2025)
  - Recognition from Mahatma Gandhi University, Kottayam, Kerala
  
- **Overall Off-Stage Winner** (2022-2023 & 2023-2024)
  - Two consecutive years of excellence
  
- **Thekkady Wildlife Week Winner** (2024)
  - Environmental art competition winner
  
- **Multiple Prize Holder** (Childhood onwards)
  - School, university, and competition awards

### 5. **Skills & Expertise Section**
Four skill cards highlighting:
- **Acrylic Painting** - Vibrant color work and contemporary styles
- **Stencil Creation** - Intricate precision stencil artworks
- **Pencil Sketching** - Detailed shading and fine line work
- **Creative Design** - Innovative visual composition

### 6. **Timeline Section**
Journey progression:
- **Childhood** - Foundation years
- **School Level** - Building skills
- **University Level** - Peak recognition
- **2022-2025** - Current excellence

### 7. **Artwork Gallery**
- 6-item grid gallery with hover effects
- Image placeholders ready for artwork photos
- Responsive design

### 8. **Call-to-Action Section**
- Links to shop collection
- Portrait session booking button

## Setting Up Images

### Image Locations
All images should be placed in: `static/img/`

### Required Images

1. **Artist Profile Photo**
   - Path: `static/img/placeholder-artist.jpg`
   - Size: 400x500px (recommended)
   - Format: JPG or PNG
   - Purpose: Main artist portrait

2. **Gallery Images** (6 images)
   - Path: `static/img/gallery-1.jpg` through `gallery-6.jpg`
   - Size: 300x400px each (recommended)
   - Format: JPG or PNG
   - Suggested content:
     - gallery-1: Acrylic painting
     - gallery-2: Stencil artwork
     - gallery-3: Pencil sketch
     - gallery-4: Wildlife artwork
     - gallery-5: Contemporary piece
     - gallery-6: Creative design

### How to Add Images

1. **Prepare your images**
   - Optimize images for web (compress to reduce file size)
   - Use consistent dimensions within each category
   - Ensure high quality (min 300x300px)

2. **Upload to static folder**
   ```
   art-ecommerce-master/
   └── static/
       └── img/
           ├── placeholder-artist.jpg
           ├── gallery-1.jpg
           ├── gallery-2.jpg
           ├── gallery-3.jpg
           ├── gallery-4.jpg
           ├── gallery-5.jpg
           └── gallery-6.jpg
   ```

3. **Update file paths (if different)**
   - Edit `templates/about.html`
   - Find the image src tags
   - Replace with your actual image paths

## Accessing the About Page

- **URL**: `http://localhost:8000/about/`
- **Navigation**: Click "About" in the main navigation bar
- **Direct links**: 
  - Shop Collection button
  - Book Portrait Session button

## CSS Features

### Animations
- Slide-in animations on hero section
- Hover effects on cards and images
- Smooth transitions throughout
- Shimmer effect on award cards

### Responsive Design
- Mobile-friendly layout
- Tablet optimization
- Desktop full-width support
- Flexible grid system

### Color Scheme
- Primary gradient: Purple (#667eea) to Pink (#764ba2)
- Secondary gradient: Pink (#f093fb) to Red (#f5576c)
- Neutral: White, light gray, dark gray

### Typography
- **Playfair Display** - Headings (serif)
- **Great Vibes** - Tagline (cursive)
- **System fonts** - Body text

## Customization Options

### Change Colors
Edit the gradient colors in `about.html` `<style>` section:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Modify Awards/Skills
Edit the card sections in the HTML to add/remove achievements

### Adjust Layout
Modify grid columns:
```css
grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
```

### Update Statistics
Modify the stats-grid section with your actual numbers

## Browser Compatibility
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## Performance Tips
1. Optimize images before uploading (use tools like TinyPNG)
2. Use WebP format for smaller file sizes
3. Lazy load images for faster page load
4. Consider CDN for image delivery

## Next Steps
1. Gather high-quality images of artworks and achievements
2. Place images in `static/img/` folder
3. Test the page at `http://localhost:8000/about/`
4. Make any customizations as needed

## Technical Details

### URL Configuration
- Added route: `/about/` in `shop/urls.py`
- View: `about()` in `home/views.py`
- Template: `templates/about.html`

### Navigation Integration
- Updated `base.html` navbar to include About link
- Changed from anchor link to dedicated page

### SEO
- Semantic HTML structure
- Descriptive content
- Image alt text included
- Proper heading hierarchy

---

**Ready to showcase Sreelekha Jayaram's artistic excellence!** 🎨✨
