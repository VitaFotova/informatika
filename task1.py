b = int(input('Введите длину: '))
c = int(input('Введите ширину: '))
SQFT_PER_ACRE  = .000022956841 * b * c 
print(SQFT_PER_ACRE, 'акров')
