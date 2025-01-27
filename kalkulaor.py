def calculator():
    print("=== Kalkulator ===")
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęgowanie")
    print("6. Pierwiastek kwadratowy")
    print("7. Wyjście")

    while True:
        try:
            choice = int(input("\nWybierz opcję (1-7): "))
            
            if choice == 7:
                print("Do widzenia!")
                break

            if choice in [1, 2, 3, 4, 5]:
                num1 = float(input("Podaj pierwszą liczbę: "))
                num2 = float(input("Podaj drugą liczbę: "))

                if choice == 1:
                    print(f"Wynik: {num1} + {num2} = {num1 + num2}")
                elif choice == 2:
                    print(f"Wynik: {num1} - {num2} = {num1 - num2}")
                elif choice == 3:
                    print(f"Wynik: {num1} * {num2} = {num1 * num2}")
                elif choice == 4:
                    if num2 != 0:
                        print(f"Wynik: {num1} / {num2} = {num1 / num2}")
                    else:
                        print("Błąd: Dzielenie przez zero!")
                elif choice == 5:
                    print(f"Wynik: {num1} ^ {num2} = {num1 ** num2}")

            elif choice == 6:
                num = float(input("Podaj liczbę do pierwiastkowania: "))
                if num >= 0:
                    print(f"Wynik: √{num} = {num ** 0.5}")
                else:
                    print("Błąd: Pierwiastek z liczby ujemnej nie jest liczbą rzeczywistą!")
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

        except ValueError:
            print("Błąd: Wprowadź poprawną liczbę!")

if __name__ == "__main__":
    calculator()
