import FreeSimpleGUI as sg
from  zip_extractor import extract_archive

sg.theme("LightBlue3")

lable1 = sg.Text("Select archived:")
input1 = sg.Input()
chooes_button1 = sg.FileBrowse("Choose", key="archive")

lable2 = sg.Text("Select destination:")
input2 = sg.Input()
chooes_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_lable = sg.Text(key="output", text_color="green")


layout = [[lable1, input1, chooes_button1],
          [lable2,input2,chooes_button2],
          [extract_button,output_lable]]


window = sg.Window('Archive Extractor',
                   layout=layout,
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Extract":
            archivepath = values["archive"]
            dest_dir = values["folder"]
            extract_archive(archivepath, dest_dir)
            window["output"].update(value= "Extraction completed!")
        case sg.WINDOW_CLOSED:
            break

window.close()