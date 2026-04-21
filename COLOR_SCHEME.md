# Color Scheme & Design Reference

## Application Color Palette

### Primary Colors
```
Blue:       #2196F3 (Information, Primary Action)
Green:      #4CAF50 (Success, Start/Play)
Orange:     #FF9800 (Warning, Pause)
Red:        #f44336 (Danger, Stop)
Purple:     #9C27B0 (Special, Schedule/Exit)
Cyan:       #00BCD4 (Refresh, Secondary Action)
Orange-Red: #FF5722 (Browse, File Selection)
```

### Neutral Colors
```
Light Gray:  #f0f0f0 (Main Background)
White:       #ffffff (Card/Input Background)
Dark Gray:   #cccccc (Borders)
Text:        #333333 (Primary Text)
Muted:       #666666 (Disabled Text)
```

## UI Element Styling

### Buttons

#### Start Button
- **Color**: Green (#4CAF50)
- **Hover**: Darker Green (#45a049)
- **Pressed**: Dark Green (#084298)
- **Disabled**: Gray (#cccccc)
- **Usage**: Begin recording or video playback

#### Play Button
- **Color**: Green (#4CAF50)
- **Hover**: Darker Green (#45a049)
- **Usage**: Start video playback

#### Pause Button
- **Color**: Orange (#FF9800)
- **Hover**: Darker Orange (#fb8500)
- **Usage**: Pause recording/playback

#### Stop Button
- **Color**: Red (#f44336)
- **Hover**: Darker Red (#da190b)
- **Usage**: Stop recording/playback

#### Fresh Button (Refresh Start Time)
- **Color**: Cyan (#00BCD4)
- **Hover**: Darker Cyan (#0097a7)
- **Usage**: Update current timestamp

#### Browse Button
- **Color**: Orange-Red (#FF5722)
- **Hover**: Darker Orange-Red (#e64a19)
- **Usage**: Select files

#### Schedule Button
- **Color**: Purple (#9C27B0)
- **Hover**: Darker Purple (#7b1fa2)
- **Usage**: Schedule future recording

#### Exit Button
- **Color**: Purple (#9C27B0)
- **Hover**: Darker Purple (#7b1fa2)
- **Usage**: Close application

### Tabs

#### Tab Bar (Inactive)
- **Background**: Light Gray (#e0e0e0)
- **Text**: Dark Gray (#333333)
- **Border**: Gray (#cccccc)
- **Style**: Rounded top corners

#### Tab Bar (Active)
- **Background**: Green (#4CAF50)
- **Text**: White
- **Border**: Dark Green (#45a049)
- **Font**: Bold

#### Tab Hover State
- **Background**: Green (#45a049)
- **Text**: White
- **Animation**: Smooth transition

### Input Fields

#### Text Input (QLineEdit)
- **Background**: White (#ffffff)
- **Border**: Gray (#cccccc)
- **Focus Border**: Blue (#2196F3)
- **Text Color**: Dark (#333333)
- **Padding**: 5px

#### Combo Box (QComboBox)
- **Background**: White (#ffffff)
- **Border**: Gray (#cccccc)
- **Focus Border**: Blue (#2196F3)
- **Dropdown Button**: Blue (#2196F3)
- **Hover**: Lighter effect

#### Date/Time Edit (QDateTimeEdit)
- **Background**: White (#ffffff)
- **Border**: Gray (#cccccc)
- **Focus Border**: Blue (#2196F3)
- **Text Color**: Dark (#333333)

### Sliders

#### Groove (Track)
- **Background**: Light Gray (#e0e0e0)
- **Border**: Gray (#cccccc)
- **Height**: 8px
- **Radius**: 4px

#### Handle (Thumb)
- **Color**: Blue (#2196F3)
- **Border**: Darker Blue (#1976d2)
- **Size**: 18px
- **Hover**: Darker Blue (#1976d2)
- **Shape**: Rounded (9px radius)

### Text Areas

#### Status Text (QTextEdit)
- **Background**: Off-White (#fafafa)
- **Border**: Gray (#cccccc)
- **Text Color**: Dark (#333333)
- **Read-Only**: True

### Labels

#### Regular Label
- **Color**: Dark Gray (#333333)
- **Font Size**: 10pt

#### Status Label (Recording)
- **Ready**: Blue (#2196F3)
- **Recording**: Red (red)
- **Paused**: Orange (orange)
- **Stopped**: Green (green)

#### Status Label (Playback)
- **Ready**: Blue (#2196F3)
- **Loading**: Orange (#FF9800)
- **Playing**: Green (#4CAF50)
- **Paused**: Orange (#FF9800)
- **Stopped**: Red (#f44336)
- **Error**: Red (#f44336)

### Video Widget
- **Background**: Black (#000000)
- **Minimum Height**: 300px
- **Stretch Factor**: 1 (takes available space)

## Color Psychology

### Green (#4CAF50)
- **Meaning**: Go, Success, Play
- **Buttons**: Start, Play
- **Status**: Recording active, Playing
- **Psychology**: Action, confidence

### Orange (#FF9800)
- **Meaning**: Caution, Pause, Loading
- **Buttons**: Pause, Fresh
- **Status**: Paused, Loading
- **Psychology**: Attention needed

### Red (#f44336)
- **Meaning**: Stop, Danger, Error
- **Buttons**: Stop
- **Status**: Stopped, Error
- **Psychology**: Stop, important

### Blue (#2196F3)
- **Meaning**: Information, Primary action
- **Buttons**: General buttons
- **Status**: Ready, Loading
- **Psychology**: Trust, stability

### Purple (#9C27B0)
- **Meaning**: Special, Future, Control
- **Buttons**: Schedule, Exit
- **Psychology**: Unique, control

### Cyan (#00BCD4)
- **Meaning**: Refresh, Update
- **Buttons**: Fresh (refresh time)
- **Psychology**: Reset, refresh

## Accessibility

### Contrast Ratios
- All text on buttons: WCAG AA compliant (4.5:1 minimum)
- Blue text on light background: High contrast
- Black video background: Reduces eye strain
- Light gray background: Comfortable for extended use

### Color Blindness Support
- Buttons use multiple cues (color + text + position)
- Status shown with both color and emoji/text
- High contrast maintained throughout

## Responsive Design

### Window Sizing
- **Default Size**: 700x800 pixels
- **Minimum Width**: 700px (accommodates all content)
- **Tab Widget**: Full width and height
- **Video Widget**: Grows with window size

### Layout Adjustments
- Horizontal layouts: Items resize proportionally
- Vertical layouts: Status area grows/shrinks as needed
- Sliders: Full width of container
- Video: Takes available space in tab

## Font Specifications

### Font Family
- Default: System font (Arial or equivalent)
- Monospace: Used where appropriate

### Font Sizes
- Labels: 10pt
- LED Indicator: 20pt Bold
- Buttons: 11pt Bold
- Tab Headers: Default system size, Bold when active

### Font Weights
- Bold: Buttons, tab headers, status indicators
- Normal: Labels, input fields

## Animation & Transitions

### Button Hover Effects
- Smooth color transition (no delay)
- Brightness adjustment on hover
- Darker on press/active state

### Tab Transitions
- Active tab: Green background with white text
- Inactive: Gray background
- Smooth visual feedback

### Slider Interaction
- Handle changes color on hover
- Smooth position updates during dragging
- Real-time feedback

## Dark Mode Considerations (Future)

If dark mode is implemented:
- Invert background colors
- Adjust text colors for contrast
- Modify button colors for visibility
- Keep status colors consistent

---

**Design Version**: 1.0
**Framework**: PySide6
**Last Updated**: April 21, 2026

