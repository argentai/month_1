
# # Напишите программу, которая принимает имя файла и выводит его расширение.
# # ПРИМЕР: 
 
#   # Ввод: "my_photo.png"
#   # Вывод: "Расширение файла - png"
 
# # Если расширение у файла определить невозможно, скажите пользователю что расширение не найдено.



file_name = input("Введите имя файла:")
point = file_name.count(".")
if point != 1:
	print ("расширение не найдено")
else:
	print ("есть расширение")
