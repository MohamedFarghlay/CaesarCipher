#python program to write ceaser cipher program

#encryption
def Encryption(plaintext,key):
    text=""
    for i in range (len(plaintext)):
        pos=ord(plaintext[i])
        #move the postion of the char key times
        pos = pos + key;
        #encrypt the lowercasr letters
        if plaintext[i].islower():
            #if the pos excededd the range of the char 
            if (pos) > 122:
                #subtract the number of char
                pos-=26
               
        #ecyrpt the uppercase letters
        if (plaintext[i].isupper()):
            if(pos) > 90:
                pos-=26
            
       
        text+=chr(pos)
    return text

#Decryption
def Decryption(plaintext,key):
    text="";
    for i in range (len(plaintext)):
        pos=ord(plaintext[i])
        #return to the original pos char 
        pos = pos - key;
        #Decrypt lower case letter
        if plaintext[i].islower():
            #if it out of range 
            if (pos) < 97:
                #add to it number of char
                pos+=26
        #decrypt uppercase letters
        if plaintext[i].isupper():
            if pos < 65:
                pos+=26
        text+=chr(pos)
    return text




def main():

    #ask the user what (he/she) want?
    print("------------CEASER CIPHER--------------")
     #get text from user
    plaintext=input("Enter Your Text: ")
    #get the key
    key=int(input("Enter the key: "))
    print("1-Encryption Text")
    print("2-Decryption Text")
    chioce=int(input("Enter your Chioce: "))
    if chioce == 1:
        print("Encryption....")
        #encrypt the text and assing it to encrypt
        encrypt=Encryption(plaintext,key)
        print ("Your Encrypion Text : " ,encrypt)
    elif chioce == 2:
        print("Decryption....")      
        print("Your Decryption Text : " ,Decryption(plaintext,key))
    else:
        print("Wrong Chioce ...Tey Again!")

    

  
main()
