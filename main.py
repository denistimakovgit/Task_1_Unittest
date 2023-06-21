def sort_sollection(courses, mentors, durations):
	"""
	Коллекции данных: словари
	Задача 1. Наводим порядок: упорядочиваем курсы по продолжительности
	"""

	courses_list = []
	for course, mentor, duration in zip(courses, mentors, durations):
		course_dict = {"title":course, "mentors":mentor, "duration":duration}
		courses_list.append(course_dict)

	# Сортируем длительности курсов с сохранением порядковых номеров в courses_list
	# Так как lambda-функции ещё не изучались, будем использовать словарь: ключ — duration, значение — исходный номер курса в courses_list
	# Могут быть курсы с одинаковой длительностью, поэтому значение словаря — список индексов
	durations_dict = {}
	for id, course in enumerate(courses_list):
		key = course["duration"]
		durations_dict.setdefault(key, [])
		durations_dict[key].append(id)

	# Сортируем словарь по ключам
	durations_dict = dict(sorted(durations_dict.items()))

	sorted_data = []
	# Выводим курсы, отсортированные по длительности
	for duration, ids in durations_dict.items():
		for id in ids:
			row = f'{courses_list[id]["title"]} - {duration} месяцев'
			sorted_data.append(row)

	return sorted_data

def top_3_names(mentors):
	"""
	Коллекции данных: множества
	Задача 2. Функция Узнайте топ-3 популярных имён
	"""
	# Объединить списки преподавателей по всем курсам
	all_list = []
	[all_list.extend(x) for x in mentors]
	# Отделить имя от фамилии
	all_names_list = [x.split(" ")[0].strip() for x in all_list]
	# Убрать дубли при помощи множеств
	all_names_set = set(all_names_list)

	# Подсчитываем встречаемость каждого имени
	popular = [[all_names_list.count(x), x] for x in all_names_set]
	# Сортируем по убыванию встречаемости
	popular.sort(key=lambda x: x[0], reverse=True)
	# Выводим топ-3 имён
	top_3 = [f"{str(x[1])}: {str(x[0])} раз(а)" for x in popular[:3]]

	return top_3

def uniq_names(mentors):
	"""
	Коллекции данных: множества
	Задача 3. Соберите уникальные имена преподавателей
	"""

	# Объединить списки преподавателей по всем курсам
	all_list = []
	[all_list.extend(x) for x in mentors]
	# Отделить имя от фамилии
	all_names_list = [x.split(" ")[0].strip() for x in all_list]
	# Убрать дубли при помощи множеств
	all_names_set = set(all_names_list)
	# Тренажёру нужен постояннный порядок, поэтому сортируем имена по алфавиту
	all_names_sorted = sorted(list(all_names_set))

	return all_names_sorted

if __name__ == "__main__":
	courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
			   "Frontend-разработчик с нуля"]
	mentors = [
		["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
		 "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
		 "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
		 "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
		["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
		 "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
		 "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
		["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
		 "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
		 "Азамат Искаков", "Роман Гордиенко"],
		["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
		 "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
	]
	durations = [14, 20, 12, 20]

	sorted_collection = sort_sollection(courses, mentors, durations)

	for elem in sorted_collection:
		print(elem)

	top_names = top_3_names(mentors)
	print(", ".join(top_names))

	uniq_mentor_names = uniq_names(mentors)
	print(f'Уникальные имена преподавателей: {", ".join(uniq_mentor_names)}')