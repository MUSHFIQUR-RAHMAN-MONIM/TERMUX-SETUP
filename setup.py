# ASSALAMUALAYKUM IT'S ME MONIM 😉 #
# THIS SCRIPT WRITTEN BY MONIM #
#━━━━━━━━━━━━IMPORT━━━━━━━━━━━━#
import os,sys,time
try:
    import rich
except:
    (" pip install rich ")
    import rich
from rich import print
from rich.panel import Panel
#━━━━━━━━━━━━LOGO━━━━━━━━━━━━#
logo = """╔═╗╔═╗╔╦╗  ╦ ╦╔═╗
╚═╗║╣  ║───║ ║╠═╝
╚═╝╚═╝ ╩   ╚═╝╩  """
#━━━━━━━━━━━━MAIN-DEF━━━━━━━━━━━━#
def main():
    os.system("clear")
    print(Panel.fit(logo))
    print(Panel.fit("DEVELOPER  : MUSHFIQUR RAHMAN MONIM\nGITHUB     : MUSHFIQUR RAHMAN MONIM\nTOOLS TYPE : TERMUX SETUP"))
    print(Panel.fit("[1] NORMAL SETUP\n[2] FULL SETUP "))
    option =input("└──> CHOICE YOUR OPTION :")
    if option in ["1","a","A"]:
        normal()
    elif option in ["2","b","B"]:
        full()
def normal():
#    os.system("termux-setup-storage");time.sleep(2)
    os.system("""
    pkg update -y && pkg upgrade -y
    pkg install python -y
    pkg install python-pip
    pip install --upgrade pip
    pkg install python2
    pkg upgrade -y
    pkg install git -y
    pkg install bash -y
    pkg install php -y
    pkg inatall curl -y
    pkg install nano -y
    pkg install git -y
    pkg Install bs4 -y
    pkg Install rdf - y
    pkg Install chr -y
    pkg Install http -y
    pkg install sudo -y
    pkg install tsu -y
    pip2 install mechanize 
    pip install mechanize requests 
    pip3 install -U pyrogram 
    pip install rich 
    pip install requests 
    pip2 install requests 
    pip install mechanize 
    pip2 install mechanize   
    pip install lolcat 
    pip install bs4 
    pip2 install bs4
    pip install futures
    pip2 install futures
    pip install sys
    pip2 install sys
    pip install so""");print(Panel.fit("[bold green]NORMAL SETUP COMPLETE"))
def full():
    os.system("termux-setup-storage");time.sleep(2)
    os.system("""
    pkg update
    pkg upgrade
    pkg install python
    pkg install python2
    pkg install python3
    pkg install python-pip
    pkg install wget
    pkg install fish
    pkg install ruby
    pkg install help
    pkg install git
    pkg install dnsutils  
    pkg install php
    pkg install perl
    pkg install lua
    pkg install parallel
    pkg install nmap
    pkg install bash
    pkg install clang
    pkg install nano
    pkg install w3m
    pkg install hydra
    pkg install figlet
    pkg install cowsay
    pkg install curl
    pkg install tar
    pkg install zip
    pkg install unzip
    pkg install net-tools
    pkg install tor -y
    pkg install sudo -y
    pkg install wireshark
    pkg install wgetrc
    pkg install wcalc
    pkg install openssl
    pkg install openssl-tool
    pkg install bmon
    pkg install vpn
    pkg install unrar
    pkg install toilet
    pkg install proot
    pkg install net-tools
    pkg install vim
    pkg install vim-python
    pkg install ired
    pkg install goaccess
    pkg install golang
    pkg install tar
    pkg install kibi
    pkg install tsu
    pkg install tmux
    pkg install mtools
    pkg install file
    pkg install vis
    pkg install pass
    pkg install pick
    pkg install chroot
    termux-chroot
    pkg install macchanger
    pkg install ninja
    pkg install elixir
    pkg install swift
    pkg install xmlstarlet
    pkg install fakeroot
    pkg install texinfo
    pkg install netcat
    pkg install wren
    pkg install gatling
    pkg install cvs
    pkg install ffmpeg
    pkg install screen 
    pkg install neofetch 
    pkg install mariadb
    pkg install picolisp
    pkg install toilet
    pkg install cmatrix
    pkg install dropbear
    pkg install openssh
    pkg install python-pip
    pip2 install wget
    pip install bs4
    pip2 install bs4
    pip install requests
    pip2 install requests
    pip install mechanize
    pip2 install mechanize
    pip install php
    pip2 install php""");print(Panel.fit("[bold green]FULL SETUP COMPLETE "))
main()