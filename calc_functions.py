#팩토리얼 함수

def factorial(n):
    try:
        n=int(n)
    except:
        return "-->error!"

    if n==0:
        return 1
    if n>40:
        return "-->Answer will not fit in the screen!"
    if n<0:
        return "--> error!"

    ans=n
    while n>1:
        ans=ans*(n-1)
        n=n-1
    return ans
    

def to_roman(n):
    try:
        n=int(n)
    except:
        return "-->Error"
    if n>4999:
        return "--> Over the range."
    numberBreaks = (1000,900,500,400,100,90,50,40,10,9,5,4,1)
    letters = {
1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL",10:"X",
9:"IX", 5:"V", 4:"IV",1:"I"
        }
    result=""
    for value in numberBreaks:
        while n>=value:
            result = result+letters[value]
            n=n-value
    return result

def to_binary(n):
    try:
        n=int(n)
        return bin(n)[2:]
    except:
        return "-->Error!"

def from_binary(n):
    try:
        return int(n,2)
    except:
        return"-->Error!"

