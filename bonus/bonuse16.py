import FreeSimpleGUI as sg
from zipp_creator import make_archive

label1 = sg.Text("Select files to compress:")
button1 = sg.FilesBrowse("Choose", key='Files')
input1 = sg.Input()

label2 = sg.Text("Select destination folder:")
button2 = sg.FolderBrowse("Choose", key='Folder')
input2 = sg.Input()

compress_btn = sg.Button("Compress")
output_lable = sg.Text(key="output", text_color="green")

window = sg.Window('File Zipper',
                   layout=[[label1, input1, button1],
                           [label2, input2, button2],
                           [compress_btn, output_lable]])
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["Files"].split(";")
    folder = values["Folder"]
    make_archive(filepaths, folder)
    window["output"].update(value = "Comptession completed")
window.close()
