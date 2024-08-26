import FreeSimpleGUI as sg

lable1 = sg.Text("Enter feet: ")
input1 = sg.Input(key="feet")
lable2 = sg.Text("Enter inches: ")
input2 = sg.Input(key="inches")
button = sg.Button("Convert")

output_lable = sg.Text()
window = sg.Window("Convertor",
                   layout= [[lable1, input1],
                            [lable2, input2],
                            [button, output_lable]])
while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = meters = feet * 0.3048 + inches * 0.0254
    if event == "Convert":
        output_lable.update(value=f"{result} m", text_color="white")
window.close()
