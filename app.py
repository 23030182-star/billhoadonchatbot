import streamlit as st

# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="Huỳnh Phương - Trà sữa",
    page_icon="🧋",
    layout="centered"
)

# =========================================================
# CSS GIAO DIỆN
# =========================================================

st.markdown("""
<style>

    .main {
        background-color: #fffaf5;
    }

    .shop-name {
        text-align: center;
        font-size: 40px;
        font-weight: 800;
        color: #d97706;
        margin-top: 5px;
        margin-bottom: 0px;
    }

    .shop-slogan {
        text-align: center;
        color: #777777;
        font-size: 16px;
        margin-bottom: 20px;
    }

    .title {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #333333;
    }

    .total-box {
        background-color: #fff1df;
        padding: 22px;
        border-radius: 18px;
        text-align: center;
        border: 2px solid #f59e0b;
        margin-top: 15px;
        margin-bottom: 20px;
    }

    .total-title {
        font-size: 20px;
        font-weight: bold;
        color: #b45309;
    }

    .total-money {
        font-size: 34px;
        font-weight: 800;
        color: #d97706;
        margin-top: 8px;
    }

    .chat-title {
        font-size: 24px;
        font-weight: bold;
        color: #d97706;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# MENU
# =========================================================

TRA_SUA = {
    "Trà sữa truyền thống": 30000,
    "Trà sữa matcha": 35000,
    "Trà sữa socola": 35000,
    "Trà sữa khoai môn": 38000,
    "Trà sữa thái xanh": 35000,
    "Trà sữa dâu": 38000
}

TOPPING = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 6000,
    "Pudding trứng": 7000,
    "Thạch trái cây": 5000,
    "Kem cheese": 10000
}


# =========================================================
# HÀM ĐỊNH DẠNG TIỀN
# =========================================================

def dinh_dang_tien(tien):
    return f"{tien:,} VNĐ"


# =========================================================
# LOGO
# =========================================================

try:
    st.image(
        "logo1.jpg",
        use_container_width=True
    )
except Exception:
    st.warning(
        "⚠️ Không tìm thấy file logo1.jpg. "
        "Hãy đặt logo1.jpg cùng thư mục với app.py."
    )


# =========================================================
# TÊN QUÁN
# =========================================================

st.markdown(
    '<div class="shop-name">HUỲNH PHƯƠNG</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="shop-slogan">🧋 TRÀ SỮA & ĐỒ UỐNG</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# TẠO 2 TAB
# =========================================================

tab1, tab2 = st.tabs([
    "🧾 TÍNH HÓA ĐƠN",
    "🤖 CHATBOT"
])


# =========================================================
# TAB 1 - TÍNH HÓA ĐƠN
# =========================================================

with tab1:

    st.markdown(
        '<div class="title">🧾 NHẬP ĐƠN HÀNG</div>',
        unsafe_allow_html=True
    )

    st.write("")

    # ---------------------------------------------
    # CHỌN TRÀ SỮA
    # ---------------------------------------------

    loai_tra_sua = st.selectbox(
        "🧋 Chọn loại trà sữa",
        list(TRA_SUA.keys())
    )

    # ---------------------------------------------
    # CHỌN SỐ LƯỢNG
    # ---------------------------------------------

    so_luong = st.number_input(
        "🔢 Số lượng",
        min_value=1,
        max_value=50,
        value=1,
        step=1
    )

    # ---------------------------------------------
    # CHỌN TOPPING
    # ---------------------------------------------

    topping_da_chon = st.multiselect(
        "🥤 Chọn topping",
        list(TOPPING.keys()),
        placeholder="Chọn một hoặc nhiều topping"
    )

    # ---------------------------------------------
    # CHỌN MỨC ĐƯỜNG
    # ---------------------------------------------

    muc_duong = st.radio(
        "🍬 Mức độ đường",
        ["100%", "70%", "0%"],
        horizontal=True
    )

    st.write("")

    # ---------------------------------------------
    # NÚT TÍNH BILL
    # ---------------------------------------------

    if st.button(
        "🧾 TÍNH HÓA ĐƠN",
        use_container_width=True,
        type="primary"
    ):

        # Giá trà sữa
        gia_tra_sua = TRA_SUA[loai_tra_sua]

        # Tiền topping / ly
        tien_topping_mot_ly = sum(
            TOPPING[topping]
            for topping in topping_da_chon
        )

        # Giá một ly
        gia_mot_ly = (
            gia_tra_sua
            + tien_topping_mot_ly
        )

        # Tổng tiền
        tong_tien = gia_mot_ly * so_luong

        # Lưu thông tin vào session
        st.session_state["bill"] = {
            "loai_tra_sua": loai_tra_sua,
            "so_luong": so_luong,
            "topping": topping_da_chon,
            "muc_duong": muc_duong,
            "gia_tra_sua": gia_tra_sua,
            "tien_topping": tien_topping_mot_ly,
            "gia_mot_ly": gia_mot_ly,
            "tong_tien": tong_tien
        }


    # =====================================================
    # HIỂN THỊ BILL
    # =====================================================

    if "bill" in st.session_state:

        bill = st.session_state["bill"]

        st.divider()

        st.markdown(
            '<div class="title">🧾 KẾT QUẢ ĐƠN HÀNG</div>',
            unsafe_allow_html=True
        )

        st.write("")

        # ---------------------------------------------
        # THÔNG TIN ĐÃ NHẬP
        # ---------------------------------------------

        st.info(
            f"""
🧋 **Loại trà sữa:** {bill["loai_tra_sua"]}

🔢 **Số lượng:** {bill["so_luong"]} ly

🍬 **Mức độ đường:** {bill["muc_duong"]}
"""
        )

        # ---------------------------------------------
        # TOPPING
        # ---------------------------------------------

        if bill["topping"]:

            st.write("🥤 **Topping đã chọn:**")

            for item in bill["topping"]:

                st.write(
                    f"• {item}: "
                    f"{dinh_dang_tien(TOPPING[item])}"
                )

        else:

            st.write(
                "🥤 **Topping:** Không có"
            )

        st.divider()

        # ---------------------------------------------
        # CHI TIẾT GIÁ
        # ---------------------------------------------

        st.write(
            f"💵 Giá trà sữa: "
            f"**{dinh_dang_tien(bill['gia_tra_sua'])}/ly**"
        )

        st.write(
            f"🥤 Tiền topping: "
            f"**{dinh_dang_tien(bill['tien_topping'])}/ly**"
        )

        st.write(
            f"💰 Thành tiền mỗi ly: "
            f"**{dinh_dang_tien(bill['gia_mot_ly'])}**"
        )

        st.write(
            f"🔢 Số lượng: "
            f"**{bill['so_luong']} ly**"
        )

        # ---------------------------------------------
        # TỔNG TIỀN
        # ---------------------------------------------

        st.markdown(
            f"""
            <div class="total-box">
                <div class="total-title">
                    💵 TỔNG TIỀN CẦN THANH TOÁN
                </div>

                <div class="total-money">
                    {dinh_dang_tien(bill['tong_tien'])}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success(
            "✅ Cảm ơn quý khách đã mua hàng tại HUỲNH PHƯƠNG!"
        )


# =========================================================
# TAB 2 - CHATBOT
# =========================================================

with tab2:

    st.markdown(
        '<div class="chat-title">🤖 CHATBOT HUỲNH PHƯƠNG</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Xin chào! 👋 Mình là trợ lý của quán trà sữa "
        "**Huỳnh Phương**."
    )

    st.write(
        "Bạn có thể hỏi mình về menu, giá, topping "
        "hoặc mức độ đường."
    )

    st.divider()

    # -----------------------------------------------------
    # LỊCH SỬ CHAT
    # -----------------------------------------------------

    if "messages" not in st.session_state:

        st.session_state.messages = [
            {
                "role": "assistant",
                "content":
                "Xin chào 👋 Bạn muốn hỏi gì về trà sữa "
                "Huỳnh Phương?"
            }
        ]


    # Hiển thị lịch sử
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.write(message["content"])


    # -----------------------------------------------------
    # HÀM CHATBOT
    # -----------------------------------------------------

    def chatbot_tra_loi(cau_hoi):

        cau_hoi = cau_hoi.lower()

        # MENU
        if (
            "menu" in cau_hoi
            or "món" in cau_hoi
            or "trà sữa" in cau_hoi
        ):

            noi_dung = "🧋 **Menu Huỳnh Phương:**\n\n"

            for ten, gia in TRA_SUA.items():

                noi_dung += (
                    f"- {ten}: "
                    f"{dinh_dang_tien(gia)}\n"
                )

            return noi_dung


        # TOPPING
        elif (
            "topping" in cau_hoi
            or "trân châu" in cau_hoi
        ):

            noi_dung = "🥤 **Danh sách topping:**\n\n"

            for ten, gia in TOPPING.items():

                noi_dung += (
                    f"- {ten}: "
                    f"{dinh_dang_tien(gia)}\n"
                )

            return noi_dung


        # GIÁ
        elif (
            "giá" in cau_hoi
            or "bao nhiêu" in cau_hoi
            or "tiền" in cau_hoi
        ):

            return (
                "💰 Giá trà sữa tại Huỳnh Phương "
                "dao động từ **30.000 - 38.000 VNĐ/ly**.\n\n"
                "Topping có giá từ **5.000 - 10.000 VNĐ**."
            )


        # ĐƯỜNG
        elif (
            "đường" in cau_hoi
            or "ngọt" in cau_hoi
        ):

            return (
                "🍬 Quán có 3 mức độ đường:\n\n"
                "• 100% - ngọt bình thường\n"
                "• 70% - ít ngọt\n"
                "• 0% - không đường"
            )


        # TƯ VẤN
        elif (
            "tư vấn" in cau_hoi
            or "nên chọn" in cau_hoi
            or "gợi ý" in cau_hoi
        ):

            return (
                "😊 Nếu bạn thích vị truyền thống, "
                "mình gợi ý **Trà sữa truyền thống + "
                "trân châu đen + 70% đường**.\n\n"
                "Nếu thích vị thanh nhẹ, bạn có thể chọn "
                "**Matcha + 70% hoặc 0% đường**."
            )


        # XIN CHÀO
        elif (
            "hello" in cau_hoi
            or "xin chào" in cau_hoi
            or "chào" in cau_hoi
        ):

            return (
                "Xin chào 👋 Chào mừng bạn đến với "
                "**Huỳnh Phương**! 🧋"
            )


        # CẢM ƠN
        elif "cảm ơn" in cau_hoi:

            return (
                "Không có gì ạ ❤️ "
                "Cảm ơn bạn đã ủng hộ Huỳnh Phương!"
            )


        # KHÔNG HIỂU
        else:

            return (
                "🤔 Mình có thể giúp bạn về:\n\n"
                "• 🧋 Menu trà sữa\n"
                "• 💰 Giá sản phẩm\n"
                "• 🥤 Topping\n"
                "• 🍬 Mức độ đường\n"
                "• 😊 Tư vấn chọn món\n\n"
                "Bạn thử hỏi mình nhé!"
            )


    # -----------------------------------------------------
    # Ô CHAT
    # -----------------------------------------------------

    cau_hoi = st.chat_input(
        "Nhập câu hỏi cho Huỳnh Phương..."
    )


    if cau_hoi:

        # Hiển thị câu hỏi người dùng
        st.session_state.messages.append(
            {
                "role": "user",
                "content": cau_hoi
            }
        )

        # Chatbot trả lời
        tra_loi = chatbot_tra_loi(cau_hoi)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": tra_loi
            }
        )

        # Refresh
        st.rerun()
