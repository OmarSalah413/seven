#####librairies#####

import socket

#####logo#####

print(' _____   _____   _     _   _____   __   _ ')
print('/  ___/ | ____| | |   / / | ____| |  \ | |')
print('| |___  | |__   | |  / /  | |__   |   \| |')
print('\___  \ |  __|  | | / /   |  __|  | |\   |')
print(' ___| | | |___  | |/ /    | |___  | | \  |')
print('/_____/ |_____| |___/     |_____| |_|  \_| 7 by omar salah')

#####yeah#####

print("-"*42)

####script####

def main():
    remote_host = input('the target please :')

    try:
        print("IP Address Of " + remote_host + " is " + socket.gethostbyname(remote_host))

    except socket.error as e:
        print("Error " , e)




if __name__ == "__main__":
    main()
