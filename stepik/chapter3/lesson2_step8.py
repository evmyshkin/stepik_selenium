# Задание: составные сообщения об ошибках https://stepik.org/lesson/36285/step/8?unit=162401

def test_input_text(expected_result, actual_result):
    str1 = str(expected_result)
    str2 = str(actual_result)
    assert expected_result == actual_result, f"expected {str1}, got {str2}"

test_input_text(15, 11)
