def encode_message(message):    
    return "".join(message.replace('e','3').replace('a','@').replace('i','!').replace('o','0').replace('u','^'))
print(3,encode_message("I Love You"))
