import streamlit as st
import datetime

st.set_page_config(
    page_title="Billing | Shree Ganesh Collections",
    page_icon="🪷",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Raleway:wght@300;400;500;600&display=swap');
html, body, [class*="css"] {
    font-family: 'Raleway', sans-serif;
    background-color: #faf6f1;
    color: #2c1810;
}
.topbar {
    background: linear-gradient(135deg, #7b2d00, #c0392b);
    border-radius: 14px;
    padding: 22px 36px;
    margin-bottom: 36px;
}
.topbar h2 {
    font-family: 'Playfair Display', serif;
    color: #fff8f0;
    margin: 0;
    font-size: 1.9rem;
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: #7b2d00;
    border-left: 5px solid #e67e22;
    padding-left: 12px;
    margin-bottom: 20px;
}
.bill-box {
    background: #ffffff;
    border: 1px solid #f0ddd0;
    border-radius: 16px;
    padding: 28px;
    box-shadow: 0 4px 20px rgba(123,45,0,0.09);
}
.bill-row {
    display: flex;
    justify-content: space-between;
    padding: 10px 0;
    border-bottom: 1px dashed #f0ddd0;
    font-size: 0.97rem;
}
.bill-label { color: #7a6050; font-weight: 500; }
.bill-value { color: #2c1810; font-weight: 600; }
.total-row {
    display: flex;
    justify-content: space-between;
    padding: 16px 0 8px 0;
    font-size: 1.25rem;
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    color: #7b2d00;
    border-top: 2px solid #e67e22;
    margin-top: 8px;
}
.success-box {
    background: #f0fdf4;
    border: 1.5px solid #86efac;
    border-radius: 14px;
    padding: 28px;
    text-align: center;
}
.success-box h3 { font-family: 'Playfair Display', serif; color: #166534; font-size: 1.7rem; }
.success-box p { color: #15803d; font-size: 1rem; }
div.stButton > button {
    background: linear-gradient(135deg, #7b2d00, #c0392b);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 32px;
    font-family: 'Raleway', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    width: 100%;
}
.footer {
    text-align: center;
    padding: 30px 0 10px 0;
    color: #9a7060;
    font-size: 0.83rem;
    border-top: 1px solid #e8d5c8;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="topbar">
    <h2>🧾 Billing & Payment — Shree Ganesh Collections</h2>
</div>
""", unsafe_allow_html=True)

order = st.session_state.get("order", {})

base_prices = {
    "Formal Shirts":   799,
    "Premium Jeans":   1199,
    "Casual T-Shirts": 399,
    "Trendy Shoes":    999,
}

if not order:
    st.warning("⚠️ No order found. Please go back and fill in the order form.")
    if st.button("← Back to Home"):
        st.switch_page("app.py")
    st.stop()

product = order.get("product", "N/A")
budget  = order.get("budget", 0)
name    = order.get("name", "")
phone   = order.get("phone", "")
email   = order.get("email", "")
address = order.get("address", "")

left, right = st.columns([1.1, 1], gap="large")

with left:
    st.markdown('<div class="section-title">Customer Details</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="bill-box">
        <div class="bill-row"><span class="bill-label">👤 Name</span><span class="bill-value">{name}</span></div>
        <div class="bill-row"><span class="bill-label">📞 Phone</span><span class="bill-value">{phone}</span></div>
        <div class="bill-row"><span class="bill-label">📧 Email</span><span class="bill-value">{email if email else '—'}</span></div>
        <div class="bill-row"><span class="bill-label">📦 Product</span><span class="bill-value">{product}</span></div>
        <div class="bill-row"><span class="bill-label">📍 Address</span><span class="bill-value">{address}</span></div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="section-title">Order Customisation</div>', unsafe_allow_html=True)

    qty = st.number_input("Quantity", min_value=1, max_value=20, value=1)

    size_options = {
        "Formal Shirts":   ["S", "M", "L", "XL", "XXL"],
        "Premium Jeans":   ["28", "30", "32", "34", "36", "38"],
        "Casual T-Shirts": ["S", "M", "L", "XL", "XXL"],
        "Trendy Shoes":    ["6", "7", "8", "9", "10", "11", "12"],
    }
    size = st.selectbox("Size / Fit", size_options.get(product, ["Free Size"]))

    color_options = {
        "Formal Shirts":   ["White", "Sky Blue", "Light Pink", "Charcoal", "Beige"],
        "Premium Jeans":   ["Dark Blue", "Black", "Grey", "Light Wash", "Olive"],
        "Casual T-Shirts": ["White", "Black", "Red", "Navy", "Mustard"],
        "Trendy Shoes":    ["Black", "White", "Brown", "Navy", "Tan"],
    }
    color = st.selectbox("Colour", color_options.get(product, ["Default"]))

    payment_method = st.radio(
        "Payment Method",
        ["💳 Credit / Debit Card", "📱 UPI / QR Code", "🏦 Net Banking", "💵 Cash on Delivery"],
        horizontal=True
    )

with right:
    st.markdown('<div class="section-title">Bill Summary</div>', unsafe_allow_html=True)

    unit_price  = base_prices.get(product, 999)
    subtotal    = unit_price * qty
    gst_amount  = round(subtotal * 0.12)
    delivery    = 0 if subtotal >= 1500 else 99
    grand_total = subtotal + gst_amount + delivery
    invoice_no  = f"SGC-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
    today       = datetime.date.today().strftime("%d %B %Y")

    st.markdown(f"""
    <div class="bill-box">
        <div style="text-align:center;margin-bottom:18px;">
            <div style="font-family:'Playfair Display',serif;font-size:1.25rem;color:#7b2d00;font-weight:700;">🪷 Shree Ganesh Collections</div>
            <div style="font-size:0.8rem;color:#9a7060;">Mumbai, Maharashtra · GST: 27AABCG1234Z1Z5</div>
        </div>
        <div class="bill-row"><span class="bill-label">Invoice No.</span><span class="bill-value">{invoice_no}</span></div>
        <div class="bill-row"><span class="bill-label">Date</span><span class="bill-value">{today}</span></div>
        <div class="bill-row"><span class="bill-label">Product</span><span class="bill-value">{product}</span></div>
        <div class="bill-row"><span class="bill-label">Size / Colour</span><span class="bill-value">{size} / {color}</span></div>
        <div class="bill-row"><span class="bill-label">Unit Price</span><span class="bill-value">₹{unit_price:,}</span></div>
        <div class="bill-row"><span class="bill-label">Quantity</span><span class="bill-value">× {qty}</span></div>
        <div class="bill-row"><span class="bill-label">Sub-total</span><span class="bill-value">₹{subtotal:,}</span></div>
        <div class="bill-row"><span class="bill-label">GST (12%)</span><span class="bill-value">₹{gst_amount:,}</span></div>
        <div class="bill-row"><span class="bill-label">Delivery</span><span class="bill-value">{'FREE 🎉' if delivery == 0 else f'₹{delivery}'}</span></div>
        <div class="total-row"><span>Grand Total</span><span>₹{grand_total:,}</span></div>
    </div>
    """, unsafe_allow_html=True)

    if grand_total > budget:
        st.warning(f"⚠️ Total ₹{grand_total:,} exceeds your budget of ₹{budget:,}.")

    st.write("")

    if "paid" not in st.session_state:
        st.session_state["paid"] = False

    if not st.session_state["paid"]:
        if st.button(f"✅  Confirm & Pay  ₹{grand_total:,}"):
            st.session_state["paid"] = True
            st.session_state["invoice"] = invoice_no
            st.rerun()
    else:
        st.markdown(f"""
        <div class="success-box">
            <h3>🎉 Order Confirmed!</h3>
            <p>Thank you, <strong>{name}</strong>!<br>
            Invoice: <strong>{st.session_state['invoice']}</strong><br>
            Amount Paid: <strong>₹{grand_total:,}</strong><br>
            Payment via: <strong>{payment_method}</strong><br><br>
            Expected delivery in <strong>3–5 business days</strong>.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.button("🛍️  Shop More"):
            st.session_state.pop("paid", None)
            st.session_state.pop("order", None)
            st.switch_page("app.py")

st.write("")
_, back_col, _ = st.columns([3, 1, 3])
with back_col:
    if st.button("← Back"):
        st.switch_page("app.py")

st.markdown("""
<div class="footer">
    🪷 Shree Ganesh Collections | Since 2005 | Mumbai, Maharashtra
</div>
""", unsafe_allow_html=True)
