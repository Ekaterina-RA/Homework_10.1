import logging

# Настройка логирования для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)  # Уровень не ниже DEBUG

# Настройка обработчика для записи логов в файл
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Настройка формата записей в логе
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    logger.debug(f"Номер карты: {card_number}")  # Логирование входного параметра
    masked_number = ""

    for i in range(len(card_number)):
        if i < 6 or i >= len(card_number) - 4:
            masked_number += card_number[i]
        elif card_number[i].isdigit():
            masked_number += "*"
        else:
            masked_number += ""

    masked_number = " ".join(
        [masked_number[i : i + 4] for i in range(0, len(masked_number), 4)]
    )
    logger.info(
        f"Сгенерирована маска номера карты: {masked_number}"
    )  # Логирование успешного результата
    return masked_number


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    logger.debug(
        f"Получен номер счета: {account_number}"
    )  # Логирование входного параметра
    if len(account_number) < 4:
        logger.warning("Номер счета слишком короткий.")  # Логирование предупреждения
        return account_number

    masked_account = "**" + account_number[-4:]
    logger.info(
        f"Сгенерирована маска номера счета: {masked_account}"
    )  # Логирование успешного результата
    return masked_account


if __name__ == "__main__":
    print(get_mask_card_number("1234567890123456"))
    print(get_mask_account("123456789012"))
    print(get_mask_account("123"))  # Проверка на короткий номер счета
