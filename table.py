def print_table():
    print(f"{'a':<5}\t\t{'b':<5}\t\t{'a ** b':<5}")

    for a in range(1 , 6):
        b = a + 1
        result = a ** b
        print(f"{a:<5}\t\t{b:<5}\t\t{result:<5}")

print_table()