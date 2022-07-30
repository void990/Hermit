from rich.console import Console
import rich
import os, sys

console = Console()

update = console.input(
"[bold white]Update Tool? |y/n|: "
)

if update == "y":
   console.print("[bold yellow][ Update in progress... ]")
   os.system("git pull")
   console.print("[bold green][ + ] You now have the latest version")

