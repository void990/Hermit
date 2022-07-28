import os, sys
from rich.console import Console
import update
import banner

console = Console()

banner={}

def functions():
     menu = console.input(
      "[bold white]choose number: "
       )
     if menu == "1":
        console.print(
        "[bold red][ wait ] ubuntu setting..."
         )
        os.system("cd .. && git clone https://github.com/MFDGaming/ubuntu-in-termux")
        console.print(
        "[bold green][ + ] Installation completed\n[ √ ] tool saved in $HOME"
         )
     elif menu == "6":
          delete = str(console.input("[bold white]instrument name: "))
          os.system(f"rm -rf {delete}")
          console.print(f"[bold red][ — ] Instrument delete : [bold white]{delete}")

     elif menu == "5":
          console.print("[bold red][ wait ] Termux Arch setting...")
          os.system("cd .. && git clone https://github.com/sdrausty/TermuxArch")
          console.print("[bold green][ + ] Installation completed\n[ √ ] tool saved in $HOME")

     elif menu == "3":
          console.print("[bold red][ wait ] Debian on Termux setting...")
          os.system("cd .. && git clone https://github.com/sp4rkie/debian-on-termux")
          console.print("[bold green][ + ] Installation completed\n[ √ ] tool saved in $HOME")

     elif menu == "4":
          console.print("[bold red][ wait ] Termux Kali setting...")
          os.system("cd .. && git clone https://github.com/MasterDevX/Termux-Kali")
          console.print("[bold green][ + ] Installation completed\n[ √ ] tool saved in $HOME")

     elif menu == "2":
          console.print("[bold red][ wait ] Nethunter in Termux setting...")
          os.system("cd .. && git clone https://github.com/Hax4us/Nethunter-In-Termux")
          console.print("[bold green][ + ] Installation completed\n[ √ ] tool saved in $HOME")

     elif menu == "7":
          print("bye!")
          sys.exit()
          

functions()
