total = int(input('How much money do you have in your pocket\n'))

# ✅ ↓ YOUR CODE HERE ↓ ✅


if(total >= 100):
    print("Dame tu dinero!")

elif total < 50:
    print("Eres pobre!")

elif(total >= 50):
    print("Comprame un cafe!")

else:
    print("Valores introducidos no validos")