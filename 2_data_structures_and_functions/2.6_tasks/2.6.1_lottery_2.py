def gen_ticket_number(count, series, length=6):
    """
    генератор номеров билетов, входные параметры: count - количество билетов,
    series - номер серии, необязательный аргумент length - количество цифр
    в номере, по умолчанию равен 6, выход - строка вида: <номер билета> <серия билета>
    """
    m = gen_number(length)
    n = gen_series(series)
    n_next = next(n)
    total = 1
    while total <= count:
        if total % (10 ** length) == 0:
            m = gen_number(length)
            m_next = next(m)
            total = total + 1
            n_next = next(n)
            yield m_next + " " + n_next.upper()
        else:
            m_next = next(m)
            total = total + 1
            yield m_next + ' ' + n_next.upper()
    else:
        return StopIteration


def gen_series(series):
    """
    генератор серий лотерейных билетов начиная с series по "ZZ" включительно, входные 
    параметры: series -  - номер серии, выход - строка, состоящая из двух заглавных 
    букв латинского алфавита
    """
    series = series.upper()
    ascii_one = ord(series[0])
    ascii_two = ord(series[1])
    while ascii_one != 91:
        if ascii_one <= 90 and ascii_two <= 90:
            yield chr(ascii_one) + chr(ascii_two)
            ascii_two += 1

        if ascii_one < 90 and ascii_two == 91:
            ascii_two = 65
            ascii_one += 1
            yield chr(ascii_one) + chr(ascii_two)
            ascii_two += 1

        if ascii_one == 90 and ascii_two == 90:
            yield chr(ascii_one) + chr(ascii_two)
            ascii_two += 1

        if ascii_one > 90 or ascii_two > 90:
            return StopIteration

def gen_number(length=6):
    """
    генератор номеров лотерейных билетов в одной серии, входные параметры: 
    необязательный аргумент length - количество цифр в номере, по умолчанию равен 6
    """
    total = (10 ** length - 1)
    count = 0

    while count < total:
        count = count + 1
        zero_str = '0' * (length - len(str(count)))
        yield str(zero_str) + str(count)
