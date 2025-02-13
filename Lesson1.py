# def is_valid_email(email: str) -> bool:
#    if type(email) != str:
#       return None
#    if email.count("@") != 1:
#       return False
#    local_part, domain_part = email.split("@")
#    if not local_part or not domain_part:
#       return False
#    if domain_part.count(".") != 1:
#       return False
#
#    return True
#
# def calculate_power(base: int | float, exponent: int | float) -> int | float:
#    return base ** exponent
#
#
# def merge_dicts(dict1: dict, dict2: dict) -> dict:
# 	result = dict1.copy()
# 	result.update(dict2)
# 	return result
# print(merge_dicts({1:2, 3:4, 5:6}, {7:8, 9:0, 10:11}))

categories = {
   "Электроника": {
       "Телефоны": {
           "Смартфоны": {},
           "Проводные": {}
       },
       "Компьютеры": {
           "Ноутбуки": {},
           "Стационарные": {
               "Игровые": {},
               "Для работы": {}
           }
       }
   },
   "Одежда": {
       "Мужская": {
           "Джинсы": {},
           "Куртки": {}
       }
   }
}
def extract_categories(list_cat, parent_path=[]):
    paths = []
    for key, val in list_cat.items():
        paths.append(key)
        if type(val) == dict:
            extract_categories(val, paths)
        else:
            return paths
    return paths
pits = extract_categories(categories)
for pith in pits:
   print(pith)
