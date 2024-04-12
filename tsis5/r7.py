def snake_to_camel(text):
    return ''.join(word.title() for word in text.split('_'))

snake_string = "hellohorwaearea_ajfa_fdiopajfs"
print( snake_string)
print(snake_to_camel(snake_string))