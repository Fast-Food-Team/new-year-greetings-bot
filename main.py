import telebot
from telebot import types
import random
from secrets import secrets

token = secrets.get('BOT_API_TOKEN')
bot = telebot.TeleBot(token)

first_part = ('с новым счастьем',
              '365 новых дней — 365 новых шансов',
              'наслаждайтесь каждым его моментом',
              'примите мои искренние поздравления',
              'годом Кролика',
              'новый старт начинается сегодня',
              'и пусть самые лучшие сюрпризы будут у вас впереди')

second_part = ('много новых достижений, крепкого здоровья и любьви, пусть задуманное сбудется',
               'чтобы этот год подарил много поводов для радости и счастливых моментов',
               'чтобы будущий год принёс столько радостей, сколько дней в году, и чтобы каждый день дарил вам улыбку',
               'вам прекрасного года, полного здоровья и благополучия',
               'чтобы Кролик принёс в вашу семью любовь, нежность, взаимпонимание и счастье',
               'всем в Новом году быть здоровыми, красивыми, любимыми и успешными',
               'чтобы сбылось всё то, что вы пожелали. Все цели были достигнуты, а планы перевыполнены')

third_part = ('Новый год принесёт много радостных и счастливых дней!',
              'каждый новый миг наступающего года приносит в дом счастье, везение, уют и тепло!',
              'всё, что мы планировалим, обязательно сбудется!',
              'наступающий год станет самым плодотворным годом в вашей жизни!',
              'год будет полон ярких красок, приятных впечатлний и радостных событий!',
              'этот год будет ВАШИМ годом!',
              'Новый год принесёт всё, о чём вы мечтаете и немного больше!')

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🎄 Сгенерировать")
    btn2 = types.KeyboardButton("❓ Информация")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет 👋, {0.first_name}! Я помогу тебе сгенерировать новогоднее поздравление. "
                                           "Просто нажми на кнопку «Сгенерировать» и всё будет готово!\n"
                                           "\n"
                                           "Если у тебя есть идеи, то нажимай на кнопку «Информация» и отправляй предложение. "
                                           "Код проекта отрыт, поэтому можешь делать форк и развивать самостоятельно.\n"
                                           "\n"
                                           "🎄 🎄 🎄\n".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "🎄 Сгенерировать"):
        bot.send_message(message.chat.id, text=f"С новым годом, {random.choice(first_part)}, "
                                               f"я желаю {random.choice(second_part)}, "
                                               f"и пусть {random.choice(third_part)}")
    elif (message.text == "❓ Информация"):
        bot.send_message(message.chat.id, 'Made with ❤️ by human\n'
                                          '\n'
                                          '[GitHub](https://github.com/Fast-Food-Team/new-year-greetings-bot) | '
                                          '[Habr](https://habr.com/ru/users/daniilshat/) | '
                                          '[Telegram](t.me/wa1pper) | \n'
                                          '\n'
                                          '[Fast Food Team](https://github.com/Fast-Food-Team) 2022', parse_mode='MARKDOWN', disable_web_page_preview=True)
    elif (message.text):
        bot.send_message(message.chat.id, text="{0.first_name}, пожалуйста, пользуйся кнопками.".format(message.from_user))

bot.polling(none_stop=True, interval=0)
