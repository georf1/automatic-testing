from automatic_testing.capitalize import capitalize

def test_capitalize():
    assert capitalize('hello') == 'Hello'
    assert capitalize('Hi!') == 'Hi!'
    assert capitalize('') == ''
    print('Все тесты пройдены!')

