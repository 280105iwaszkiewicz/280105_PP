class Singleton:
    _ins = None

    def __new__(cls):
        if cls._ins is None:
            cls._ins = super().__new__(cls)

        return cls._ins


# test
if __name__ == "__main__":
    # próba utworzenia dwóch osobnych obiektów
    obiekt_A = Singleton()
    obiekt_B = Singleton()

    print("TEST WZORCA SINGLETON")
    print(f"Adres pamięci obiektu A: {hex(id(obiekt_A))}")
    print(f"Adres pamięci obiektu B: {hex(id(obiekt_B))}")

    czy_to_samo = obiekt_A is obiekt_B
    print(f"Czy obiekt A i obiekt B to dokładnie to samo? {czy_to_samo}")