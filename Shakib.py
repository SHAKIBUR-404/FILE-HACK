import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support this Tools \n \n \033[1;31mFOLLOW MY GITHUB")
    os.system('xdg-open https://github.com/Shakibur-Cyber-King');time.sleep(2)
    from PRO import main_apv
    main_apv()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
