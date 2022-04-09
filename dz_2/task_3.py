#b (in place)
start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'вохдуха', 'была', '+5', 'градусов']

for index, element in enumerate(start_list):
    if element.isdigit():
        start_list[index] = f'"{int(element):02d}"'
    elif element[1:].isdigit():
        start_list[index] = f'"{element[0]}{int(element):02d}"'

print(' '.join(start_list))