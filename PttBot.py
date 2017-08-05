import telnetlib
import time

telnet = telnetlib.Telnet('ptt.cc')

def sleep():
    time.sleep(0.5)

def read():
    telnet.write("\u000c".encode("ascii"))
    sleep()
    content = telnet.read_very_eager().decode('big5','ignore')
    return content

def functionKey(key):
    if(key == 'left'):
        telnet.write("\u001b[D".encode("ascii"))
    elif(key == 'right'):
        telnet.write("\u001b[C".encode("ascii"))
    elif(key == 'end'):
        telnet.write("\u001b[F".encode("ascii"))
    elif(key == 'enter'):
        telnet.write("\r\n".encode("ascii"))
    sleep()
        
def write(string):
    telnet.write(string.encode("big5"))
    sleep()
    

def login(acc, pw):
    write(acc + "\r\n")
    write(pw + "\r\n")
    if "密碼不對" in read():
        return False

    while "按任意鍵繼續" in read():
        functionKey("enter")
    
    if "您想刪除其他重複登入的連線嗎" in read():
        write("y\r\n") 
        
    if "您要刪除以上錯誤嘗試的記錄嗎" in read():
        write("y\r\n")
    
    return True

def logout():
    while("主功能表" not in read()):
        functionKey("left")
    functionKey("end")
    functionKey("right")
    write("y\r\n")
