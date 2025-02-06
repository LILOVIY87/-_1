def group_by_type(data):
    
    # Создаём словарь, в котором ключ - название типа переменной в полученном списке аргументов, а зачение - список
    grouped = {}                            
    
    for item in data:
        # Получаем название типа
        item_type = type(item).__name__     

        # Если такого типа ещё нет в нашем словаре - добавляем новый ключ с этим типом и инициализируем пустрой список для него
        # Если такой ключ уже есть - добавляем элемент к уже существующему списку
        grouped.setdefault(item_type,[]).append(item)      

    return grouped

# Пример использования
input_data = [1, "hello", 3.14, [1, 2, 3], "world", 42, True, None, {"key": "value"}]
result = group_by_type(input_data)
for key, value in result.items():
    print(f"{key:8} - {value}")