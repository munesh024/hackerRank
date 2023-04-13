def sockMerchant(n, ar):
    # Write your code here
    dataValue = 0
    count = 0
    while n>=0 :
        if ar :
            valueInTheArray = ar[dataValue]
        else :
            return count

        ar.remove(valueInTheArray)
        for each in ar :
            if each == valueInTheArray :
                count = count + 1
                ar.remove(each)       
                break
                
        n = n - 1

    
    
data = int(input("enter the max number"))
arrayList = []
print(data)
for each in range(1,data+1) :
    arrayList.append(int(input("enter your Number")))
    
print("\n")
print(sockMerchant(data,arrayList))