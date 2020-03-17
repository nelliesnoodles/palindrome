# A palindrome is a word/string that is the same
# forwards as backwards, such as "racecar" or
# "I am amama ma I".

BPS ="Binary Palindrome Search"

        

def BPS(astring):
    print(f"\n --{astring}-- \n ")
    max_length = len(astring) - 1
    # floor division.
    mid = max_length // 2 
    mid2 = None
    done = False
    j = 1
    count = 0
    first_palindrome = None
    second_palindrome = None
    list_of_palindromes = []

    # if string is an even length, the mid will have two values.
    if len(astring) % 2 == 0:
        mid2 = mid + 1
        mid = mid
   
    while mid > 0:
        print("mid > 0")
        if mid < 1:
            break
        first_palindrome = string_loop(mid, astring)
        if first_palindrome != None:
            for item in first_palindrome:
                list_of_palindromes.append(item)

        mid -= 1


    while mid < max_length:
        print("mid < max_length")
        second_palindrome = string_loop(mid, astring)       
        if second_palindrome != None:
            for item in second_palindrome:
                list_of_palindromes.append(item)

        mid += 1
    
    if mid2 != None:
        
        while mid2 > 0:
            print("mid2 > 0")
            if mid2 < 1:
                break
            first_palindrome = string_loop(mid2, astring)
            if first_palindrome != None:
                for item in first_palindrome:
                    list_of_palindromes.append(item)

            mid2 -= 1


        while mid2 < max_length:
            print("mid2 < max_length")
            second_palindrome = string_loop(mid2, astring)       
            if second_palindrome != None:
                for item in second_palindrome:
                    list_of_palindromes.append(item)

            mid2 += 1
        # clean duplicates by making a set:
        palindrome_set = set(list_of_palindromes)
        print(palindrome_set)
    else:
        palindrome_set = set(list_of_palindromes)
        print(palindrome_set)





def string_loop(mid, astring):
    print("---------  STRING LOOP ---------")
    j = 1
    done = False
    count = 0
    print("mid = ", mid)
    
    strings_found = []
   

    while not done and count < mid:
        back_index = mid + j
        front_index = mid - j 
        #print("mid = ", mid)
        x = astring[front_index: back_index + 1]
        print("back_index = ", back_index)
        print("front_index =", front_index)

        string_length = len(x)
        #reverse string
        y = x[string_length::-1]
       
        print("x=", x)
        print("y=", y)
        if x == y: 
            
            print("palindrome found")
            #print(x)
            strings_found.append(x)
            
       
        j += 1
        count += 1

        #--- Return strings or None ---#
    if len(strings_found) > 0:
        return strings_found
    else:
        return None

BPS("a tt aa tt a")


