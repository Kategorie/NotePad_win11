import tkinter as tk
from tkinter import ttk, filedialog, simpledialog

class TabbedNotepadUI:
    def __init__(self, root):
        self.root = root
        self.notebook = None
        self.menu_bar = None
        self.toggle_menu_button = None
        self.current_x = 0
        self.current_y = 0

    def setup_ui(self):
        # 노트북 생성
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # 메뉴 생성
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Tab", command=self.add_tab)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.destroy)

        # 메뉴바 숨기기/나타내기 버튼 추가
        self.toggle_menu_button = tk.Button(self.menu_bar, text="↓", relief=tk.FLAT)
        self.menu_bar.add_command(label="Toggle Menu", command=self.toggle_menu)

    def toggle_menu(self, event=None):
        if self.menu_bar.winfo_ismapped():
            self.menu_bar.forget()
            self.toggle_menu_button.config(text="↑")
        else:
            self.menu_bar.pack(side=tk.TOP, fill=tk.X)
            self.toggle_menu_button.config(text="↓")

    def on_mousewheel(self, event):
        if event.widget == self.notebook.winfo_children()[0].winfo_children()[1]:
            self.notebook.winfo_children()[0].winfo_children()[0].set(
                self.notebook.winfo_children()[0].winfo_children()[0].get() - (event.delta / 120), 0
            )
        else:
            self.notebook.winfo_children()[0].winfo_children()[0].set(
                self.notebook.winfo_children()[0].winfo_children()[0].get() + (event.delta / 120), 0
            )

    def add_tab(self):
        # 탭 추가
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Untitled")

        # Frame 내에 또 다른 Frame 생성 (텍스트 에디터와 닫기 아이콘을 가지는)
        content_frame = ttk.Frame(tab)
        content_frame.grid(row=0, column=0, sticky="nsew")

        # 탭에 닫기 아이콘 추가
        close_button = tk.Button(content_frame, text="x", relief=tk.FLAT)
        close_button.grid(row=0, column=1, padx=2, pady=2, sticky="e")

        # 텍스트 에디터 추가
        text_editor = tk.Text(content_frame, wrap="word")
        text_editor.grid(row=0, column=0, sticky="nsew")

        # 스크롤바 추가
        scrollbar = ttk.Scrollbar(content_frame, orient=tk.VERTICAL, command=text_editor.yview)
        scrollbar.grid(row=0, column=2, sticky="ns")
        text_editor.config(yscrollcommand=scrollbar.set)

        # 탭 이름 수정 기능 추가
        tab.bind("<Double-Button-1>", lambda event, tab=tab: self.rename_tab(tab))

        # 이벤트 바인딩: 탭 클릭 시 발생하는 이벤트
        tab.bind("<Button-1>", self.on_tab_click)

        # 그리드에 대한 가중치 설정
        tab.grid_rowconfigure(0, weight=1)
        tab.grid_columnconfigure(0, weight=1)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            tab_index = self.notebook.index(tk.CURRENT)
            tab = self.notebook.tabs()[tab_index]
            text_widget = tab.winfo_children()[0].winfo_children()[0]
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, content)
            self.notebook.tab(tab, text=file_path)

    def save_file(self):
        tab_index = self.notebook.index(tk.CURRENT)
        tab = self.notebook.tabs()[tab_index]
        text_widget = tab.winfo_children()[0].winfo_children()[0]
        content = text_widget.get(1.0, tk.END)

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)
            self.notebook.tab(tab, text=file_path)

    def close_tab(self, tab):
        tab_index = self.notebook.index(tab)
        self.notebook.forget(tab_index)

    def on_tab_click(self, event):
        # 탭 클릭 시 현재 마우스 위치 저장
        self.current_x = event.x
        self.current_y = event.y

    def rename_tab(self, tab):
        # 탭 이름 수정 다이얼로그 표시
        tab_index = self.notebook.index(tab)
        current_text = self.notebook.tab(tab_index, "text")
        new_text = simpledialog.askstring("Rename Tab", "Enter new name:", initialvalue=current_text)
        if new_text:
            self.notebook.tab(tab, text=new_text)
