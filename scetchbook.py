def generate_diff(first_file, second_file):
    result = []
    for sorted_key in sort_keys(first_file, second_file)['added']:
        result.append(f'  + {sorted_key}: {second_file[sorted_key]}')
    for sorted_key in sort_keys(first_file, second_file)['deleted']:
        result.append(f'  - {sorted_key}: {first_file[sorted_key]}')
    for sorted_key in sort_keys(first_file, second_file)['unchanged']:
        result.append(f'    {sorted_key}: {first_file[sorted_key]}')
    for sorted_key in sort_keys(first_file, second_file)['changed']:
        result.append(f'  - {sorted_key}: {first_file[sorted_key]}')
        result.append(f'  + {sorted_key}: {second_file[sorted_key]}')
    result.sort(key=lambda key: key[4])
    result.insert(0, '{')
    result.append('}')
    print('\n'.join(result))



a = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
}

b = {
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io"
}

generate_diff(a, b)