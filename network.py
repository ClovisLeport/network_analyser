import subprocess

class Network:
    
    def __init__(self):
        self.ip,self.mask=self.wlan_ip()

    def wlan_ip(self):
        result=subprocess.run('ipconfig',stdout=subprocess.PIPE,text=True).stdout.lower()
        scan=0
        ip=None
        mask=None
        for i in result.split('\n'):
            if 'wi-fi' in i: scan=1
            if scan:
                if 'passerelle par d' in i: ip= i.split(':')[1].strip()
                if 'masque de sous' in i: mask= i.split(':')[1].strip()
        
        mask=mask.split(".")
        number_of_bits=0
        for i in mask:
            number_of_bits+= bin(int(i)).count("1")
        return ip,number_of_bits