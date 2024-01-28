import platform
import cpuinfo
import psutil
from time import sleep

def system_info():
    print('OS INFO'.center(32))
    print('='*32)
    print(f'System: {platform.system()} {platform.release()} {platform.win32_edition()}')
    print(f'Version: {platform.version()}')
    print(f'Type: {platform.architecture()[0]}')

def hardware_info():
    print('HARDWARE INFO'.center(32))
    print('='*32)
    print(f'Procesor: {cpuinfo.get_cpu_info()['brand_raw']} {cpuinfo.get_cpu_info()['hz_advertised'][0] / 1000 / 1000 / 1000} GHz')
    print(f'Cores: {psutil.cpu_count()}')
    print(f'Memory: {psutil.virtual_memory().total // 1024 // 1024 // 1024}')

def usage_monitor(cpu_usage, memory_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '▮' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    memory_percent = (memory_usage / 100.0)
    memory_bar = '▮' * int(memory_percent * bars) + '-' * (bars - int(memory_percent * bars))
    print(f'\rCPU usage: |{cpu_bar}| {cpu_usage:.2f}%  ', end=' ')
    print(f'Memory usage: |{memory_bar}| {memory_usage:.2f}%  ', end='\r')

system_info()
hardware_info()
while True:
    usage_monitor(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    sleep(0.5)
    