#####librairies#####

import socket

###contact me###

follow = """
{+}-- https://www.instagram.com/mktr_blk
         """

####yeah####

print("-"*59)

#####logo#####

print(' _____   _____   _     _   _____   __   _ ')
print('/  ___/ | ____| | |   / / | ____| |  \ | |')
print('| |___  | |__   | |  / /  | |__   |   \| |')
print('\___  \ |  __|  | | / /   |  __|  | |\   |')
print(' ___| | | |___  | |/ /    | |___  | | \  |')
print('/_____/ |_____| |___/     |_____| |_|  \_|','by omar salah')

#####yeah#####

print("-"*59)

####script####

def main():
    remote_host = input('Enter The Target :')

    remote_ip = socket.gethostbyname(remote_host)

    try:

        print("IP Address Of " + remote_host + " is " + remote_ip)




    except socket.error as e:
        print("Error" , e)




if __name__ == "__main__":
    main()
