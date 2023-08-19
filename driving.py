driving = input('你有沒有開過車?')
if driving != '有' and driving != '沒有':
    print('請輸入有/沒有')
    raise systemexit

age = input('請輸入年齡')
age = int(age)
if driving == '有':
    if age >= 18:
        print('你通過測驗了')
    else:
        print('低於18歲,你怎麼有開過車?')
elif driving == '沒有'
    if age >= 18:
        print('你年紀到了還沒開過車,要試試看嗎?')
    else:
        print('很好,再過幾年就可以試開看看')
    