# AI Communication & Public Speaking Coach

This application is an AI-powered communication and public speaking assessment tool designed to help users refine scripts, improve vocal modulation, correct pronunciation, and enhance body language.

## User Review Required

Since you haven't specified a particular framework, I will build the frontend using **Vanilla HTML, CSS, and JavaScript** to ensure maximum flexibility, performance, and a stunning design. Let me know if you would prefer a framework like React/Vite or Next.js instead.

## Open Questions

1. **Color Palette:** Do you have a preferred color scheme for this application (e.g., professional corporate blue/gray, vibrant modern purple/dark mode, etc.)? By default, I will use a sleek dark mode with premium gradients.
2. **Mock Data:** For the frontend, I will mock the backend AI evaluations (since the backend doesn't exist yet). Is that acceptable for this step?

## Proposed Changes

### Frontend Architecture

We will build a Single Page Application (SPA) feel using Vanilla JS for navigation and state management. The UI will be broken down into functional sections matching the PRD.

#### [NEW] `index.html`
- The main structure of the application.
- Navigation bar to switch between modes (Script Analysis, Video Recording, Impromptu Mode, Analytics).
- Container for dynamically displayed views.

#### [NEW] `index.css`
- A premium, responsive design system.
- Variables for a rich dark mode color palette.
- Styling for glassmorphism effects, modern typography, and smooth micro-animations.
- Specific styles for recording interfaces, dashboards, and topic roulette.

#### [NEW] `app.js`
- Logic for switching between the different views.
- MediaRecorder API integration for capturing video and audio.
- Timers for the Impromptu mode preparation.
- Mock generation for analysis results (diffs, pronunciation flags, metrics).

## Verification Plan

### Manual Verification
- Open `index.html` in a local browser.
- Verify that camera and microphone permissions can be requested and recording starts/stops.
- Check that the 10-minute timer and topic roulette work in Impromptu Mode.
- Ensure the UI looks premium, dynamic, and responsive across different window sizes.
