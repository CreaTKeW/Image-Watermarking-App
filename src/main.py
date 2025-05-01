from ui.main_window import App
import ttkbootstrap as ttk

if __name__ == '__main__':
    root = ttk.Window(themename="darkly")
    app = App(root)
    root.mainloop()