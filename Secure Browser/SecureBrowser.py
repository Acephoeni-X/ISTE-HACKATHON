import test
import os
import tkinter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def tor():
    desktop = os.path.join(os.environ['HOMEPATH'], 'DESKTOP')
    onion = os.popen(r'C:{d}\Tor Browser\Browser\TorBrowser\Tor\tor.exe'.format(d = desktop))
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('excludeSwitches', ['enable-automation'])
    opt.add_experimental_option('useAutomationExtension', False)
    opt.add_argument("--proxy-server=socks5://127.0.0.1:9050")
    opt.add_argument("--incognito")
    opt.add_argument("--silent")
    opt.add_argument('--disable-blink-features=AutomationControlled')
    opt.add_argument('--log-level=OFF')
    global driver
    driver = webdriver.Chrome(service_log_path = 'NUL', options = opt,executable_path = 'chromedriver.exe')
    driver.maximize_window()
    driver.get('http://www.duckduckgo.com')
    driver.execute_script('alert("This browser is fully tor routed with built in VPN for extreme security!")')

def new_tab():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get('http://www.duckduckgo.com')

if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry("300x400")
    root.title('Anony Browser')
    root.configure(bg='#424543')
    text = tkinter.Label(root, text = "Want To Go UnderGround ?", font = ("Helvetica",15,"bold"), bg='#424543', fg='white')
    text.place(x=60, y=50)
    startTor = tkinter.Button(root, text ="Start Tor", command = tor, bg='#424543',fg='white')
    startTor.place(x=100, y=150)
    newTab = tkinter.Button(root, text ="New Tab", command = new_tab, bg='#424543',fg='white')
    newTab.place(x=100, y=300)
    root.resizable(False, False)
    root.mainloop()
