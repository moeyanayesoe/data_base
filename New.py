#pylint:disable=E0602
#pylint:disable=W0104
#----------import------------#
import os
#----------colour------------#
G="\x1b[38;5;46m";W="\x1b[38;5;15m";R="\x1b[38;5;160m";B="\033[1;90m";Y="\033[1;33m";T="\033[1;34m";P="\x1b[38;5;205m"
#----------style--------------#
nx=f"{R}<{W}={R}>{G}";nx1=f"{R}<{W}1{R}>{G}";nx2=f"{R}<{W}2{R}>{G}";nx3=f"{R}<{W}3{R}>{G}";nx4=f"{R}<{W}4{R}>{G}";nx5=f"{R}<{W}5{R}>{G}";nx6=f"{R}<{W}6{R}>{G}";nx0=f"{R}<{W}0{R}>{G}";nxx=f"{R}<{W}?{R}>{G}";nxxx=f"{R}:{G}"
#----------logo--------------#
logo= f"""
{B}.88b  d88.  .d88b.  d88888b db    db  .d8b.  d8b   db
{B}88'YbdP`88 .8P  Y8. 88'     `8b  d8' d8' `8b 888o  88
{R}88  88  88 88    88 88ooooo  `8bd8'  88ooo88 88V8o 88
{R}88  88  88 88    88 88~~~~~    88    88~~~88 88 V8o88
{B}88  88  88 `8b  d8' 88.        88    88   88 88  V888
{B}YP  YP  YP  `Y88P'  Y88888P    YP    YP   YP VP   V8P    
{W}──────────────────────────────────────────────────
{nx} OWNER    {nxxx} MOE HTET YAN
{nx} FACEBOOK {nxxx} AINSLEY{R}[{T}GOTTEE{R}]
{nx} TOOLTYPE {nxxx} FILE{R}[{T}ALL-COUNTRY{R}]{G}CLONE
{nx} STATUS   {nxxx} PAID
{nx} Teligerm {nxxx} https://t.me/MinkoGyi4
{W}──────────────────────────────────────────────────"""
#----------clear--------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{W}──────────────────────────────────────────────────')
#---------menu------------#
def AINSLEY():
    clear()
    print(f"{nx1} START FILE CLONE ")
    print(f"{nx2} CONTACT TOOL OWNER")
    print(f"{nx0} EXIT CLONING")
    linex()
    option=input(f"{nxx} SELECT {nxxx} ")
    if option in ['1']:
        file()
    elif option in ['2']:
        os.system('xdg-open https://www.facebook.com/moe.htet.yan.124755?mibextid=ZbWKwL');AINSLEY()
    elif option in ['0']:
        exit(f"{R}[{T} THANKS FOR USE BYE BYE{R} ] ")
    else:
        linex()
        print(f'{nx} OPTION NOT FOUND ')
        linex()
        time.sleep(1)
        print(f"{nx} TRY AGAIN")
        time.sleep(1)
    
#----------File Clone---------#
#---------Randon------------#
#---------METHOD-----------#
#---------END-------------#
AINSLEY ()
