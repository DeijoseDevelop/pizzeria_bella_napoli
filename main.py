salir = False
pv = False
pnv = False
cuenta = 0
while salir == False:
  print(' Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t Vegetariana\n\t\t Precio: 5$ \n\t No vegetariana \n\t\t Precio: 6$ \n Ambas pizzas traen Mozzarella y Tomate \n Cada ingrediente tiene un costo adicional \n')
  pizza = input('¿Deseas ordenar una pizza vegetariana? \n>>>')
  ingredientes = ['Mozzarella', 'Tomate']
  si = 'si'
  no = 'no'
  if pizza == si:
    cuenta += 5
    while pv == False:
      ingrediente = int(input('Elige los ingredientes para tu pizza vegetariana\n0.Salir\n1.Pimiento: 2$\n2.Tofú: 1$\n>>>'))
      if ingrediente == 0:
        pv = True
        print('Elegiste la pizza vegetariana con los ingredientes: ', ', '.join(ingredientes))
        print('Su costo total es:',cuenta,'$')
        salir = True
      elif ingrediente == 1:
        cuenta += 2
        print('Has elegido pimiento,','van',cuenta,'$', '¿algo más?\n')
        ingredientes.append('Pimiento')
      elif ingrediente == 2:
        cuenta += 1
        print('Has elegido tofú,','van',cuenta,'$', '¿algo más?\n')
        ingredientes.append('Tofú')
      else:
        print('Valor introducido no válido')
  elif pizza == no:
    cuenta += 6
    while pnv == False:
      ingrediente = int(input('Elige los ingredientes para tu pizza no vegetariana\n0.Salir\n1.Peperoní: 2$\n2.Jamón: 3$\n3.Salmón: 3$\n>>>'))
      if ingrediente == 0:
        pnv = True
        print('Elegiste la pizza no vegetariana con los ingredientes: ', ', '.join(ingredientes))
        print('Su costo total es:',cuenta,'$')
        salir = True

      elif ingrediente == 1:
        cuenta += 2
        print('Has elegido peperoní,','van',cuenta,'$', '¿algo más?\n')
        ingredientes.append('Peperoní')
      elif ingrediente == 2:
        cuenta += 3
        print('Has elegido jamón,','van',cuenta,'$', '¿algo más?\n')
        ingredientes.append('Jamón')
      elif ingrediente == 3:
        cuenta += 3
        print('Has elegido salmón,','van',cuenta,'$', '¿algo más?\n')
        ingredientes.append('Salmón')
      else:
        print('Valor introducido no válido')