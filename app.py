import streamlit as st

st.set_page_config(
    page_title="Shree Ganesh Collections",
    page_icon="🪷",
    layout="wide"
)

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Raleway:wght@300;400;500;600&display=swap');

/* Global */
html, body, [class*="css"] {
    font-family: 'Raleway', sans-serif;
    background-color: #faf6f1;
    color: #2c1810;
}

/* Hero banner */
.hero {
    background: linear-gradient(135deg, #7b2d00 0%, #c0392b 40%, #e67e22 100%);
    border-radius: 20px;
    padding: 60px 40px;
    text-align: center;
    margin-bottom: 40px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: "🪷";
    position: absolute;
    font-size: 200px;
    opacity: 0.07;
    top: -30px;
    left: -30px;
}
.hero::after {
    content: "🪷";
    position: absolute;
    font-size: 200px;
    opacity: 0.07;
    bottom: -30px;
    right: -30px;
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 3.2rem;
    font-weight: 900;
    color: #fff8f0;
    margin: 0;
    letter-spacing: 2px;
    text-shadow: 2px 4px 12px rgba(0,0,0,0.3);
}
.hero p {
    font-size: 1.15rem;
    color: #ffe0cc;
    margin-top: 12px;
    font-weight: 300;
    letter-spacing: 3px;
    text-transform: uppercase;
}

/* Section headings */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.9rem;
    font-weight: 700;
    color: #7b2d00;
    border-left: 5px solid #e67e22;
    padding-left: 14px;
    margin-bottom: 24px;
}

/* Product card */
.product-card {
    background: #ffffff;
    border-radius: 16px;
    padding: 24px 20px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(123,45,0,0.10);
    border: 1px solid #f0ddd0;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    height: 100%;
}
.product-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 30px rgba(123,45,0,0.18);
}
.product-emoji {
    font-size: 4rem;
    display: block;
    margin-bottom: 10px;
}
.product-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: #2c1810;
    margin-bottom: 6px;
}
.product-price {
    font-size: 1rem;
    font-weight: 600;
    color: #c0392b;
    margin-bottom: 4px;
}
.product-desc {
    font-size: 0.85rem;
    color: #7a6050;
    font-weight: 400;
}

/* Badge */
.badge {
    display: inline-block;
    background: #fff3e8;
    color: #c0392b;
    border: 1px solid #f5c6a0;
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 16px;
}

/* Footer */
.footer {
    text-align: center;
    padding: 30px 0 10px 0;
    color: #9a7060;
    font-size: 0.85rem;
    border-top: 1px solid #e8d5c8;
    margin-top: 50px;
}

/* Streamlit button override */
div.stButton > button {
    background: linear-gradient(135deg, #7b2d00, #c0392b);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 32px;
    font-family: 'Raleway', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    letter-spacing: 1px;
    width: 100%;
    cursor: pointer;
    transition: opacity 0.2s;
}
div.stButton > button:hover {
    opacity: 0.88;
    color: white;
}

/* Select / slider label */
label {
    font-family: 'Raleway', sans-serif !important;
    font-weight: 500 !important;
    color: #2c1810 !important;
}
</style>
""", unsafe_allow_html=True)

# ── Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>🪷 Shree Ganesh Collections</h1>
    <p>Tradition · Style · Excellence</p>
</div>
""", unsafe_allow_html=True)

# ── Products ──────────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">Our Collections</div>', unsafe_allow_html=True)

products = [
    {"emoji": "👔", "name": "Formal Shirts",  "price": "₹799 – ₹2,499",  "desc": "Crisp cotton & linen blends for every occasion"},
    {"emoji": "👖", "name": "Premium Jeans",  "price": "₹1,199 – ₹3,999", "desc": "Slim, straight & relaxed fits in classic washes"},
    {"emoji": "👕", "name": "Casual T-Shirts","price": "₹399 – ₹1,299",  "desc": "100% cotton comfort with vibrant prints"},
    {"emoji": "👟", "name": "Trendy Shoes",   "price": "₹999 – ₹5,999",  "desc": "Sneakers, loafers & formal footwear"},
]

cols = st.columns(4, gap="medium")
for col, p in zip(cols, products):
    with col:
        st.markdown(f"""
        <div class="product-card">
            <span class="product-emoji">{p['emoji']}</span>
            <div class="product-name">{p['name']}</div>
            <div class="product-price">{p['price']}</div>
            <div class="product-desc">{p['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.write("")

# ── Quick Order Form ──────────────────────────────────────────────────────────
st.markdown('<div class="section-title">Place Your Order</div>', unsafe_allow_html=True)

left, right = st.columns([1.2, 1], gap="large")

with left:
    selected_product = st.selectbox(
        "Select Product Category",
        ["— Choose a product —", "Formal Shirts", "Premium Jeans", "Casual T-Shirts", "Trendy Shoes"]
    )
    budget = st.slider(
        "Your Budget (₹)",
        min_value=500,
        max_value=10000,
        step=500,
        value=2000
    )
    st.caption(f"💰 Selected Budget: **₹{budget:,}**")

with right:
    name     = st.text_input("Full Name", placeholder="e.g. Ramesh Sharma")
    phone    = st.text_input("Contact Number", placeholder="+91 98765 43210")
    email    = st.text_input("Email Address", placeholder="you@example.com")
    address  = st.text_area("Delivery Address", placeholder="Flat No, Street, City, PIN", height=90)

st.write("")
if st.button("🛒  Proceed to Billing"):
    if selected_product == "— Choose a product —":
        st.warning("Please select a product category before proceeding.")
    elif not name or not phone or not address:
        st.warning("Please fill in Name, Contact, and Address.")
    else:
        st.session_state["order"] = {
            "product": selected_product,
            "budget":  budget,
            "name":    name,
            "phone":   phone,
            "email":   email,
            "address": address,
        }
        st.switch_page("pages/billing.py")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    🪷 Shree Ganesh Collections &nbsp;|&nbsp; Since 2005 &nbsp;|&nbsp; Mumbai, Maharashtra<br>
    Crafting style with devotion.
</div>
""", unsafe_allow_html=True)