import discord
import random
from giphy_client.rest import ApiException
from pprint import pprint

# Инициализируем клиента Discord
client = discord.Client()

# Инициализируем клиента GIPHY API
giphy_api_key = 'YOUR_GIPHY_API_KEY'
api_instance = giphy_client.DefaultApi()

# Список доступных эмоций и соответствующих гифок
emotions = {
    'поцелуй': 'kiss',
    'объятие': 'hug',
    'подшептывание': 'whisper'
}

# Обработка сообщений
@client.event
async def on_message(message):
    if message.content.startswith('!эмоция'):
        # Выбираем случайную эмоцию из списка
        emotion = random.choice(list(emotions.keys()))
        # Получаем гифку для выбранной эмоции
        try:
            api_response = api_instance.gifs_search_get(giphy_api_key, emotions[emotion], limit=1)
            gif_url = api_response.data[0].images.downsized.url
        except ApiException as e:
            print("Ошибка при получении гифки из GIPHY: %s\n" % e)
            return
        # Отправляем сообщение с гифкой и упоминанием пользователя
        await message.channel.send(f'{message.author.mention}, тебя {emotion} :heart:\n{gif_url}')

# Запуск бота
client.run('YOUR_DISCORD_BOT_TOKEN_HERE')
