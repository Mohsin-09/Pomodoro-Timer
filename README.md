# 🍅 Pomodoro Timer

A beautiful, modern Pomodoro Timer application built with Python and Tkinter. This application helps you implement the Pomodoro Technique for improved productivity and focus.

## ✨ Features

### 🎨 **Modern UI Design**
- **Sidebar Layout**: Clean sidebar with vertical control buttons
- **Beautiful Typography**: Segoe UI and Consolas fonts for modern appearance
- **Dark Theme**: Professional dark color scheme (#2C3E50, #34495E)
- **Custom Vertical Buttons**: Unique vertical text buttons with 0.1px line spacing
- **Animated Progress Bar**: Rounded progress bar with pulse animation

### ⏱️ **Timer Functionality**
- **Work Sessions**: Customizable work time (default: 25 minutes)
- **Short Breaks**: Quick breaks between work sessions (default: 5 minutes)
- **Long Breaks**: Extended breaks after completing cycles (default: 15 minutes)
- **Multiple Cycles**: Complete Pomodoro cycles (default: 4 cycles)
- **Pause/Resume**: Toggle timer without losing progress
- **Reset**: Reset timer to initial state

### 🚀 **Quick Start Options**
- **25min Work**: Quick start for standard work session
- **5min Break**: Quick start for short break
- **15min Break**: Quick start for long break

### 🎯 **Visual Feedback**
- **Status Messages**: Dynamic status updates with emojis
- **Cycle Counter**: Shows current cycle progress (e.g., "Cycle: 2/4")
- **Progress Bar**: Visual progress indicator with color coding
- **Hover Effects**: Interactive button hover states

## 🛠️ **Technical Details**

### **Dependencies**
- `tkinter` - GUI framework (built-in with Python)
- `time` - Timer functionality
- `math` - Mathematical calculations for animations

### **Architecture**
- **Object-Oriented Design**: Clean class-based structure
- **Custom Button System**: Canvas-based vertical buttons with precise control
- **Event-Driven**: Responsive UI with proper event handling
- **Animation System**: Smooth progress bar animations

### **Key Components**
- `PomodoroTimer` - Main application class
- `setup_ui()` - UI initialization and layout
- `create_vertical_button()` - Custom button creation
- `start_timer()` - Timer initialization
- `pause_timer()` - Pause/resume functionality
- `reset_timer()` - Reset functionality
- `countdown()` - Core timer logic
- `update_progress()` - Progress bar updates

## 🎨 **UI Layout**

### **Sidebar (Left)**
- **Title**: "🍅 TIMER"
- **Control Buttons**: 
  - 🚀 START (Green)
  - ⏸️ PAUSE (Orange) 
  - 🔄 RESET (Red)
- **Vertical Text**: Each button displays text vertically with minimal spacing

### **Main Content (Right)**
- **Settings Section**: 
  - Work Time (minutes)
  - Short Break (minutes)
  - Long Break (minutes)
  - Number of Cycles
- **Timer Display**: Large digital clock with status
- **Progress Bar**: Animated progress indicator
- **Quick Start Buttons**: One-click timer presets

## 🚀 **How to Run**

1. **Prerequisites**: Python 3.6+ with tkinter
2. **Download**: Save `pomodoroTimer.py` to your desired directory
3. **Run**: Execute the following command:
   ```bash
   python pomodoroTimer.py
   ```
   or
   ```bash
   py pomodoroTimer.py
   ```

## 📱 **How to Use**

### **Basic Usage**
1. **Set Times**: Adjust work, break, and cycle settings in the main area
2. **Start Timer**: Click the green START button in the sidebar
3. **Pause/Resume**: Click the orange PAUSE button to pause/resume
4. **Reset**: Click the red RESET button to reset the timer
5. **Quick Start**: Use the quick start buttons for preset times

### **Pomodoro Technique**
1. **Work Session**: Focus for 25 minutes (or your set time)
2. **Short Break**: Take a 5-minute break
3. **Repeat**: Complete 4 work/break cycles
4. **Long Break**: Take a 15-minute break after all cycles
5. **Repeat**: Start a new set of cycles

## 🎯 **Features in Detail**

### **Custom Vertical Buttons**
- **Precise Control**: Canvas-based rendering for exact positioning
- **Minimal Spacing**: 0.1px line spacing between characters
- **Hover Effects**: Color changes on mouse hover
- **Click Responsiveness**: Single-click activation (not hold)

### **Progress Bar Animation**
- **Rounded Design**: Custom rounded rectangle implementation
- **Color Coding**: Red for work sessions, green for breaks
- **Pulse Effect**: Subtle animation during active sessions
- **Smooth Updates**: Real-time progress visualization

### **Timer Logic**
- **Cycle Management**: Automatic progression through work/break cycles
- **Session Types**: Distinguishes between work, short break, and long break
- **State Management**: Proper handling of running, paused, and stopped states
- **Completion Handling**: Automatic transitions and notifications

## 🎨 **Color Scheme**
- **Background**: #2C3E50 (Dark Blue-Gray)
- **Cards**: #34495E (Medium Gray)
- **Accent**: #E74C3C (Red)
- **Success**: #27AE60 (Green)
- **Warning**: #F39C12 (Orange)
- **Text**: #ECF0F1 (Light Gray)
- **Secondary Text**: #BDC3C7 (Medium Light Gray)

## 🔧 **Customization**

### **Timer Settings**
- Work time: 1-999 minutes
- Short break: 1-999 minutes  
- Long break: 1-999 minutes
- Cycles: 1-99 cycles

### **Visual Customization**
- Font sizes and families
- Color schemes
- Button dimensions
- Animation speeds

## 📋 **System Requirements**
- **Operating System**: Windows, macOS, Linux
- **Python Version**: 3.6 or higher
- **Dependencies**: tkinter (usually included with Python)
- **Memory**: Minimal requirements
- **Display**: 700x600 minimum resolution

## 🐛 **Troubleshooting**

### **Common Issues**
1. **Buttons not responding**: Ensure Python and tkinter are properly installed
2. **Display issues**: Check screen resolution and scaling settings
3. **Timer not working**: Verify all input fields contain valid numbers

### **Error Handling**
- Input validation for timer settings
- Graceful error messages for invalid inputs
- Exception handling for button interactions

## 📝 **License**
This project is open source and available under the MIT License.

## 🤝 **Contributing**
Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## 📞 **Support**
For support or questions, please open an issue in the project repository.

---

**Happy Productivity! 🍅✨**
