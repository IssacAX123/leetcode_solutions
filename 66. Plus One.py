import timeit



def plus_one_issac(integer):
    sum = 0
    for i, number in enumerate(integer[::-1]):
        sum += number *(10 ** i)
    sum += 1
    new_array = []
    while sum != 0:
        new_array.insert(0, sum % 10)
        sum = sum // 10
    return new_array

def plus_one_issac_2(integer):
    one = 1
    i = len(integer)-1
    while one == 1:
        if i >= 0:
            if integer[i] == 9:
                integer[i] = 0
            else:
                integer[i] += 1
                one = 0
        else:
            integer.insert(0, one)
            one = 0
        i -= 1
    return integer


# slower than issac 2
def plus_one_online(digits):
     for i in range(1,len(digits)+1): #Traverse each value
         if(digits[-i]==9):   #0 if 9
             digits[-i]=0
         else:                #Exit if 1 is added
             digits[-i]+=1
             break
     if(digits[0]==0):        #If it's all 9, then the first digit is 1 followed by a 0
         digits[0] = 1          #eg:[9,9,9] --> [1,0,0,0]
         digits.append(0)
     return digits

print(plus_one_issac_2([9,9,9]))