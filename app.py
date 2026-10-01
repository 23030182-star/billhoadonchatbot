import streamlit as st
from openai import OpenAI
from pathlib import Path

# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="HuynhPhuong",
    page_icon="🧋",
    layout="wide"
)

# =========================================================
# MENU
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

SIZE_PRICE = {
    "S": 0,
    "M": 5000,
    "L": 10000
}

SUGAR_LEVELS = [
    "100%",
    "70%",
    "0%"
]

MENU = {}
MENU.update(TRA_SUA)
MENU.update(TRA)
MENU.update(DA_XAY)

CATEGORIES = {
    "Trà sữa": TRA_SUA,
    "Trà": TRA,
    "Đá xay": DA_XAY
}

# =========================================================
# CSS
# =========================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #fffaf5;
    }

    .shop-title {
        font-size: 42px;
        font-weight: 800;
        color: #d97706;
        margin-bottom: 0;
    }

    .shop-subtitle {
        font-size: 18px;
        color: #666;
        margin-top: 0;
    }

    .price {
        color: #d97706;
        font-weight: 700;
    }

    .cart-box {
        background-color: #fff;
        border-radius: 15px;
        padding: 15px;
        border: 1px solid #f1dfca;
        margin-bottom: 10px;
    }

    .total-box {
        background-color: #fff3e0;
        border-radius: 15px;
        padding: 18px;
        border: 2px solid #f59e0b;
    }

    .chat-title {
        color: #d97706;
        font-size: 25px;
        font-weight: 700;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SESSION STATE
# =========================================================

if "cart" not in st.session_state:
    st.session_state.cart = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# =========================================================
# HÀM TIỆN ÍCH
# =========================================================

def format_money(number):
    return f"{number:,.0f}đ".replace(",", ".")


def cart_total():
    return sum(item["total"] for item in st.session_state.cart)


def create_cart_item(
    category,
    drink,
    size,
    quantity,
    toppings,
    sugar
):
    base_price = MENU[drink]
    size_price = SIZE_PRICE[size]

    topping_price = sum(
        TOPPING[topping]
        for topping in toppings
    )

    unit_price = (
        base_price
        + size_price
        + topping_price
    )

    total = unit_price * quantity

    return {
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
    }


def cart_text():
    if not st.session_state.cart:
        return "Giỏ hàng hiện đang trống."

    lines = []

    for i, item in enumerate(st.session_state.cart, 1):

        topping_text = (
            ", ".join(item["toppings"])
            if item["toppings"]
            else "Không topping"
        )

        lines.append(
            f"{i}. {item['drink']} - Size {item['size']} - "
            f"Số lượng {item['quantity']} - Đường {item['sugar']} - "
            f"Topping: {topping_text} - "
            f"{format_money(item['total'])}"
        )

    lines.append(
        f"TỔNG: {format_money(cart_total())}"
    )

    return "\n".join(lines)


# =========================================================
# LOGO
# =========================================================

logo_path = Path("logo1.jpg")

col_logo, col_title = st.columns([1, 5])

with col_logo:
    if logo_path.exists():
        st.image(
            str(logo_path),
            width=130
        )
    else:
        st.markdown("🧋")

with col_title:
    st.markdown(
        '<div class="shop-title">HuynhPhuong</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="shop-subtitle">'
        'Trà sữa & đồ uống yêu thích của bạn'
        '</div>',
        unsafe_allow_html=True
    )

st.divider()

# =========================================================
# 2 CỘT CHÍNH
# =========================================================

menu_col, cart_col = st.columns([1.45, 1])

# =========================================================
# MENU / ĐẶT HÀNG
# =========================================================

with menu_col:

    st.header("🧋 Đặt món")

    category = st.selectbox(
        "Loại đồ uống",
        list(CATEGORIES.keys())
    )

    current_menu = CATEGORIES[category]

    drink = st.selectbox(
        "Chọn đồ uống",
        list(current_menu.keys())
    )

    base_price = MENU[drink]

    st.markdown(
        f"Giá gốc: **{format_money(base_price)}**"
    )

    size = st.radio(
        "Size",
        ["S", "M", "L"],
        horizontal=True
    )

    quantity = st.number_input(
        "Số lượng",
        min_value=1,
        max_value=50,
        value=1,
        step=1
    )

    sugar = st.selectbox(
        "Mức đường",
        SUGAR_LEVELS
    )

    toppings = st.multiselect(
        "Topping",
        list(TOPPING.keys()),
        format_func=lambda x:
            f"{x} (+{format_money(TOPPING[x])})"
    )

    size_price = SIZE_PRICE[size]

    topping_price = sum(
        TOPPING[t]
        for t in toppings
    )

    unit_price = (
        base_price
        + size_price
        + topping_price
    )

    total_item = unit_price * quantity

    st.info(
        f"Đơn giá: **{format_money(unit_price)}**  \n"
        f"Thành tiền: **{format_money(total_item)}**"
    )

    if st.button(
        "➕ THÊM VÀO GIỎ HÀNG",
        use_container_width=True,
        type="primary"
    ):

        item = create_cart_item(
            category=category,
            drink=drink,
            size=size,
            quantity=quantity,
            toppings=toppings,
            sugar=sugar
        )

        st.session_state.cart.append(item)

        st.success(
            f"Đã thêm {quantity} × {drink} vào giỏ hàng!"
        )

        st.rerun()

# =========================================================
# GIỎ HÀNG
# =========================================================

with cart_col:

    st.header("🛒 Giỏ hàng")

    if not st.session_state.cart:

        st.info("Chưa có món nào trong giỏ.")

    else:

        for index, item in enumerate(
            st.session_state.cart
        ):

            st.markdown(
                f"""
                <div class="cart-box">
                    <b>{item["drink"]}</b><br>
                    Size: {item["size"]}<br>
                    Đường: {item["sugar"]}<br>
                    Số lượng: {item["quantity"]}<br>
                    Topping:
                    {", ".join(item["toppings"])
                    if item["toppings"]
                    else "Không có"}<br>
                    <span class="price">
                    {format_money(item["total"])}
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "🗑️ Xóa món",
                key=f"delete_{index}",
                use_container_width=True
            ):

                st.session_state.cart.pop(index)

                st.rerun()

        st.markdown(
            f"""
            <div class="total-box">
                <h3>Tổng thanh toán</h3>
                <h2>{format_money(cart_total())}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "🧹 Xóa giỏ",
                use_container_width=True
            ):

                st.session_state.cart = []

                st.rerun()

        with col2:

            if st.button(
                "💳 Thanh toán",
                use_container_width=True,
                type="primary"
            ):

                st.success(
                    f"Thanh toán thành công: "
                    f"{format_money(cart_total())}"
                )

                st.session_state.cart = []

                st.rerun()

# =========================================================
# CHATBOT
# =========================================================

st.divider()

st.markdown(
    '<div class="chat-title">'
    '🤖 Trợ lý của HuynhPhuong'
    '</div>',
    unsafe_allow_html=True
)

st.caption(
    "Bạn có thể hỏi về menu, giá, size, topping "
    "hoặc nhờ trợ lý tư vấn đồ uống."
)

# =========================================================
# OPENAI
# =========================================================

client = None
api_error = None

try:

    api_key = st.secrets.get("OPENAI_API_KEY", "")

    if api_key:

        client = OpenAI(
            api_key=api_key
        )

except Exception as e:

    api_error = str(e)


def ask_ai(question):

    if client is None:

        return (
            "⚠️ Chatbot AI chưa được kết nối.\n\n"
            "Bạn hãy kiểm tra OPENAI_API_KEY "
            "trong file .streamlit/secrets.toml."
        )

    menu_text = []

    for category_name, drinks in CATEGORIES.items():

        menu_text.append(
            f"\n{category_name}:"
        )

        for name, price in drinks.items():

            menu_text.append(
                f"- {name}: {format_money(price)}"
            )

    topping_text = []

    for name, price in TOPPING.items():

        topping_text.append(
            f"- {name}: +{format_money(price)}"
        )

    system_prompt = f"""
Bạn là "Trợ lý của HuynhPhuong",
trợ lý tư vấn cho cửa hàng trà sữa HuynhPhuong.

Hãy trả lời bằng tiếng Việt, thân thiện, ngắn gọn,
dễ hiểu.

THÔNG TIN CỬA HÀNG:

MENU:
{"".join(menu_text)}

SIZE:
- S: +0đ
- M: +5.000đ
- L: +10.000đ

MỨC ĐƯỜNG:
- 100%
- 70%
- 0%

TOPPING:
{"".join(topping_text)}

GIỎ HÀNG HIỆN TẠI:
{cart_text()}

QUY TẮC:

1. Không được tự bịa món hoặc giá.
2. Nếu khách hỏi giá, dùng đúng giá trong MENU.
3. Giá M và L cộng thêm phí size.
4. Topping cộng thêm vào giá.
5. Có thể tư vấn khách chọn đồ uống.
6. Nếu khách hỏi tổng tiền giỏ hàng,
   dùng đúng thông tin GIỎ HÀNG HIỆN TẠI.
7. Nếu giỏ hàng trống thì nói rõ giỏ đang trống.
8. Không tự xác nhận thanh toán.
9. Nếu khách muốn đặt món bằng giao diện,
   hướng dẫn họ chọn món ở phần "Đặt món".
10. Không nói rằng bạn đã thực hiện một hành động
    nếu thực tế chưa thực hiện.
"""

    try:

        response = client.responses.create(
            model="gpt-5.6-luna",
            instructions=system_prompt,
            input=question
        )

        answer = response.output_text

        if not answer:
            return "Xin lỗi, AI không trả về nội dung."

        return answer

    except Exception as e:

        return (
            "❌ Không gọi được AI.\n\n"
            f"Chi tiết lỗi: `{str(e)}`\n\n"
            "Hãy kiểm tra API Key và model trong "
            "file secrets.toml."
        )


# =========================================================
# HIỂN THỊ LỊCH SỬ CHAT
# =========================================================

for message in st.session_state.chat_history:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"]
        )

# =========================================================
# Ô CHAT
# =========================================================

question = st.chat_input(
    "Nhập câu hỏi cho Trợ lý HuynhPhuong..."
)

if question:

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    answer = ask_ai(question)

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):

        st.markdown(answer)
