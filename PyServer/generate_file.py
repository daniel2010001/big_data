def generate_file(param1, param2):
    with open('generated_file.txt', 'w') as file:
        file.write(f'Parámetro 1: {param1}\n')
        file.write(f'Parámetro 2: {param2}\n')

if __name__ == '__main__':
    import sys
    param1 = sys.argv[1]
    param2 = sys.argv[2]
    generate_file(param1, param2)