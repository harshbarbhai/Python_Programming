from functools import reduce

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is: ",Data)

    FData = list(filter((lambda No : (No % 2 == 0)),Data))  #filter accept one value at a time and written Boolen true or false
    print("Data after filter is: ",FData)

    MData=list(map((lambda No : No+1),FData))
    print("Data after map is: ",MData)

    RData=reduce((lambda A,B : A+B),MData)
    print("Data afer reduce is: ",RData)

if __name__ == "__main__":
    main()