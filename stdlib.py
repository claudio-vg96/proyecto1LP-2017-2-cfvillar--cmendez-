def bin_to_dec(num):
    num_dec=0
    list_num=[]
    potencia = 0
    for i in num:
        list_num.insert(0, int(i))
    for i in list_num:
        if i==1:
            num_dec+=2**potencia
        potencia+=1
    return num_dec

def dec_to_bin(num):
    num_dec=int(num)
    num_dec_copy=int(num)
    num_bin=[]
    while num_dec_copy>0:
        num_dec=num_dec/2
        num_dec_copy=num_dec_copy/2.0
        if num_dec_copy>num_dec:
            num_bin.insert(0,str(1))
            num_dec_copy-=0.5
        else:
            num_bin.insert(0,str(0))
    return ''.join(num_bin)

base_hex={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
hex_base={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

def hex_to_bin(num):
    num_bin=[]
    add=[]
    for i in num:
        if i in base_hex:
            bin=dec_to_bin(base_hex[i])
            for num in bin:
                add.append(num)
        else:
            bin=dec_to_bin(i)
            for num in bin:
                add.append(num)
        while len(add)<4:
            add.insert(0,'0')
        add = ''.join(add)
        num_bin.append(add)
        add=[]
    return ''.join(num_bin)

def bin_to_hex(num):
    num_bin=[]
    cont_inf=0
    cont_sup=4
    part_bin=[]
    num_hex=[]
    for i in num:
        num_bin.append(i)
    while len(num_bin)%4!=0:
        num_bin.insert(0,'0')
    while cont_inf<len(num_bin):
        part_bin=num_bin[cont_inf:cont_sup]
        hexa=str(bin_to_dec(''.join(part_bin)))
        if int(hexa)<10:
            num_hex.append(hexa)
        else:
            num_hex.append(hex_base[int(hexa)])
        cont_inf+=4
        cont_sup+=4
    return ''.join(num_hex)