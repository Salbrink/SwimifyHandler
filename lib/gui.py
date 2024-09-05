from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from Competition import competition
from Club import club
from Session import session
from Swimmer import swimmer
from SwimifyHandler import swimify_handler

# Handler setup
handler = swimify_handler(10)

# Path setup
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# List of competition buttons. Must be set with call to set_competition_buttons
competition_buttons = []

def set_competition_buttons(comp_list: list[competition]):
    button_list = []

    for index, comp in enumerate(comp_list):
        comp_button = Button(
            text=comp.competition_name,
            font=("Arial", 14),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: handler.select_competition(comp),  # Restore original layout
            relief="flat",
            bg="#A0A0A0",
            fg="black"
        )

        comp_button.place(
            x=100.0, y=400 + 50*index, width=800.0, height=25.0
        )

        button_list.append(comp_button)
        return button_list





# Function to show only the clicked button and hide others
def show_single_button(button_index):
    for i, button in enumerate(buttons):
        if i == button_index:
            button.place(x=75.0, y=200.0, width=850.0, height=100.0)
        else:
            button.place_forget()  # Hide other buttons

    match button_index:
        case 0:
            print("Upcoming competitions pressed")
            upcoming_competitions = handler.get_upcoming_competitions()
            competition_buttons = set_competition_buttons(upcoming_competitions)

        case 1:
            print("Finished competitions pressed")
            finished_competitions = handler.get_upcoming_competitions()
            competition_buttons = set_competition_buttons(finished_competitions)

        case 2:
            print("Competitions this week pressed")    
            competitions_this_week = handler.get_competitions_this_week()
            competition_buttons = set_competition_buttons(competitions_this_week)

    # Show the small "Back" button at the bottom left corner
    back_button.place(x=10.0, y=750.0, width=50.0, height=30.0)

# Function to restore the original layout with all three buttons
def show_all_buttons():
    y_positions = [200.0, 400.0, 600.0]
    for i, button in enumerate(buttons):
        button.place(x=75.0, y=y_positions[i], width=850.0, height=125.0)
    
    back_button.place_forget()  # Hide the back button
    for button in competition_buttons:
        button.place_forget()

# Main window setup
window = Tk()
window.geometry("1000x800")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=800,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

# Background rectangle
canvas.create_rectangle(
    0.0,
    0.0,
    1000.0,
    150.0,
    fill="#A0A0A0",
    outline="")

# Example image
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(
    181.0,
    75.0,
    image=image_image_1
)

# Button creation
buttons = []

for i in range(3):
    button_image = PhotoImage(file=relative_to_assets(f"button_{i + 1}.png"))
    button = Button(
        image=button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda i=i: show_single_button(i),  # Capture button index in lambda
        relief="flat"
    )
    button.image = button_image  # Keep a reference to the image
    buttons.append(button)

# Positioning the buttons initially
y_positions = [200.0, 400.0, 600.0]
for i, button in enumerate(buttons):
    button.place(x=75.0, y=y_positions[i], width=850.0, height=125.0)

# Small "Back" button with "<" sign
back_button = Button(
    text="<",
    font=("Arial", 14),
    borderwidth=0,
    highlightthickness=0,
    command=show_all_buttons,  # Restore original layout
    relief="flat",
    bg="#A0A0A0",
    fg="black"
)
back_button.place_forget()  # Hide initially

window.resizable(False, False)
window.mainloop()
