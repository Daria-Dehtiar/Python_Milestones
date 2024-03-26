input_key = int(input("Enter key: "))
input_message = input("Enter message: ")

def encrypt(key, message):
    result = ""
    for char in message:
        if "A" <= char <= "Z" or "a" <= char <= "z":
            if char.islower():
                shift = (ord(char) + key - ord("a")) % 26
                result += chr(shift + ord("a"))
            elif char.isupper():
                shift = (ord(char) + input_key - ord("A")) % 26
                result += chr(shift + ord("A"))
        else:
            result += char
    return result

encrypted_message = encrypt(input_key, input_message)
print(encrypted_message)