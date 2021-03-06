class Driver:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class PREC:
    descr = "Новизна проекта"
    drivers = [
        Driver("Полное отсутствие прецедентов, полностью непредсказуемый проект", 6.2),
        Driver("Почти полное отсутствие прецедентов, в значительной мере непредсказуемый проект", 4.96),
        Driver("Наличие некоторого количества прецедентов", 3.72),
        Driver("Общее знакомство с проектом", 2.48),
        Driver("Значительное знакомство с проектом", 1.24),
        Driver("Полное знакомство с проектом", 0)
    ]


class FLEX:
    descr = "Гибкость процесса разработки"
    drivers = [
        Driver("Точный, строгий процесс разработки", 5.07),
        Driver("Случайные послабления в процессе", 4.05),
        Driver("Некоторые послабления в процессе", 3.04),
        Driver("Большей частью согласованный процесс", 2.03),
        Driver("Некоторое согласование процесса", 1.01),
        Driver("Заказчик определил только общие цели", 0)
    ]


class RESL:
    descr = "Разрешение рисков в архитектуре системы"
    drivers = [
        Driver("Малое (20%)", 7),
        Driver("Некоторое (40%)", 5.65),
        Driver("Частое (60%)", 4.24),
        Driver("В целом (75%)", 2.83),
        Driver("Почти полное (90%)", 1.41),
        Driver("Полное (100%)", 0)
    ]


class TEAM:
    descr = "Сплоченность команды"
    drivers = [
        Driver("Сильно затрудненное взаимодействие", 5.48),
        Driver("Несколько затрудненное взаимодействие", 4.38),
        Driver("Некоторая согласованность", 3.29),
        Driver("Повышенная согласованность", 2.19),
        Driver("Высокая согласованность", 1.1),
        Driver("Взаимодействие как в едином целом", 0)
    ]


class PMAT:
    descr = "Уровень зрелости процесса разработки"
    drivers = [
        Driver("Уровень 1 СММ", 7),
        Driver("Уровень 1+ СММ", 6.24),
        Driver("Уровень 2 СММ", 4.68),
        Driver("Уровень 3 СММ", 1.12),
        Driver("Уровень 7 СММ", 1.56),
        Driver("Уровень 5 СММ", 0)
    ]


class Cocomo2:
    Factors = [
        PREC,
        FLEX,
        RESL,
        TEAM,
        PMAT
    ]

    @staticmethod
    def get_p(factors_idxs):
        p = 0
        n = len(factors_idxs)
        for i in range(n):
            p += Cocomo2.Factors[i].drivers[factors_idxs[i]].value
        p /= 100
        p += 1.01
        return p
