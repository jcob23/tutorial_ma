file = open('textfile.txt','r') 
tekst=file.read()
new_text= ''.join([i for i in tekst if not i.isdigit()]) # funkcje znalazłem w internecie, tutaj -> https://stackoverflow.com/questions/12851791/removing-numbers-from-string
print(new_text)
file.close()
