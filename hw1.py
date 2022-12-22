class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key=lambda x: x[0] - x[1]) # Сортируем список, высчитывая разности перелетов.
        n = len(costs) // 2                   # Выбираем средний индекс списка
        res = 0                               # результат по умолчанию равен нулю
        for i in range(len(costs)):           # Для каждого индекса в списке
            n -= 1                            # Понижаем значение n
            if n < 0:                         # Если n меньше нуля
                res += costs[i][1]            # То увеличиваем res на стоимость перелета в город b
            else:                             # Иначе
                res += costs[i][0]            # увеличиваем res на стоимость перелета в город a
        return res                            # Вовзращаем результат