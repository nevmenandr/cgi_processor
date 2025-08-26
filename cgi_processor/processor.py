import re
from pathlib import Path


def process_text(text: str) -> str:
    """
    Обрабатывает текст с помощью регулярных выражений.
    """
    # Пример замены: вставить ~ между короткими и длинными словами
    text = re.sub(r'([А-ЯЁ]\.)?\s?([А-ЯЁ]\.)\s?([А-ЯЁ][а-яё])', r'\1\,\2\,\3', text)
    text = re.sub(r'([А-Я][а-яё]+)\s+([А-ЯЁ]\.)(\s|\,)?([А-ЯЁ]\.)(\s|\,)', r'\1~\2\,\3 ', text)
    text = re.sub(r'([А-Я][а-яё]+)~([А-ЯЁ]\.)\\,\s', r'\1\,\2 ', text)
    text = re.sub(r'([А-Я][а-яё]+)\s+([А-ЯЁ]\.)\\,([А-ЯЁ]\.)\\,([А-Я][а-яё]+)\s', r'\1\,\2\,\3 \4 ', text)
    text = re.sub(r'([А-Я][а-яё]+)\s+([А-ЯЁ]\.)\\,([А-Я][а-яё]+)\s', r'\1\,\2 \3 ', text)
    text = re.sub(r'\b([а-яё]{1,2})(,|\.|;|:)?\s+([а-яёxiclv]+)', r'\1\2~\3', text, flags=re.IGNORECASE)
    text = re.sub(r'\b([а-яё]{1,2})(,|;|:)?\n', r'\1\2~', text, flags=re.IGNORECASE)
    text = re.sub(r'~([а-яё]+)(,|\.|;|:)?\s+([а-яё]{1,2})\b', r' \1\2~\3', text, flags=re.IGNORECASE)
    text = re.sub(r'(\\,[А-ЯЁ]\.)(~|\\,)([А-Я][а-яё]+)\b', r'\1 \3', text)
    text = re.sub(r'и\s+т\.\s?д\.', r'и~т.\,д.', text)
    text = re.sub(r' (-|---)(\s|\n)', r' —\2', text)
    text = re.sub(r'([0-9])(-|—)([0-9])', r'\1--\3', text)
    text = re.sub(r'([а-яё0-9]+)(-|—)([а-яё]+)', r'\1"=\3', text, flags=re.IGNORECASE)
    text = re.sub(r'(Т\.|№|С\.)\s?([0-9])', r'\1\,\2', text)
    text = re.sub(r'([0-9])\s?(с\.)', r'\1~\2', text)
    text = text.replace(r'\\emph', r'\\textit')
    return text


def process_file(filepath: str) -> str:
    """
    Обрабатывает одиночный файл и сохраняет результат с суффиксом _processed.
    Возвращает путь к новому файлу.
    """
    input_path = Path(filepath)
    if not input_path.is_file():
        raise FileNotFoundError(f"Файл не найден: {filepath}")

    text = input_path.read_text(encoding='utf-8')
    processed = process_text(text)

    output_path = input_path.with_name(f"{input_path.stem}_processed{input_path.suffix}")
    output_path.write_text(processed, encoding='utf-8')
    return str(output_path)


def process_directory(directory: str, pattern: str = '*.tex') -> list:
    """
    Обрабатывает все файлы в директории, соответствующие шаблону (по умолчанию *.tex).
    Возвращает список путей к новым файлам.
    """
    dir_path = Path(directory)
    if not dir_path.is_dir():
        raise NotADirectoryError(f"Директория не найдена: {directory}")

    processed_files = []
    for file_path in dir_path.glob(pattern):
        if file_path.is_file():
            output_file = process_file(str(file_path))
            processed_files.append(output_file)

    return processed_files

