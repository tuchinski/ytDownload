from pytube import YouTube

url = "https://www.youtube.com/watch?v=fN6uzhy5uvU&ab_channel=TheLateLateShowwithJamesCorden"
a = YouTube(url)

videos = a.streams

i = 1

for v in videos:
    # print(v)
    resolucao = ""
    if v.type == 'audio':
        resolucao = v.abr
    else:
        resolucao =  v.resolution
    print(i,v.mime_type,resolucao,v.type)
    i += 1


index_video_escolhido = int(input("Escolhe ai: ")) -1
video_escolhido = videos[index_video_escolhido]

print(video_escolhido)

