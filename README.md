# Krepšinio komandos valdymo ir rungtynių statistikos sistema

## 1. Introduction

Šio kursinio darbo tikslas – sukurti paprastą krepšinio komandos valdymo sistemą naudojant Python ir objektinio programavimo principus.

Aš sukūriau programą, kuri leidžia:
- sukurti komandą
- pridėti žaidėjus ir trenerį
- parodyti komandos informaciją
- simuliuoti rungtynes tarp dviejų komandų
- registruoti žaidėjų statistiką
- išsaugoti ir nuskaityti duomenis iš failo

Programą galima paleisti su komanda:

python main.py

Paleidus programą sukuriama komanda, parodoma jos sudėtis, duomenys išsaugomi į failą ir vėliau nuskaitomi. Taip pat parodoma rungtynių informacija.


## 2. Body / Analysis

Šiame projekte aš pritaikiau pagrindinius objektinio programavimo principus.

# Paveldėjimas (Inheritance)

Aš sukūriau bazinę klasę Person, iš kurios atributus paveldi Player ir Coach klasės.  
Taip išvengiau pasikartojančio kodo, nes bendri atributai (vardas ir amžius) aprašyti vienoje vietoje.

# Polimorfizmas (Polymorphism)

Polimorfizmą realizavau per get_info metodą.  
Šis metodas skirtingose klasėse veikia skirtingai, bet kviečiamas vienodai.

# Enkapsuliacija (Encapsulation)

Enkapsuliaciją panaudojau paslėpdamas duomenis klasėje Person.  
Atributai _name ir _age yra privatūs ir pasiekiami per metodus.

# Abstrakcija (Abstraction)

Abstrakciją realizavau per FileManager klasę.  
Vietoj to, kad tiesiogiai dirbčiau su failais ir JSON, sukūriau metodus duomenų saugojimui ir nuskaitymui, kurie paslepia vidinę logiką.

# Kompozicija (Composition)

Programoje naudojau kompoziciją:
- Team klasė saugo žaidėjus
- Match klasė saugo komandų informaciją ir statistiką

Tai leidžia kurti sudėtingesnę sistemą iš paprastesnių dalių.

# Design pattern

Panaudojau Factory metodą.  
Sukūriau PersonFactory klasę, kuri atsakinga už žaidėjų ir trenerių kūrimą.  
Tai leidžia patogiau ir tvarkingiau kurti objektus.

# Duomenų saugojimas

Duomenis saugau JSON faile kuri man veikia kaip mini duomenų bazė.
Tai leidžia išsaugoti informaciją ir ją vėliau nuskaityti.

# Testavimas

Parašiau testus naudodamas unittest.  
Testavau pagrindines funkcijas:
- objektų kūrimą
- komandos veikimą
- rungtynių logiką
- failų saugojimą ir nuskaitymą



## 3. Results

- Sukūriau veikiančią krepšinio komandos valdymo sistemą
- Įgyvendinau visus OOP principus
- Panaudojau design pattern
- Duomenys sėkmingai saugomi JSON formatu
- Parašyti testai pagrindinėms funkcijoms
- Programa veikia be problemų


## 4. Conclusions

Šio darbo metu sukūriau paprastą, bet veikiančią sistemą krepšinio komandai valdyti, stebėti rezultatus, statistiką, lyginti žaidėjus, komandas ir matyti rezultatus.

Pritaikiau objektinio programavimo principus, kurie padėjo sukurti aiškią ir tvarkingą programos struktūrą.

Ateityje sistemą būtų galima patobulinti:
- pridedant vartotojo sąsają
- naudojant duomenų bazę vietoj JSON pavyzdžiui kaip MySQL arba SQLite. Ji galėtų būti susieta su tikra internetine visuomet atnaujinama duomenų baze dėl tiksliausios statistikos ir patikimumo ir naudos.
- leidžiant vartotojui patogiau įvesti duomenis, pasirūpinti tuom jog vartotojas paprastai ir greitai galėtų gauti rezultatą ir tai ko jam reikia.


