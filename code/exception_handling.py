try:
    num = int(input("Enter a number: "))
    r = 10/num
    print(r)
except Exception as e:
    print(e)
finally:
    print("in finally.")


