import streamlit as st

# ==============================
# CẤU HÌNH APP
# ==============================
st.set_page_config(
    page_title="Tính Bill Trà Sữa",
    page_icon="🧋"
)

st.title("🧋 APP TÍNH BILL TRÀ SỮA")
st.write("Vui lòng nhập thông tin đơn hàng bên dưới.")

# ==============================
# DANH SÁCH SẢN PHẨM
# ==============================
gia_tra_sua = {
    "Trà sữa truyền thống": 30000,
    "Trà sữa matcha": 35000,
    "Trà sữa socola": 35000,
    "Trà sữa khoai môn": 38000,
    "Trà sữa thái xanh": 35000
}

gia_topping = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 6000,
    "Pudding": 7000,
    "Thạch trái cây": 5000,
    "Kem cheese": 10000
}

# ==============================
# NHẬP THÔNG TIN
# ==============================
st.subheader("📋 Nhập thông tin đơn hàng")

loai_tra_sua = st.selectbox(
    "🧋 Chọn loại trà sữa:",
    list(gia_tra_sua.keys())
)

so_luong = st.number_input(
    "🔢 Số lượng:",
    min_value=1,
    max_value=20,
    value=1
)

topping = st.multiselect(
    "🥤 Chọn topping:",
    list(gia_topping.keys())
)

muc_duong = st.radio(
    "🍬 Mức độ đường:",
    ["100%", "70%", "0%"],
    horizontal=True
)

# ==============================
# NÚT TÍNH BILL
# ==============================
if st.button("🧾 TÍNH HÓA ĐƠN", use_container_width=True):

    # Tính tiền topping
    tien_topping = sum(
        gia_topping[item] for item in topping
    )

    # Giá một ly
    gia_mot_ly = gia_tra_sua[loai_tra_sua] + tien_topping

    # Tổng tiền
    tong_tien = gia_mot_ly * so_luong

    # ==============================
    # HIỂN THỊ KẾT QUẢ
    # ==============================
    st.divider()

    st.subheader("🧾 KẾT QUẢ ĐƠN HÀNG")

    st.write("### Thông tin đã nhập")

    st.write(f"🧋 **Loại trà sữa:** {loai_tra_sua}")

    st.write(f"🔢 **Số lượng:** {so_luong}")

    st.write(f"🍬 **Mức độ đường:** {muc_duong}")

    # Hiển thị topping
    if topping:
        st.write("🥤 **Topping:**")
        for item in topping:
            st.write(
                f"- {item}: {gia_topping[item]:,} VNĐ"
            )
    else:
        st.write("🥤 **Topping:** Không có")

    st.divider()

    # Hiển thị giá
    st.write(
        f"💵 **Giá trà sữa:** "
        f"{gia_tra_sua[loai_tra_sua]:,} VNĐ/ly"
    )

    st.write(
        f"🥤 **Tổng tiền topping:** "
        f"{tien_topping:,} VNĐ/ly"
    )

    st.write(
        f"💰 **Thành tiền mỗi ly:** "
        f"{gia_mot_ly:,} VNĐ"
    )

    st.divider()

    # Tổng thanh toán
    st.success(
        f"## 💵 TỔNG TIỀN CẦN THANH TOÁN: "
        f"{tong_tien:,} VNĐ"
    )
