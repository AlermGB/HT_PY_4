
main_chain = []
element = 0
row = 1
disappear_limit = 3
result_sum = 0

chain_length = int(input('Склько всего шариков в линии от 0 до 1000: '))
while chain_length < 0 or chain_length > 1000:
    chain_length = int(input('От 0 до 1000!: '))

print(f'Последовательно введите значение цветов шариков, всего {chain_length}. ')
for i in range(chain_length):
    element = int(input('Значение от 0 до 9: '))
    while element < 0 or element > 9:
        element = int(input('ОТ 0 ДО 9!!! '))
    main_chain.append(element)

print(main_chain)

for i in range(1, len(main_chain)):
    if main_chain[i] == main_chain[i-1]:
        row += 1
    elif row >= disappear_limit:
        result_sum += row
    else:
        row = 1
if row >= disappear_limit:
        result_sum += row

print(result_sum)
        
