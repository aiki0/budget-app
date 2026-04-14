class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka."""

    def __init__(self, service):
        self._service = service

    def start(self):
        print("--- Budjettisovellus ---")
        print("Komennot:")
        print("1: Lisää kulu")
        print("2: Listaa kulut")
        print("0: Lopeta")

        while True:
            komento = input("\nValitse komento: ")

            if komento == "0":
                break
            
            elif komento == "1":
                try:
                    maara_syote = input("Määrä: ")
                    if not maara_syote:
                        print("Virhe: Määrä ei voi olla tyhjä!")
                        continue
                    
                    maara = int(maara_syote)
                    kategoria = input("Kategoria: ")
                    
                    self._service.lisaa_kulu(maara, kategoria)
                    print("Kulu lisätty!")
                except ValueError:
                    print("Virhe: Syötä määrä numerona.")

            elif komento == "2":
                kulut = self._service.hae_kaikki()
                if not kulut:
                    print("Ei kuluja vielä.")
                for kulu in kulut:
                    print(f"{kulu['category']}: {kulu['amount']}€")
            
            else:
                print("Tuntematon komento.")