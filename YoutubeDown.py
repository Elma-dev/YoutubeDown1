def finish():
    print("Download Finish.")

from pytube import YouTube

print("----------Download Youtube Videos----------",end="\n")
url=input("Enter Url Video:")
url=YouTube(url)
t=url.title
print(f'---------------//{t}//---------------')
type=input("Enter Type (video/audio):")
path=input("Enter saved Path(C:\....): ")

if type=="audio":
    url.streams.get_audio_only("mp4").download(output_path=path)
    url.register_on_complete_callback(print("Download Finish..."))

elif type=="video":
    while True:
        resolution=str(input("Enter resolution:"))
        video=url.streams.filter(res=resolution+"p",type="video")
        if len(video)!=0:
            break
    video[0].download(output_path=path)
    print("Wait...")
    url.register_on_complete_callback(print("Download Finish..."))
else:
    print("Unknow Type!!")
