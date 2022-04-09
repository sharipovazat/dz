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