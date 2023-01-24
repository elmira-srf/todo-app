import PySimpleGUI as sg

label1 = sg.Text("Select files to compress:")
button1 = sg.FileBrowse("Choose")
input1 = sg.Input()

label2 = sg.Text("Select destination folder:")
button2 = sg.FolderBrowse("Choose")
input2 = sg.Input()

compress_btn = sg.Button("Compress")
somsething = sg.Text()

window = sg.Window('File Zipper', layout=[[label1, input1, button1], [label2, input2, button2], [compress_btn]])
window.read()
window.close()
