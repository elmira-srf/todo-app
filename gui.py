import functions
# import PySimpleGUI as sg
import FreeSimpleGUI as sg

lable = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip= "Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My Do To', layout=[[lable], [input_box], [add_button]])
window.read()
window.close()

