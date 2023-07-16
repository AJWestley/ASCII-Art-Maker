from tkinter import font, filedialog
import tkinter
import ASCII


def choose_file():
    extensions = ["*.png", "*.PNG", "*.jpg", "*.JPG", "*.jpeg", "*.JPEG"]
    ftypes = [("images", extensions)]
    filepath = filedialog.askopenfilename(
        title="Choose an image", initialdir="/", filetypes=ftypes
    )
    print(f'filepath: "{filepath}"')
    fname.configure(text=filepath if filepath != "" else "No file selected")


def generate():
    filepath = fname["text"]
    if filepath == "No file selected":
        print("No image selected")
        return

    art_width = int(char_width.get())
    inverted = bool(invert.get())
    image = ASCII.ASCII_Artwork()
    image.import_adjust(filepath, art_width)
    image.translate(inv=inverted)
    output_box.configure(text=image.to_string())


root = tkinter.Tk()
root.geometry("1000x700")
root.title("ASCII Art Generator")
root.resizable(False, False)
root.configure(padx=10, pady=10)

# Title
title_fnt = font.Font(size=24, family="Helvetica", weight="bold")
title = tkinter.Label(
    root,
    text="ASCII Art Generator",
    font=title_fnt,
    pady=10,
)
title.pack(side="top")

# Content Frames
main_content = tkinter.Frame(root)
main_content.pack(side="top")

options_frame = tkinter.Frame(main_content, padx=10, pady=10)
options_frame.pack(side="left")

fselect_frame = tkinter.Frame(options_frame, pady=20)
fselect_frame.pack()

display_frame = tkinter.Frame(main_content, padx=10, pady=10)
display_frame.pack(side="right")

# File Path
fselect_fnt = font.Font(size=10, family="Helvetica")
fname = tkinter.Label(
    fselect_frame,
    text="No file selected",
    font=fselect_fnt,
    padx=5,
    pady=10,
    wraplength=120,
)
fname.pack()

# File Selector
fselect_btn = tkinter.Button(
    fselect_frame, text="Choose a file", command=choose_file, font=fselect_fnt
)
fselect_btn.pack()

# Size Slider
char_width = tkinter.StringVar(value=100)
width_slider = tkinter.Spinbox(options_frame, from_=60, to=120, textvariable=char_width)
width_slider.pack()

# Invert Checkbox
invert = tkinter.IntVar(value=0)
checkbox_fnt = font.Font(size=12, family="Helvetica")
inv_checkbox = tkinter.Checkbutton(
    options_frame, text="Invert", font=checkbox_fnt, pady=10, variable=invert
)
inv_checkbox.pack()

# Create button
button_fnt = font.Font(size=14, family="Helvetica", weight="bold")
create_btn = tkinter.Button(
    options_frame, text="Create", command=generate, font=button_fnt
)
create_btn.pack(side="bottom")

# Display Box
out_fnt = font.Font(size=7, family="Terminal", weight="bold")
output_box = tkinter.Label(
    display_frame, width=120, height=80, font=out_fnt, borderwidth=5, relief="ridge"
)
output_box.pack()

root.mainloop()
