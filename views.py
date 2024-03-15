from __future__ import unicode_literals
from django.shortcuts import redirect
from django.shortcuts import render

# from django.urls import 
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from urllib.request import pathname2url

from .models import Todo

import sys,youtube_dl,yt_dlp,re,os
from collections import OrderedDict
import itertools

        # Area for Global variables
audio_id =''
url = ''
title = ''
thumbnail = '#'
global webpage_urls
webpage_urls=[]





def home(request):
    return render(request, 'ytb_main.html ')


    
    
        
def playlist_download(request):
    i = request.POST.get('id_value')
    print(i)
    print('i am playlist_download function')
    
    global url
    global audio_id
    global title
    global thumbnail
    global webpage_urls
    protocol=[]

    duration='NaN'
    link=[]
    format_ids =[]
    filesize =[]
    file_s=[]
    cod=[]
    resolution =[]
    extension =[]
    formats =[]
    vcodec=[]
    vbr=[]
    

    regex_youtube = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
    regex_vimeo = r'^(http(s)?:\/\/)?((w){3}.|(player.))?vimeo?(\.com)?\/.+'
    regex_bili = r'^(http(s)?:\/\/)?((w){3}.)?bilibili?(\.com)?\/.+'
    regex_daily_motion = r'^(http(s)?:\/\/)?((w){3}.)?dailymotion?(\.com)?\/.+'
    regex_VLive = r'^(http(s)?:\/\/)?((w){3}.|m.)?vlive?(\.tv)?\/.+'



    

    # print(i)
    # print("this is webpage url from playlist ",webpage_urls)
    i = int(i)
    url = webpage_urls[i]
    print(url)

    
               
    
    
    
    
    
    
    
    
    
    
   
    

    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(url, download=False)

    for k, v in meta.items():
        
        if k == "duration":
            try:

                duration = v
                if duration > 3600:
                    duration=round(duration/3600,2)
                    duration = str(duration)+'hr'
                    
                elif duration > 60:
                    duration = round(duration/60,2)
                    duration = str(duration)+'min'
                    

                else:
                    duration=str(duration)+'sec'
                   

            except:
                duration = 'NaN'
                

        elif k == 'duration_string':
            duration = v
            
            if len(duration) <=2:
                duration = duration+" sec"
            elif len(duration) <=5:
                duration = duration + " minutes"
            elif len(duration) > 5:
                duration = duration + " hours"
        elif k == 'title':
            title=v
            
        
        elif k == "thumbnail":
            thumbnail = v
                
            
        
        elif k == 'formats':
            for i in v:
                for a, b in i.items():
                    if a == 'format_id':
                        format_ids.append(b)
                    elif a == 'format':
                        formats.append(b)
                    elif a == 'resolution':
                        resolution.append(b)
                    elif a == 'ext':
                        extension.append(b)
                    elif a == 'filesize':
                        filesize.append(b)
                    elif a == 'acodec':
                        cod.append(b)
                    elif a == 'filesize_approx':
                        file_s.append(b)
                    elif a == 'tbr':
                        vbr.append((b))
                    elif a == 'vcodec':
                        vcodec.append((b))
                    elif a == 'url':
                        link.append(b)
                    elif a == 'protocol':
                        protocol.append(b)
        elif k == 'entries':
            print('This is entries condition')
            
                
            for i in v:
                for a, b in i.items():
                    

                    
                    if a == 'formats':
                        
                        for d in b:
                            for i,j in d.items():
                                if i == 'format_id':
                                    format_ids.append(j)
                                elif i == 'resolution':
                                    resolution.append(j)
                                elif i == 'acodec':
                                    cod.append(j)
                                elif i == 'filesize_approx':
                                    file_s.append(j)
                                elif i == 'ext':
                                    extension.append(j)
                                elif i == 'tbr':
                                    vbr.append(j)
                                elif i == 'vcodec':
                                    vcodec.append(j)
                                elif i == 'url':
                                    link.append(j)
                                elif i == 'protocol':
                                    protocol.append(j)
                        
                    elif a == 'thumbnail':
                        thumbnail = b
                    elif a == 'duration':
                        duration = b
                        if duration > 3600:
                            duration=round(duration/3600,2)
                            duration = str(duration)+'hr'
                            
                        elif duration > 60:
                            duration = round(duration/60,2)
                            duration = str(duration)+'min'
                            

                        else:
                            duration = round(duration,2)
                            duration=str(duration)+'sec'
                    
                                                    
                    elif a == 'format_id':
                        format_ids.append(b)
                    
                    elif a == 'resolution':
                        resolution.append(b)
                    elif a == 'ext':
                        extension.append(b)
                    elif a == 'filesize':
                        filesize.append(b)
                    elif a == 'acodec':
                        cod.append(b)
                    elif a == 'filesize_approx':
                        file_s.append(b)
                    elif a == 'tbr':
                        vbr.append((b))     
                    elif a == 'vcodec':
                        vcodec.append((b)) 
                    elif a == 'url':
                        link.append(b)
                    elif a == 'protocol':
                        protocol.append(b)  
        
    
    if re.match(regex_youtube, url):
        
        
        value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr)
        
        size=0
        f=[]
        up=[]
        s =len(format_ids)-len(filesize)
        del resolution[0:s] 
        del extension[0:s] 
        del format_ids[0:s]
        del link[0:s] 
    
        
    

        resolution.reverse()
        extension.reverse()
        format_ids.reverse()
        filesize.reverse()
        cod.reverse()
        vbr.reverse()
        link.reverse()

        value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr)
        for i,j in zip(resolution,extension):
            f.append(i+j)



    
        s=len(resolution)
        s1=len(extension)
        s2=len(format_ids)
        s3=len(filesize)
        s4=len(cod)
        s5= len(vbr)
        s6 = len(link)
        

    

        for i,j in enumerate(f):
            
            if j not in up:
                up.append(j)
            else:
                resolution.pop(i-s)
                extension.pop(i-s1)
                format_ids.pop(i-s2)
                filesize.pop(i-s3)
                cod.pop(i-s4)
                vbr.pop(i-s5)
                link.pop(i-s6)
        
        
        
    
        num = filesize.count(None)
        file_s.reverse()
        c=0
    
        for i,j in enumerate(filesize):
        
            if j == None:
                filesize[i]=file_s[-(num-c)]
                c+=1

    
    
        
        value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr,link)
        
        
        return render(request, 'yt_download.html', {"title": title, "dur": duration, 'thumbnail':thumbnail,'val':value})
        
        
        
    
        
    elif re.match(regex_bili,url):
        
        val = itertools.zip_longest(format_ids,resolution,extension,file_s,vbr,vcodec,link)
            
        i=[]
        r=[]
        e=[]
        s=[]
        v=[]
        l=[]
        for ids,res,ext,size,vb,vcd,lin in val:
                            
            
            if ext == 'm4a' and vcd == 'none' and ids != 0:
                
                i.append(ids)
                r.append(res)
                e.append(ext)
                s.append(size)
                v.append(vb)
                l.append(lin)
            elif vcd is not None and vcd[:4] == 'avc1' :
                i.append(ids)
                r.append(res+" Video Only")
                e.append(ext)
                s.append(size)
                v.append(vb)
                l.append(lin)
                

        value = zip(i,r,e,s,v,l)

        


        
        return render(request, 'general.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':value})
        
                    
    elif re.match(regex_vimeo,url):

        format_ids.reverse()
        resolution.reverse()
        extension.reverse()
        vbr.reverse()
        cod.reverse()
        link.reverse()

        
        val = itertools.zip_longest(format_ids,extension,resolution,vbr,cod,link)
        i=[]
    
    
        e=[]
        r=[]
        t=[]
        l=[]
    
    
        for ids,ext,res,tb,co,lin in val:
            
            if 'http' in ids or 'source' in ids:
                i.append(ids)
            
                t.append(tb)
                e.append(ext)
                r.append(res)
                l.append(lin)

        
            
        print('vimeo')
        
        value = itertools.zip_longest(i,r,e,t,l)
        return render(request, 'twitter_dow.html', {"title": title,'dur':duration,'thumbnail':thumbnail ,'val': value})
    elif(re.match(regex_daily_motion, url)):
        r_t=[]

        for i, j in zip(resolution, vbr):
            r_t.append(str(i)+' '+str(j)+'kbps')

        val = zip(format_ids,file_s,extension,r_t,link)
        i=[]
        s=[]
        e=[]
        r=[]
        l=[]
    
        for ids,b,c,d,lin in val:
            
            if ids[:4] == 'http' and ids[-1] == '1':
                i.append(ids)
                s.append(b)
                e.append(c)
                r.append(d)
                l.append(lin)
    
        value=zip(i,s,e,r,l)    
        return render(request, 'dow_size.html', {"title": title,'dur':duration, 'thumbnail': thumbnail,'val':value})
    elif(re.match(regex_VLive, url)):
        val = itertools.zip_longest(format_ids,resolution,extension,vbr,link)
        i=[]
    
        r=[]
        e=[]
        t=[]
        l=[]
        for ids,c,d,tr,lin in val:
        

            if 'avc' in ids:
                i.append(ids)
            
                r.append(c)
                e.append(d)
                t.append(tr)
                l.append(lin)
            
        value = itertools.zip_longest(i,r,e,t,l)
        return render(request, 'twitter_dow.html', {"title": title, 'thumbnail':thumbnail,'dur':duration,'val': value})
    else:
        resolution.reverse()
        extension.reverse()
        link.reverse()
        protocol.reverse()
        
                

        if(all(v is None for v in resolution)):
                

            return render(request,'errors.html')
        else:
            
            r=[]
            e=[]
            l=[]
            
            val = zip(resolution,extension,vbr,link,protocol)
            for res,ext,vb,lin,pro in val:
                if pro == 'https':

                    r.append(res)
                    e.append(ext)
                    l.append(lin)
                else:
                    pass

                    
            val = itertools.zip_longest(r,e,l)

            return render(request, 'general2.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':val})

def submit(request):
    print('I am submit function')
    global url
    


    if url is None:
        print("url is None")
    global audio_id
    audio_id=''
    global title
    global thumbnail
    thumbnail = '#'

    global webpage_urls
    link=[]
    webpage_urls=[]
    duration = ''
    protocol=[]
    format_ids =[]
    filesize =[]
    file_s=[]
    cod=[]
    resolution =[]
    extension =[]
    formats =[]
    vcodec=[]
    vbr=[]
    titles=[]
    vid_ids=[]
    abr=[]
    



    
    
    
    
    
    

                # ''' Regex to match url '''
    regex_youtube = r'^(http(s)?:\/\/)?((w){3}.|m.)?youtu(be|.be)?(\.com)?\/.+'
    # regex_youtube_playlist = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/(playlist)+'
    regex_twitter = r'^(http(s)?:\/\/)?((w){3}.)?twitter?(\.com)?\/.+'
    regex_khan_acdmy = r'^(http(s)?:\/\/)?((w){3}.)?khanacademy?(\.org|.com)?\/.+'
    regex_reddit = r'^(http(s)?:\/\/)?((w){3}.)?reddit?(\.org|.com)?\/.+'
    # veoh,khan_acedmy,reddit
    regex_vimeo = r'^(http(s)?:\/\/)?(((w){3}.)|(player.))?vimeo?(\.com)?\/.+'
    regex_VLive = r'^(http(s)?:\/\/)?((w){3}.|m.)?vlive?(\.tv)?\/.+'
    regex_daily_motion = r'^(http(s)?:\/\/)?((w){3}.)?dailymotion?(\.com)?\/.+'
    regex_SoundCloud = r'^(http(s)?:\/\/)?((w){3}.)?soundcloud?(\.com)?\/.+'
    regex_instagram = r'^(http(s)?:\/\/)?((w){3}.)?instagram?(\.com)?\/.+'
    regex_fb = r'^(http(s)?:\/\/)?((w){3}|m|fb|web)?(.facebook|.watch)?(\.com)?\/.+'
    regex_streamable = r'^(http(s)?:\/\/)?((w){3}.)?streamable?(\.com)?\/.+'
    regex_vk = r'^(http(s)?:\/\/)?((w){3}.)?vk?(\.com)?\/.+'
    regex_tiktok = r'^(http(s)?:\/\/)?((w){3}.)?tiktok?(\.com)?\/.+'
    regex_espn = r'^(http(s)?:\/\/)?((w){3}.)?espn?(\.com)?\/.+'
    regex_cnn = r'^(http(s)?:\/\/)?((w){3}|edition)?(.cnn)?(\.com)?\/.+'
    regex_ok_ru = r'^(http(s)?:\/\/)?((w){3}.|ok.)?ru?(\/video)?\/.+'
    regex_ted = r'^(http(s)?:\/\/)?((w){3}.)?ted?(\.com)?\/.+'
    regex_bili = r'^(http(s)?:\/\/)?((w){3}.)?bilibili?(\.com)?\/.+'

    # if re.match(regex_fb,url):
    #     with youtube_dl.YoutubeDL() as ydl:
    #         meta = ydl.extract_info(url, download=False)
    #         for k, v in meta.items():
    #             if k == 'webpage_url':
    #                 url = v
    
    
    
    
    
    uploader_url = ''
    ids = []
    key=[]
    count = 1
    
    ydl_opts = {
        'playliststart':1,
        'playlistend':2,
        'cachedir': False,
    }
    
        
    url = request.POST.get('url')
    print('this is url',url)
    # url = 'https://youtu.be/TkYEN69cQf0'

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(url, download=False)

    
        

    for k,v in meta.items():
        key.append(k)
        if k == 'playlist_count':
            count = v
    if ('_type' in key and  ("playlist_count" in key and count != 1)):
        # webpage_urls=[]

        print('Now i am in playlist processing')

        
        ydl_opts = {
                
                # 'playliststart':22,
                # 'playlistend':39

            }

        
            
            
        
        for i, j in meta.items():
            
            if i == 'entries':
                
                for a in j:
                    
                    for x, y in a.items():
                        
                        if x == 'title':
                            titles.append(y)
                        

                            
                            
                        elif x == 'webpage_url':
                            # vid_ids=[]
                            
                            webpage_urls.append(y)
                            
                            
                        

        
        # print('webpage url',webpage_urls)
        for i in range(len(webpage_urls)):
            vid_ids.append(i)
            # print(vid_ids)
        
        
        
        values= itertools.zip_longest(vid_ids,titles)
   

    

        return render(request, 'playlist.html',{"values":values})
    


    else:
        print('This is not a playlist')
        # ydl_opts = {}
        # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        #     meta = ydl.extract_info(url, download=False)

        for k, v in meta.items():
            # print(k)
            
            
        
            if k == "duration":
                try:

                    duration = v
                    if duration > 3600:
                        duration=round(duration/3600,2)
                        duration = str(duration)+'hr'
                    elif duration > 60:
                        duration = round(duration/60,2)
                        duration = str(duration)+'min'
                    else:
                        duration=str(duration)+'sec'
                except:
                    duration = 'NaN'
            elif k == 'duration_string':
                duration = v
                if len(duration) <=2:
                    duration = duration+" sec"
                elif len(duration) <=5:
                    duration = duration + " minutes"
                elif len(duration) > 5:
                    duration = duration + " hours"
            elif k == 'title':
            
                title = v
            elif k == 'uploader_url':
                uploader_url=v
            elif k == "thumbnail" and v != 'NaN':
                
        
            
                thumbnail = v
            
            elif k == 'formats':
                print('formats')
                for i in v:
                    for a, b in i.items():
                        if a == 'format_id':
                            format_ids.append(b)
                        elif a == 'format':
                            formats.append(b)
                        elif a == 'resolution':
                            resolution.append(b)
                        elif a == 'ext':
                            extension.append(b)
                        elif a == 'filesize':
                            filesize.append(b)
                        elif a == 'acodec':
                            cod.append(b)
                        elif a == 'filesize_approx':
                            file_s.append(b)
                        elif a == 'tbr':
                            vbr.append((b))
                        elif a == 'uploader_url':
                            uploader_url = b
                        
                        elif a == 'url':
                            link.append(b)
                        elif a == 'abr':
                            abr.append(b)
                        elif a == 'protocol':
                            protocol.append(b)
                     
            elif k == 'entries':
                print("entries")
                
                for i in v:
                    for a, b in i.items():
                        

                        
                        if a == 'formats':
                            print('this is bilibili')
                            for d in b:
                                for i,j in d.items():
                                    if i == 'format_id':
                                        format_ids.append(j)
                                    elif i == 'resolution':
                                        resolution.append(j)
                                    elif i == 'acodec':
                                        cod.append(j)
                                    elif i == 'filesize_approx':
                                        file_s.append(j)
                                    elif i == 'ext':
                                        extension.append(j)
                                    elif i == 'tbr':
                                        vbr.append(j)
                                    elif i == 'vcodec':
                                        vcodec.append(j)
                                    elif i == 'uploader_url':
                                        uploader_url = j
                                    elif i == 'url':
                                        link.append(j)
                                    elif i == 'abr':
                                        abr.append(j)
                                    elif i == 'protocol':
                                        protocol.append(j)
                        elif a == 'webpage_url':
                            uploader_url = b 
                        elif a == 'thumbnail':
                            thumbnail = b
                        elif a == 'duration':
                            duration = b
                            if duration > 3600:
                                duration=round(duration/3600,2)
                                duration = str(duration)+'hr'
                                
                            elif duration > 60:
                                duration = round(duration/60,2)
                                duration = str(duration)+'min'
                                

                            else:
                                duration = round(duration,2)
                                duration=str(duration)+'sec'
                        
                                                        
                        
                        elif a == 'format_id':
                            format_ids.append(b)
                        
                        elif a == 'resolution':
                            resolution.append(b)
                        elif a == 'ext':
                            extension.append(b)
                        elif a == 'filesize':
                            filesize.append(b)
                        elif a == 'acodec':
                            cod.append(b)
                        elif a == 'filesize_approx':
                            file_s.append(b)
                        elif a == 'tbr':
                            vbr.append((b))
                        elif a == 'url':
                            link.append(b)
                        elif a == 'abr':
                            abr.append(b)
                        elif a == 'protocol':
                            protocol.append(b)
                        
                        

        if re.match(regex_fb, url):
            
            
            
            
            value = itertools.zip_longest(format_ids,link)

            
        
            return render(request, 'fb_dow.html', {"title": title, "dur": duration, 'thumbnail':thumbnail,'val':value})

        elif re.match(regex_reddit,url):
            # print(uploader_url)
            if re.match(regex_youtube, uploader_url):
            
                size=0
                f=[]
                up=[]
                s =len(format_ids)-len(filesize)
                del resolution[0:s] 
                del extension[0:s] 
                del format_ids[0:s]
                del link[0:s] 
            
                
            

                resolution.reverse()
                extension.reverse()
                format_ids.reverse()
                filesize.reverse()
                cod.reverse()
                vbr.reverse()
                link.reverse()

                value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr,link)
                for i,j in zip(resolution,extension):
                    f.append(i+j)



            
                s=len(resolution)
                s1=len(extension)
                s2=len(format_ids)
                s3=len(filesize)
                s4=len(cod)
                s5= len(vbr)
                s6=len(link)
                

            

                for i,j in enumerate(f):
                    
                    if j not in up:
                        up.append(j)
                    else:
                        # print(i) 3,6,10,11,12
                        resolution.pop(i-s)
                        extension.pop(i-s1)
                        format_ids.pop(i-s2)
                        filesize.pop(i-s3)
                        cod.pop(i-s4)
                        vbr.pop(i-s5)
                        link.pop(i-s6)
                
                
                
            
                num = filesize.count(None)
                file_s.reverse()
                c=0
            
                for i,j in enumerate(filesize):
                
                    if j == None:
                        filesize[i]=file_s[-(num-c)]
                        c+=1

            
            
                
                value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr,link)
                
               
                
                
                return render(request, 'yt_download.html', {"title": title, "dur": duration, 'thumbnail':thumbnail,'val':value})
            elif re.match(regex_twitter,uploader_url):

                val = itertools.zip_longest(format_ids,resolution,extension,vbr,link)
                i=[]
                r=[]
                e=[]
                t=[]
                l=[]
            
                for ids,c,d,tb,lin in val:
                

                    if 'http' in ids or 'source' in ids:
                        i.append(ids)
                    
                        r.append(c)
                        e.append(d)
                        t.append(tb)
                        l.append(lin)
                    
                    
                value = itertools.zip_longest(i,r,e,t,l)
            
                return render(request, 'twitter_dow.html', {"title": title,'dur':duration,'thumbnail':thumbnail ,'val': value})
            else:
            
        
                
                resolution.reverse()
                extension.reverse()
                file_s.reverse()
                vbr.reverse()
                link.reverse()
                cod.reverse()
                protocol.reverse()


                # l1=len(format_ids)
                # l2=len(resolution)
                # l3=len(extension)
                # l4=len(file_s)
                # l5=len(vbr)
                # l5 = len(link)
            
                
            
                val=itertools.zip_longest(resolution,extension,file_s,vbr,cod,link,protocol)
               

                
            
                i=[]
                r=[]
                e=[]
                t=[]
                s=[]
                l=[]
                for res,ext,size,datarate,cd,lin,pro in val:
                    # print(res,'',ext,'',size,'',lin,'',pro)
                    if pro == 'https' and cd == 'mp4a.40.2':
                        
                        
                        r.append(res)
                        e.append(ext)
                        s.append(size)
                        t.append(datarate)
                        l.append(lin)
                  
                    elif pro == 'https' and cd != 'mp4a.40.2':
                        r.append('No Audio')
                        e.append(ext)
                        s.append(size)
                        t.append(datarate)
                        l.append(lin)

                    # elif  pro == 'https' or cd != 'mp4a.40.2':
                    
                    #     r.append('No Audio')
                    #     e.append(ext)
                    #     s.append(size)
                    #     t.append(datarate)
                    #     l.append(lin)
                
                
                    

                    
            
                value= itertools.zip_longest(i,r,e,s,t,l)

                return render(request, 'general.html', {"title": title, "dur": duration, 'thumbnail':thumbnail,'val':value})

        elif (re.match(regex_youtube, url) or re.match(regex_khan_acdmy, url)):
            
        
            
            size=0
            f=[]
            up=[]
            s =len(format_ids)-len(filesize)
            del resolution[0:s] 
            del extension[0:s] 
            del format_ids[0:s]
            del link[0:s]
        
            
        

            resolution.reverse()
            extension.reverse()
            format_ids.reverse()
            filesize.reverse()
            cod.reverse()
            vbr.reverse()
            link.reverse()

            value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr,link)
            for i,j in zip(resolution,extension):
                f.append(i+j)



        
            s=len(resolution)
            s1=len(extension)
            s2=len(format_ids)
            s3=len(filesize)
            s4=len(cod)
            s5= len(vbr)
            s6= len(link)
            

        

            for i,j in enumerate(f):
                
                if j not in up:
                    up.append(j)
                else:
                    # print(i) 3,6,10,11,12
                    resolution.pop(i-s)
                    extension.pop(i-s1)
                    format_ids.pop(i-s2)
                    filesize.pop(i-s3)
                    cod.pop(i-s4)
                    vbr.pop(i-s5)
                    link.pop(i-s6)
            
            
            
        
            num = filesize.count(None)
            file_s.reverse()
            c=0
        
            for i,j in enumerate(filesize):
            
                if j == None:
                    filesize[i]=file_s[-(num-c)]
                    c+=1

        
        
            for i in link:
                print(i)
            value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr,link)
            
             
            
            return render(request, 'yt_download.html', {"title": title, "dur": duration, 'thumbnail':thumbnail,'val':value})
        
        
            
            
        elif(re.match(regex_twitter, url)):
        
            val = itertools.zip_longest(format_ids,resolution,extension,vbr,link)
            i=[]
        
            r=[]
            e=[]
            t=[]
            l=[]
        
            for ids,c,d,tb,lin in val:
            

                if 'http' in ids or 'source' in ids:
                    i.append(ids)
                
                    r.append(c)
                    e.append(d)
                    t.append(tb)
                    l.append(lin)
                
                
            value = itertools.zip_longest(i,r,e,t,l)
        
            return render(request, 'twitter_dow.html', {"title": title,'dur':duration,'thumbnail':thumbnail ,'val': value})
        elif (re.match(regex_ok_ru,url)):
            if re.match(regex_youtube, uploader_url):
        
                size=0
                f=[]
                up=[]
                s =len(format_ids)-len(filesize)
                del resolution[0:s] 
                del extension[0:s] 
                del format_ids[0:s] 
                del link[0:s]
            
                
            

                resolution.reverse()
                extension.reverse()
                format_ids.reverse()
                filesize.reverse()
                cod.reverse()
                vbr.reverse()
                link.reverse()

                value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr,link)
                for i,j in zip(resolution,extension):
                    f.append(i+j)



            
                s=len(resolution)
                s1=len(extension)
                s2=len(format_ids)
                s3=len(filesize)
                s4=len(cod)
                s5= len(vbr)
                s6= len(link)
                

            

                for i,j in enumerate(f):
                    
                    if j not in up:
                        up.append(j)
                    else:
                        # print(i) 3,6,10,11,12
                        resolution.pop(i-s)
                        extension.pop(i-s1)
                        format_ids.pop(i-s2)
                        filesize.pop(i-s3)
                        cod.pop(i-s4)
                        vbr.pop(i-s5)
                        link.pop(i-s6)
                
                
                
            
                num = filesize.count(None)
                file_s.reverse()
                c=0
            
                for i,j in enumerate(filesize):
                
                    if j == None:
                        filesize[i]=file_s[-(num-c)]
                        c+=1

            
            
                
                value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr,link)
                
                
                
                return render(request, 'yt_download.html', {"title": title, "dur": duration, 'thumbnail':thumbnail,'val':value})
            else:
                index=[]
                for i,j in enumerate(format_ids):
                    if j[:3] != 'mpd' and j[:3] != 'hls':
                        index.append(i)
                for i,j in enumerate(index):
                    file_s.insert(int(j),'NaN')


                val = itertools.zip_longest(format_ids,resolution,extension,file_s,vbr,link)
                i=[]
                s=[]
                r=[]
                e=[]
                t=[]
                l=[]
                for ids,res,ext,size,tb,lin in val:
                
                    if 'mpd' in ids:
                    
                        i.append(ids)
                        s.append(size)
                        r.append(res)
                        e.append(ext)
                        t.append(tb)
                        l.append(lin)

                value = itertools.zip_longest(i,r,e,s,t,l)
                        

                return render(request, 'general.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':value})

        elif (re.match(regex_vimeo,url) or re.match(regex_vimeo,uploader_url)):
        
            
            format_ids.reverse()
            resolution.reverse()
            extension.reverse()
            vbr.reverse()
            cod.reverse()
            link.reverse()

            
            val = itertools.zip_longest(format_ids,extension,resolution,vbr,cod,link)
            i=[]
        
        
            e=[]
            r=[]
            t=[]
            l=[]
        
            for ids,ext,res,tb,co,lin in val:
                
                
                if 'http' in ids or 'source' in ids:
                    i.append(ids)
                
                    t.append(tb)
                    e.append(ext)
                    r.append(res)
                    l.append(lin)

            
                
            # print('vimeo')
            
            value = itertools.zip_longest(i,r,e,t,l)
            return render(request, 'twitter_dow.html', {"title": title,'dur':duration,'thumbnail':thumbnail ,'val': value})
        
        
        elif(re.match(regex_VLive, url)):
            val = itertools.zip_longest(format_ids,resolution,extension,vbr,link)
            i=[]
        
            r=[]
            e=[]
            t=[]
            l=[]
            for ids,c,d,tr,lin in val:
            

                if 'avc' in ids:
                    i.append(ids)
                
                    r.append(c)
                    e.append(d)
                    t.append(tr)
                    l.append(lin)
                
            value = itertools.zip_longest(i,r,e,t,l)
            return render(request, 'twitter_dow.html', {"title": title, 'thumbnail':thumbnail,'dur':duration,'val': value})

        elif(re.match(regex_SoundCloud, url)):
            i=[]
            r=[]
            e=[]
            a=[]
            l=[]
            
           
        
            val = zip(format_ids,resolution,extension,abr,link)
            for ids,res,ext,ab,lin in val:
                if ids[:4] == 'http':
                    i.append(ids)
                    r.append(res)
                    e.append(ext)
                    a.append(ab)
                    l.append(lin)
            value = itertools.zip_longest(i,r,e,a,l)
        

        
            return render(request, 'twitter_dow.html', {"title": title,'thumbnail': thumbnail,'dur':duration,'val':value})

        elif(re.match(regex_daily_motion, url)):
            r_t=[]

            for i, j in zip(resolution, vbr):
                r_t.append(str(i)+' '+str(j)+'kbps')

            val = zip(format_ids,file_s,extension,r_t,link)
            i=[]
            s=[]
            e=[]
            r=[]
            l=[]
        
            for ids,b,c,d,lin in val:
                
                if ids[:4] == 'http' and ids[-1] == '1':
                    i.append(ids)
                    s.append(b)
                    e.append(c)
                    r.append(d)
                    l.append(lin)
        
            value=zip(i,s,e,r,l)    
            return render(request, 'dow_size.html', {"title": title,'dur':duration, 'thumbnail': thumbnail,'val':value})

        elif(re.match(regex_instagram, url)):
            val = itertools.zip_longest(format_ids,resolution,extension,vbr,link)
        

        
            return render(request, 'twitter_dow.html', {"title": title,'thumbnail': thumbnail,'dur':duration,'val':val})

        


        elif (re.match(regex_streamable,url)):
          
            val = itertools.zip_longest(format_ids,resolution,extension,filesize,vbr,link)
            

            
            return render(request, 'general.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':val})
        elif (re.match(regex_vk,url)):
            if re.match(regex_youtube,uploader_url):
                size=0
                f=[]
                up=[]
                s =len(format_ids)-len(filesize)
                del resolution[0:s] 
                del extension[0:s] 
                del format_ids[0:s] 
                del link[0:s]

                


                resolution.reverse()
                extension.reverse()
                format_ids.reverse()
                filesize.reverse()
                cod.reverse()
                vbr.reverse()
                link.reverse()

                value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr,link)
                for i,j in zip(resolution,extension):
                    f.append(i+j)




                s=len(resolution)
                s1=len(extension)
                s2=len(format_ids)
                s3=len(filesize)
                s4=len(cod)
                s5= len(vbr)
                s6=len(link)
                



                for i,j in enumerate(f):
                    
                    if j not in up:
                        up.append(j)
                    else:
                        resolution.pop(i-s)
                        extension.pop(i-s1)
                        format_ids.pop(i-s2)
                        filesize.pop(i-s3)
                        cod.pop(i-s4)
                        vbr.pop(i-s5)
                        link.pop(i-s6)
                
                
                

                num = filesize.count(None)
                file_s.reverse()
                c=0

                for i,j in enumerate(filesize):
                
                    if j == None:
                        filesize[i]=file_s[-(num-c)]
                        c+=1



                
                value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr,link)
                
                file_s=[]
                for s,c in zip(filesize,cod):
                    if c != 'mp4a.40.2':
                        s+=size
                        file_s.append(s)
                    else:
                        file_s.append(s)
                    
                val=itertools.zip_longest(format_ids,resolution,file_s,extension,cod,vbr,link)
                
                return render(request, 'yt_download.html', {"title": title, "dur": duration, 'thumbnail':thumbnail,'val':val})
            else:

                l1=len(format_ids)
                l2=len(file_s)
                l3=len(resolution)
                l4 = len(extension)
                l5 = len(vbr)
                l6=len(link)
                
                i=[]
                s=[]
                e=[]
                r=[]
                t=[] 
                l=[]           
                val = itertools.zip_longest(format_ids,resolution,extension,file_s,vbr,link)
                for ids,res,ext,size,tb,lin in val:
                    if ids[:3] == 'url':
                        # print(size)
                        i.append(ids)
                        r.append(res)
                        e.append(ext)
                        s.append(size)
                        t.append(tb)
                        l.append(lin)
                    
                value = zip(i,r,e,t,l)
                return render(request, 'twitter_dow.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':value})
        elif re.match(regex_espn,url):
            format_ids.reverse()
            resolution.reverse()
            extension.reverse()
            file_s.reverse()
            vbr.reverse()
            link.reverse()

                        

            s=len(file_s)
            print(s)
            s1= len(format_ids)
            print(s1)
            s2=s1-s
            for i in range(s2):
                file_s.append('NaN')
            filesize=['NaN']
            for i,j in enumerate(file_s):
                filesize.append(file_s[i])
            
            
            
            val = zip(format_ids,resolution,extension,filesize,vbr,link)
            i=[]
            s=[]
            e=[]
            r=[]
            tr=[]
            l=[]
        
            for ids,b,c,d,t,lin in val:
                if 'mezzanine' in ids :
                    i.append(ids)
                    r.append("Full HD")
                    e.append(c)
                    s.append('NaN')
                    tr.append(t)
                    l.append(lin)
                
                 

                elif 'http' in ids:
                    i.append(ids)
                    r.append(b)
                    e.append(c)
                    s.append(d)
                    tr.append(t)
                    l.append(lin)
                
            value = zip(i,r,e,s,tr,l)



            return render(request, 'general.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':value})
            
                
        
        
        elif (re.match(regex_tiktok,url)):

            val = zip(format_ids,resolution,extension,filesize,vbr,link)
            i=[]
            s=[]
            e=[]
            r=[]
            tr=[]
            l=[]
        
            for ids,b,c,d,t,lin in val:
            
                if ('download_addr-0' in ids):

                
                    i.append(ids)
                    s.append(b)
                    e.append('Watermarked')
                    r.append(d)
                    tr.append(t)
                    l.append(lin)
                elif ('h264' in ids and ids[-1] == '0'):

                
                    i.append(ids)
                    s.append(b)
                    e.append('No Watermarked')
                    r.append(d)
                    tr.append(t)
                    l.append(lin)

            
            value=zip(i,s,e,r,tr,l)
            return render(request, 'general.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':value})

        elif re.match(regex_ted,url):
            index=[]
            for i,j in enumerate(format_ids):
                if 'hls-audio' in j:
                    index.append(i)
            for i,j in enumerate(index):
                file_s.insert(j,'NaN')
            l=len(index)
            for i in range((l-1)):
                format_ids.pop(i)
                resolution.pop(i)
                extension.pop(i)
                file_s.pop(i)
                vbr.pop(i)
                link.pop(i)
            
            value = itertools.zip_longest(format_ids,resolution,extension,file_s,vbr,link)
            i=[]
            r=[]
            e=[]
            s=[]
            v=[]
            l=[]
            for ids,res,ext,size,vb,lin in value:
                if 'mp4' in lin[-4:]:
                    i.append(ids)
                    r.append(res)
                    e.append(ext)
                    s.append(size)
                    v.append(vb)
                    l.append(lin)
            val = itertools.zip_longest(i,r,e,s,v,l)
        
            return render(request, 'general.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':val})

        elif re.match(regex_cnn,url):
            
            i=[]
            r=[]
            e=[]
            s=[]
            v=[]
            l=[]
            val = zip(format_ids,resolution,extension,file_s,vbr,link)
            for ids,res,ext,size,vb,lin in val:
                if 'mp4' in lin[-4:]:
                    i.append(ids)
                    r.append(res)
                    e.append(ext)
                    s.append(size)
                    v.append(vb)
                    l.append(lin)
            val = itertools.zip_longest(i,r,e,s,v,l)
                    

            return render(request, 'general.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':val})
        elif re.match(regex_bili,url):
            # print(link)
            
            print('this is bilibili video')
            val = itertools.zip_longest(format_ids,resolution,extension,file_s,vbr,vcodec,link)
            
            i=[]
            r=[]
            e=[]
            s=[]
            v=[]
            l=[]
            for ids,res,ext,size,vb,vcd,lin in val:
                             
                
                if ext == 'm4a' and vcd == 'none' and ids != 0:
                    
                    i.append(ids)
                    r.append(res)
                    e.append(ext)
                    s.append(size)
                    v.append(vb)
                    l.append(lin)
                elif vcd is not None and vcd[:4] == 'avc1' :
                    i.append(ids)
                    r.append(res+" Video Only")
                    e.append(ext)
                    s.append(size)
                    v.append(vb)
                    l.append(lin)
                    

            value = zip(i,r,e,s,v,l)

            


            
            return render(request, 'general.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':value})
            
            

        else:
            try:
                print('This is last try block')
                # print('This is uploader url = ',uploader_url)
                if re.match(regex_youtube,uploader_url):
                    # print('this is regex youtube match with uploader url ')
                    f=[]
                    up=[]
                    s =len(format_ids)-len(filesize)
                    del resolution[0:s] 
                    del extension[0:s] 
                    del format_ids[0:s] 
                
                    
                

                    resolution.reverse()
                    extension.reverse()
                    format_ids.reverse()
                    filesize.reverse()
                    cod.reverse()
                    vbr.reverse()

                    value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr)
                    for i,j in zip(resolution,extension):
                        f.append(i+j)



                
                    s=len(resolution)
                    s1=len(extension)
                    s2=len(format_ids)
                    s3=len(filesize)
                    s4=len(cod)
                    s5= len(vbr)
                    

                

                    for i,j in enumerate(f):
                        
                        if j not in up:
                            up.append(j)
                        else:
                            # print(i) 3,6,10,11,12
                            resolution.pop(i-s)
                            extension.pop(i-s1)
                            format_ids.pop(i-s2)
                            filesize.pop(i-s3)
                            cod.pop(i-s4)
                            vbr.pop(i-s5)
                    
                    
                    
                
                    num = filesize.count(None)
                    file_s.reverse()
                    c=0
                
                    for i,j in enumerate(filesize):
                    
                        if j == None:
                            filesize[i]=file_s[-(num-c)]
                            c+=1

                
                
                    
                    value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr)
                    audio_id = ''

        

                    for i,r,s,e,c,t in value:
                        if r == 'audio only' and e == 'm4a':
                            audio_id = i
                            size = int(s)
                            print('This is audio size',size)
            

                    print(audio_id)
                    file_s=[]
                    for s,c in zip(filesize,cod):
                        if c != 'mp4a.40.2':
                            s+=size
                            file_s.append(s)
                        else:
                            file_s.append(s)

                    if(all(v is None for v in resolution)):
                        return render(request,'errors.html') 
                    else: 
                        val=itertools.zip_longest(format_ids,resolution,file_s,extension,cod,vbr)

                        return render(request, 'yt_download.html', {"title": title, "dur": duration, 'thumbnail':thumbnail,'val':val})
                else:
                    print('This is else function of last try block ')
                
            

            
                    l1=len(format_ids)
                    l3=len(resolution)
                    l4 = len(extension)
                    l6 = len(link)
                    l7 = len(protocol)
                
                    
                    
                    
                    if l3 == 0:
                        for i in range(l1):
                            resolution.insert(i,'NaN')
                    elif l4 == 0:
                        for i in range(l1):
                            extension.insert(i,'NaN')
                    elif l7 == 0:
                        for i in range(l1):
                            protocol.insert(i,'NaN')

                   
                    elif l1 != l3:
                        for i in range((l1-l3)):
                            resolution.insert((i),'NaN')
                    elif l1 != l4:
                        for i in range((l1-l4)):
                            extension.insert((i),'NaN')
                    
                    elif l1 != l6:
                        for i in range((l1-l6)):
                            link.insert((i),'NaN')
                    elif l1 != l7:
                        for i in range((l1-l7)):
                            protocol.insert((i),'NaN')

                
                    resolution.reverse()
                    extension.reverse()
                    link.reverse()
                    protocol.reverse()
                   
                            

                    if(all(v is None for v in resolution)):
                         

                        return render(request,'errors.html')
                    else:
                        
                        r=[]
                        e=[]
                        l=[]
                        
                        val = zip(resolution,extension,link,protocol)
                        # lin.endswith('.m3u8') and
                        for res,ext,lin,pro in val:
                            if pro == 'https':

                                r.append(res)
                                e.append(ext)
                                l.append(lin)
                            else:
                                pass

                                
                        val = itertools.zip_longest(r,e,l)
                        # error = yt_dlp.YoutubeDL.trouble

                        return render(request, 'general2.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':val})

            except:
                print("this is duration",len(duration))
                print('This is last except block')
                e=[]
                l=[]
                val = zip(extension,link,protocol)
                for ext,lin,pro in val:
                    if pro == 'https':
                        e.append(ext)
                        l.append(lin)
                    else:
                        pass

                val = itertools.zip_longest(e,l)
                
                return render(request, 'cat3.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':val})
        




def error_404(request, exception):
    print('This is 404 error')
    
    return render(request,'errors.html')
    
def error_500(request):
    print('This is 500 error')

    return render(request,'errors.html')
    

def error_403(request,exception):
    print('This is 403 error')

    return render(request,'errors.html')
    
    

def error_400(request,exception):
    print('This is 400 error')

    return render(request,'errors.html')
    







