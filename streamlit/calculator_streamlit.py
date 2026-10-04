import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Smart Calculator",
    page_icon="🧮",
    layout="centered"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e293b);
    }

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: white;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 16px;
        margin-bottom: 30px;
    }

    .calculator-card {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 25px;
        padding: 25px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.35);
    }

    .result-box {
        background: #020617;
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 20px;
        text-align: right;
    }

    .result-label {
        color: #94a3b8;
        font-size: 14px;
    }

    .result {
        color: white;
        font-size: 40px;
        font-weight: bold;
    }

    div.stButton > button {
        width: 100%;
        height: 55px;
        border-radius: 14px;
        border: none;
        font-size: 20px;
        font-weight: 600;
        background: #334155;
        color: white;
        transition: 0.2s;
    }

    div.stButton > button:hover {
        background: #475569;
        transform: scale(1.02);
    }

    .history-title {
        color: white;
        font-size: 22px;
        font-weight: bold;
        margin-top: 30px;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Session State
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "result" not in st.session_state:
    st.session_state.result = 0


# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="main-title">🧮 Smart Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Fast • Simple • Beautiful</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Calculator Card
# -----------------------------
st.markdown('<div class="calculator-card">', unsafe_allow_html=True)

# Display
st.markdown(
    f"""
    <div class="result-box">
        <div class="result-label">RESULT</div>
        <div class="result">{st.session_state.result}</div>
    </div>
    """,
    unsafe_allow_html=True
)


# Inputs
col1, col2 = st.columns(2)

with col1:
    number1 = st.number_input(
        "First Number",
        value=0.0,
        step=1.0
    )

with col2:
    number2 = st.number_input(
        "Second Number",
        value=0.0,
        step=1.0
    )


st.write("")

# Operations
st.subheader("Choose Operation")

col1, col2, col3, col4 = st.columns(4)

with col1:
    add = st.button("➕ Add")

with col2:
    subtract = st.button("➖ Subtract")

with col3:
    multiply = st.button("✖️ Multiply")

with col4:
    divide = st.button("➗ Divide")


# -----------------------------
# Calculation
# -----------------------------
if add:
    result = number1 + number2
    st.session_state.result = result

    st.session_state.history.append(
        f"{number1} + {number2} = {result}"
    )

    st.rerun()


if subtract:
    result = number1 - number2
    st.session_state.result = result

    st.session_state.history.append(
        f"{number1} - {number2} = {result}"
    )

    st.rerun()


if multiply:
    result = number1 * number2
    st.session_state.result = result

    st.session_state.history.append(
        f"{number1} × {number2} = {result}"
    )

    st.rerun()


if divide:
    if number2 == 0:
        st.error("⚠️ Cannot divide by zero.")
    else:
        result = number1 / number2
        st.session_state.result = result

        st.session_state.history.append(
            f"{number1} ÷ {number2} = {result}"
        )

        st.rerun()


# Close card
st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# History
# -----------------------------
if st.session_state.history:

    st.markdown(
        '<div class="history-title">📜 Calculation History</div>',
        unsafe_allow_html=True
    )

    for item in reversed(st.session_state.history[-10:]):
        st.info(item)

    if st.button("🗑️ Clear History"):
        st.session_state.history = []
        st.session_state.result = 0
        st.rerun()