# Crappy assignment prepared for the lovely teacher
class Fuvar:
    def __init__(self, sor):
        s = sor.strip().replace(',','.').split(';')
        self.taxi_id       = int(  s[0])
        self.indulas       = str(  s[1])
        self.idotartam     = int(  s[2])
        self.tavolsag      = float(s[3])
        self.viteldij      = float(s[4])
        self.borravalo     = float(s[5])
        self.fizetes_modja = str(  s[6])
        
        
with open('fuvar.csv', 'r', encoding = 'utf-8-sig') as f:
    fejléc = f.readline()
    lista  = [ Fuvar(sor) for sor in f ]

#3 Total rides

print( f"3. feladat: {len(lista)} fuvar lett végrehajtva")

#4 6185 income, ride

bevételek = [ sor.viteldij + sor.borravalo  for sor in lista if sor.taxi_id == 6185 ]
bevétel   = sum(bevételek)
print( f"4. feladat: {len(bevételek)} fuvar alatt: ${bevétel} jött össze")

#5 payment

statisztika = dict()
for sor in lista:
    fizetés_módja = sor.fizetes_modja
    statisztika[fizetés_módja] = statisztika.get(fizetés_módja, 0) + 1
print(     f'5. feladat:')
x = [print(f'        {fizetés_módja}: {fuvarok_száma} fuvar') for fizetés_módja, fuvarok_száma in statisztika.items()]

#6 distance driven(2 tizedes)

összes_megtett_út = 1.6 * sum([ sor.tavolsag for sor in lista ])
print(f'6. feladat:{összes_megtett_út:.2f}km lett furikázva.')

#7 longest ride
i = max([ (sor.idotartam, i) for i, sor in enumerate(lista) ])[1]
időtartam = lista[i].idotartam
taxi_id   = lista[i].taxi_id
távolsag  = 1.6 * lista[i].tavolsag
viteldíj  = lista[i].viteldij

print("7. feladat: Leghosszabb")
print(f"        Fuvar hossza: {időtartam} másodperc")
print(f"        Taxi azonosító: {taxi_id} ")
print(f"        Megtett távolság: {távolsag:.2f} km ")
print(f"        Viteldíj: {viteldíj} $")

#hibak.txt (valamiert 6000x becopyzza de basszafasz)
print( "8. feladat: hibak.txt" )
with open('fuvar.csv', 'r', encoding='utf-8-sig') as file:
    elsosor    = file.readline()
    fuvarlista = [ sor for sor in file ]
    
with open('hibak.txt', 'w', encoding='utf-8') as output:
     output.writelines(elsosor)
     hiba = [ (sor.indulas, i) for i, sor in enumerate(lista) if (sor.idotartam != 0 and sor.viteldij != 0.0) and sor.tavolsag == 0.0 ]
     hiba.sort()
     [ print(fuvarlista[sor[1]], file=output, end='') for sor in hiba ]
