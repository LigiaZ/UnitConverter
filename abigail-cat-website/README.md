# Abigail's Cat Website 🐱

A beautiful, interactive website dedicated to Abigail, the most adorable cat! This Next.js application showcases Abigail's photos with a charming pink-themed design and smooth animations.

## Features

- **Interactive Photo Gallery**: Drag and drop photos of Abigail directly into the browser
- **Beautiful Animations**: Smooth entrance animations powered by Framer Motion
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Custom Styling**: Pink gradient background with elegant typography using Dancing Script font
- **Modern Tech Stack**: Built with Next.js 16, TypeScript, and Tailwind CSS

## Technologies Used

- **Framework**: [Next.js 16](https://nextjs.org) with App Router
- **Language**: TypeScript
- **Styling**: [Tailwind CSS](https://tailwindcss.com) with custom CSS variables
- **Animations**: [Framer Motion](https://www.framer-motion.com) for smooth transitions
- **File Upload**: [React Dropzone](https://react-dropzone.js.org) for drag-and-drop functionality
- **Fonts**: [Dancing Script](https://fonts.google.com/specimen/Dancing+Script) for elegant headings

## Getting Started

First, install the dependencies:

```bash
npm install
```

Then, run the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see Abigail's website.

## Project Structure

```
abigail-cat-website/
├── app/
│   ├── layout.tsx          # Root layout with fonts and metadata
│   ├── page.tsx           # Main page (currently default Next.js)
│   └── globals.css        # Global styles with pink theme
├── components/
│   ├── Header.tsx         # Animated header with Abigail's name
│   └── PhotoSection.tsx   # Drag-and-drop photo upload component
└── public/                # Static assets
```

## Key Components

### Header Component
- Displays "Abigail - The Most Adorable Cat" with elegant typography
- Animated entrance with Framer Motion

### Photo Section Component
- Drag and drop area for uploading cat photos
- Supports multiple image formats (JPEG, PNG, GIF)
- Grid layout for displaying uploaded photos
- Hover effects and smooth animations

## Customization

The website uses CSS custom properties for easy theming:
- `--background`: Pink gradient background
- `--foreground`: Text color
- `--accent`: Accent color for interactive elements

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
