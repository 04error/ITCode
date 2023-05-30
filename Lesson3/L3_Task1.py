import datetime

day = datetime.date.today().day
month = datetime.date.today().month
temperature = None

while temperature is None:
    try:
        temperature = int(input("Сколько на градуснике?\n"))
    except ValueError:
        print("Введите число!")

out_str = f"Сегодня {day}.{month}. На улице {temperature} градусов."
if temperature < 0:
    out_str += " Холодно, лучше остаться дома."

print(out_str)
