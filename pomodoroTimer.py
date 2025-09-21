import tkinter as tk
from tkinter import messagebox, ttk
import time
import math

class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🍅 Pomodoro Timer")
        self.root.geometry("700x600")
        self.root.configure(bg='#2C3E50')
        
        # Make window appear on top
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after(1000, lambda: self.root.attributes('-topmost', False))
        
        # Timer variables
        self.is_running = False
        self.is_paused = False
        self.seconds = 0
        self.total_seconds = 0
        self.is_work_session = True
        self.cycle_count = 0
        self.animation_frame = 0
        self.pulse_animation = False
        
        self.setup_ui()
        
    def setup_ui(self):
        # Create main container with sidebar layout
        main_container = tk.Frame(self.root, bg='#2C3E50')
        main_container.pack(fill='both', expand=True)
        
        # Create sidebar
        sidebar = tk.Frame(main_container, bg='#34495E', width=200)
        sidebar.pack(side='left', fill='y', padx=(0, 10))
        sidebar.pack_propagate(False)
        
        # Create main content area
        content_area = tk.Frame(main_container, bg='#2C3E50')
        content_area.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        # Sidebar title
        sidebar_title = tk.Label(
            sidebar, 
            text="🍅 TIMER", 
            font=("Segoe UI", 20, "bold"),
            fg='#E74C3C',
            bg='#34495E'
        )
        sidebar_title.pack(pady=20)
        
        # Remove the control panel subtitle to move buttons up
        
        # Settings frame in main content area
        settings_frame = tk.Frame(content_area, bg='#34495E', relief='raised', bd=2)
        settings_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(settings_frame, text="⚙️ Settings", font=("Segoe UI", 16, "bold"), 
                fg='white', bg='#34495E').pack(pady=10)
        
        # Settings grid
        settings_grid = tk.Frame(settings_frame, bg='#34495E')
        settings_grid.pack(pady=10, padx=20)
        
        # Work time
        tk.Label(settings_grid, text="Work (min):", font=("Segoe UI", 12), 
                fg='white', bg='#34495E').grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.work_entry = tk.Entry(settings_grid, font=("Segoe UI", 12), width=10, 
                                  relief='flat', bd=3, justify='center')
        self.work_entry.grid(row=0, column=1, padx=10, pady=5)
        self.work_entry.insert(0, "25")
        
        # Short break time
        tk.Label(settings_grid, text="Short Break (min):", font=("Segoe UI", 12), 
                fg='white', bg='#34495E').grid(row=0, column=2, padx=10, pady=5, sticky='w')
        self.short_break_entry = tk.Entry(settings_grid, font=("Segoe UI", 12), width=10,
                                         relief='flat', bd=3, justify='center')
        self.short_break_entry.grid(row=0, column=3, padx=10, pady=5)
        self.short_break_entry.insert(0, "5")
        
        # Long break time
        tk.Label(settings_grid, text="Long Break (min):", font=("Segoe UI", 12), 
                fg='white', bg='#34495E').grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.long_break_entry = tk.Entry(settings_grid, font=("Segoe UI", 12), width=10,
                                        relief='flat', bd=3, justify='center')
        self.long_break_entry.grid(row=1, column=1, padx=10, pady=5)
        self.long_break_entry.insert(0, "15")
        
        # Cycles
        tk.Label(settings_grid, text="Cycles:", font=("Segoe UI", 12), 
                fg='white', bg='#34495E').grid(row=1, column=2, padx=10, pady=5, sticky='w')
        self.cycle_entry = tk.Entry(settings_grid, font=("Segoe UI", 12), width=10,
                                   relief='flat', bd=3, justify='center')
        self.cycle_entry.grid(row=1, column=3, padx=10, pady=5)
        self.cycle_entry.insert(0, "4")
        
        # Main content area - Timer display
        timer_frame = tk.Frame(content_area, bg='#34495E', relief='raised', bd=2)
        timer_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        self.status_label = tk.Label(
            timer_frame,
            text="Ready to Focus! 🎯",
            font=("Segoe UI", 18, "bold"),
            fg='#27AE60',
            bg='#34495E'
        )
        self.status_label.pack(pady=10)
        
        # Cycle counter
        self.cycle_label = tk.Label(
            timer_frame,
            text="Cycle: 0/0",
            font=("Segoe UI", 12),
            fg='#BDC3C7',
            bg='#34495E'
        )
        self.cycle_label.pack()
        
        # Timer display with beautiful font
        self.timer_label = tk.Label(
            timer_frame,
            text="00:00",
            font=("Consolas", 56, "bold"),
            fg='#E74C3C',
            bg='#34495E'
        )
        self.timer_label.pack(pady=20)
        
        # Animated progress bar
        self.progress = tk.Canvas(timer_frame, width=320, height=25, bg='#2C3E50', highlightthickness=0)
        self.progress.pack(pady=15)
        
        # Create rounded progress bar background
        self.create_rounded_rect(self.progress, 5, 5, 315, 20, 10, '#34495E')
        
        # Control buttons in sidebar - vertical layout (moved up)
        button_frame = tk.Frame(sidebar, bg='#34495E')
        button_frame.pack(pady=10, padx=10, fill='both', expand=True)
        
        # Create custom vertical buttons with 0.1px line spacing
        def create_vertical_button(parent, text, bg_color, active_color, command, state='normal'):
            # Create a frame to act as button - increased height by 45px total (25+20)
            btn_frame = tk.Frame(parent, bg=bg_color, relief='raised', bd=2, width=50, height=165)
            btn_frame.pack(pady=5)
            btn_frame.pack_propagate(False)
            
            # Create canvas for custom text rendering - increased height by 45px total (25+20)
            canvas = tk.Canvas(btn_frame, bg=bg_color, highlightthickness=0, width=46, height=161)
            canvas.pack()
            
            # Draw vertical text with 0.1px line spacing
            chars = list(text)
            y_pos = 15
            for char in chars:
                if char == '\n':
                    y_pos += 12.1  # 0.1px spacing between lines
                else:
                    canvas.create_text(25, y_pos, text=char, font=("Segoe UI", 10, "bold"), 
                                     fill='white', anchor='center')
                    y_pos += 12.1
            
            # Add click functionality
            def on_click(event):
                try:
                    command()
                except Exception as e:
                    print(f"Error in button command: {e}")
            
            def on_enter(event):
                canvas.config(bg=active_color)
                btn_frame.config(bg=active_color)
            
            def on_leave(event):
                canvas.config(bg=bg_color)
                btn_frame.config(bg=bg_color)
            
            # Bind events to both canvas and frame - only single click
            canvas.bind('<Button-1>', on_click)
            canvas.bind('<Enter>', on_enter)
            canvas.bind('<Leave>', on_leave)
            
            btn_frame.bind('<Button-1>', on_click)
            btn_frame.bind('<Enter>', on_enter)
            btn_frame.bind('<Leave>', on_leave)
            
            # Make sure the canvas can receive focus and is clickable
            canvas.focus_set()
            canvas.config(cursor='hand2')
            
            return btn_frame
        
        # Create vertical buttons with 0.1px line spacing
        self.start_button = create_vertical_button(
            button_frame, "🚀\nS\nT\nA\nR\nT", '#27AE60', '#229954', self.start_timer
        )
        
        self.pause_button = create_vertical_button(
            button_frame, "⏸️\nP\nA\nU\nS\nE", '#F39C12', '#E67E22', self.pause_timer, 'normal'
        )
        
        self.reset_button = create_vertical_button(
            button_frame, "🔄\nR\nE\nS\nE\nT", '#E74C3C', '#C0392B', self.reset_timer
        )
        
        # Quick buttons in main content area
        quick_frame = tk.Frame(content_area, bg='#34495E', relief='raised', bd=2)
        quick_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(quick_frame, text="Quick Start", font=("Segoe UI", 14, "bold"), 
                fg='white', bg='#34495E').pack(pady=10)
        
        quick_buttons_frame = tk.Frame(quick_frame, bg='#34495E')
        quick_buttons_frame.pack(pady=10, padx=20)
        
        tk.Button(
            quick_buttons_frame,
            text="25min Work",
            font=("Segoe UI", 12, "bold"),
            bg='#2C3E50',
            fg='white',
            padx=20,
            pady=10,
            relief='raised',
            bd=2,
            command=lambda: self.set_timer(25*60, "Work"),
            cursor='hand2'
        ).pack(side='left', padx=10)
        
        tk.Button(
            quick_buttons_frame,
            text="5min Break",
            font=("Segoe UI", 12, "bold"),
            bg='#2C3E50',
            fg='white',
            padx=20,
            pady=10,
            relief='raised',
            bd=2,
            command=lambda: self.set_timer(5*60, "Short Break"),
            cursor='hand2'
        ).pack(side='left', padx=10)
        
        tk.Button(
            quick_buttons_frame,
            text="15min Break",
            font=("Segoe UI", 12, "bold"),
            bg='#2C3E50',
            fg='white',
            padx=20,
            pady=10,
            relief='raised',
            bd=2,
            command=lambda: self.set_timer(15*60, "Long Break"),
            cursor='hand2'
        ).pack(side='left', padx=10)
        
    def create_rounded_rect(self, canvas, x1, y1, x2, y2, radius, fill, outline=''):
        """Create a rounded rectangle on canvas"""
        points = []
        for i in range(16):
            angle = i * math.pi / 32
            if i < 4:
                x = x2 - radius + radius * math.cos(angle)
                y = y1 + radius - radius * math.sin(angle)
            elif i < 8:
                x = x2 - radius + radius * math.cos(angle)
                y = y2 - radius + radius * math.sin(angle)
            elif i < 12:
                x = x1 + radius - radius * math.cos(angle)
                y = y2 - radius + radius * math.sin(angle)
            else:
                x = x1 + radius - radius * math.cos(angle)
                y = y1 + radius - radius * math.sin(angle)
            points.extend([x, y])
        return canvas.create_polygon(points, fill=fill, outline=outline, smooth=True)
        
    def set_timer(self, seconds, session_type):
        self.seconds = seconds
        self.total_seconds = seconds
        mins, secs = divmod(seconds, 60)
        self.timer_label.config(text=f"{mins:02d}:{secs:02d}")
        self.status_label.config(text=f"{session_type} Session Set! 🎯")
        self.update_progress()
        
    def start_timer(self):
        if not self.is_running:
            try:
                work_min = int(self.work_entry.get())
                short_break_min = int(self.short_break_entry.get())
                long_break_min = int(self.long_break_entry.get())
                cycles = int(self.cycle_entry.get())
                
                if work_min <= 0 or short_break_min <= 0 or long_break_min <= 0 or cycles <= 0:
                    messagebox.showerror("Error", "Please enter positive numbers!")
                    return
                    
                self.work_min = work_min
                self.short_break_min = short_break_min
                self.long_break_min = long_break_min
                self.total_cycles = cycles
                self.cycle_count = 0
                self.is_work_session = True
                
                self.start_work_session()
                
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers!")
                
    def start_work_session(self):
        self.cycle_count += 1
        self.is_work_session = True
        self.seconds = self.work_min * 60
        self.total_seconds = self.work_min * 60
        self.is_running = True
        self.is_paused = False
        
        # Disable start button but keep pause button enabled
        self.start_button.config(bg='#7D7D7D')  # Gray out start button
        # Pause button stays enabled (no change needed)
        self.status_label.config(text="🔥 Focus Time!", fg='#E74C3C')
        self.cycle_label.config(text=f"Cycle: {self.cycle_count}/{self.total_cycles}")
        
        self.countdown()
        
    def start_break_session(self):
        self.is_work_session = False
        self.is_running = True
        self.is_paused = False
        
        # Check if this is the last cycle (long break) or a regular cycle (short break)
        if self.cycle_count >= self.total_cycles:
            # Long break after completing all cycles
            self.seconds = self.long_break_min * 60
            self.total_seconds = self.long_break_min * 60
            self.status_label.config(text="🎉 Long Break Time!", fg='#F39C12')
        else:
            # Short break between cycles
            self.seconds = self.short_break_min * 60
            self.total_seconds = self.short_break_min * 60
            self.status_label.config(text="☕ Short Break Time!", fg='#27AE60')
        
        self.countdown()
                
    def pause_timer(self):
        if not self.is_running:
            return  # Don't pause if timer is not running
            
        if self.is_paused:
            # Resume the timer
            self.is_paused = False
            self.status_label.config(text="▶️ Resumed", fg='#27AE60')
            self.countdown()
        else:
            # Pause the timer
            self.is_paused = True
            self.status_label.config(text="⏸️ Paused", fg='#F39C12')
            
    def reset_timer(self):
        self.is_running = False
        self.is_paused = False
        self.seconds = 0
        self.total_seconds = 0
        self.cycle_count = 0
        self.is_work_session = True
        
        self.timer_label.config(text="00:00")
        self.status_label.config(text="Ready to Focus! 🎯", fg='#27AE60')
        self.cycle_label.config(text="Cycle: 0/0")
        self.progress.delete("all")
        # Redraw progress bar background
        self.create_rounded_rect(self.progress, 5, 5, 315, 20, 10, '#34495E')
        
        self.start_button.config(bg='#27AE60')  # Re-enable start button
        # Pause button stays enabled (no change needed)
        
    def countdown(self):
        if self.is_running and self.seconds > 0 and not self.is_paused:
            mins, secs = divmod(self.seconds, 60)
            self.timer_label.config(text=f"{mins:02d}:{secs:02d}")
            self.update_progress()
            self.seconds -= 1
            self.root.after(1000, self.countdown)
        elif self.seconds == 0 and self.is_running:
            self.is_running = False
            
            if self.is_work_session:
                # Work session finished
                self.status_label.config(text="🎉 Work done! Starting break...", fg='#27AE60')
                if self.cycle_count < self.total_cycles:
                    messagebox.showinfo("Work Complete!", f"Great job! Cycle {self.cycle_count} complete! Time for a short break! 🎉")
                else:
                    messagebox.showinfo("Work Complete!", f"Amazing! All {self.total_cycles} cycles complete! Time for a long break! 🎊")
                self.root.after(2000, self.start_break_session)
            else:
                # Break session finished
                if self.cycle_count >= self.total_cycles:
                    # Long break finished - all cycles complete
                    self.status_label.config(text="🎊 All cycles complete! Amazing work!", fg='#27AE60')
                    messagebox.showinfo("Pomodoro Complete!", "Congratulations! You've completed all your Pomodoro cycles! 🎊")
                    self.reset_timer()
                else:
                    # Short break finished - start next work session
                    self.status_label.config(text="Break over! Starting next work session...", fg='#E74C3C')
                    messagebox.showinfo("Break Over!", "Break time is up! Ready for the next work session? 🚀")
                    self.root.after(2000, self.start_work_session)
            
    def update_progress(self):
        if self.total_seconds > 0:
            progress = (self.total_seconds - self.seconds) / self.total_seconds
            width = int(310 * progress)
            
            # Clear canvas
            self.progress.delete("all")
            
            # Draw background
            self.create_rounded_rect(self.progress, 5, 5, 315, 20, 10, '#34495E')
            
            # Draw progress with animation
            if width > 10:
                # Choose color based on session type
                if self.is_work_session:
                    color = '#E74C3C'  # Red for work
                else:
                    color = '#27AE60'  # Green for break
                    
                self.create_rounded_rect(self.progress, 5, 5, 5 + width, 20, 10, color)
                
                # Add pulse animation when running
                if self.is_running and not self.is_paused:
                    self.animate_progress_pulse()
                    
    def animate_progress_pulse(self):
        """Add a subtle pulse animation to the progress bar"""
        if self.is_running and not self.is_paused:
            # Create a subtle glow effect
            pulse_alpha = 0.3 + 0.2 * math.sin(self.animation_frame * 0.2)
            self.animation_frame += 1
            
            # Add a subtle overlay for pulse effect
            if self.total_seconds > 0:
                progress = (self.total_seconds - self.seconds) / self.total_seconds
                width = int(310 * progress)
                if width > 10:
                    # Create a subtle white overlay for pulse
                    pulse_color = f'#{int(255 * pulse_alpha):02x}{int(255 * pulse_alpha):02x}{int(255 * pulse_alpha):02x}'
                    self.create_rounded_rect(self.progress, 5, 5, 5 + width, 20, 10, pulse_color)
            
            # Schedule next animation frame
            self.root.after(50, self.animate_progress_pulse)
            
    def run(self):
        # Set default to 00:00 instead of 25:00
        self.timer_label.config(text="00:00")
        self.root.mainloop()

if __name__ == "__main__":
    app = PomodoroTimer()
    app.run()