#import
import hashlib
import itertools
print('''
 
 _____________________________________________
|                                             |
|---------------------------------------------|
|                                             |
|- CI510 Security and Dependablity            |
|- Password Cracking Assignment               |
|                                             |
|===[[[[[[[]]]]]]]===||-||===[[[[[[[]]]]]]]===|
|                                             |
|- Enter "1" for Dictionary Attack!           |
|- Enter "2" for Brute Force Attack!          |
|                                             |
|---------------------------------------------|
|_____________________________________________|
''')
option = input("[*] Please enter choice of attack: ")
option = int(option)
if option == 1:
    print('''
[*] Loading Dictionary Attack...
[*] Please wait...
''')
    hlist = input("[*] Please enter hashlist txt file: ")
    print("[*] Loading and reading hashlist...")
    try:
            hfile = open(hlist, 'r')
            hlistread = hfile.read()
            hfile.close()
            hdictionary = hlistread.split()
            hdictionary_length = len(hdictionary)
            print(f"[*] {hdictionary_length} : Hashes have been loaded")
    except:
            print('''
[*] Error hashList file not found
[*] Please check file spelling and location
    ''')
            exit()
            
    wlist = input("[*] Please enter wordlist txt file: ")
    print("[*] Loading and reading wordlist...")
    try:
            wlistlines = open(wlist, 'r').readlines()
    except:
            print('''
[*] Error wordlist file not found
[*] Please check file spelling and location
    ''')
            exit()
    cracked_count = int(0)
    print("[*] Comparing hashlist to wordlist...")
    for i in range(0, len(wlistlines)):
            wlisthash = hashlib.md5(wlistlines[i].replace("\n","").encode()).hexdigest()
            if wlisthash in hdictionary:
                    cracked_count += 1
                    print("[*] Hash cracked: "+wlisthash,"| Password: "+wlistlines[i].replace("\n",""))
                    print(f"[*] {cracked_count} out of {hdictionary_length} cracked!")
    print("[*] All inputted hashes have been checked against inputted wordlist!")
    if cracked_count == 0:
        print("[*] Could Not Crack Any Hash Values Given!")
        exit()
    elif cracked_count != hdictionary_length:
        print(f"[*] Could only crack: {cracked_count} out of: {hdictionary_length} hashes given")
        exit()
    elif cracked_count == hdictionary_length:
        print("[*] All inputted hashes have been cracked")
        exit()
        
elif option == 2:
    print('''
[*] Loading Brute Force Attack...
[*] Please wait...
''')
    whole_char_set = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' #Set the character chart
    password_length = 1 #Initial password length, start at 1 and work our way up
    hlist = input("[*] Please enter hashlist txt file: ")
    print("[*] Loading and reading hashlist...")
    try:
        hfile = open(hlist, 'r')
        hlistread = hfile.read()
        hfile.close()
        hdictionary = hlistread.split()
        hdictionary_length = len(hdictionary)
        print(f"[*] {hdictionary_length} : Hashes have been loaded")
    except:
            print('''
[*] Error hash list file not found
[*] Please check file spelling and location
''')
            exit()
    print('''
[*] Starting brute force attack...
[*] Please wait as this may take a while depending on computing power...
''')
    cracked_count = int(0)
    while True: # loop through the possible characters of the current password length
        for char_set in itertools.product(whole_char_set, repeat = password_length):
            password = ''.join(char_set)
            h = hashlib.md5(password.encode('utf-8'))# obtains MD5 of the password
            if h.hexdigest() in hdictionary: # compares the MD5
                cracked_count += 1
                print("[*] Hash cracked: "+h.hexdigest(),"| Password: "+password)
                print(f"[*] {cracked_count} out of {hdictionary_length} cracked!")
        if cracked_count == hdictionary_length:
            print("[*] All inputted hash values have been cracked!")
            exit()
        password_length += 1 # moves on to the next password (by length) to crack
else:
    print('''
[*] ERROR!
[*] Please enter valid option choice!
''')
    exit()
