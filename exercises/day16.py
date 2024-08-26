import FreeSimpleGUI as sg

lable1 = sg.Text("Enter feet: ")
input1 = sg.Input()
lable2 = sg.Text("Enter inches: ")
input2 = sg.Input()
button = sg.Button("Convert")

window = sg.Window("Convertor",
                   layout= [[lable1, input1],
                            [lable2, input2],
                            [button]])
window.read()
window.close()
