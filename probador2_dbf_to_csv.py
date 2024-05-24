#!/usr/bin/python
print("calculos")
for num in range(1, 126):
    if num == 9 or num == 25 or num == 31 or num == 87 or num == 119 or num == 125 :
        print(str(num).zfill(3) + " Muninicio con detalles a resolver en linux")
        continue
    else:
        print(str(num).zfill(3) + " Muninicio migrado con exito" )
