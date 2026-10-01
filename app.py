import streamlit as st
from openai import OpenAI

# =========================================================
# 1. CẤU HÌNH APP
# =========================================================

st.set_page_config(
    page_title="HuynhPhuong",
    page_icon="🧋",
    layout="centered"
)

# =========================================================
# 2. OPENAI API KEY
# =========================================================

try:
    API_KEY = st.secrets["OPENAI_API_KEY"]

    client = OpenAI(
        api_key=API_KEY
    )

    AI_CONNECTED = True

except Exception:
    client = None
    AI_CONNECTED = False


# =========================================================
# 3. MENU
# =========================================================

TRA_SUA = {
    "Trà sữa truyền thống": 30000,
    "Trà sữa trân châu đường đen": 38000,
    "Trà sữa matcha": 35000,
    "Trà sữa matcha kem cheese": 42000,
    "Trà sữa socola": 35000,
    "Trà sữa socola kem cheese": 42000,
    "Trà sữa khoai môn": 38000,
    "Trà sữa khoai môn kem cheese": 45000,
    "Trà sữa thái xanh": 35000,
    "Trà sữa thái đỏ": 35000,
    "Trà sữa dâu": 38000,
    "Trà sữa dâu kem cheese": 45000,
    "Trà sữa bạc hà": 35000,
    "Trà sữa caramel": 38000,
    "Trà sữa vani": 35000,
    "Trà sữa hạnh nhân": 40000,
    "Trà sữa ô long": 35000,
    "Trà sữa ô long kem cheese": 42000,
}

TRA = {
    "Trà đào cam sả": 35000,
    "Trà đào": 32000,
    "Trà vải": 32000,
    "Trà tắc mật ong": 30000,
    "Trà chanh": 25000,
    "Trà dâu": 35000,
    "Trà xoài": 35000,
    "Trà passion": 35000,
    "Trà ô long đào": 38000,
    "Trà ô long vải": 38000,
}

DA_XAY = {
    "Matcha đá xay": 45000,
    "Socola đá xay": 45000,
    "Cookie đá xay": 48000,
    "Dâu đá xay": 45000,
    "Khoai môn đá xay": 48000,
    "Caramel đá xay": 45000,
}

TOPPING = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 6000,
    "Trân châu đường đen": 7000,
    "Pudding trứng": 7000,
    "Thạch trái cây": 5000,
    "Thạch dừa": 5000,
    "Thạch nha đam": 5000,
    "Trân châu hoàng kim": 7000,
    "Thạch phô mai": 8000,
    "Kem cheese": 10000,
    "Kem trứng": 10000,
}

MENU = {}

MENU.update(TRA_SUA)
MENU.update(TRA)
MENU.update(DA_XAY)


# =========================================================
# 4. SIZE
# =========================================================

SIZE_PRICE = {
    "S": 0,
    "M": 5000,
    "L": 10000
}


# =========================================================
# 5. SESSION STATE
# =========================================================

if "cart" not in st.session_state:
    st.session_state.cart = []

if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================================================
# 6. CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #fff8f0,
        #fff0df
    );
}

.main-title {
    text-align: center;
    color: #d96b27;
    font-size: 42px;
    font-weight: 800;
}

.sub-title {
    text-align: center;
    color: #7a4a2a;
    font-size: 18px;
    margin-bottom: 20px;
}

.cart-item {
    background: white;
    border-radius: 15px;
    padding: 16px;
    margin-bottom: 12px;
    border-left: 5px solid #e9782d;
    box-shadow: 0 3px 10px rgba(0,0,0,0.06);
}

.total-box {
    background: #fff3e6;
    border: 2px solid #f0a66a;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
}

.total-text {
    color: #c95716;
    font-size: 30px;
    font-weight: 800;
}

.ai-status {
    background: #fff7ed;
    border-radius: 12px;
    padding: 12px;
    margin-bottom: 15px;
    border: 1px solid #f3bd91;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 7. HÀM
# =========================================================

def format_money(number):
    return f"{number:,.0f}đ".replace(",", ".")


def get_topping_total(toppings):

    return sum(
        TOPPING[topping]
        for topping in toppings
    )


def get_cart_total():

    return sum(
        item["total"]
        for item in st.session_state.cart
    )


def add_to_cart(
    category,
    drink,
    size,
    quantity,
    toppings,
    sugar
):

    base_price = MENU[drink]

    size_price = SIZE_PRICE[size]

    topping_price = get_topping_total(
        toppings
    )

    unit_price = (
        base_price
        + size_price
        + topping_price
    )

    total = unit_price * quantity

    st.session_state.cart.append({

        "category": category,

        "drink": drink,

        "size": size,

        "quantity": quantity,

        "toppings": toppings,

        "sugar": sugar,

        "base_price": base_price,

        "size_price": size_price,

        "topping_price": topping_price,

        "unit_price": unit_price,

        "total": total

    })


# =========================================================
# 8. TẠO DATABASE MENU CHO CHATBOT
# =========================================================

def create_menu_database():

    data = ""

    data += "\n=== TRÀ SỮA ===\n"

    for name, price in TRA_SUA.items():

        data += (
            f"{name}: "
            f"{format_money(price)}\n"
        )

    data += "\n=== TRÀ ===\n"

    for name, price in TRA.items():

        data += (
            f"{name}: "
            f"{format_money(price)}\n"
        )

    data += "\n=== ĐÁ XAY ===\n"

    for name, price in DA_XAY.items():

        data += (
            f"{name}: "
            f"{format_money(price)}\n"
        )

    data += "\n=== TOPPING ===\n"

    for name, price in TOPPING.items():

        data += (
            f"{name}: "
            f"{format_money(price)}\n"
        )

    data += """

=== SIZE ===

Size S: +0đ
Size M: +5.000đ
Size L: +10.000đ

=== MỨC ĐƯỜNG ===

100%
70%
0%

"""

    return data


# =========================================================
# 9. CHATBOT AI
# =========================================================

def ask_ai(user_question):

    if not AI_CONNECTED:

        return """
⚠️ **Chưa kết nối API Key**

Bạn cần tạo file:

`.streamlit/secrets.toml`

và thêm:

```toml
OPENAI_API_KEY = "API_KEY_CUA_BAN"
