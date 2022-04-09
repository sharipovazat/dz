#a
start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'вохдуха', 'была', '+5', 'градусов']
finish_list = []

for element in start_list:
    if element.isdigit():
        finish_list.append(f'"{int(element):02d}"')
    elif element[1:].isdigit():
        finish_list.append(f'"{element[0]}{int(element):02d}"')
    else:
        finish_list.append(element)

print(' '.join(finish_list))


#b (in place)
start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'вохдуха', 'была', '+5', 'градусов']

for index, element in enumerate(start_list):
    if element.isdigit():
        start_list[index] = f'"{int(element):02d}"'
    elif element[1:].isdigit():
        start_list[index] = f'"{element[0]}{int(element):02d}"'

print(' '.join(start_list))