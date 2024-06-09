n = int(input('Введите число от 3 до 20:' "\n"))
if n < 3 or n > 20:
    print('Некорректно введено число, попробуйте повторить!')
else:
    set_ = []


    def result():
        for i in range(1, n):
            for j in range(i, n):
                if n % (i + j) == 0:
                    number1 = i
                    number2 = j
                    if i == j:
                        continue
                    set_.extend([f'{number1}' f'{number2}'])

        print('Искомый порядок: ', *set_)
        result_ = ''.join(set_)
        print('Либо в таком виде:', result_)


    result()
