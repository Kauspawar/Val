import streamlit as st
import streamlit.components.v1 as components
import time

# Page config
st.set_page_config(page_title="Valentine 💖", layout="centered")

# Session state
if "yes_clicked" not in st.session_state:
    st.session_state.yes_clicked = False

# Title
st.markdown(
    """
    <h1 style="text-align:center; color:#ff4b5c;">
        Will you be my Valentine? 💘
    </h1>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# BEFORE YES CLICK
if not st.session_state.yes_clicked:
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes 💖"):
            st.session_state.yes_clicked = True

    with col2:
        components.html(
            """
            <html>
            <head>
            <style>
            #noBtn {
                position: absolute;
                background-color: #ff6b6b;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 8px;
                cursor: pointer;
            }
            </style>
            </head>
            <body>
            <button id="noBtn">No 😝</button>

            <script>
            const btn = document.getElementById("noBtn");
            document.addEventListener("mousemove", function () {
                const x = Math.random() * (window.innerWidth - 100);
                const y = Math.random() * (window.innerHeight - 50);
                btn.style.left = x + "px";
                btn.style.top = y + "px";
            });
            </script>
            </body>
            </html>
            """,
            height=200,
        )

# AFTER YES CLICK
else:
    st.balloons()
    time.sleep(1)

    st.markdown(
        """
        <h1 style="text-align:center; color:#ff1493;">
            I LOVE YOU ❤️🔥
        </h1>
        <h3 style="text-align:center;">
            Happy Valentine’s Day 💞
        </h3>
        """,
        unsafe_allow_html=True
    )

    st.snow()
