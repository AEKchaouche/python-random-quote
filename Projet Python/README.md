
## Exemple instruction break
Dans cet exemple, nous recherchons un nombre «88» dans la liste de nombres donnée. La condition est d'afficher tous les nombres jusqu'à ce que le nombre «88» soit trouvé et quand il est trouvé, terminer la boucle et ne pas afficher le reste des nombres.

# programme pour afficher tous les éléments avant le numéro 88

for num in [11, 9, 88, 10, 90, 3, 19]:
   print(num)
   if(num==88):
	   print("The number 88 is found")
	   print("Terminating the loop")
	   break
Output:
11
9
88
The number 88 is found
Terminating the loop