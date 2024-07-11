# importing all the required modules
from django.shortcuts import render, redirect
from pytube import *


# defining function
def youtube(request):
    # checking whether request.method is post or not
    if request.method == 'POST':

        link = request.POST['link']
        video = YouTube(link)


        stream = video.streams.get_lowest_resolution()

        # downloads video
        stream.download()

        # returning HTML page
        return render(request, 'youtube.html')
    return render(request, 'youtube.html')
