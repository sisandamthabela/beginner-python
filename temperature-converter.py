print('=========================')
print('  Temperature Converter  ')
print('=========================')
print('What is the current temperature?')
temperature = input('')
print('Fahrenheit(F) or Celsius(C)')
unit = input('').title()

if unit == 'F' or unit == 'Fahrenheit':
    temperature_celsius = ( int(temperature) - 32 ) * 5/9
    print(f'{int(temperature)}°F is {int(temperature_celsius)}°C ')
elif unit == 'C' or unit == 'Celsius' :
    temperature_fahrenheit = (int(temperature) * 9/5 ) + 32
    print(f'{int(temperature)}°C is {int(temperature_fahrenheit)}°F')
else:
    print('Invalid input')