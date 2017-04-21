from operator import xor

def encrypt(plaintext,kunci):
    #rumusnya C = (P XOR K0) add mod 2^64 K1
    asciikey = [None] * len(kunci)
    for i in range(0,len(kunci)):
        asciikey[i] = ord(kunci[i])
        #print asciikey[i]

    key0 = [None] * 4
    key1 = [None] * 4

    j = 0
    for i in range(0,len(asciikey)):
        if i <= 3:
            key0[i] = asciikey[i]
        else:
            key1[j] = asciikey[i]
            j = j + 1

    recur = len(plaintext)/4
    kosong = 4 - (len(plaintext)%4)
    if kosong > 0:
        recur = recur + 1

    asciitext = [None] * (recur*4)
    for i in range(0,len(asciitext)):
        if i < len(plaintext):
            asciitext[i] = ord(plaintext[i])
        else:
            asciitext[i] = ord(' ');

    diisi = (recur*4)

    x = 0
    for i in range(0,recur):
        for j in range(0,4):
            asciitext[x] = xor(asciitext[x], key0[j])
            x = x + 1

    #print asciitext
    #print key1
    x = 0
    hasilEncryp = [None] * len(asciitext)
    for i in range(0,recur):
        for j in range(0,4):
            hasilEncryp[x] = asciitext[x] + key1[j]
            hasilEncryp[x] = hasilEncryp[x]%256
            #print hasilEncryp[x]
            x = x + 1

    hasilEncrypted = [None] * (len(hasilEncryp) - kosong)
    for i in range(0,len(hasilEncrypted)):
        hasilEncrypted[i] = chr(hasilEncryp[i])

    #return hasilEncryp
    stringHasil = ''
    for i in range(0,len(hasilEncrypted)):
        stringHasil = stringHasil + hasilEncrypted[i]

    return stringHasil


def decrypt(hasilEnkripsi, kunci):
    # rumusnya P = (C add mod 2^64 -K1) XOR K0
    asciikey = [None] * len(kunci)
    for i in range(0, len(kunci)):
        asciikey[i] = ord(kunci[i])

    key0 = [None] * 4
    key1 = [None] * 4

    j = 0
    for i in range(0, len(asciikey)):
        if i <= 3:
            key0[i] = asciikey[i]
        else:
            key1[j] = asciikey[i]
            j = j + 1

    recur = len(hasilEnkripsi) / 4
    sisa = len(hasilEnkripsi) % 4
    ukuranEncryp = ((4*recur) + sisa)
    asciiEncryp = [None] * ukuranEncryp
    for i in range(0, len(asciiEncryp)):
        asciiEncryp[i] = ord(hasilEnkripsi[i])

    #print asciiEncryp

    for i in range(0,ukuranEncryp):
        asciiEncryp[i] = asciiEncryp[i] - key1[i%4]

    #print asciiEncryp

    hasilDecryp = [None] * len(asciiEncryp)
    for i in range(0,ukuranEncryp):
        hasilDecryp[i] = xor(asciiEncryp[i],key0[i%4])

    hasilDecrypted = [None] * len(hasilDecryp)
    for i in range(0,len(hasilDecrypted)):
        hasilDecrypted[i] = chr(hasilDecryp[i])

    #return hasilDecryp
    stringHasil = ''
    for i in range(0, len(hasilDecrypted)):
        stringHasil = stringHasil + hasilDecrypted[i]

    return stringHasil

key = 'cobacoba'

while 1:
    text = raw_input("Masukkan Text: ")
    arr_text = [None] * len(text)

    for i in range(0,len(text)):
        arr_text[i] = text[i]

    encrypted = encrypt(arr_text, key)
    print "Hasil enkripsi dari " + text + ": \r\n" + str(encrypted) + "\r\n \r\n"

    decrypted = decrypt(encrypted,key)
    print "Hasil dekripsi dari " + str(encrypted) + ": \r\n" + str(decrypted)

    print "\r\n"