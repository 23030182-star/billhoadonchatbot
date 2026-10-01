import streamlit as st

# =========================================================
# 1. CẤU HÌNH APP
# =========================================================

st.set_page_config(
    page_title="HuynhPhuong",
    page_icon="🧋",
    layout="centered"
)


# =========================================================
# 2. GIAO DIỆN
# =========================================================

st.markdown("""
<style>

body {
    background-color: #fffaf5;
}

.main {
    background-color: #fffaf5;
}

/* Tên quán */
.shop-name {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #d97706;
    margin-top: 10px;
    margin-bottom: 0px;
}

/* Slogan */
.shop-slogan {
    text-align: center;
    font-size: 16px;
    color: #777777;
    margin-bottom: 20px;
}

/* Tiêu đề */
.title {
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    color: #333333;
    margin-bottom: 20px;
}

/* Tổng tiền */
.total-box {
    background-color: #fff1df;
    border: 2px solid #f59e0b;
    border-radius: 18px;
    padding: 25px;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 20px;
}

.total-title {
    font-size: 21px;
    font-weight: bold;
    color: #b45309;
}

.total-money {
    font-size: 35px;
    font-weight: 800;
    color: #d97706;
    margin-top: 10px;
}

/* Chatbot */
.chat-title {
    text-align: center;
    font-size: 27px;
    font-weight: bold;
    color: #d97706;
    margin-bottom: 15px;
}

/* Nút */
.stButton > button {
    border-radius: 12px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. MENU TRÀ SỮA
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


# =========================================================
# 4. MENU TRÀ
# =========================================================

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


# =========================================================
# 5. MENU ĐÁ XAY
# =========================================================

DA_XAY = {

    "Matcha đá xay": 45000,

    "Socola đá xay": 45000,

    "Cookie đá xay": 48000,

    "Dâu đá xay": 45000,

    "Khoai môn đá xay": 48000,

    "Caramel đá xay": 45000,

}


# =========================================================
# 6. TOPPING
# =========================================================

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


# =========================================================
# 7. GỘP TOÀN BỘ MENU
# =========================================================

MENU = {}

MENU.update(TRA_SUA)
MENU.update(TRA)
MENU.update(DA_XAY)


# =========================================================
# 8. HÀM ĐỊNH DẠNG TIỀN
# =========================================================

def tien(vnd):

    return f"{vnd:,} VNĐ"


# =========================================================
# 9. LOGO
# =========================================================

try:

    st.image(
        "logo1.jpg",
        use_container_width=True
    )

except:

    st.warning(
        "⚠️ Không tìm thấy file logo1.jpg"
    )


# =========================================================
# 10. TÊN QUÁN
# =========================================================

st.markdown(
    '<div class="shop-name">HuynhPhuong</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="shop-slogan">'
    '🧋 TRÀ SỮA • TRÀ • ĐÁ XAY'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# 11. TẠO 2 TAB
# =========================================================

tab_bill, tab_chat = st.tabs(
    [
        "🧾 TÍNH HÓA ĐƠN",
        "🤖 TRỢ LÝ CỦA HUYNHPHUONG"
    ]
)


# =========================================================
# 12. TAB TÍNH HÓA ĐƠN
# =========================================================

with tab_bill:

    st.markdown(
        '<div class="title">'
        '🧾 NHẬP ĐƠN HÀNG'
        '</div>',
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # CHỌN NHÓM ĐỒ UỐNG
    # -----------------------------------------------------

    nhom_mon = st.selectbox(
        "📋 Chọn nhóm đồ uống",

        [
            "Trà sữa",
            "Trà",
            "Đá xay"
        ]
    )


    # -----------------------------------------------------
    # CHỌN MENU TƯƠNG ỨNG
    # -----------------------------------------------------

    if nhom_mon == "Trà sữa":

        menu_hien_tai = TRA_SUA

    elif nhom_mon == "Trà":

        menu_hien_tai = TRA

    else:

        menu_hien_tai = DA_XAY


    # -----------------------------------------------------
    # CHỌN MÓN
    # -----------------------------------------------------

    mon = st.selectbox(
        "🧋 Chọn món",
        list(menu_hien_tai.keys())
    )


    # -----------------------------------------------------
    # SỐ LƯỢNG
    # -----------------------------------------------------

    so_luong = st.number_input(
        "🔢 Số lượng",

        min_value=1,

        max_value=50,

        value=1,

        step=1
    )


    # -----------------------------------------------------
    # TOPPING
    # -----------------------------------------------------

    topping_chon = st.multiselect(
        "🥤 Chọn topping",

        list(TOPPING.keys()),

        placeholder="Bạn có thể chọn nhiều topping"
    )


    # -----------------------------------------------------
    # MỨC ĐƯỜNG
    # -----------------------------------------------------

    muc_duong = st.radio(
        "🍬 Mức độ đường",

        [
            "100%",
            "70%",
            "0%"
        ],

        horizontal=True
    )


    st.write("")


    # =====================================================
    # NÚT TÍNH HÓA ĐƠN
    # =====================================================

    if st.button(
        "🧾 TÍNH HÓA ĐƠN",

        use_container_width=True,

        type="primary"
    ):

        gia_mon = menu_hien_tai[mon]


        tien_topping = sum(
            TOPPING[x]
            for x in topping_chon
        )


        gia_mot_ly = (
            gia_mon
            + tien_topping
        )


        tong_tien = (
            gia_mot_ly
            * so_luong
        )


        # Lưu dữ liệu
        st.session_state.bill = {

            "nhom_mon": nhom_mon,

            "mon": mon,

            "so_luong": so_luong,

            "topping": topping_chon,

            "muc_duong": muc_duong,

            "gia_mon": gia_mon,

            "tien_topping": tien_topping,

            "gia_mot_ly": gia_mot_ly,

            "tong_tien": tong_tien
        }


    # =====================================================
    # HIỂN THỊ BILL
    # =====================================================

    if "bill" in st.session_state:

        bill = st.session_state.bill


        st.divider()


        st.markdown(
            '<div class="title">'
            '🧾 KẾT QUẢ ĐƠN HÀNG'
            '</div>',
            unsafe_allow_html=True
        )


        # -------------------------------------------------
        # THÔNG TIN
        # -------------------------------------------------

        st.info(
            f"""
📋 **Nhóm món:** {bill["nhom_mon"]}

🧋 **Tên món:** {bill["mon"]}

🔢 **Số lượng:** {bill["so_luong"]} ly

🍬 **Mức độ đường:** {bill["muc_duong"]}
"""
        )


        # -------------------------------------------------
        # TOPPING
        # -------------------------------------------------

        if bill["topping"]:

            st.write(
                "🥤 **Topping đã chọn:**"
            )

            for item in bill["topping"]:

                st.write(
                    f"• {item}: "
                    f"{tien(TOPPING[item])}"
                )

        else:

            st.write(
                "🥤 **Topping:** Không có"
            )


        st.divider()


        # -------------------------------------------------
        # CHI TIẾT GIÁ
        # -------------------------------------------------

        st.write(
            f"💵 Giá món: "
            f"**{tien(bill['gia_mon'])}/ly**"
        )


        st.write(
            f"🥤 Tiền topping: "
            f"**{tien(bill['tien_topping'])}/ly**"
        )


        st.write(
            f"💰 Thành tiền mỗi ly: "
            f"**{tien(bill['gia_mot_ly'])}**"
        )


        st.write(
            f"🔢 Số lượng: "
            f"**{bill['so_luong']} ly**"
        )


        # =================================================
        # TỔNG TIỀN
        # =================================================

        st.markdown(
            f"""
<div class="total-box">

<div class="total-title">
💵 TỔNG TIỀN CẦN THANH TOÁN
</div>

<div class="total-money">
{tien(bill['tong_tien'])}
</div>

</div>
""",
            unsafe_allow_html=True
        )


        st.success(
            "❤️ Cảm ơn quý khách đã ủng hộ HuynhPhuong!"
        )


# =========================================================
# 13. CHATBOT
# =========================================================

with tab_chat:

    st.markdown(
        '<div class="chat-title">'
        '🤖 Trợ lý của HuynhPhuong'
        '</div>',
        unsafe_allow_html=True
    )


    st.write(
        "Xin chào 👋 Mình là **trợ lý của HuynhPhuong**."
    )


    st.write(
        "Bạn có thể hỏi mình về menu, giá, "
        "bestseller, topping hoặc nhờ mình gợi ý món."
    )


    st.divider()


    # =====================================================
    # KHỞI TẠO CHAT
    # =====================================================

    if "messages" not in st.session_state:

        st.session_state.messages = [

            {
                "role": "assistant",

                "content":
                "Xin chào 👋 Mình là **trợ lý của HuynhPhuong**. "
                "Bạn muốn hỏi gì nào? 🧋"
            }

        ]


    # =====================================================
    # HIỂN THỊ LỊCH SỬ
    # =====================================================

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )


    # =====================================================
    # HÀM CHATBOT
    # =====================================================

    def chatbot_tra_loi(cau_hoi):

        cau_hoi = cau_hoi.lower().strip()


        # =================================================
        # TÍNH MÓN RẺ NHẤT
        # =================================================

        mon_re = min(
            MENU.items(),
            key=lambda x: x[1]
        )


        # =================================================
        # TÍNH MÓN ĐẮT NHẤT
        # =================================================

        mon_dat = max(
            MENU.items(),
            key=lambda x: x[1]
        )


        # =================================================
        # TÍNH TOPPING RẺ NHẤT
        # =================================================

        topping_re = min(
            TOPPING.items(),
            key=lambda x: x[1]
        )


        # =================================================
        # TÍNH TOPPING ĐẮT NHẤT
        # =================================================

        topping_dat = max(
            TOPPING.items(),
            key=lambda x: x[1]
        )


        # =================================================
        # BESTSELLER
        # =================================================

        if (

            "bestseller" in cau_hoi

            or "best seller" in cau_hoi

            or "bán chạy nhất" in cau_hoi

            or "bán chạy" in cau_hoi

            or "yêu thích nhất" in cau_hoi

            or "phổ biến nhất" in cau_hoi

        ):

            return f"""
🔥 **MÓN BESTSELLER CỦA HUYNHPHUONG**

🧋 **Trà sữa truyền thống**

💰 Giá: **{tien(TRA_SUA["Trà sữa truyền thống"])}/ly**

⭐ Đây là món HuynhPhuong giới thiệu
cho khách hàng muốn thử hương vị
truyền thống.

💡 Gợi ý:

**Trà sữa truyền thống
+ Trân châu đen
+ 70% đường**
"""


        # =================================================
        # MÓN RẺ NHẤT
        # =================================================

        if (

            "món rẻ nhất" in cau_hoi

            or "món nào rẻ nhất" in cau_hoi

            or "rẻ nhất" in cau_hoi

            or "giá thấp nhất" in cau_hoi

        ):

            return f"""
💰 **MÓN RẺ NHẤT**

🍹 **{mon_re[0]}**

💵 Giá:

**{tien(mon_re[1])}/ly**
"""


        # =================================================
        # MÓN ĐẮT NHẤT
        # =================================================

        if (

            "món đắt nhất" in cau_hoi

            or "món nào đắt nhất" in cau_hoi

            or "đắt nhất" in cau_hoi

            or "giá cao nhất" in cau_hoi

            or "mắc nhất" in cau_hoi

        ):

            return f"""
💎 **MÓN ĐẮT NHẤT**

🧋 **{mon_dat[0]}**

💵 Giá:

**{tien(mon_dat[1])}/ly**
"""


        # =================================================
        # TOPPING RẺ NHẤT
        # =================================================

        if (

            "topping rẻ nhất" in cau_hoi

            or "topping nào rẻ nhất" in cau_hoi

        ):

            return f"""
🥤 **TOPPING RẺ NHẤT**

**{topping_re[0]}**

💰 Giá:

**{tien(topping_re[1])}**
"""


        # =================================================
        # TOPPING ĐẮT NHẤT
        # =================================================

        if (

            "topping đắt nhất" in cau_hoi

            or "topping nào đắt nhất" in cau_hoi

            or "topping mắc nhất" in cau_hoi

        ):

            return f"""
🥤 **TOPPING ĐẮT NHẤT**

**{topping_dat[0]}**

💰 Giá:

**{tien(topping_dat[1])}**
"""


        # =================================================
        # MENU
        # =================================================

        if (

            "menu" in cau_hoi

            or "có món gì" in cau_hoi

            or "món gì" in cau_hoi

            or "danh sách món" in cau_hoi

        ):

            tra_loi = "🧋 **MENU HUYNHPHUONG**\n\n"


            tra_loi += "### 🧋 TRÀ SỮA\n\n"

            for ten, gia in TRA_SUA.items():

                tra_loi += (
                    f"• {ten}: "
                    f"{tien(gia)}\n"
                )


            tra_loi += "\n### 🍵 TRÀ\n\n"

            for ten, gia in TRA.items():

                tra_loi += (
                    f"• {ten}: "
                    f"{tien(gia)}\n"
                )


            tra_loi += "\n### 🥤 ĐÁ XAY\n\n"

            for ten, gia in DA_XAY.items():

                tra_loi += (
                    f"• {ten}: "
                    f"{tien(gia)}\n"
                )


            return tra_loi


        # =================================================
        # TOPPING
        # =================================================

        if (

            "topping" in cau_hoi

            or "có topping gì" in cau_hoi

        ):

            tra_loi = "🥤 **TOPPING HUYNHPHUONG**\n\n"


            for ten, gia in TOPPING.items():

                tra_loi += (
                    f"• {ten}: "
                    f"{tien(gia)}\n"
                )


            return tra_loi


        # =================================================
        # MỨC ĐƯỜNG
        # =================================================

        if (

            "đường" in cau_hoi

            or "ngọt" in cau_hoi

        ):

            return """
🍬 **MỨC ĐỘ ĐƯỜNG**

🟠 **100%**
Ngọt bình thường.

🟡 **70%**
Ít ngọt, dễ uống.

⚪ **0%**
Không đường.

💡 Nếu bạn không thích quá ngọt,
có thể chọn **70%**.
"""


        # =================================================
        # MÓN 0% ĐƯỜNG
        # =================================================

        if (

            "0% đường" in cau_hoi

            or "không đường" in cau_hoi

        ):

            return """
🍵 Bạn có thể chọn **0% đường**.

Một số món phù hợp:

• Trà đào
• Trà vải
• Trà ô long đào
• Trà ô long vải
• Trà chanh

Bạn cũng có thể chọn 0% đường
cho trà sữa.
"""


        # =================================================
        # MÓN DƯỚI 30K
        # =================================================

        if (

            "dưới 30k" in cau_hoi

            or "dưới 30.000" in cau_hoi

            or "dưới 30000" in cau_hoi

        ):

            danh_sach = [

                (ten, gia)

                for ten, gia in MENU.items()

                if gia < 30000

            ]


            if not danh_sach:

                return (
                    "Hiện tại không có món nào "
                    "dưới 30.000 VNĐ."
                )


            tra_loi = "💰 **MÓN DƯỚI 30.000 VNĐ**\n\n"


            for ten, gia in danh_sach:

                tra_loi += (
                    f"• {ten}: "
                    f"{tien(gia)}\n"
                )


            return tra_loi


        # =================================================
        # GIÁ
        # =================================================

        if (

            "giá" in cau_hoi

            or "bao nhiêu" in cau_hoi

        ):

            return """
💰 **MỨC GIÁ HUYNHPHUONG**

🧋 Trà sữa:
30.000 - 45.000 VNĐ

🍵 Trà:
25.000 - 38.000 VNĐ

🥤 Đá xay:
45.000 - 48.000 VNĐ

🍮 Topping:
5.000 - 10.000 VNĐ
"""


        # =================================================
        # TƯ VẤN
        # =================================================

        if (

            "tư vấn" in cau_hoi

            or "gợi ý" in cau_hoi

            or "nên uống gì" in cau_hoi

            or "nên chọn gì" in cau_hoi

        ):

            return """
😊 **GỢI Ý TỪ TRỢ LÝ CỦA HUYNHPHUONG**

🔥 Muốn thử bestseller:

Trà sữa truyền thống
+ Trân châu đen
+ 70% đường

🍵 Muốn thanh nhẹ:

Trà đào cam sả
+ 70% đường

🍵 Muốn thơm:

Trà ô long đào
+ 70% đường

🍫 Thích chocolate:

Socola đá xay
+ Kem cheese

🍵 Thích matcha:

Matcha kem cheese
+ Trân châu trắng

💰 Muốn tiết kiệm:

Trà chanh
+ 70% đường
"""


        # =================================================
        # CHÀO
        # =================================================

        if (

            "xin chào" in cau_hoi

            or "hello" in cau_hoi

            or cau_hoi == "chào"

        ):

            return (
                "Xin chào 👋 "
                "Mình là **trợ lý của HuynhPhuong**. "
                "Mình có thể tư vấn món cho bạn! 🧋❤️"
            )


        # =================================================
        # CẢM ƠN
        # =================================================

        if "cảm ơn" in cau_hoi:

            return (
                "Không có gì ạ ❤️ "
                "Cảm ơn bạn đã ghé HuynhPhuong!"
            )


        # =================================================
        # KHÔNG HIỂU
        # =================================================

        return """
🤖 **Trợ lý của HuynhPhuong có thể giúp bạn:**

🧋 Xem menu

🔥 Hỏi món bestseller

💰 Tìm món rẻ nhất

💎 Tìm món đắt nhất

🥤 Tìm topping rẻ/đắt nhất

🍬 Hỏi mức đường

😊 Tư vấn món

💵 Hỏi giá

Ví dụ:

👉 "Món bestseller là món nào?"

👉 "Món nào rẻ nhất?"

👉 "Món nào đắt nhất?"

👉 "Topping nào rẻ nhất?"

👉 "Có món nào dưới 30k không?"

👉 "Tư vấn cho tôi một món ít ngọt"
"""


    # =====================================================
    # Ô NHẬP CHAT
    # =====================================================

    cau_hoi = st.chat_input(
        "Nhập câu hỏi cho trợ lý của HuynhPhuong..."
    )


    # =====================================================
    # XỬ LÝ CHAT
    # =====================================================

    if cau_hoi:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": cau_hoi
            }
        )


        tra_loi = chatbot_tra_loi(
            cau_hoi
        )


        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": tra_loi
            }
        )


        st.rerun()
