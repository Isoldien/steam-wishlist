import tkinter as tk
from tkinter import font
import logic.logic as logic

class HomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Steam Wishlist Manager")
        self.root.geometry("600x500")
        self.root.configure(bg="#1b2838")
        
        # Center the window on screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the home screen UI"""
        # Title Label
        title_font = font.Font(family="Helvetica", size=28, weight="bold")
        title_label = tk.Label(
            self.root,
            text="Steam Wishlist",
            font=title_font,
            fg="#00a8ff",
            bg="#1b2838"
        )
        title_label.pack(pady=30)
        
        # Subtitle
        subtitle_font = font.Font(family="Helvetica", size=12)
        subtitle_label = tk.Label(
            self.root,
            text="Manage and search your Steam wishlist with ease",
            font=subtitle_font,
            fg="#b0b8c1",
            bg="#1b2838"
        )
        subtitle_label.pack(pady=(0, 40))
        
        # Main content frame
        content_frame = tk.Frame(self.root, bg="#1b2838")
        content_frame.pack(expand=True, padx=20)
        
        # Run Program Button
        run_button = tk.Button(
            content_frame,
            text="🔍 Run Search",
            command=self.run_search,
            bg="#1f7f6f",
            fg="white",
            font=("Helvetica", 12, "bold"),
            padx=20,
            pady=15,
            relief=tk.RAISED,
            cursor="hand2",
            activebackground="#16543d",
            activeforeground="white"
        )
        run_button.pack(pady=10, fill=tk.X)
        
        # About Button
        about_button = tk.Button(
            content_frame,
            text="About",
            command=self.show_about,
            bg="#2d3d4f",
            fg="white",
            font=("Helvetica", 12),
            padx=20,
            pady=15,
            relief=tk.RAISED,
            cursor="hand2",
            activebackground="#1f2936",
            activeforeground="white"
        )
        about_button.pack(pady=10, fill=tk.X)
        
        # Exit Button
        exit_button = tk.Button(
            content_frame,
            text="❌ Exit",
            command=self.root.quit,
            bg="#5a3a3a",
            fg="white",
            font=("Helvetica", 12),
            padx=20,
            pady=15,
            relief=tk.RAISED,
            cursor="hand2",
            activebackground="#3a2a2a",
            activeforeground="white"
        )
        exit_button.pack(pady=10, fill=tk.X)
        
        # Status bar
        status_frame = tk.Frame(self.root, bg="#0e1419", height=30)
        status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        status_label = tk.Label(
            status_frame,
            text="Ready",
            font=("Helvetica", 9),
            fg="#b0b8c1",
            bg="#0e1419"
        )
        status_label.pack(side=tk.LEFT, padx=10, pady=5)
        self.status_label = status_label
    
    def run_search(self):
        """Execute the search function"""
        try:
            self.status_label.config(text="Running search...")
            self.root.update()
            logic.search()
            self.status_label.config(text="Search completed")
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")
    
    def show_about(self):
        """Show about information"""
        about_text = (
            "Steam Wishlist Manager\n"
            "Version 1.0\n\n"
            "A utility to manage and search your Steam wishlist.\n"
            "Made by isoldien"
        )
        self.status_label.config(text=about_text)


def start():
    """Start the home screen application"""
    root = tk.Tk()
    app = HomeScreen(root)
    root.mainloop()


if __name__ == "__main__":
    start()
