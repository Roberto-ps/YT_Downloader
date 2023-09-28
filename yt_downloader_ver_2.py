from PySimpleGUI import theme, Image, Text, Input, Submit, Push, Window, WIN_CLOSED
from pytube import YouTube


theme("DarkBlack")

layout = [
    [Image(filename="index.png", key="-IMAGE-")],
    [Text("Url do vídeo: ",
          justification="center",
          text_color="Gray",
          # background_color="white",
          size=(10, 0)),
     Input(key="-URL-", do_not_clear=True)],
    [Push(), Push(), Submit("Info", size=(10, 0), key="-GET-"),
     Submit("Download",
            button_color="Gray",
            size=(10, 0),
            key="-DOWNLOAD-"),
     Push(), Push()],
    [Text(key="-INFO-")],
    [Text(key="-COMPLET-")]
]

window = Window("YouTube Downloader",
                size=(400, 500),
                layout=layout,
                element_justification="l"
                )
while True:
    event, values = window.read()
    if event == "-GET-":
        my_video = YouTube(values["-URL-"])
        my_video_size = my_video.streams.get_by_resolution("360p").filesize_mb
        window["-INFO-"].update(f"Título: {my_video.title}\n"
                                f"Duração: {my_video.length} seconds\n"
                                f"Tamanho: {my_video_size:.2f} mb")

    if event == "-DOWNLOAD-":
        my_video = YouTube(values["-URL-"])
        my_video = my_video.streams.get_by_resolution("360p")
        my_video.download()
        window["-COMPLET-"].update("Download concluído!!! ")

    if event == WIN_CLOSED:
        break

window.close()
