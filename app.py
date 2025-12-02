import streamlit as st

# --- Page config ---
st.set_page_config(page_title="Amazon Demo", layout="wide")

# --- Fake product database ---
products = [
    {
        "name": "Wireless Headphones",
        "price": 49.99,
        "rating": 4.5,
        "image": "https://via.placeholder.com/200"
    },
    {
        "name": "Mechanical Keyboard",
        "price": 89.99,
        "rating": 4.7,
        "image": "https://via.placeholder.com/200"
    },
    {
        "name": "Smart Watch",
        "price": 129.99,
        "rating": 4.3,
        "image": "https://via.placeholder.com/200"
    }
]

# --- Sidebar ---
st.sidebar.title("Amazon Demo")
search = st.sidebar.text_input("Search products")
max_price = st.sidebar.slider("Max price", 0, 200, 200)

st.title("🛒 Amazon-Style Product Demo")

# --- Filter products ---
filtered = [
    p for p in products
    if search.lower() in p["name"].lower() and p["price"] <= max_price
]

# --- Display products ---
cols = st.columns(3)
for idx, product in enumerate(filtered):
    with cols[idx % 3]:
        st.image(product["image"])
        st.subheader(product["name"])
        st.write(f"Price: **${product['price']}**")
        st.write(f"⭐ {product['rating']}")
        if st.button("Add to Cart", key=product["name"]):
            st.success(f"Added {product['name']} to cart!")

if not filtered:
    st.info("No products match your search.")
