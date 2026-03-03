def myfunc():
    print("hello word")


    myfunc()
    print(__name__)
if __name__ == "__main__":
    #if this code is directly executed by running the file its present in 
    print("we are directly running this code ")
    myfunc()
    print(__name__)