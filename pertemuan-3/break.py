for i in range(5):
    if i == 3: #jika i =3 
        break  #maka loop akan berhenti
    print(i)   #jika i selain

text = input() 

while True: 
    if text == "stop" or text == "end": #jika inputan "stop" aatau "end"
        print("program has stopped!")   #maka program akan print 
        break                           #dan program berhenti 
    print("Text: {}".format(text))      #jika input selain "stop" dan "end" maka akan print
    text = input ()                     #dan program akan berlanjut dengan memasukkan inputan lagi