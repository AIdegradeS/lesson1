def get_summ(one, two, delimiter='&'):
    result = '{}{}{}'.format(one, delimiter, two)
    return result

print(get_summ('Learn', 'python').upper())