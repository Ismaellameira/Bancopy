from models.cliente import Cliente
from models.conta import Conta


nef: Cliente = Cliente('Nef ramos', 'nef@gmail.com', '123.456.786-03', '12/08/1987')

carlos: Cliente = Cliente('Carlos augusto', 'carlos@gmail.com', '123.456.654-03', '20/06/1978')

# print(nef)
# print(carlos)

contan: Conta = Conta(nef)
contac: Conta = Conta(carlos)

print(contan)
print(contac)