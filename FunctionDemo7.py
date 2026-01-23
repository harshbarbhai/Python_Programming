#Accept:Multiple Parameters
#Return:one value
def Marvellous1(Value1,value2):
    print("Inside marvellous 1: ",Value1,value2)
    return 11

def main():
    Result=None 
    Result=Marvellous1("python",21)
    print("Return value is : ",Result)

if __name__=="__main__":
    main()