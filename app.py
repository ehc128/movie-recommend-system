import streamlit as st

# =========================================================
# 🎬 電影資料庫
# =========================================================

def get_absolute_comprehensive_database_2026():

    database = [
        {
            "title": "燃燒烈愛 (Burning) - 數位重映",
            "genre": "劇情 / 懸疑 / 藝術",
            "style": ["孤獨", "寂寞", "文藝", "深度", "思考"],
            "story": "改編自村上春樹小說，極具後現代神祕感。",
            "theater": "光點華山電影館"
        },
        {
            "title": "極限返航 (Project Hail Mary)",
            "genre": "科幻 / 奇幻 / 劇情",
            "style": ["震撼", "爽片", "科幻", "熱血"],
            "story": "萊恩葛斯林主演的太空科幻鉅作。",
            "theater": "威秀影城"
        },
        {
            "title": "破墓",
            "genre": "恐怖 / 驚悚 / 懸疑",
            "style": ["恐怖", "鬼片", "刺激", "驚悚"],
            "story": "亞洲話題風水薩滿恐怖神作。",
            "theater": "威秀影城、秀泰影城"
        },
        {
            "title": "加菲貓：瘋狂大冒險",
            "genre": "動畫 / 喜劇 / 闔家觀賞",
            "style": ["放鬆", "歡樂", "療癒", "哈哈"],
            "story": "輕鬆搞笑的療癒動畫。",
            "theater": "威秀影城"
        }
    ]

    return database


# =========================================================
# 🎯 推薦引擎
# =========================================================

def recommend_movies_ultimate(user_input, movies):

    user_input = user_input.lower()

    mood_map = {
        "憂鬱": ["憂鬱", "低潮", "寂寞", "孤單"],
        "煩躁": ["煩", "壓力", "阿雜", "氣死"],
        "開心": ["開心", "快樂", "放鬆"],
        "難過": ["難過", "傷心", "失戀"],
        "興奮": ["刺激", "熱血", "爽"]
    }

    style_targets = {
        "憂鬱": ["文藝", "深度", "療癒"],
        "煩躁": ["爽片", "刺激", "動作"],
        "開心": ["歡樂", "喜劇", "療癒"],
        "難過": ["愛情", "淚水", "療癒"],
        "興奮": ["熱血", "震撼", "科幻"]
    }

    matched_moods = []

    for mood, words in mood_map.items():
        if any(word in user_input for word in words):
            matched_moods.append(mood)

    recommended = []

    for movie in movies:

        score = 0

        movie_text = (
            movie["title"] +
            movie["genre"] +
            movie["story"]
        ).lower()

        movie_styles = movie["style"]

        for mood in matched_moods:

            for target in style_targets[mood]:

                if target in movie_styles:
                    score += 10

                if target in movie_text:
                    score += 5

        if score > 0:
            recommended.append((movie, score))

    recommended.sort(key=lambda x: x[1], reverse=True)

    return [movie for movie, score in recommended]


# =========================================================
# 🎨 Streamlit UI
# =========================================================

st.set_page_config(
    page_title="電影推薦系統",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 台北影城智慧電影推薦系統")

st.write("輸入你現在的心情，我們會推薦最適合你的電影。")

user_input = st.text_input(
    "你現在的狀態是？",
    placeholder="例如：最近壓力好大，想放鬆一下..."
)

if st.button("開始推薦"):

    if not user_input:
        st.warning("請先輸入內容")
        st.stop()

    # =========================================================
    # ⭐⭐⭐ 這裡就是「接資料庫」的位置 ⭐⭐⭐
    # =========================================================
    movie_db = get_absolute_comprehensive_database_2026()

    # 推薦系統
    results = recommend_movies_ultimate(user_input, movie_db)

    st.subheader("🍿 推薦結果")

    if not results:

        st.info("目前找不到符合的電影")

    else:

        for movie in results:

            with st.expander(f"🎥 {movie['title']}"):

                st.write(f"🎭 類型：{movie['genre']}")

                st.write(f"📍 推薦影城：{movie['theater']}")

                st.write(f"📝 劇情介紹：{movie['story']}")

                st.write(f"🏷️ 風格標籤：{'、'.join(movie['style'])}")
