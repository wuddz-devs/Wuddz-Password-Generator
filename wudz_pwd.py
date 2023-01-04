"""
 [*]WUDDZ PASSWORD GENERATOR
 
    Info:
        Coder:     Wuddz_Devs                                                                                 
        Email:     wuddz_devs@protonmail.com                                                                  
        Github:    https://github.com/wuddz-devs                                                              
        Reddit:    https://reddit.com/users/wuddz-devs                                                        
        Twitter:   https://twitter.com/wuddz_devs                                                             
        Telegram:  https://t.me/wuddz_devs                                                                    
        Videos:    https://mega.nz/folder/IWVAXTqS#FoZAje2NukIcIrEXXKTo0w                                     
        Youtube:   https://youtube.com/@wuddz-devs
    
    Password Types:
        d = Digits
        s = Special Characters
        l = Upper & Lower Case Letters
    
    Usage:
        python wudz_pwd passwordlength passwordtype  (Default Password Type = Letters+Digits)
        
    Examples
        python wudz_pwd           =>    Prints Help Document
        python wudz_pwd 24        =>    Generates A 24 Character Password Consisting Of Letters+Digits
        python wudz_pwd 40 d      =>    Generates A 40 Character Password Consisting Of Digits
        python wudz_pwd 32 ls     =>    Generates A 32 Character Password Consisting Of Letters+Special Characters
        python wudz_pwd 18 lds    =>    Generates A 18 Character Password Consisting Of Letters+Digits+Special Characters
"""

import secrets, sys, platform
from os import system
system('')

def clear_screen(name,c=None):
    if c is None:input('\n\033[1;32;40m...Hit Enter|Return Key To Clear Screen....\033[0m\n') or None
    if name=='Linux':system('clear')
    elif name=='Windows':system('cls')
    elif name=='Darwin':system("printf '\\33c\\e[3J'")

def wudz_pwd():
    name=platform.system()
    clear_screen(name,'c')
    d='0123456789'
    s='!#$%&()*+,-.:;<=>?@[]^_`{|}~'
    l='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if len(sys.argv)==1:print(f'\033[1;32;40m{__doc__}\033[0m')
    else:
        try:
            pl=int(sys.argv[1])
            pwc=''
            pt='ld'
            if len(sys.argv)>2:pt=sys.argv[2]
            for p in list(pt):
                pwc+=eval(p)
            print("\n\033[1;32;40mPassword => \033[0m"+''.join(secrets.choice(pwc.strip()) for i in range(pl)))
        except:
            print(f'\033[1;32;40m{__doc__}\033[0m')
            return
        clear_screen(name)
wudz_pwd()
