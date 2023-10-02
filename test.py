import openai

# Замените 'your_api_key' на ваш собственный API ключ
api_key = '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'

# Функция для отправки запроса к GPT-3 (или GPT-4)
def ask_gpt(question):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-002",  # Выберите желаемый движок
        prompt=question,
        max_tokens=50  # Максимальное количество токенов в ответе
    )
    return response.choices[0].text

# Запрос о времени
question = "Какое сейчас время?"
response = ask_gpt(question)
print(response)
