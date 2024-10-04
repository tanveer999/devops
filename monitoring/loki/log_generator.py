import time
from datetime import datetime

def generate_log():
    
    with open('/var/log/custom_python.log', 'w') as logfile:
        count = 0
        while True:
            count = 0
            while count < 400:
                logfile.write(f'f{datetime.now()} - custom log - {count} \n')
                count += 1
            # logfile.write(f'f{datetime.now()} - custom log - {count} \n')
            # count += 1
            print('Sleep 1s')
            time.sleep(1)


if __name__ == '__main__':
    generate_log()