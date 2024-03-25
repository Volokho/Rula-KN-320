a = True # це змінна з булевим значенням
b = True # якщо хочемо побачити не виконання умов, то тут потрібно поставити False

assert a == b, "Твердження не є істинним" # після твердження ми можемо записати текст помилки або допомогу чому маємо помилку 

# така перевірка assert повністю підпадає під конструкцію блоку if 
if True == True:
    print("Наша умова виконалась, твердження є вірним")
else:
    raise AssertionError ("Твердження не є істинним")
c = 1 # тут змінна з числом цілого типу
d = "1" # а тут вже є стрічка 
e = 1.0 # тут число з плаваючою крапкою

# зробимо твердження на правильність типів даних для наших змінних
assert isinstance(a,bool), "Змінна не відноситься до логічного типу даних"
assert isinstance(c, int), "Змінна не є цілого типу"
assert isinstance(d, str), "Змінна не є стрічкою"

# можемо перевіряти власне значення на відповідальність чомусь
assert c == e, "Значенння не співпадають"
# твердження нижче будуть видавати помилки тому що:
# тому що не співпадають типи значення що перевіряються
#assert type(c) is type(e), f"{type(c)} не відповідає {type(e)}"
# тому що не співпадають значення, число 1 не є рівним символу 1

#assert c ==d, f"Значення не є рівними бо {c} не рівне {d}"

# тому що не співпадають типи даних, числа та стрічки
#assert type(c) is type(e), f"{type(c)} не відповідає {type(e)}"

# може бути твердження не на чітку рівність а на попаданняв певний діапазон
assert c >= 1, "Значення є менше за 1"
assert (0 < c < 4), "Не відповідає діапазону від 0 до 4"
assert d in[1, 1.0, "1"], " Дане значення не відповідає наперед заданим значенням "
# ми можемо писати комплексні перевірки у вигляді функції та використовувати ці функції як твоердження

def check(n):
    return n > 0


assert check(c), "перевірка значення в середині функції не є істинною"

def check_numbers(n:list, t):
    """Функція перевіряє чи в списку містяться дані заданого типу"""
    d = [x for x in n if isinstance(x, int)]
    len(d)

Test_list = [check_numbers([1, "1",1.0,2, "2", 2.5])] # Ми знаємо що у цьому списку лише 2 значення які відповідають цілому типу даних
f = check_numbers(Test_list, str)
print(f"Перевіряємо вивід функції {check_numbers(Test_list)}")
assert check_numbers(Test_list) == 2, "Тестовий масив повинен повернути значення 2"
# Таку саму логіку з твердженнями ми можемо виконувати на об'єктах
class Test:
    pass

o = Test()
h = Test()
assert isinstance(o, Test)
assert o.__hash__() == hash(o), "об'єкти мають одинаковий Хеш, тобто вони є ідентичними"
# Два об'єкти навіть одного класу не будуть одинаковими, бо кожен об'єкт є унікальним
#assert o ==h, f"{o} не буде те саме що {h}"
class SwordMock:
    pass

assert type (object) 

print (type())
assert hasattr (object,"damage")
sw = SwordMock() # створений макет меча
