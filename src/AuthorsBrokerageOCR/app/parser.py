import re

def extract_client_data(text):
    fio_pattern = r"[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+"
    passport_pattern = r"\d{4}\s?\d{6}"

    fio = re.search(fio_pattern, text)
    passport = re.search(passport_pattern, text)

    return {
        "fio": fio.group(0) if fio else "Не найдено",
        "passport": passport.group(0) if passport else "Не найдено"
    }
