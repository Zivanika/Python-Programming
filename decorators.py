def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Have a good day ahead...")
        return mfx

@greet
def hello():
    print("I am Akshat")

hello