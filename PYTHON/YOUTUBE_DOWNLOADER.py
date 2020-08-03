from pytube import YouTube
try:
    link=input("PASTE YOUR YOUTUBE LINK WHICH U WANT TO DOWNLOAD")
    YouTube(link).streams.first().download()
except:
    pass
    
