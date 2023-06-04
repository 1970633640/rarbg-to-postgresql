with open('data/everything.txt') as f:
    i=0
    for line in f.readlines():
        i+=1
        l = line.strip().split('&dn=')
        magnet, name = l[0], l[1]
        magnet = magnet.replace('magnet:?xt=urn:btih:', '')
        if len(magnet) != 40:
            print('error')
        else:
            #print(magnet,name)
            pass
print('结束')
