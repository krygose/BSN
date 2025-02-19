# Komunikacja 


## Pliki do użytku
proj.py jest to plik do użycia z urządzeniem fizycznym
mock.py jest to plik do użycia z wirtualną atrapą uzywana do testów


## Moduły
-numpy
-serial
-argparse
-ast
Instalacja

`pip install numpy pyserial`


## Użycie 

configstart – wysyła komendę rozpoczęcia konfiguracji

neuronsetup – konfiguruje neurony

synapses – wysyła synapsy na podstawie plików wag

configend – wysyła komendę zakończenia konfiguracji

aer – wysyła i odczytuje dane z urządzenia

Użycie tych argumentów powinno przebiegać zgodnie z podaną kolejnością od górnego do dolnego


### Przykładowe użycie 
`python mock.py -d neuronsetup`

## Pliki danych 

proj.py – główny skrypt programu

mock.py – główny skrypt programu 

neuron_weights_first.txt – plik z wagami pierwszej warstwy

neuron_weights_second.txt – plik z wagami drugiej warstwy

image_1_spikes.txt – dane wejściowe pojedynczego obrazka 
