
main_chain = []
element = 0
row = 1
disappear_limit = 3
position = 0
row_counter = 0


chain_length = int(input('Склько всего шариков в линии от 0 до 1000: '))
while chain_length < 0 or chain_length > 1000:
    chain_length = int(input('От 0 до 1000!: '))


print(f'Последовательно введите значение цветов шариков, всего {chain_length}. ')
while position < chain_length:
    element = int(input('Значение от 0 до 9: '))
    while element < 0 or element > 9:
        element = int(input('ОТ 0 ДО 9!!! '))
    main_chain.append(element)
    if position != 0:
        if main_chain[position] == main_chain[position - 1]: 
            row += 1
        elif row >= disappear_limit:
            row_counter += 1
            row = 1
    position += 1
    if (position == chain_length and row >= 3  and row_counter == 1) or row_counter > 1 :
        print('В линии не может быть больше одной непрерывной цепочки из 3-х и более элементов.')
        print('Ввод отменен. Начните с первого шарика')
        position = 0
        row_counter = 0
        main_chain.clear()
   
print(main_chain)

row = 1
position = 1
while position < len(main_chain):
    if main_chain[position] == main_chain[position - 1]:
        row += 1
        position += 1
    elif row >= disappear_limit:
        for i in range(position - 1, position - row - 1, -1):
            main_chain.pop(i)
        row = 1
        position = 1
    else:
        row = 1
        position += 1
    
print(chain_length - len(main_chain))
        