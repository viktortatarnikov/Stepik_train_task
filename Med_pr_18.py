with open('cyrillic.txt', 'r', encoding='utf-8') as old_file, open('transliteration.txt', 'w', encoding='utf-8') as new_file:
    d = {
        'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
        'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
        'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
        'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
    }

    line_old = old_file.read().strip()
    # line_lower = line_old.lower()
    for simb in line_old:
        if simb.lower() in d:
            if simb.isupper():
                print(d[simb.lower()].capitalize(), file=new_file, end='')
            else:
                print(d[simb], file=new_file, end='')
        else:
            print(simb, file=new_file, end='')
