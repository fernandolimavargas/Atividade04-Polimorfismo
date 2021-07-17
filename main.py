'''
Implementar as classes do diagrama a seguir:

Crie o construtor para cada uma das classes

O método acelerar da classe Veículo deve somar o valor passado por parâmetro da velocidadeAtual do veículo.

O método frear da classe Veículo deve subtrair o valor passado por parâmetro da velocidadeAtual do veículo.

O método imprimirInformacoes de cada uma das classes deve exibir na tela o conteúdo de cada um dos atributos da classe.'''


from Veiculo import Veiculo
from Bicicleta import Bicicleta
from Automovel import Automovel
from Moto import Moto
from Carro import Carro

vei = Veiculo('Fiat', 4, 'Carro')
vei.imprimirInformacoes()
print('---------------------------------')
print()
print('==== ACELERAR === ') 
vei.acelerar(5)
vei.imprimirInformacoes()
print('---------------------------------')
print()
print('==== FREAR === ') 
vei.frear(2)
vei.imprimirInformacoes()
print('---------------------------------')

bike = Bicicleta('Caloi', 2, 'Race', 3, 'Nenhum')
bike.imprimirInformacoes()
print('---------------------------------')
print()
print('==== ACELERAR === ') 
bike.acelerar(3)
bike.imprimirInformacoes()
print('---------------------------------')
print()
print('==== FREAR === ') 
bike.frear(1)
bike.imprimirInformacoes()
print('---------------------------------')

moto = Moto('Honda', 2, 'CB500', 350, 'Sim')
moto.imprimirInformacoes()
print('---------------------------------')
print()
print('==== ACELERAR === ') 
moto.acelerar(150)
moto.imprimirInformacoes()
print('==== FREAR === ') 
moto.frear(100)
moto.imprimirInformacoes()
print('---------------------------------')

