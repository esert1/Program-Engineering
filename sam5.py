class DataValidationError(Exception):
    """
    Упрощенное пользовательское исключение для валидации данных.
    """
    def __init__(self, field_name, value, reason):
        self.field_name = field_name
        self.value = value
        self.reason = reason
        super().__init__(f"Ошибка валидации поля '{field_name}': значение '{value}' - {reason}")

# Функция для проверки пароля
def validate_password(password):
    """
    Проверяет сложность пароля.
    """
    if len(password) < 8:
        raise DataValidationError("пароль", password, "длина менее 8 символов")
    
    if not any(char.isdigit() for char in password):
        raise DataValidationError("пароль", password, "отсутствуют цифры")
    
    if not any(char.isalpha() for char in password):
        raise DataValidationError("пароль", password, "отсутствуют буквы")
    
    return "Пароль прошел валидацию"

# Функция для проверки имени пользователя
def validate_username(username):
    """
    Проверяет имя пользователя.
    """
    if len(username) < 3:
        raise DataValidationError("имя пользователя", username, "слишком короткое (менее 3 символов)")
    
    if len(username) > 20:
        raise DataValidationError("имя пользователя", username, "слишком длинное (более 20 символов)")
    
    if not username.isalnum():
        raise DataValidationError("имя пользователя", username, "содержит запрещенные символы")
    
    return f"Имя пользователя '{username}' валидно"

if __name__ == '__main__':
    print("=== Тестирование упрощенного исключения DataValidationError ===")
    
    tests = [
        ("validate_password", "12345", "короткий пароль"),
        ("validate_password", "password", "пароль без цифр"),
        ("validate_password", "12345678", "пароль без букв"),
        ("validate_password", "Pass1234", "валидный пароль"),
        ("validate_username", "ab", "короткое имя"),
        ("validate_username", "very_long_username_here", "длинное имя"),
        ("validate_username", "user@name", "имя с запрещенными символами"),
        ("validate_username", "john_doe123", "валидное имя"),
    ]
    
    for func_name, test_value, description in tests:
        print(f"\n{description}:")
        try:
            if func_name == "validate_password":
                result = validate_password(test_value)
            else:
                result = validate_username(test_value)
            print(f"✓ {result}")
        except DataValidationError as e:
            print(f"✗ {e}")
