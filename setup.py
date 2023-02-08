#!/bin/python
import requests as rqs
from tqdm import tqdm
import os
from time import sleep as wait
from zipfile import ZipFile
import webbrowser as wb
from bs4 import BeautifulSoup


def setup():
    os.system('clear')
    print(
"""\033[1;37m
╦ ╦╔╦╗╔═╗  ╔═╗┌─┐┌┬┐┬ ┬┌─┐
╚╦╝ ║ ║╣───╚═╗├┤  │ │ │├─┘
 ╩  ╩ ╚═╝  ╚═╝└─┘ ┴ └─┘┴  
""") 
    i = input('\033[1;33mAre U Sure to Procced Youtube Video Enhancer Installation , \033[1;32my\033[1;31m/\033[1;32mn\033[1;37m [0 for return main menu] \033[1;32m')
    if i == 'y':
        print('\n\033[1;33mStarting Installation process\nPlease Wait\033[1;34m')
        wait(3)
        path = os.getcwd()
        zip_path = path+"/YTE.zip"
        folder_path = path+"/YTE"
        if os.path.exists(zip_path):
            os.system(f'sudo rm -rf {zip_path}')
        if os.path.exists(folder_path):
            os.system(f'sudo rm -rf {folder_path}')
        if os.path.exists('/usr/bin/YTE'):
            os.system('sudo rm -rf /usr/bin/YTE')
        if os.path.exists('/usr/lib/YTE'):
            os.system('sudo rm -rf /usr/lib/YTE')
        S_url = "https://www.mediafire.com/file/iz7avqc2xydopmz/YTE.zip/file"
        try:
            headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
            print('\033[1;31mGetting Latest source url\n\033[1;34m')
            s_res = rqs.get(S_url,headers=headers)
            soup = BeautifulSoup(s_res.text,'html.parser')
            su = soup.find('a',href=True,attrs={'class':'input popsok'})
            url = su['href']
        except Exception as e:
            print(e)
            print('\033[1;31mError occured while collecting source url\nPlease Try again later')
            exit()
        sh = '#!/bin/bash\n/usr/lib/YTE/main'
        res =rqs.get(url,stream=True)
        total = int(res.headers.get('content-length',0))
        with open('YTE.zip','wb') as file ,tqdm(
            desc='YTE.zip',
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024
        ) as bar :
            for data in res.iter_content(chunk_size=1024):
                size = file.write(data)
                bar.update(size)
        
        if os.path.exists(zip_path):
            print('\033[1;32m SuccessFully Downloaded Requiremensts\n') 

            with ZipFile(zip_path,'r') as zip :
                zip.printdir()
                zip.extractall()
        if os.path.exists(folder_path):
            print('\033[1;33m Requirements Succesfully Extracted\n\033[1;31m')
            os.system('sudo mv YTE /usr/lib/')
        os.system('sudo chmod 777 /usr/lib/YTE/*')
        if os.path.exists(folder_path):
            if os.path.exists('/usr/lib/YTE'):
                os.system(f'sudo rm -rf {folder_path}')
        with open('YTE','w') as s:
            s.writelines(sh)

        os.system('sudo mv YTE /usr/bin/')
        os.system('chmod 777 /usr/bin/YTE')
        os.remove(zip_path)
        print('\033[1;34msetup Finished\n')
        wait(3)
        try:
            
            print('\033[1;33mSupport :-')
            print('\033[1;32mGITHUB   : https://github.com/codingwithdevil')
            print('\033[1;31mYoutube  : https://www.youtube.com/c/codingwithdevil')
            print('\033[1;34mTelegram : https://t.me/CodingWithDevil')
            print('\033[1;34mTelegram : https://t.me/Codingwithdevil_group_chat')
            wb.open('https://github.com/codingwithdevil')
            wb.open('https://www.youtube.com/c/codingwithdevil')
            wb.open('https://t.me/Codingwithdevil_group_chat')
            wb.open('https://t.me/CodingWithDevil')
        except Exception:
            print('\033[1;33mSupport :-')
            print('\033[1;32mGITHUB   : https://github.com/codingwithdevil')
            print('\033[1;31mYoutube  : https://www.youtube.com/c/codingwithdevil')
            print('\033[1;34mTelegram : https://t.me/CodingWithDevil')
            print('\033[1;34mTelegram : https://t.me/Codingwithdevil_group_chat')
    else:
        wait(2)
        print('\n\n\033[1;31mReturning To Main Menu....')
        wait(4)
        main()
def uninstall():
    try:
        os.system('clear')
        print(
"""\033[1;37m
╦ ╦╔╦╗╔═╗  ╔═╗┌─┐┌┬┐┬ ┬┌─┐
╚╦╝ ║ ║╣───╚═╗├┤  │ │ │├─┘
 ╩  ╩ ╚═╝  ╚═╝└─┘ ┴ └─┘┴  
""")    
        i = input('\033[1;33m Are U Sure to Delete YTE, \033[1;32my\033[1;31m/\033[1;32mn\033[1;37m [0 for return main menu] \033[1;32m')
        if i == 'y':
            if os.path.exists('/usr/bin/YTE'):
                os.system('sudo rm -rf /usr/bin/YTE')
            if os.path.exists('/usr/lib/YTE'):
                os.system('sudo rm -rf /usr/lib/YTE')
            print('\033[1;32m Uninstalled SuccessFully\n')
            try:
            
                print('\033[1;33mSupport :-')
                print('\033[1;32mGITHUB   : https://github.com/codingwithdevil')
                print('\033[1;31mYoutube  : https://www.youtube.com/c/codingwithdevil')
                print('\033[1;34mTelegram : https://t.me/CodingWithDevil')
                print('\033[1;34mTelegram : https://t.me/Codingwithdevil_group_chat')
                wb.open('https://github.com/codingwithdevil')
                wb.open('https://www.youtube.com/c/codingwithdevil')
                wb.open('https://t.me/Codingwithdevil_group_chat')
                wb.open('https://t.me/CodingWithDevil')
                wait(10)
                main()

                
            except Exception:
                print('\033[1;33mSupport :-')
                print('\033[1;32mGITHUB   : https://github.com/codingwithdevil')
                print('\033[1;31mYoutube  : https://www.youtube.com/c/codingwithdevil')
                print('\033[1;34mTelegram : https://t.me/CodingWithDevil')
                print('\033[1;34mTelegram : https://t.me/Codingwithdevil_group_chat')
                wait(10)
                main()
        elif i == 'n':
            print('\033[1;37mCanceling Uninstallation...\n')
            wait(2)
            exit()
        elif i == "0":
            main()
        else:
            uninstall()

    except Exception as err:
        print(err)
        print('\033[1;31mUnknown error occured Please Run as root and try again')
def abt():
    wb.open('')

def main():
    os.system('clear')
    print("""\033[1;37m
                                                                           V1.0

██╗   ██╗████████╗███████╗    ███████╗███████╗████████╗██╗   ██╗██████╗ 
╚██╗ ██╔╝╚══██╔══╝██╔════╝    ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
 ╚████╔╝    ██║   █████╗█████╗███████╗█████╗     ██║   ██║   ██║██████╔╝
  ╚██╔╝     ██║   ██╔══╝╚════╝╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ 
   ██║      ██║   ███████╗    ███████║███████╗   ██║   ╚██████╔╝██║     
   ╚═╝      ╚═╝   ╚══════╝    ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     
                                                Coded By DEVIL
    """)
    i = input("\033[1;35mPlease select Option:\n\n      \033[1;32m  1,\033[1;35mInstaller\n\n        \033[1;32m2,\033[1;35mUninstaller\n\n        \033[1;32m3,\033[1;35mAbout\n\n        \033[1;32m4,\033[1;35mExit\n\n\033[1;33mOption:\033[1;36m ")
    if i =='1':
        wait(3)
        setup()
    elif i == '2':
        wait(3)
        uninstall()
    elif i =='3':
        wait(3)
        os.system('open https://github.com/codingwithdevil/Youtube-video-Enhancer.git')
        wait(5)
        main()
    elif i =='4':
        print('\n\033[1;31mExiting ....')
        wait(3)
        os.system('clear')
        exit()

    else:
        print('\033[1;31mPlease chosese a valid Option ')
        wait(3)
        os.system('clear')
        main()
if __name__ == "__main__":

    main()
    