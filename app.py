import streamlit as st

# ==========================================
# CẤU HÌNH TRANG
# ==========================================
st.set_page_config(
    page_title="Huỳnh Phương - Tính Bill",
    page_icon="🧋",
    layout="centered"
)

# ==========================================
# CSS GIAO DIỆN
# ==========================================
st.markdown("""
<style>
    .main {
        background-color: #fffaf5;
    }

    .shop-name {
        text-align: center;
        font-size: 38px;
        font-weight: bold;
        color: #d97706;
        margin-bottom: 0px;
    }

    .shop-slogan {
        text-align: center;
        color: #777;
        font-size: 16px;
        margin-bottom: 20px;
    }

    .bill-title {
        text-align: center;
        font-size: 27px;
        font-weight: bold;
        color: #333;
    }

    .total-box {
        background-color: #fff1df;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 2px solid #f59e0b;
    }

    .total-text {
        font-size: 25px;
        font-weight: bold;
        color: #d97706;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# LOGO
# ==========================================
try:
    st.image(
        "logo1.jpg",
        width=300
    )
except:
    st.warning("Không tìm thấy file logo1.jpg")


# ==========================================
# TÊN QUÁN
# ==========================================
st.markdown(
    '<div class="shop-name">HUỲNH PHƯƠNG</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="shop-slogan">🧋 Trà sữa & đồ uống</div>',
    unsafe_allow_html=True
)

st.divider()


# ==========================================
# MENU TRÀ SỮA
# ==========================================
tra_sua = {
    "Trà sữa truyền thống": 30000,
    "Trà sữa matcha": 35000,
    "Trà sữa socola": 35000,
    "Trà sữa khoai môn": 38000,
    "Trà sữa thái xanh": 35000,
    "Trà sữa dâu": 38000
}


# ==========================================
# MENU TOPPING
# ==========================================
topping_menu = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 6000,
    "Pudding trứng": 7000,
    "Thạch trái cây": 5000,
    "Kem cheese": 10000
}


# ==========================================
# NHẬP ĐƠN HÀNG
# ==========================================
st.markdown(
    '<div class="bill-title">🧾 NHẬP ĐƠN HÀNG</div>',
    unsafe_allow_html=True
)

st.write("")


# Loại trà sữa
loai_tra_sua = st.selectbox(
    "🧋 Chọn loại trà sữa",
    list(tra_sua.keys())
)


# Số lượng
so_luong = st.number_input(
    "🔢 Số lượng",
    min_value=1,
    max_value=50,
    value=1,
    step=1
)


# Topping
topping = st.multiselect(
    "🥤 Chọn topping",
    list(topping_menu.keys())
)


# Mức đường
muc_duong = st.radio(
    "🍬 Mức độ đường",
    ["100%", "70%", "0%"],
    horizontal=True
)


st.write("")


# ==========================================
# NÚT TÍNH BILL
# ==========================================
if st.button(
    "🧾 TÍNH HÓA ĐƠN",
    use_container_width=True
):

    # Giá trà sữa
    gia_tra_sua = tra_sua[loai_tra_sua]

    # Tổng tiền topping cho 1 ly
    tien_topping = sum(
        topping_menu[item]
        for item in topping
    )

    # Giá 1 ly
    gia_mot_ly = gia_tra_sua + tien_topping

    # Tổng tiền
    tong_tien = gia_mot_ly * so_luong


    # ======================================
    # KẾT QUẢ
    # ======================================
    st.divider()

    st.markdown(
        '<div class="bill-title">🧾 KẾT QUẢ ĐƠN HÀNG</div>',
        unsafe_allow_html=True
    )

    st.write("")


    # ======================================
    # HIỂN THỊ LẠI THÔNG TIN ĐÃ NHẬP
    # ======================================

    st.info(
        f"""
🧋 **Loại trà sữa:** {loai_tra_sua}

🔢 **Số lượng:** {so_luong} ly

🍬 **Mức độ đường:** {muc_duong}
"""
    )


    # ======================================
    # TOPPING
    # ======================================
    if topping:

        st.write("🥤 **Topping đã chọn:**")

        for item in topping:
            st.write(
                f"• {item}: {topping_menu[item]:,} VNĐ"
            )

    else:

        st.write("🥤 **Topping:** Không có")


    st.divider()


    # ======================================
    # CHI TIẾT GIÁ
    # ======================================
    st.write(
        f"💵 Giá trà sữa: **{gia_tra_sua:,} VNĐ/ly**"
    )

    st.write(
        f"🥤 Tiền topping: **{tien_topping:,} VNĐ/ly**"
    )

    st.write(
        f"💰 Giá 1 ly: **{gia_mot_ly:,} VNĐ**"
    )

    st.write(
        f"🔢 Số lượng: **{so_luong} ly**"
    )


    # ======================================
    # TỔNG THANH TOÁN
    # ======================================
    st.write("")

    st.markdown(
        f"""
        <div class="total-box">
            <div class="total-text">
                💵 TỔNG TIỀN CẦN THANH TOÁN
            </div>
            <div style="font-size:32px; font-weight:bold; margin-top:10px;">
                {tong_tien:,} VNĐ
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")

    st.success(
        "✅ Cảm ơn quý khách đã mua hàng tại HUỲNH PHƯƠNG!"
    )
