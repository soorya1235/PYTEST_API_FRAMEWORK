def outerfunction(text):
    ts = text

    def inner_function():
        text = ".".join(ts)
        print(text)

    return inner_function


func1 = outerfunction("hello")
func1()
