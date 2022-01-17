try:
    V = int(input())
    V0 = int(input())
    t = int(input())




    def decorator(boost):
        def wrapper():
            boost()
            print(((V0*V0)-(V*V))/ (2*((V0-V)/t)))
        return wrapper()

    @decorator
    def boost():
        print((V-V0)/t)

    boost()



except ValueError:
    print("Нельзя вводить строки")
except ZeroDivisionError:
    t=0
    print("a=0 вот тебе и ошибка,я это,пошла ")
