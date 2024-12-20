import subprocess

def get_device():
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    lines = result.stdout.split('\n')
    for line in lines:
        if line.endswith('device'):
            return line.split('\t')[0]
    raise Exception('No device found')

DeviceName = get_device()