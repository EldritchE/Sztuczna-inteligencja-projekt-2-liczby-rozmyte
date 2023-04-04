import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Definicja zmiennych lingwistycznych
dawka = ctrl.Antecedent(np.arange(0, 11, 1), 'dawka')
wielkosc = ctrl.Antecedent(np.arange(0, 11, 1), 'wielkosc')
#szukana
czas = ctrl.Consequent(np.arange(0, 61, 1), 'czas')

# Definicja funkcji przynależności
dawka['niska'] = fuzz.trimf(dawka.universe, [0, 2, 5])
dawka['srednia'] = fuzz.trimf(dawka.universe, [0, 5, 10])
dawka['wysoka'] = fuzz.trimf(dawka.universe, [5, 10, 10])

wielkosc['maly'] = fuzz.trimf(wielkosc.universe, [0, 2, 5])
wielkosc['sredni'] = fuzz.trimf(wielkosc.universe, [0, 5, 7])
wielkosc['duzy'] = fuzz.trimf(wielkosc.universe, [5, 10, 10])

czas['krotki'] = fuzz.trimf(czas.universe, [0, 0, 30])
czas['sredni'] = fuzz.trimf(czas.universe, [0, 30, 60])
czas['dlugi'] = fuzz.trimf(czas.universe, [30, 60, 60])

# Definicja reguł
reguła1 = ctrl.Rule(dawka['niska'] & wielkosc['maly'], czas['krotki'])
reguła2 = ctrl.Rule(dawka['niska'] & wielkosc['sredni'], czas['sredni'])
reguła3 = ctrl.Rule(dawka['niska'] & wielkosc['duzy'], czas['dlugi'])
reguła4 = ctrl.Rule(dawka['srednia'] & wielkosc['maly'], czas['sredni'])
reguła5 = ctrl.Rule(dawka['srednia'] & wielkosc['sredni'], czas['sredni'])
reguła6 = ctrl.Rule(dawka['srednia'] & wielkosc['duzy'], czas['dlugi'])
reguła7 = ctrl.Rule(dawka['wysoka'] & wielkosc['maly'], czas['sredni'])
reguła8 = ctrl.Rule(dawka['wysoka'] & wielkosc['sredni'], czas['dlugi'])
reguła9 = ctrl.Rule(dawka['wysoka'] & wielkosc['duzy'], czas['dlugi'])


# Tworzenie systemu sterowania
czasowanie_ctrl = ctrl.ControlSystem([reguła1, reguła2, reguła3, reguła4, reguła5, reguła6, reguła7, reguła8, reguła9])

# Tworzenie symulacji
czasowanie = ctrl.ControlSystemSimulation(czasowanie_ctrl)

# Podanie wartości wejściowych do systemu sterowania
# dawka1=float(input("podaj dawkę :"))
# wielkosc1 = float(input("podaj wielkość guza :"))
czasowanie.input['dawka'] = 1
czasowanie.input['wielkosc'] = 7

# Uruchomienie symulacji
czasowanie.compute()

# Wyświetlenie wyniku
print("Czas naświetlania guza:", czasowanie.output['czas'], "dni")

# Wyświetlenie wykresów funkcji przynależności i wyniku
dawka.view()
wielkosc.view()
czas.view(sim=czasowanie)

# # Zapisanie wykresów do pliku
# dawka.view(filename='dawka.png')
# wielkosc.view(filename='wielkosc.png')
# czas.view(sim=czasowanie, filename='czas.png')

plt.show()

