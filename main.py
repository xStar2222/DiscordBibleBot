import json
import discord
import requests
import random
import os
from discord.activity import Game
from discord.ext import commands
from bs4 import BeautifulSoup


intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='!bb-help'))



@client.event
async def on_message(message):
    command = message.content
    if command.startswith('!random'):
        with open('bible.json') as json_file:
            data = json.load(json_file)
        random_key = random.choice(list(data.keys()))
        random_value = data[random_key]
        await message.reply(f"{random_key}\n\n{random_value}")
    elif command == '!Genesis':
        with open('genesis.json') as json_file:
            data1 = json.load(json_file)
        random_key1 = random.choice(list(data1.keys()))
        random_value1 = data1[random_key1]
        await message.reply(f"{random_key1}\n\n{random_value1}")


    elif message.content.lower() == '!books':
        await message.reply("**Old Testament Books**" "\n" "\n" "1. Genesis" "\n" "2. Exodus" "\n" "3. Leviticus" "\n" "4. Numbers" "\n" "5. Deuteronomy" "\n" "6. Joshua" "\n" "7. Judges" "\n" "8. Ruth" "\n" "9. 1 Samuel" "\n" "10. 2 Samuel" "\n" "11. 1 Kings" "\n" "12. 2 Kings" "\n" "13. 1 Chronicles" "\n" "14. 2 Chronicles" "\n" "15. Ezra" "\n" "16. Nehemiah" "\n" "17. Esther" "\n" "18. Job" "\n" "19. Psalms" "\n" "20. Proverbs" "\n" "21. Ecclesiastes" "\n" "22. Song of Solomon" "\n" "23. Isaiah" "\n" "24. Jeremiah" "\n" "25. Lamentations" "\n" "26. Ezekiel" "\n" "27. Daniel" "\n" "28. Hosea" "\n" "29. Joel" "\n" "30. Amos" "\n" "31. Obadiah" "\n" "32. Jonah" "\n" "33. Micah" "\n" "34. Nahum" "\n" "35. Habakkuk" "\n" "36. Zephaniah" "\n" "37. Haggai" "\n" "38. Zechariah" "\n" "39. Malachi" "\n" "\n" "**New Testament Books**" "\n" "\n" "40. Matthew" "\n" "41. Mark" "\n" "42. Luke" "\n" "43. John" "\n" "44. Acts" "\n" "45. Romans" "\n" "46. 1 Corinthians" "\n" "47. 2 Corinthians" "\n" "48. Galatians" "\n" "49. Ephesians" "\n" "50. Philippians" "\n" "51. Colossians" "\n" "52. 1 Thessalonians" "\n" "53. 2 Thessalonians" "\n" "54. 1 Timothy" "\n" "55. 2 Timothy" "\n" "56. Titus" "\n" "57. Philemon" "\n" "58. Hebrews" "\n" "59. James" "\n" "60. 1 Peter" "\n" "61. 2 Peter" "\n" "62. 1 John" "\n" "63. 2 John" "\n" "64. 3 John" "\n" "65. Jude" "\n" "66. Revelation")
    elif message.content.lower() == '!bb-help':
        await message.reply("Hi! Heres A Few Things I Can Do!" "\n" "\n" "`!books` - Provides a list of all the books of the Bible" "\n" "\n" "`!random` - Sends a random Bible Verse" "\n" "\n" "`!links` - Sends a few helpful links" "\n" "\n" "`!bb-help` - Sends this message" "\n" "\n" "`!info [topic]` - Allows you to pick a topic and the bot will respond with 5 verses on that topic" "\n" "\n" "To send a certain verse, please format the message like this, `!Genesis 1:1` Capitalization Matters!" "\n" "\n" "---------------------------------------------------------------------" "\n" "If you have any questions or suggestions please contact `xStar#2222`")
    elif message.content.lower() == "!links":
        await message.reply("Full KJV Bible - <https://www.kingjamesbibleonline.org/>" "\n" "\n" "Official Support Server - https://discord.gg/5PmJ3DHa7u")
    elif command.startswith('!info'):
        user_input = message.content[8:]
        website_url = "https://www.openbible.info/topics/"
        params = {"q": user_input}
        response = requests.get(website_url, params=params)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        elements = soup.find_all(class_='bibleref')[:5]
        for element in elements:
                await message.channel.send(element.get_text())
    elif message.content.startswith("!"):
            command = message.content[1:]
            with open('bible.json') as json_file:
                data = json.load(json_file)
            if command in data:
                await message.reply(data[command])  
            else:
                await message.reply("Hmmm, That Verse Wasn't Found." "\n" "\n" "Example: `!Genesis 1:1`" "\n" "\n" "Capitalization Matters!")


client.run('YOUR TOKEN HERE')
