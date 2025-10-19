# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut "labore" et dolore magna aliqua."""
# print(a)
# a = "Hello, World!"
# print(a[:13])
# print(len(a))
# for x in a:
#     print(x)
# if "ll" in a:
#     print("Yes, 'll' is present.")  
#modify string 
# a = " Hello , World  !"
# print(a.upper())
# print(a.lower())
# print(a.strip()) # removes whitespace at the beginning or the end
# print(a.split("o"))
balance = 100
tax = 20
urbalance =f"Your balance is {(balance-tax ):.2f} dollars"
print(urbalance)
price =input("Enter the price: ")
print(f"the price is {'expensive' if float(price)>1000 else 'cheap'}")

txt = "python"
print(f"i love {txt.upper()}!")

def Rightshift(decimalvalue,bits):
    return decimalvalue >> bits

print(f"the value after right shift is {Rightshift(8, 2)}")