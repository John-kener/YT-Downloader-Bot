# Coded By John Kener
# Copyright 2021 john-kener


# Yeah brother you can see this little script and now you can
# copy and paste it and publish this as yours 😂💔 :- For Script Thives 💯




import telegram.ext ,os,wget,glob ,youtube_dl
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram import *
from subprocess import run
import urllib

# STARTING BOT
TOKEN = "BOT TOKEN"
updater = telegram.ext.Updater(TOKEN,use_context=True)
print ("\n\n [+] Bot Started Successfully...")
bot = Bot(TOKEN)
print (bot.get_me())
send = updater.dispatcher


# DEFINED REPLIES
def start(update, context):
	frist_name = update.message.chat.first_name
	last_name = update.message.chat.last_name

	slcw = """
Hello {} {}

I am YT WARRIOR telegram bot ...

My Owner :
@john_kener - Owner of sl cyber warriorsᵀᴹ

What Can I Do :
❒ I can scrape youtube videos for you.
❒ Downloading Videos from youtube.
❒ Downloading Youtube video thumbnails.
❒ Downloading Youtube video descriptions.

➥ Use /help command to get help.


🔰 SL CYBER WARRIORSᵀᴹ ⚔
	""".format(frist_name,last_name)

	#BUTTONS
	keyboard = [
	[InlineKeyboardButton("Youtube Channel", callback_data='1',url="https://youtube.com/c/SLCyberWarriors")],
	[InlineKeyboardButton("Telegram Group", callback_data='2',url="https://t.me/By_sstp"),],
	[InlineKeyboardButton("Telegram Channel", callback_data='3',url="https://t.me/by_ss_tp")],
	[InlineKeyboardButton("Officil Website", callback_data='4',url="https://www.slcyberwarriors.com")],
	[InlineKeyboardButton("Official App", callback_data='5',url="https://www.slcyberwarriors.com/about")],
	]

	reply_markup = InlineKeyboardMarkup(keyboard)
	update.message.reply_text(slcw, reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
	query = update.callback_query
	query.answer()
	cho = query.data


def help(update ,context):
	update.message.reply_text("This is help menu ......")


def thumbnail(update,context):
	link = context.args[0]

	# GETTING CHAT ID
	chat_id = update.message.chat_id
	print (f"\n\n[#] GOT YT THUMBNAIL DOWNLOAD REQUEST FROM USER :: {chat_id}")

	# GETTING THUMBNAIL
	os.system(f'youtube-dl --get-thumbnail {link} > thumb.txt')
	with open("thumb.txt","r") as t:
		thumb_link = t.read()
	bot.send_message(chat_id=chat_id,text=thumb_link)
	print ("[✔] THUMBNAIL SENT SUCCESSFULLY")

def description(update,context):
	link = context.args[0]

	# GETTING CHAT ID
	chat_id = update.message.chat_id
	print (f"\n\n[#] GOT YT DISCRIPTION DOWNLOAD REQUEST FROM USER :: {chat_id}")

	# GETTING DESCRIPTION
	extract = {}
	with youtube_dl.YoutubeDL(extract) as ydl:
		data = ydl.extract_info(link,download=False)
	des= (data['description'])
	des = ("<b>🖤 DESCRIPTION </b>\n\n"+des)
	bot.send_message(chat_id=chat_id,text=des,parse_mode=telegram.ParseMode.HTML)
	print ("[✔] DISCRIPTION SENT SUCCESSFULLY")

def download(update,context):
	link = context.args[0]

	# GETTING CHAT ID
	chat_id = update.message.chat_id
	print (f"\n\n[#] GOT YT VIDEO DOWNLOAD REQUEST FROM USER :: {chat_id}")

	# DOWNLOADING VIDEO
	os.system(f"youtube-dl {link}")
	os.system(f"youtube-dl --get-filename {link} > name.txt")
	with open("name.txt","r") as n:
		name = n.read()
		try:
			name = name.replace("\n","")
		except:
			pass
	with open(name,"rb") as v:
		video = v.read()
	try :
		os.remove(name)
	except:
		pass
	bot.send_video(chat_id=chat_id,video=video)
	print ("[✔] VIDEO SENT SUCCESSFULLY")


# SETTING REPLY FOR THE MESSAGE
send.add_handler(telegram.ext.CommandHandler("start",start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
send.add_handler(telegram.ext.CommandHandler("help",help))
send.add_handler(telegram.ext.CommandHandler("download",download))
send.add_handler(telegram.ext.CommandHandler("thumbnail",thumbnail))
send.add_handler(telegram.ext.CommandHandler("description",description))


# RECEIVING NEW MESSAGES
updater.start_polling()
updater.idle()







