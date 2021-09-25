import numexpr
from sympy import diff


def inputData(Data):
    Data = Data.split()
    if len(Data) == 5:
        global formula, E1, E2, responce
        formula = Data[0]
        try:
            a = float(Data[1])
            b = float(Data[2])
            E1 = float(Data[3])
            E2 = float(Data[4])
            res = f"Входные данные: формула {formula}, отрезок [{a}, {b}], E1={E1} E2={E2}\n"
            step1(a, b, res)
            return responce
        except ValueError:
            return 'Введены неверные данные'
    else:
        return 'Введены неверные данные'


def deriv(x):
    try:
        Fx = numexpr.evaluate(str(diff(formula)))
        return round(float(Fx), 3)
    except ValueError:
        return False


def f(x):
    try:
        Fx = numexpr.evaluate(formula)
        return round(float(Fx), 3)
    except ValueError:
        return False


def step1(a, b, res):
    delt = round(b - a, 3)
    res = res+f'1.1\nDel={b}-{a}={delt}\n'
    n = 0
    step2(a, b, delt, res, n)


def step2(a, b, delt, res, n):
    global responce
    n += 1
    y = round(a + 0.5 * delt, 3)
    Fy = deriv(y)
    res = res + f"{n}.2\ny={a}+0.5*{delt}={y}\nf(y)={Fy}\n"
    if Fy:
        if Fy > 0-E1 and Fy < 0+E1:
            Fx = f(y)
            if Fx:
                responce = res + f"Ответ: X = {y}, F(x) = {f(y)}"
            else:
                responce = "Введены неверные данные"
        elif Fy < 0:
            res = res + f"{Fy} < 0 => 3 шаг\n"
            step3(b, y, res, n)
        elif Fy > 0:
            res = res + f"{Fy} > 0 => 4 шаг\n"
            step4(a, y, res, n)


def step3(bOld, y, res, n):
    global responce
    a = y
    b = bOld
    delt = round(b - a, 3)
    res = res + f"{n}.3\na={a}\nb={b}\nDel={b}-{a}={delt}\n"
    if delt <= E2:
        Fx = f(y)
        if Fx:
            responce = res + f"Ответ: X = {y}, F(x) = {f(y)}"
        else:
            responce = "Введены неверные данные"
    else:
        step2(a, b, delt, res, n)


def step4(aOld, y, res, n):
    global responce
    a = aOld
    b = y
    delt = round(b - a, 3)
    res = res + f"{n}.4\na={a}\nb={b}\nDel={b}-{a}={delt}\n"
    if delt <= E2:
        Fx = f(y)
        if Fx:
            responce = res + f"Ответ: X = {y}, F(x) = {f(y)}"
        else:
            responce = "Введены неверные данные"
    else:
        step2(a, b, delt, res, n)



if __name__ == "__main__":
    data = input()
    print(inputData(data))