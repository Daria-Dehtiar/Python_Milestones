input_key =  int(input("Enter key: "))
input_message = input("Enter message: ")

def decrypt(message, key):
    result = ""
    for char in message:
        if "A" <= char <= "Z" or "a" <= char <= "z":
            if char.islower():
                shift = (ord(char) - key - ord("a")) % 26
                result += chr(shift + ord("a"))
            elif char.isupper():
                shift = (ord(char) - key - ord("A")) % 26
                result += chr(shift + ord("A"))
        else:
            result += char
    return result

decrypted_message = decrypt(input_message, input_key)
print(decrypted_message)