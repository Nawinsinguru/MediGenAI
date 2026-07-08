# Design System - MediGenAI Frontend

## Design Philosophy

The MediGenAI frontend is inspired by modern health and wellness applications, featuring:

- Clean, minimalist interface
- Soft, welcoming color palette
- Smooth animations and transitions
- Glass morphism effects
- Excellent accessibility

## Color Palette

### Primary Colors (Medical/Professional)

- Primary Purple: `#9b7fee` - Trust, professionalism
- Primary Gradient: `from-primary-500 to-primary-600`
- Light Accent: `#ede9ff` - Subtle highlights

### Secondary Colors (Warm & Welcoming)

- Cream/Warm: `#ffb896` - Friendly, approachable
- Cream Light: `#fff5eb` - Soft backgrounds
- Cream Gradient: Warm accent colors

### Neutral Colors

- Text: `#1f2937` (Gray-900)
- Secondary Text: `#4b5563` (Gray-600)
- Borders: `#e5e7eb` (Gray-200)
- Backgrounds: `#f9fafb` (Gray-50)

## Typography

- **Font Family**: System fonts (San Francisco, Segoe UI, Roboto)
- **Headings**: Bold weights (700-900)
- **Body**: Regular (400) to Medium (500)
- **Code**: Monospace (when applicable)

## Components

### Buttons

- **Primary**: Gradient purple background, white text
- **Secondary**: Gray background, gray text
- **States**: Hover shadow, disabled opacity

### Cards

- White background with subtle shadow
- Rounded corners (2xl = 16px)
- Hover elevation effect
- Glass morphism option for overlays

### Input Fields

- Soft gray borders
- Purple focus state with ring
- Rounded corners (lg = 8px)
- Padding: py-3 px-4

### Navigation

- Glass morphism header
- Sticky positioning
- Smooth transitions

## Spacing Scale

- xs: 4px
- sm: 8px
- md: 16px
- lg: 24px
- xl: 32px
- 2xl: 48px

## Border Radius

- Default: 8px (lg)
- Cards: 16px (2xl)
- Avatars/Icons: 12px (xl) or 50% (full)

## Animations

- **Fade In**: 300ms ease-in
- **Slide Up**: 300ms ease-out
- **Hover Transitions**: 200ms smooth

## Responsive Design

### Breakpoints

- Mobile: < 640px (sm)
- Tablet: 640px - 1024px (md/lg)
- Desktop: > 1024px (xl)

### Layout

- Mobile: Single column, full width
- Tablet: 2 columns for cards
- Desktop: 3+ columns for grids

## Dark Mode (Future)

The design supports future dark mode implementation:

- Invert color values
- Maintain contrast ratios
- Preserve glass morphism effects

## Accessibility Features

- Semantic HTML structure
- ARIA labels where needed
- Keyboard navigation support
- Focus indicators
- Color contrast compliance (WCAG AA)
- Responsive touch targets (44px minimum)

## Usage Examples

### Glass Morphism Container

```html
<div class="glass-effect">
  <!-- Content -->
</div>
```

### Primary Button

```html
<button class="btn-primary">Action</button>
```

### Card Layout

```html
<div class="card">
  <!-- Content -->
</div>
```

### Input Field

```html
<input type="text" class="input-field" />
```

## Animation Classes

### Fade In

```html
<div class="animate-fade-in">Content appears gradually</div>
```

### Slide Up

```html
<div class="animate-slide-up">Content slides up</div>
```

## Hover Effects

- Cards: Subtle shadow increase
- Buttons: Background color shift
- Links: Underline or color change
- Icons: Scale/rotate transformation

## Loading States

- Disabled button opacity
- Animated dots for loading
- Progress bars for uploads
- Skeleton screens (future)

## States

### Idle

- Standard styling
- Full opacity

### Hover

- Elevated shadow
- Color shift
- Cursor change

### Active/Focus

- Ring highlight
- Color emphasis
- Outlined state

### Disabled

- Reduced opacity (50%)
- No hover effects
- Cursor not-allowed

### Error

- Red border: `#ef4444`
- Red background: `#fee2e2`
- Icon indicator

### Success

- Green border: `#10b981`
- Green background: `#ecfdf5`
- Icon indicator

## Icons

- Source: Heroicons (stroke style)
- Size: Scaled with w-4 to w-8
- Color: Inherits from parent

## Responsive Image Handling

- Lazy loading for performance
- Aspect ratio preservation
- Mobile optimization
- SVG icons for scalability

## CSS Architecture

- **Tailwind CSS**: Utility-first framework
- **Custom Classes**: Global CSS classes for repeated patterns
- **CSS Variables**: Theme colors (future enhancement)
- **PostCSS**: For processing

## Performance Considerations

- Minimal animations on mobile
- CSS-based animations instead of JS
- Optimized SVG icons
- Lazy loading components
- Image optimization

## Future Enhancements

- Dark mode support
- High contrast mode
- Reduced motion preferences
- Custom theming
- Internationalization (i18n) support
