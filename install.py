import os, sys

print('[ + ] update packets\n')
os.system('pkg update -y && pkg upgrade -y')

print('[ + ] install console\n')
os.system('pip3 install console')
