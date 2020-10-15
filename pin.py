sosedi = {1: {1,2,4}, 2: {1,2,3,5}, 3: {3,2,6}, 4: {1,4,5,7}, 5: {2,4,5,6,8}, 6: {3,5,6,9}, 7: {4,7,8}, 8: {5,7,8,9,0}, 9: {6,8,9}, 0: {8,0}}

# Primer kode: 801

def get_pins(koda, kombinacije = None ):
    # Empty case
    if koda == '':
        return kombinacije
    
    # Začeten primer
    elif kombinacije == None:
        nove_kombinacije = []  
        for sosed in sosedi[int(koda[0])]:   # Primer cifre: 8 ===> nove_kombinacije = ['5', '7', '8', '9', '0']
            nove_kombinacije.append(str(sosed))
        
        return get_pins(koda[1:], nove_kombinacije)
    
    else:
        nove_kombinacije = []
        for sosed in sosedi[int(koda[0])]:
            for kombinacija in kombinacije:
                nove_kombinacije.append(kombinacija + str(sosed)) # nove_kombinacije = ['58', '78', '88', ....., '50', '70',... ]

        return get_pins(koda[1:], nove_kombinacije)


def get_pins_hitri(koda):
    nove_kombinacije = [' ']
    for stevka in koda:
        kombinacije = nove_kombinacije
        nove_kombinacije = []
        for sosed in sosedi[int(stevka)]:
            for kombinacija in kombinacije:
                kombinacija = kombinacija.strip()
                nove_kombinacije.append(kombinacija + str(sosed))

    return nove_kombinacije
    
# print(get_pins('876'))
# print(get_pins_hitri('876'))
