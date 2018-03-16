def last_word_len(num):
    count = 0
    for i,val in enumerate(num[::-1]):
        if val != " ":
            count = count +1
        else:
            break
    if count == len(num):
        count = 0
    return count

print(last_word_len("Hello World"))
        
        
        
