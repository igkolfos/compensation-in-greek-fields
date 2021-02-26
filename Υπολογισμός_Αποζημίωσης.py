#!/usr/bin/env python3
str = 'continue'
while(str != 'stop'):
    ektasi = float(input('Έκταση Αγροτεμαχίου σε στρέμματα: '))
    mesipar = float(input('Μέση παραγωγή σε κιλά: '))
    pososto_zimias = float(input('Ποσοστό ζημιάς (0 - 100): '))
    stathera = float(input('Σταθερά (πέρυσι ήταν 0.88): '))
    timi_monadas_proiontos = float(input('Τιμή ανά μονάδα προϊόντος: '))
    pososto_apozimiosis = ektasi * mesipar * (pososto_zimias - 15) * stathera * timi_monadas_proiontos/100
    print('**** Ποσοστό ζημιάς = ', pososto_apozimiosis,' ****')
    str = input('Για τερματισμό γράψτε stop, αλλίως enter: ')