
def choice(www,ooy=')', ooi='>>>'):
    while True:
        h = 0
        while h < len(www):
            print(h+1,ooy,www[h])
            h += 1
        il = input(ooi)

        for w in range(len(www)):
            if str(w+1) == il:
                return www[w]

def yes_no(meaning=''):
    while True:
        www = input(meaning+' (Y/N)?').lower()
        if www == 'y':
            return True
        elif www == 'n':
            return False