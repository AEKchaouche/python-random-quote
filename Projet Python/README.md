
## Exemple instruction break
Dans cet exemple, nous recherchons un nombre �88� dans la liste de nombres donn�e. La condition est d'afficher tous les nombres jusqu'� ce que le nombre �88� soit trouv� et quand il est trouv�, terminer la boucle et ne pas afficher le reste des nombres.

# programme pour afficher tous les �l�ments avant le num�ro 88

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