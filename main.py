import platform
import cpuinfo
import psutil

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

system_info()
hardware_info()
    





