''' Tak wygląda tekst w pliku  -> L1or1em i2ps2um do3lo3r si4t a5met5, c6ons6ec6tet6ur a7di7p7i7sci7ng7 el7it7. S8e8d l8uct8u8s, i8psu8m n8ec f8er8mentu8m8 s8c888eler9isque, e9r9os f9el9is f999eugiat fe0lis,
id ma43xi2m1us a24nte i3p5sum n32ec tu215rpis. U333t vi532tae di3456gnis32si4234m en234im. Du234is eg234esta234s 234velit 2t34urpis43. Do2nec 4v34el e4l5ei2fe6nd 2e3ra4t. Sed magna velit,
imperdiet et diam sit amet, lobortis rutrum leo. Aenean eget eros quis velit ultricies fringilla. Curabitur dignissim commodo massa, quis imperdiet libero tristiq23u23e i23d.'''

file = open('textfile.txt','r') 
tekst=file.read()
new_text= ''.join([i for i in tekst if not i.isdigit()]) # funkcje znalazłem w internecie, tutaj -> https://stackoverflow.com/questions/12851791/removing-numbers-from-string
print(new_text)
file.close()
