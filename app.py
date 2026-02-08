import streamlit as st

# Page setup
st.set_page_config(page_title="Be My Valentine?", page_icon="💌", layout="centered")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Yeseva+One&family=Playfair+Display:wght@400;700&family=Quicksand:wght@400;600&display=swap');

    :root {
        --rose: #ff5b7a;
        --peach: #ffb4a2;
        --cream: #fff3e8;
        --berry: #7a1f3d;
        --leaf: #2f6f5e;
        --ink: #2b1b1f;
    }

    /* Atmospheric background with soft patterns */
    .stApp {
        background:
            radial-gradient(1200px 600px at 10% 10%, rgba(255, 224, 178, 0.75), transparent 60%),
            radial-gradient(900px 500px at 90% 20%, rgba(255, 192, 203, 0.6), transparent 60%),
            radial-gradient(800px 400px at 50% 80%, rgba(186, 255, 233, 0.35), transparent 60%),
            linear-gradient(135deg, #fff6f0 0%, #ffe2e9 45%, #f8f1ff 100%);
    }

    /* Floating confetti hearts */
    @keyframes floatUp {
        0% { transform: translateY(0) rotate(0deg); opacity: 0; }
        25% { opacity: 0.8; }
        100% { transform: translateY(-120vh) rotate(360deg); opacity: 0; }
    }
    .floaty {
        position: fixed;
        bottom: -20px;
        font-size: 22px;
        animation: floatUp 12s linear infinite;
        z-index: -1;
        filter: drop-shadow(0 6px 10px rgba(255, 91, 122, 0.25));
    }

    /* Main card */
    .valentine-card {
        background: rgba(255, 255, 255, 0.65);
        border: 1px solid rgba(255, 255, 255, 0.55);
        border-radius: 28px;
        padding: 36px 28px 32px 28px;
        text-align: center;
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        box-shadow:
            0 10px 30px rgba(122, 31, 61, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.7);
    }

    .title {
        font-family: 'Yeseva One', serif;
        color: var(--berry);
        font-size: 3.2rem;
        margin-bottom: 0.4rem;
        letter-spacing: 0.5px;
    }

    .subtitle {
        font-family: 'Playfair Display', serif;
        color: var(--ink);
        font-size: 1.35rem;
        margin-top: 0.4rem;
        margin-bottom: 1.2rem;
    }

    .chip {
        display: inline-block;
        font-family: 'Quicksand', sans-serif;
        color: var(--leaf);
        background: rgba(47, 111, 94, 0.1);
        border: 1px dashed rgba(47, 111, 94, 0.35);
        border-radius: 999px;
        padding: 6px 14px;
        font-size: 0.95rem;
        margin-bottom: 12px;
    }

    /* Buttons */
    div.stButton > button:first-child {
        border-radius: 999px;
        padding: 10px 24px;
        border: none;
        font-family: 'Quicksand', sans-serif;
        background: #111111 !important;
        color: #ffffff !important;
        transition: transform 0.15s ease, box-shadow 0.2s ease, background 0.2s ease;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.25);
    }
    </style>

    <div class="floaty" style="left:8%; animation-duration:10s;">💖</div>
    <div class="floaty" style="left:22%; animation-duration:14s; font-size:28px;">💌</div>
    <div class="floaty" style="left:45%; animation-duration:11s;">🌸</div>
    <div class="floaty" style="left:70%; animation-duration:16s; font-size:30px;">💕</div>
    <div class="floaty" style="left:88%; animation-duration:9s;">❤️</div>
    """,
    unsafe_allow_html=True,
)

# State
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0
if "said_yes" not in st.session_state:
    st.session_state.said_yes = False

no_phrases = [
    "No",
    "Are you sure?",
    "Really sure?",
    "Pinky promise no?",
    "I made you a playlist...",
    "What if I bring snacks?",
    "I will be so sad 🥺",
    "Plot twist: you meant YES",
    "Look how big YES is now",
    "Okay, last chance 💞",
]

# Content
if not st.session_state.said_yes:
    st.markdown(
        """
        <div class="valentine-card">
            <div class="chip">An important question</div>
            <div class="title">Hey, you ✨</div>
            <div class="subtitle">Will you be my Valentine?</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p class='subtitle' style='margin-top: 0.6rem;'>"
        "Choose wisely. The universe is watching. ✨"
        "</p>",
        unsafe_allow_html=True,
    )

    yes_font_size = 18 + (st.session_state.no_clicks * 16)
    yes_padding_y = 10 + (st.session_state.no_clicks * 2)
    yes_padding_x = 24 + (st.session_state.no_clicks * 3)

    col1, col2 = st.columns([1.1, 1])

    with col1:
        st.markdown(
            f"""
            <style>
            button[key="yes_btn"] {{
                background: #e3123a !important;
                color: white !important;
                font-size: {yes_font_size}px !important;
                padding: {yes_padding_y}px {yes_padding_x}px !important;
                width: 100% !important;
                box-shadow: 0 12px 26px rgba(227, 18, 58, 0.35) !important;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )
        if st.button("YES! 💘", key="yes_btn"):
            st.session_state.said_yes = True
            st.rerun()

    with col2:
        btn_text = no_phrases[min(st.session_state.no_clicks, len(no_phrases) - 1)]
        if st.button(btn_text, key="no_btn"):
            st.session_state.no_clicks += 1
            st.rerun()

else:
    st.balloons()
    st.markdown(
        """
        <div class="valentine-card">
            <div class="title">YAY! 💞</div>
            <div class="subtitle">Best date ever incoming.</div>
            <div class="chip">See you on February 14</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("### Countdown to the cutest date ever 🥂")
