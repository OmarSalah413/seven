#####librairies#####

import socket

###contact me###

follow = """
{+}-- https://www.instagram.com/mktr_blk
         """

####yeah####

print("-"*59)

#####logo#####

                                                       
                                                       
print('           .         ,;                  ,; L.            ')
print('          ;W       f#i                 f#i  EW:        ,ft')
print('         f#E     .E#t                .E#t   E##;       t#E')
print('       .E#f     i#W,    t      .DD.  i#W,   E###t      t#E')
print('      iWW;     L#D.     EK:   ,WK.  L#D.    E#fE#f     t#E')
print('     L##Lffi :K#Wfff;   E#t  i#D  :K#Wfff;  E#t D#G    t#E')
print('    tLLG##L  i##WLLLLt  E#t j#f   i##WLLLLt E#t  f#E.  t#E')
print('      ,W#i    .E#L      E#tL#i     .E#L     E#t   t#K: t#E')
print('     j#E.       f#E:    E#WW,        f#E:   E#t    ;#W,t#E')
print('   .D#j          ,WW;   E#K:          ,WW;  E#t     :K#D#E')
print('  ,WK,            .D#;  ED.            .D#; E#t      .E##E')
print('  EG.               tt  t                tt ..         G#E')
print('  F.                                                    fE')
print('  ,                                                      ,')

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