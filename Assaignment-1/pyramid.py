import pyautogui

num_rows = int(input("Enter the number of rows: "))

character = "#"

for i in range(1, num_rows + 1):
    row_string = character * i
    pyautogui.typewrite(row_string)
    pyautogui.typewrite('\n')

print("Pyramid drawn successfully using PyAutoGUI.")

