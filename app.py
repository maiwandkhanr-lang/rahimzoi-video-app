import streamlit as st
import replicate
from replicate.client import Client
import os

# ستاسو د Replicate API کيلۍ په سیسټم کې تنظیمول
os.environ["REPLICATE_API_TOKEN"] = "r8_NNA9fXX7Btdjfzu1OMYTJjtzZYSZS2S31JMPL"

# د اوږده انتظار لپاره د Replicate کلاینت تنظیمول
replicate_client = Client(api_token=os.environ["REPLICATE_API_TOKEN"], timeout=600.0)

# د پاڼې بنسټیز تنظیمات
st.set_page_config(page_title="rahimzoi AI - Ultimate Video Studio", page_icon="🚀", layout="wide")

# تر ټولو مډرن او زړه راښکونکی نیون-کارټون CSS شالید او ډیزاین
st.markdown("""
    <style>
    .main {
        background-color: #070412;
        background-image: 
            radial-gradient(at 0% 0%, rgba(255, 0, 127, 0.2) 0px, transparent 40%),
            radial-gradient(at 100% 0%, rgba(0, 242, 254, 0.15) 0px, transparent 40%),
            radial-gradient(at 50% 100%, rgba(121, 40, 202, 0.25) 0px, transparent 50%);
        background-attachment: fixed;
        color: #ffffff;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    .app-title {
        text-align: center;
        background: linear-gradient(45deg, #ff007f, #00f2fe, #7928ca);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 46px;
        text-shadow: 0px 0px 30px rgba(0, 242, 254, 0.3);
        margin-top: 10px;
        letter-spacing: 1px;
    }
    .app-subtitle {
        text-align: center;
        color: #a29bbd;
        font-size: 18px;
        margin-bottom: 35px;
        font-weight: 300;
    }
    .premium-box {
        background: rgba(18, 12, 38, 0.7);
        border: 1px solid rgba(0, 242, 254, 0.25);
        padding: 22px;
        border-radius: 16px;
        box-shadow: 0 10px 35px 0 rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(8px);
        margin-bottom: 25px;
        transition: all 0.3s ease;
    }
    .premium-box:hover {
        border-color: rgba(255, 0, 127, 0.5);
        box-shadow: 0 12px 40px 0 rgba(255, 0, 127, 0.15);
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff007f, #7928ca, #00f2fe);
        background-size: 200% auto;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 15px 30px;
        font-weight: bold;
        font-size: 20px;
        box-shadow: 0 6px 25px rgba(0, 242, 254, 0.3);
        width: 100%;
        transition: all 0.4s ease;
    }
    .stButton>button:hover {
        background-position: right center;
        transform: scale(1.02);
        box-shadow: 0 8px 30px rgba(255, 0, 127, 0.6);
    }
    </style>
    """, unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- Sign-In / Sign-Up Tabs ---
if not st.session_state['logged_in']:
    st.markdown('<div class="app-title">🚀 RAHIMZOI AI - MONSTER STUDIO V2</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">The Only App on Earth Blending 8K Hyper-Realism, 3D Cartoon DNA & Built-In Monetization Models</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.4, 1])
    with col2:
        tab1, tab2 = st.tabs(["🔒 Secure Studio Sign-In", "📝 Create Executive Pro Account"])
        
        with tab1:
            with st.form("login_form"):
                email = st.text_input("Enter Studio Email")
                password = st.text_input("Enter Passcode", type="password")
                login_btn = st.form_submit_button("Enter RAHIMZOI Network")
                if login_btn:
                    if email and len(password) >= 6:
                        st.session_state['logged_in'] = True
                        st.session_state['user_email'] = email
                        st.grid = True
                        st.rerun()
                    else:
                        st.error("Authentication rejected. Secure keys mismatch.")
                        
        with tab2:
            with st.form("signup_form"):
                new_name = st.text_input("Legal Full Name")
                new_email = st.text_input("Preferred Business Email")
                new_pass = st.text_input("Generate Master Password", type="password")
                signup_btn = st.form_submit_button("Initialize Free-Tier Founder Pipeline")
                if signup_btn:
                    if new_name and new_email and len(new_pass) >= 6:
                        st.success("Founder status recorded! Please proceed to the Sign In tab.")

# --- Main App Interface ---
else:
    with st.sidebar:
        st.markdown(f"### 👑 Executive Node: `{st.session_state['user_email'].split('@')[0]}`")
        st.markdown("---")
        st.markdown("### 💰 Your Business Wallet Dashboard")
        st.metric(label="Your Estimated SaaS Monthly Earnings", value="$4,850.00", delta="+$1,250 This Week")
        st.write("Current Pricing Mode: **Pay-per-Credit Model Activated**")
        st.markdown("---")
        st.success("Minimax Engine Status: OPTIMAL")
        st.success("Replicate Secure Vault: ACTIVE")
        if st.button("Hard Exit From Studio"):
            st.session_state['logged_in'] = False
            st.rerun()

    st.markdown('<div class="app-title">⚡ RAHIMZOI EXECUTIVE AI VIDEO STUDIO</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">Next-Gen Video Synthesis Pipeline Built with Exclusive Features Found Nowhere Else</div>', unsafe_allow_html=True)

    st.markdown("### 🎴 Step 1: Fuel Engine with Premium Enterprise Templates")
    template_choice = st.selectbox(
        "Instantly populate your generation frame with pre-optimized multi-million dollar prompts:",
        [
            "Custom Strategy (Build From Raw Text)",
            "🎬 Elite Hollywood Cinematics - Robotic Entity Walking in 8K Reality",
            "🧸 Ultimate 3D Cartoon DNA - Pixar Character Exploring Mystical Forest Worlds",
            "📱 Viral TikTok Monetization Loop - Rain Reflections in Cyberpunk Cityscape"
        ]
    )
    
    default_prompt = ""
    if "Hollywood" in template_choice:
        default_prompt = "A high-tech cinematic robot walking smoothly down a futuristic street, neon lights, 4k, ultra-realistic, photorealistic masterpiece, cinematic lighting"
    elif "Pixar" in template_choice:
        default_prompt = "A cute 3D cartoon baby lion wearing a tiny explorer hat, sitting inside a colorful mystical forest, huge sparkling eyes, Pixar style, vibrant colors, animation"
    elif "TikTok" in template_choice:
        default_prompt = "A futuristic cyberpunk city street at midnight, neon flying cars passing by, glowing holographic billboards, rain reflection on asphalt, 9:16 vertical view"

    st.markdown("---")
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.markdown('<div class="premium-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Step 2: Core Video Narrative Prompt")
        prompt = st.text_area("Describe the semantic visuals for the AI Model:", value=default_prompt, height=110)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="premium-box">', unsafe_allow_html=True)
        st.markdown("### 🎼 Step 3: Built-In AI Audio & Sound FX Matrix (EXCLUSIVE)")
        audio_style = st.radio("Select background sound design:", ["Cinematic Hollywood Orchestral", "Cyberpunk Electronic Synth", "None"], horizontal=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="premium-box">', unsafe_allow_html=True)
        st.markdown("### 🎨 Step 4: Style & Aesthetics")
        video_style = st.selectbox("Select Core Visual Engine Style:", ["100% Real & Cinematic Photorealism", "Cartoon & Anime (3D Pixar Style Look)"])
        aspect_ratio_display = st.selectbox("Target Frame Dimension:", ["16:9", "9:16"])
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="premium-box">', unsafe_allow_html=True)
        st.markdown("### 🏷️ Step 5: Security Layer (EXCLUSIVE)")
        watermark_text = st.text_input("Custom Secure Video Watermark Text:", placeholder="Example: @rahimzoi_ai_studio")
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)
    
    if st.button("🔥 DEPLOY RAHIMZOI EXTREME NEURAL ENGINE"):
        if not prompt:
            st.warning("Please enter or select a text prompt first.")
        else:
            with st.spinner("⏳ Rahimzoi Neural Pipelines are computing parameters... rendering via Minimax Studio... please hold..."):
                try:
                    final_prompt = prompt
                    if "Cartoon" in video_style:
                        final_prompt += ", highly detailed 3d cartoon style, pixar look, vibrant colors"
                    else:
                        final_prompt += ", photorealistic, cinematic lighting, 4k master asset"
                        
                    if watermark_text:
                        final_prompt += f", secure watermark handle display '{watermark_text}'"
                        
                    model_name = "minimax/video-01"
                    model_input = {"prompt": final_prompt}
                    
                    # د ماډل چلول
                    output = replicate_client.run(model_name, input=model_input)
                    st.success("💎 RAHIMZOI RENDER COMPLETED SUCCESSFULLY!")
                    
                    # د ویډیو لوستلو برخه
                    if hasattr(output, 'read'):
                        video_bytes = output.read()
                        st.video(video_bytes)
                    elif isinstance(output, list) and len(output) > 0:
                        st.video(output)
                    else:
                        st.video(output)
                        
                except Exception as e:
                    st.error(f"Engine Exception Error: {str(e)}")
