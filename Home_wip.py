import streamlit as st
import base64

st.set_page_config(page_title="Goriber University", layout="wide")

def img_to_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

logo_base64 = img_to_base64("images/logo.png")
campus_base64 = img_to_base64("images/campus.jpg")

st.markdown(f"""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap" rel="stylesheet">

<style>
/* Remove default Streamlit toolbar */
header[data-testid="stHeader"], div[data-testid="stToolbar"] {{
    display: none !important;
}}

/* Navbar fixed on top */
.navbar {{
    position: fixed;
    top: 0;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 40px;
    background-color: rgb(122,30,31);
    z-index: 1000;
}}
.nav-left {{
    display: flex;
    align-items: center;
}}
.nav-left img {{
    height: 40px;
    margin-right: 15px;
}}
.nav-links a {{
    color: rgb(222,178,106);
    text-decoration: none;
    margin-left: 25px;
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    font-size: 1.1rem;
    letter-spacing: 1px;
}}
.nav-links a:hover {{
    text-decoration: underline;
}}

/* Banner full-width with overlay */
.banner {{
    position: relative;
    width: 100%;
    height: 300px;
    background-image: url("data:image/jpeg;base64,{campus_base64}");
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 0;
}}
.banner::after {{
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-color: rgba(158,110,55,0.5);
    z-index: 0;
}}

/* Centered banner text */
.banner-text {{
    position: relative;
    text-align: center;
    color: white;
    z-index: 1;
}}
.banner-text h1 {{
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 10px;
    text-shadow: 0px 2px 8px rgba(0,0,0,0.6);
    letter-spacing: 2px;
}}
.banner-text p {{
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    font-weight: 400;
    opacity: 0.9;
    text-shadow: 0px 2px 6px rgba(0,0,0,0.6);
}}

/* Spacer to prevent navbar overlapping content */
.navbar-spacer {{
    height: 60px; /* same as navbar height */
}}

.container {{
    padding: 20px 40px;
}}

@media (max-width: 768px) {{
    .navbar {{ flex-direction: column; padding: 10px 20px; }}
    .nav-links a {{ margin-left: 0; margin-top: 10px; display: block; }}
    .banner-text h1 {{ font-size: 2rem; }}
    .banner-text p {{ font-size: 1rem; }}
}}
</style>

<!-- Navbar -->
<div class="navbar">
    <div class="nav-left">
        <img src="data:image/png;base64,{logo_base64}" alt="Logo">
        <span style="color:white; font-family: 'Playfair Display', serif; font-size:1.3rem;">Goriber University</span>
    </div>
    <div class="nav-links">
        <a href="?page=Home">Home</a>
        <a href="?page=Departments">Departments</a>
        <a href="?page=About">About</a>
        <a href="?page=Contact">Contact</a>
    </div>
</div>

<!-- Spacer -->
<div class="navbar-spacer"></div>

<!-- Banner -->
<div class="banner">
    <div class="banner-text">
        <h1>Welcome to Goriber University</h1>
        <p>The pride of Debuland, where dreams meet reality.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Streamlit content below banner
st.markdown('<div class="container">', unsafe_allow_html=True)
st.subheader("Goriber University Offers numerous majors.")
st.write("Visit the Departments page for more information. We offer courses that make Debuland proud!")
st.markdown('</div>', unsafe_allow_html=True)


st.markdown("<h4 style='text-align: center;'>Want to regret your future life choices and enroll here? Then, Join Us!</h4>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center;'>Our Adress:</h5>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>456 Oreo Street, H-Town, Now York-420, Debuland</h6>", unsafe_allow_html=True)
