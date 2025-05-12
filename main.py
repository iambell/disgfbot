import discord
import asyncio
import os
import random
import datetime
from zoneinfo import ZoneInfo  # 日本時間取得用

+ # ── 環境変数から読み込む ──
+ import os
+ 
+ TOKEN     = os.getenv("DISCORD_TOKEN")
+ TARGET_ID = int(os.getenv("TARGET_ID"))

# ── 時間帯ごとのメッセージリスト ──
MORNING = [
    "また寝坊した"
]

AFTERNOON = [
    "…", "つかれたーーー", "また後で…？", "思い出しただけ", "手間かけさせてごめんね",
    "ふと思った", "LINE面倒だけど…", "明日も送るかも…", "考え中…", "返事なくても大丈夫",
    "ただ思いついただけ", "また同じこと悩んでる", "ほんとは構ってほしいだけ", "やる気でないな",
    "やっぱ無理かも", "しんどい", "行きたくない", "返事待ち…", "何も考えてない",
    "またぼーっとしてた", "話すことないかな", "連絡しすぎかな…", "気分乗らない", "また会える？",
    "無理してほしくない", "放置してていいよ", "わからなくなった…", "どうしたらいいか",
    "言葉が出ない…", "ただそばにいたい", "たまにはいいよね？", "ただ…", "なんで疲れるのかな",
    "もう限界かも", "また落ち込んでる…", "話しかけづらい？", "気を使わないでね", "大丈夫…？",
    "ほんとに大丈夫？", "ただ見守ってほしい", "声だけ聞かせて", "行動に移せない",
    "手が動かない…", "やる気スイッチどこ？", "何か楽しいことない？", "また自分責めてる",
    "いつもごめんね", "面倒かもしれない…", "また長文かも…", "返信しなくていい…",
    "また自己嫌悪", "まだ話終わってない？", "たまには無視して", "いつもありがとう…",
    "これで最後…かな？", "考えすぎた…", "また暇つぶし", "本当はもう少し話したい…",
    "でも疲れた…", "また…だけど", "言いたいこと忘れた…", "多分また送る…"
]

EVENING = [
    # 夕方向けのフレーズを必要ならここに追加
]

NIGHT = [
    "おやすみ…？", "おやすみ…", "また明日…", "夢で会えたらいいな"
]

def choose_list_by_hour(hour: int):
    if 6 <= hour < 12:
        return MORNING
    if 12 <= hour < 18:
        return AFTERNOON
    if 18 <= hour < 24:
        return EVENING
    return NIGHT

intents = discord.Intents.default()
client  = discord.Client(intents=intents)

@client.event
async def on_ready():
    user = await client.fetch_user(TARGET_ID)
    print(f"[{datetime.datetime.now(ZoneInfo('Asia/Tokyo')):%Y-%m-%d %H:%M:%S}] ログイン成功: {client.user}")
    while True:
        # 日本時間で現在時刻を取得
        now = datetime.datetime.now(ZoneInfo("Asia/Tokyo"))
        word_list = choose_list_by_hour(now.hour)
        message   = random.choice(word_list)
        if message:
            await user.send(message)
            print(f"[{now:%H:%M:%S}] Sent: {message!r}")
        # 10～20分のランダム待機
        wait_sec = random.randint(600, 1200)
        print(f"Next message in {wait_sec//60}分{wait_sec%60}秒…")
        await asyncio.sleep(wait_sec)

client.run(TOKEN)
