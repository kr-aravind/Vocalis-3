# Redesign based on Template Reference

The user has requested a complete redesign of the Vocalis application to match the styling and layout of `template reference.jpg`.

## User Review Required

> [!WARNING]
> This redesign will significantly alter the layout of the application. We will move from a **Left Sidebar navigation** to a **Top Pill-shaped navigation bar** to closely match the template image. Please confirm if you approve of this layout change.

## Extracted Style Guide

Based on the template image, I will implement the following design tokens:

### Color Palette
- **Main Background**: Deep Dark Slate (e.g., `#161925`)
- **Card Background**: Lighter Slate (e.g., `#242736`)
- **Accent Color**: Neon Lime Green (e.g., `#9CFF2E`)
- **Secondary Accent**: Bright White (`#FFFFFF`) for specific panels (like the bottom section in the reference) and top navigation container.
- **Text (Dark Theme)**: Pure White for headings, light gray for secondary text.
- **Text (Light Theme)**: Dark slate for text inside the white panels.

### UI Characteristics
- **Border Radius**: Extreme rounding. Cards will use ~24px-32px border radii. Buttons and navigation items will be fully pill-shaped (e.g., `border-radius: 50px`).
- **Layout**: Top navigation centered in a white pill. A dashboard-style grid with a mix of dark panels on top and a contrasting white panel on the bottom for list views or detailed actions.
- **Shadows**: Soft, diffuse drop shadows for the white sections to create depth against the dark background.

## Proposed Changes

### `index.html`
- **[MODIFY]**: Remove the `<aside class="sidebar">` and convert it into a top `<nav>` bar that sits in a white pill container at the top of the screen.
- **[MODIFY]**: Wrap the main content views to support the new styling. For instance, in the dashboard, the top metrics will be dark cards, and the chart area will be wrapped in a white contrasting container.

### `index.css`
- **[MODIFY]**: Completely overhaul the `:root` variables to use the new Neon Green / Deep Slate palette.
- **[MODIFY]**: Update `.card`, `.btn`, and layout classes to use heavy border radii and remove the previous glassmorphism/blue aesthetic.
- **[MODIFY]**: Add specific classes for the contrasting white panel sections (`.panel-light`).

### `app.js`
- **[MODIFY]**: Ensure the navigation logic correctly updates the new top-nav pill classes (e.g., moving the neon green background to the active item).

## Verification Plan
- Visually compare the running application against the `template reference.jpg`.
- Ensure all text remains accessible and readable with the new high-contrast colors.
- Verify that the layout remains responsive despite the heavy rounded corners and top navigation change.
