# Задание: составные сообщения об ошибках и поиск подстроки https://stepik.org/lesson/36285/step/9?unit=162401

""" s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}') """

def test_substring(full_string, substring):
    fullstr = str(full_string)
    substr = str(substring)
    assert substr in fullstr, f"expected '{substr}' to be substring of '{fullstr}'"

test_substring("some_text", "some")