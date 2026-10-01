import streamlit as st

# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="HuynhPhuong",
    page_icon="🧋",
    layout="centered"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #fff8f0, #fff1df);
    }

    .main-title {
        text-align: center;
        color: #d96b27;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 0px;
    }

    .sub-title {
        text-align: center;
        color: #7a4a2a;
        font-size: 18px;
        margin-bottom: 20px;
    }

    .price {
        color: #d96b27;
        font-weight: bold;
    }

    .total-box {
        background: #fff3e6;
        border: 2px solid #f0a66a;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-top: 15px;
    }

    .total-text {
        color: #c95716;
        font-size: 30px;
        font-weight: 800;
    }

    .cart-item {
        background: white;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 10px;
        border-left: 5px solid #e9782d;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }

    div.stButton > button {
        border-radius: 10px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

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

MENU = {}
MENU.update(TRA_SUA)
MENU.update(TRA)
MENU.update(DA_XAY)

# =========================================================
# SESSION STATE
# =========================================================

if "cart" not in st.session_state:
    st.session_state.cart = []

if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================================================
# HÀM TIỆN ÍCH
# =========================================================

def format_money(number):
    return f"{number:,.0f}đ".replace(",", ".")


def get_topping_total(toppings):
    return sum(TOPPING[topping] for topping in toppings)


def get_cart_total():
    total = 0

    for item in st.session_state.cart:
        total += item["total"]

    return total


def add_to_cart(category, drink, quantity, toppings, sugar):
    base_price = MENU[drink]
    topping_price = get_topping_total(toppings)

    unit_price = base_price + topping_price
    total_price = unit_price * quantity

    item = {
        "category": category,
        "drink": drink,
        "quantity": quantity,
        "toppings": toppings,
        "sugar": sugar,
        "base_price": base_price,
        "topping_price": topping_price,
        "unit_price": unit_price,
        "total": total_price
    }

    st.session_state.cart.append(item)


# =========================================================
# HEADER
# =========================================================

try:
    st.image("logo1.jpg", width=180)
except:
    pass

st.markdown(
    '<div class="main-title">🧋 HuynhPhuong</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Milk Tea & Drinks</div>',
    unsafe_allow_html=True
)

# =========================================================
# TABS
# =========================================================

tab1, tab2 = st.tabs([
    "🧾 ĐẶT HÀNG",
    "🤖 TRỢ LÝ HUYNHPHUONG"
])

# =========================================================
# TAB 1 - ĐẶT HÀNG
# =========================================================

with tab1:

    st.subheader("🛒 Thêm món vào đơn hàng")

    # -----------------------------------------------------
    # CHỌN LOẠI ĐỒ UỐNG
    # -----------------------------------------------------

    category = st.selectbox(
        "1️⃣ Chọn loại đồ uống",
        [
            "Trà sữa",
            "Trà",
            "Đá xay"
        ]
    )

    if category == "Trà sữa":
        current_menu = TRA_SUA

    elif category == "Trà":
        current_menu = TRA

    else:
        current_menu = DA_XAY

    # -----------------------------------------------------
    # CHỌN MÓN
    # -----------------------------------------------------

    drink = st.selectbox(
        "2️⃣ Chọn món",
        list(current_menu.keys())
    )

    base_price = current_menu[drink]

    st.markdown(
        f"💰 Giá gốc: <span class='price'>{format_money(base_price)}</span>",
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # SỐ LƯỢNG
    # -----------------------------------------------------

    quantity = st.number_input(
        "3️⃣ Số lượng",
        min_value=1,
        max_value=50,
        value=1,
        step=1
    )

    # -----------------------------------------------------
    # TOPPING
    # -----------------------------------------------------

    toppings = st.multiselect(
        "4️⃣ Chọn topping",
        list(TOPPING.keys())
    )

    topping_price = get_topping_total(toppings)

    if toppings:
        st.write(
            f"🧋 Tiền topping / ly: **{format_money(topping_price)}**"
        )

    # -----------------------------------------------------
    # ĐƯỜNG
    # -----------------------------------------------------

    sugar = st.radio(
        "5️⃣ Mức đường",
        [
            "100%",
            "70%",
            "0%"
        ],
        horizontal=True
    )

    # -----------------------------------------------------
    # GIÁ MÓN HIỆN TẠI
    # -----------------------------------------------------

    unit_price = base_price + topping_price
    item_total = unit_price * quantity

    st.info(
        f"💵 {format_money(unit_price)} / ly × {quantity} = "
        f"**{format_money(item_total)}**"
    )

    # -----------------------------------------------------
    # NÚT THÊM MÓN
    # -----------------------------------------------------

    if st.button(
        "➕ THÊM MÓN VÀO ĐƠN",
        use_container_width=True,
        type="primary"
    ):

        add_to_cart(
            category,
            drink,
            quantity,
            toppings,
            sugar
        )

        st.success(
            f"Đã thêm {quantity} × {drink} vào đơn hàng!"
        )

    # =====================================================
    # GIỎ HÀNG
    # =====================================================

    st.divider()

    st.subheader("🛍️ ĐƠN HÀNG HIỆN TẠI")

    if len(st.session_state.cart) == 0:

        st.info(
            "Chưa có món nào trong đơn. "
            "Hãy chọn món ở phía trên rồi bấm 'THÊM MÓN VÀO ĐƠN'."
        )

    else:

        # -------------------------------------------------
        # HIỂN THỊ TỪNG MÓN
        # -------------------------------------------------

        for index, item in enumerate(st.session_state.cart):

            toppings_text = (
                ", ".join(item["toppings"])
                if item["toppings"]
                else "Không có"
            )

            st.markdown(
                f"""
                <div class="cart-item">

                <b>#{index + 1} {item["drink"]}</b><br>

                📂 Loại: {item["category"]}<br>

                🔢 Số lượng: {item["quantity"]} ly<br>

                🍬 Đường: {item["sugar"]}<br>

                🧋 Topping: {toppings_text}<br>

                💰 Đơn giá: {format_money(item["unit_price"])} / ly<br>

                💵 Thành tiền:
                <b>{format_money(item["total"])}</b>

                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                f"🗑️ Xóa món #{index + 1}",
                key=f"delete_{index}"
            ):

                st.session_state.cart.pop(index)

                st.rerun()

        # -------------------------------------------------
        # TỔNG BILL
        # -------------------------------------------------

        total_bill = get_cart_total()

        total_quantity = sum(
            item["quantity"]
            for item in st.session_state.cart
        )

        st.markdown(
            f"""
            <div class="total-box">

                <div>
                    🧋 Tổng số ly:
                    <b>{total_quantity}</b>
                </div>

                <br>

                <div>
                    💰 TỔNG THANH TOÁN
                </div>

                <div class="total-text">
                    {format_money(total_bill)}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        # -------------------------------------------------
        # XÓA TOÀN BỘ ĐƠN
        # -------------------------------------------------

        st.write("")

        if st.button(
            "🗑️ XÓA TOÀN BỘ ĐƠN HÀNG",
            use_container_width=True
        ):

            st.session_state.cart = []

            st.success("Đã xóa toàn bộ đơn hàng.")

            st.rerun()

        # -------------------------------------------------
        # THANH TOÁN
        # -------------------------------------------------

        st.write("")

        if st.button(
            "💳 THANH TOÁN",
            use_container_width=True,
            type="primary"
        ):

            st.balloons()

            st.success(
                f"🎉 Đặt hàng thành công! "
                f"Tổng thanh toán: {format_money(total_bill)}"
            )


# =========================================================
# TAB 2 - CHATBOT
# =========================================================

with tab2:

    st.subheader("🤖 Trợ lý của HuynhPhuong")

    st.caption(
        "Bạn có thể hỏi về menu, giá, topping, mức đường "
        "hoặc nhờ tư vấn món."
    )

    # -----------------------------------------------------
    # HÀM CHATBOT
    # -----------------------------------------------------

    def chatbot_response(question):

        q = question.lower().strip()

        # ================================================
        # CHÀO HỎI
        # ================================================

        if any(
            word in q
            for word in [
                "xin chào",
                "chào",
                "hello",
                "hi",
                "hey"
            ]
        ):
            return (
                "👋 Xin chào! Mình là **Trợ lý của HuynhPhuong** 🧋\n\n"
                "Bạn có thể hỏi mình:\n"
                "- Menu\n"
                "- Giá đồ uống\n"
                "- Topping\n"
                "- Món rẻ nhất / đắt nhất\n"
                "- Bestseller\n"
                "- Món dưới 30k\n"
                "- Món 35k\n"
                "- Món ít đường\n"
                "- Gợi ý đồ uống"
            )

        # ================================================
        # CẢM ƠN
        # ================================================

        if any(
            word in q
            for word in [
                "cảm ơn",
                "thanks",
                "thank"
            ]
        ):
            return (
                "🥰 Không có gì nha! "
                "HuynhPhuong rất vui được phục vụ bạn 🧋❤️"
            )

        # ================================================
        # BESTSELLER
        # ================================================

        if any(
            word in q
            for word in [
                "bestseller",
                "best seller",
                "bán chạy nhất",
                "bán chạy",
                "yêu thích nhất",
                "phổ biến nhất"
            ]
        ):

            return (
                "🔥 Món được thiết lập là **bestseller** của HuynhPhuong "
                "hiện tại là **Trà sữa truyền thống – 30.000đ**.\n\n"
                "Đây là thông tin bestseller được cấu hình trong ứng dụng."
            )

        # ================================================
        # MENU
        # ================================================

        if (
            "menu" in q
            or "thực đơn" in q
            or "có những món" in q
        ):

            response = "📋 **MENU HUYNHPHUONG**\n\n"

            response += "🥛 **TRÀ SỮA**\n"

            for name, price in TRA_SUA.items():
                response += f"- {name}: {format_money(price)}\n"

            response += "\n🍑 **TRÀ**\n"

            for name, price in TRA.items():
                response += f"- {name}: {format_money(price)}\n"

            response += "\n🥤 **ĐÁ XAY**\n"

            for name, price in DA_XAY.items():
                response += f"- {name}: {format_money(price)}\n"

            return response

        # ================================================
        # TOPPING
        # ================================================

        if "topping" in q:

            response = "🧋 **TOPPING HUYNHPHUONG**\n\n"

            for name, price in TOPPING.items():
                response += (
                    f"- {name}: {format_money(price)}\n"
                )

            return response

        # ================================================
        # TOPPING RẺ NHẤT
        # ================================================

        if (
            "topping rẻ nhất" in q
            or "topping nào rẻ nhất" in q
        ):

            name, price = min(
                TOPPING.items(),
                key=lambda x: x[1]
            )

            return (
                f"💰 Topping rẻ nhất hiện tại là "
                f"**{name} – {format_money(price)}**."
            )

        # ================================================
        # TOPPING ĐẮT NHẤT
        # ================================================

        if (
            "topping đắt nhất" in q
            or "topping nào đắt nhất" in q
            or "topping mắc nhất" in q
        ):

            name, price = max(
                TOPPING.items(),
                key=lambda x: x[1]
            )

            return (
                f"💎 Topping có giá cao nhất là "
                f"**{name} – {format_money(price)}**."
            )

        # ================================================
        # MÓN RẺ NHẤT
        # ================================================

        if (
            "món rẻ nhất" in q
            or "món nào rẻ nhất" in q
            or "rẻ nhất" in q
            or "giá thấp nhất" in q
        ):

            name, price = min(
                MENU.items(),
                key=lambda x: x[1]
            )

            return (
                f"💰 Món có giá thấp nhất là "
                f"**{name} – {format_money(price)}**."
            )

        # ================================================
        # MÓN ĐẮT NHẤT
        # ================================================

        if (
            "món đắt nhất" in q
            or "món nào đắt nhất" in q
            or "đắt nhất" in q
            or "giá cao nhất" in q
            or "mắc nhất" in q
        ):

            name, price = max(
                MENU.items(),
                key=lambda x: x[1]
            )

            return (
                f"💎 Món có giá cao nhất là "
                f"**{name} – {format_money(price)}**."
            )

        # ================================================
        # MÓN DƯỚI 30K
        # ================================================

        if (
            "dưới 30" in q
            or "dưới 30k" in q
            or "dưới 30 nghìn" in q
        ):

            items = [
                (name, price)
                for name, price in MENU.items()
                if price < 30000
            ]

            if not items:
                return "Hiện tại không có món nào dưới 30.000đ."

            response = "💰 **MÓN DƯỚI 30.000đ**\n\n"

            for name, price in items:
                response += (
                    f"- {name}: {format_money(price)}\n"
                )

            return response

        # ================================================
        # MÓN 35K
        # ================================================

        if (
            "35k" in q
            or "35.000" in q
            or "35 nghìn" in q
        ):

            items = [
                (name, price)
                for name, price in MENU.items()
                if price == 35000
            ]

            response = "💰 **MÓN GIÁ 35.000đ**\n\n"

            for name, price in items:
                response += (
                    f"- {name}: {format_money(price)}\n"
                )

            return response

        # ================================================
        # ĐƯỜNG
        # ================================================

        if (
            "đường" in q
            or "ngọt" in q
            or "ít ngọt" in q
        ):

            return (
                "🍬 HuynhPhuong có 3 mức đường:\n\n"
                "• 100% – Ngọt bình thường\n"
                "• 70% – Ít ngọt\n"
                "• 0% – Không thêm đường\n\n"
                "Bạn có thể chọn mức đường riêng cho từng món."
            )

        # ================================================
        # 0% ĐƯỜNG
        # ================================================

        if (
            "0%" in q
            or "không đường" in q
            or "zero sugar" in q
        ):

            return (
                "🥤 Bạn có thể chọn mức **0% đường** "
                "cho từng món trong đơn hàng.\n\n"
                "Khi đặt nhiều món, mỗi món có thể chọn "
                "mức đường khác nhau."
            )

        # ================================================
        # GỢI Ý
        # ================================================

        if (
            "gợi ý" in q
            or "nên uống gì" in q
            or "tư vấn" in q
            or "recommend" in q
        ):

            return (
                "✨ Một vài lựa chọn bạn có thể thử:\n\n"
                "🧋 Trà sữa truyền thống – 30.000đ\n"
                "🍵 Trà sữa matcha – 35.000đ\n"
                "🍑 Trà đào cam sả – 35.000đ\n"
                "🍫 Socola đá xay – 45.000đ\n"
                "🍓 Dâu đá xay – 45.000đ\n\n"
                "Bạn thích vị **trà sữa, trái cây hay đá xay** "
                "thì mình có thể gợi ý tiếp."
            )

        # ================================================
        # GIÁ
        # ================================================

        if (
            "giá" in q
            or "bao nhiêu" in q
            or "price" in q
        ):

            return (
                "💰 Giá đồ uống HuynhPhuong hiện dao động "
                f"từ **{format_money(min(MENU.values()))}** "
                f"đến **{format_money(max(MENU.values()))}**.\n\n"
                "Bạn có thể hỏi cụ thể tên món, ví dụ:\n"
                "👉 'Trà sữa matcha bao nhiêu?'\n"
                "👉 'Trà đào giá bao nhiêu?'"
            )

        # ================================================
        # TÌM TÊN MÓN CỤ THỂ
        # ================================================

        for name, price in MENU.items():

            if name.lower() in q:

                return (
                    f"🧋 **{name}** có giá "
                    f"**{format_money(price)}**.\n\n"
                    "Bạn có thể chọn thêm topping và "
                    "mức đường khi đặt hàng."
                )

        # ================================================
        # KHÔNG HIỂU
        # ================================================

        return (
            "🤔 Mình chưa hiểu câu hỏi này.\n\n"
            "Bạn có thể hỏi như:\n"
            "• Menu có gì?\n"
            "• Topping có những gì?\n"
            "• Món nào rẻ nhất?\n"
            "• Món nào đắt nhất?\n"
            "• Bestseller là món nào?\n"
            "• Có món dưới 30k không?\n"
            "• Có món 35k không?\n"
            "• Mức đường như thế nào?\n"
            "• Gợi ý món cho mình"
        )

    # =====================================================
    # HIỂN THỊ LỊCH SỬ CHAT
    # =====================================================

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    # =====================================================
    # NHẬP CÂU HỎI
    # =====================================================

    prompt = st.chat_input(
        "Nhập câu hỏi cho HuynhPhuong..."
    )

    if prompt:

        # User message
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        # Bot response
        answer = chatbot_response(prompt)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        st.rerun()
