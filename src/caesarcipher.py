ALPHA = 'abcdefghijklmnopqrstuvwxyz'
 
def encrypt_caesar(key, text):
    final_text = ''
    for k in text.lower():
        temp = (ALPHA.index(k) + key) % 26
        final_text += ALPHA[temp]
            
    return final_text.lower()
    
def decrypt(key,encrypt_text):
    decrypt_text=''
    for i in encrypt_text.lower():
        tem = (ALPHA.index(i) - key) % 26
        decrypt_text += ALPHA[tem]
            
    return decrypt_text.lower()
 
inp_key = int(input("enter the key:"))
 
inp_text=input("Enter the Input Text : ")
 
encrypt_text = encrypt_caesar(inp_key,inp_text)
 
print("Encrypted Text :",encrypt_text)

decrypt_final=decrypt(inp_key,encrypt_text)

print("decrypted text:"+decrypt_final)
        
