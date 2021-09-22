from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from utils.Logger import *
from utils.Config import Config

Config = Config()


def getMessage(message, action):
    try:
        ALLOWED_CHAT_TYPES = config.get("ALLOWED_CHAT_TYPES")

        if action == "private-chat":
            send_message = f"**Salam 🎵 {message.chat.first_name if hasattr(message.chat, 'first_name') else 'User'}"
            send_message = send_message + \
                f"\n\n𝐁𝐨𝐬𝐬 𝐌𝐮𝐬𝐢𝐜 @Mamedov_Elgiz tərəfindən hazırlanıb."
            send_message = send_message + \
                f"\nBotu qrupunuza əlavə edərək səsli söhbətdə mahnı dinləyə bilərsiniz."
            send_message = send_message + \
                f"\n\n**Daha ətraflı məlumat üçün /help basın"
            return send_message, getReplyKeyBoard(message, action)

        elif action == "help-msg":
            helpMessage = f"**𝐁𝐨𝐬𝐬 𝐌𝐮𝐬𝐢𝐜 istifadə qaydası**"
            helpMessage = helpMessage + \
                f"\n\n• **/play mahnı adı/mahnı linki : ** __Qrupda səslidə mahnı oxudar.__"
            helpMessage = helpMessage + f"\n• **/skip : ** __Növbəti mahnıya keçər.__"
            helpMessage = helpMessage + f"\n• **/stop : ** __Mahnı oxumanı dayandırar.__"
            helpMessage = helpMessage + \
                f"\n• **/refreshadmins : ** __Botun Admin siyahısını yeniləyər.__"
            helpMessage = helpMessage + \
                f"\n• **/auth : ** __Mesajına yanıt verdiyiniz şəxsi botda admin edər.__"
            helpMessage = helpMessage + \
                f"\n• **/unauth : ** __Mesajına yanıt verdiyiniz şəxsi botda adminlikdən silər.__"
            helpMessage = helpMessage + \
                f"\n• **/listadmins : ** __Botun admin siyahısını göstərər.__"
            helpMessage = helpMessage + \
                f"\n• **/adminmode on|off : ** __Admin modunu açar və səslidə mahnını yalnızca adminlər başlada bilər.__"
            helpMessage = helpMessage + \
                f"\n• **/loop [2-5]|off : ** __Mahnı sürətini ayarlayar Maks 2-5.__"
            helpMessage = helpMessage + f"\n\n**__Botun asitanı @BOSS_CLUB_Asistant**"
            return helpMessage, getReplyKeyBoard(message, action)

        elif action == "chat-not-allowed":
            send_message = f"**😖 Sorry but this chat is not yet allowed to access the service. You can always check the demo in [Support Group]({config.get('SUPPORT_GROUP')}).**"
            send_message = send_message + \
                f"\n\n**Why ❓**\n- __Due to high usage we have restrcited the usage of the bot in just our [Support Group]({config.get('SUPPORT_GROUP')}) __"
            send_message = send_message + \
                f"\n- __Join the [Qrupumuz🇦🇿](https://t.me/BOSS_QURUP) to access the bot or deploy your own bot __"

            return send_message, getReplyKeyBoard(message, action)

        elif action == "start-voice-chat":
            send_message = f"**Zəhmət olmasa səsli söhbət başladın və əmrii yenidən göndərin**"
            send_message = send_message + \
                f"\n**1.** __Səsli söhbət başlatmaq üçün, qrupun açıqlama səhifəsinə keçid edin.__"
            send_message = send_message + \
                f"\n**2.** __Daha sonra sağda 3nöqtəyə basın, Sesli söhbet başlata basın.__"
            return send_message, getReplyKeyBoard(message, action)

    except Exception as ex:
        logException(f"**__Error : {ex}__**", True)


def getReplyKeyBoard(message, action):
    try:
        if action == "private-chat":
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "➕ Botu qrupa əlavə et ➕", url=f"{config.get('BOT_URL')}?startgroup=bot"),
                    ],
                    [
                        InlineKeyboardButton(
                            "👥 Sahib", url=f"https://t.me/Mamedov_Elgiz"),

                        InlineKeyboardButton(
                            "🇦🇿 Qrupumuz", url=f"https://t.me/BOSS_QURUP"),
                    ],

                ]
            )
            return keyboard
        elif action == "chat-not-allowed":
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🏁 Bot yaradılması xidməti", url=f"https://t.me/YusifinBiosu"),
                    ],
                    [
                        InlineKeyboardButton(
                            "📔 Qrupumuz", url=f"https://t.me/BOSS_QURUP"),

                    ],

                ]
            )
            return keyboard
        return None
    except Exception as ex:
        logException(f"**__Error : {ex}__**", True)
