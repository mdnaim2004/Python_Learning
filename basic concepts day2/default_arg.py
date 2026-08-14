def full_name(first, last):
    name = f'Full name is : {first} {last}'
    return name

# TAKE  parameter in order (serial wise)
#name = full_name('kadom', 'ali')

name = full_name(last = 'ali', first='kadom')
print(name)



def famous_name(fist, last, title, **addition):
    # Base name
    name = f'{title} {fist} {last}'
    
    # Loop through the dictionary of extra info
    for key, value in addition.items():
        print(f"{key.capitalize()}: {value}")
        name += f' {value}' # Append the value to the name

    print(f"Addition dictionary: {addition}")
    return name

# Notice how 'suffix' is passed as a named argument to pack into **addition
name = famous_name(fist='Taher', last='Ali', title='Hujur', suffix='Tahire')
print(f"Final Name: {name}")