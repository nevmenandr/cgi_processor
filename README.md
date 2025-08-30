![LaTeX](https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16956676.svg)](https://doi.org/10.5281/zenodo.16956676)

# Модуль предобработки текстовых материалов для журнала «Цифровые гуманитарные исследования»

## Подготовка текстов

В [журнале](https://pushkinskijdom.ru/zhurnal-tsifrovye-issledovaniya/) статьи публикуются с использованием LaTeX. В tex из docx тексты можно перевести с помощью `pandoc`:

```bash
pandoc -s paper.docx -o paper.tex
```

Однако, текстам на русском языке требуется дополнительная обработка, связанная с правильными тире и пробелами по правилам отечественной типографики. Модуль производит все нужные преобразования автоматически. 

Примеры преобразований:

* `с новым 1970-х гг. в XXI в.:` → `с~новым 1970"=х гг.~в~XXI в.:`
* `социально-экономические` → `социально"=экономические`
* `коллеги - на` → `коллеги — на`
* `В.И. Ленина` → `В.\,И. Ленина`
* `1978-1984~гг.` → `1978--1984~гг.`

Кроме того, все `\emph` заменяются на `\textit`, потому что в системе стилей журнала `\emph` означает не курсив, а подчеркивание.

## Установка

`pip3 install cgi_processor`

## Использование

```python
from cgi_processor import process_file, process_directory

# Обработка одного файла
process_file('example.tex')

# Обработка всех .tex файлов в папке
process_directory('./texts')
```

В результате исполнения этого кода в исходной папке появляется файл с тем же именем, но суффиксом `_processed`, например:

`volodin.tex` → `volodin_processed.tex`

## Другие ресурсы

Веб-сервис с альтернативным функционалом (не полностью совпадающим с текущим) можно найти [здесь](http://nevmenandr.net/cgi-bin/texconv.py). [Репозиторий](https://github.com/nevmenandr/TexTransform) проекта. 

## Цитирование

```
@software{orekhov_2025_16956677,
  author       = {Orekhov, Boris},
  title        = {Модуль предобработки текстовых материалов для
                   журнала «Цифровые гуманитарные исследования»
                  },
  month        = aug,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {v0.1.4},
  doi          = {10.5281/zenodo.16956676},
  url          = {https://doi.org/10.5281/zenodo.16956676},
}
```
