mydict = {}
with open("input.txt") as f:
    for line in f:
        (key, val) = line.strip().split(None, 1)
        mydict[key] = val

emblem = {
    'SPACE' : 'GORILLA',
    'LAND' : 'PANDA',
    'AIR' : 'OWL',
    'WATER' : 'OCTOPUS',
    'ICE' : 'MAMMOTH',
    'FIRE' : 'DRAGON'
}

key_list = list(emblem.keys())
val_list = list(emblem.values())

lst = []

def decrypt(cipher,key):
    if cipher.islower():
        return chr((ord(cipher)-key-97)%26+97)
    else:
        return chr((ord(cipher)-key-65)%26+65)

def check(animal,message):
    animal_dict = {}
    message_dict = {}
    for i in animal:
        animal_dict[i] = animal_dict.get(i, 0) + 1
    for i in list(message):
        c = decrypt(i, len(animal))
        message_dict[c] = message_dict.get(c, 0)+1

    return not any([max(j-message_dict.get(i,0), 0) for i, j in animal_dict.items()])


def ruler():
    for k in mydict.keys():
        if emblem.get(k) != 'GORILLA':
            if check(emblem.get(k),mydict.get(k)):
                lst.append(key_list[val_list.index(emblem.get(k))])
    if len(lst) >= 3 :
        return 'SPACE ' + ' '.join(lst)
    else:
        return 'NONE'

print(ruler())
