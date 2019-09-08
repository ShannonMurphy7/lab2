def number_of_vowels(n):
    count = 0;
    for i in range(len(n)):
        if n[i] == 'a' or n[i] == 'e' or n[i] == 'i' or n[i] == 'o' or n[i] == 'u':
            count = count;
        else:
            count = count + 1;
    return count;

def check_number(n):
    newN = n #this variable will be set to n as a temporary variable to minipluate
    string = str(n) #this turns the number into a string
    length = len(string) #this finds how many digits the string is
    even = 0;
    for i in range(length):
        if int(string[i]) % 2 == 0:
            even = even + 1
    return even
        
def armstrong(n):
    newN = n #this variable will be set to n as a temporary variable to minipluate
    string = str(n) #this turns the number into a string
    length = len(string) #this finds how many digits the string is
    count = 0;
    for i in range(length):
        newN = int(n[i])**3
        count = newN + count
    if count == int(n):
        return True
    else:
        return False
def riddler():
    for i in range(1000, 9999):
        a = i // 1000 #first digit
        b = i // 100%10
        c = i // 10 % 10
        d = i % 10 #last digit
        count = a + b + c + d
        if i % 2 == 0 and count == 27:
            if a == 3 * c:
                if a != b and a != c and a != d and b != c and b != d and d != c:
                    return i
        

def main():
    #string = input("Enter a string: ")
    #print("That string has " + str(number_of_vowels(string)) + " vowels")
    #number = input("Enter a number: ")
    #print("The string has " + str(check_number(number)) + " even numbers")
    #armstrongg = input("Enter a number: ")
    #print("Armstrong number? " + str(armstrong(armstrongg)))
    print(riddler())


    
