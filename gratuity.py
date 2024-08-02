def subtotal_gratuity_rate(subtotal , gratuity_rate):
    gratuity = (gratuity_rate / 100) * subtotal
    total = subtotal + gratuity
    return f"The gratuity is {gratuity:.2f} and the total is {total:.2f}"

subtotal ,  gratuity_rate = eval(input("Enter the subtotal and a gratuity rate: "))
print(subtotal_gratuity_rate(subtotal , gratuity_rate))