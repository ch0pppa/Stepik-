text = input()
decoded_text = ""
i = 0
while i < len(text):
    if text[i:i+3] == "[u-":
      # Нашли начало зашифрованного символа
        end_index = text.find("]", i)
        if end_index == -1:
        # Закрывающей скобки не найдено, выходим из цикла
            break
        unicode_code = int(text[i+3:end_index])
        decoded_text += chr(unicode_code)
        i = end_index + 1
    else:
        decoded_text += text[i]
        i += 1

# Вывод расшифрованного текста
print(f"{decoded_text}")
