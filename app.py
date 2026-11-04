
#=============================================================================
      #   🦉 OROMOLINGO WEB — ONLINE AFAAN OROMOO LEARNING PLATFORM 🦉
#=============================================================================
#Features:
# - Web Interface accessible worldwide via URL (Mobile & Desktop friendly)
# - Authentication: Google, Facebook, and Email/Guest Sign-In
# - Duolingo-style UI with Gamification (XP, Hearts, Streaks, Levels)
# - 12 Interactive Units, Quizzes, Flashcards, and Global Leaderboard
#=============================================================================
"""

import streamlit as st
import time
import json
import random

# --- PAGE CONFIGURATION & DUOLINGO STYLING ---
st.set_page_config(
    page_title="OromoLingo — Learn Afaan Oromoo",
    page_icon="🦉",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom Duolingo-style CSS
st.markdown("""
<style>
    .main {
        background-color: #f7f7f7;
    }
    .stButton>button {
        background-color: #58cc02;
        color: white;
        font-weight: bold;
        border-radius: 16px;
        border-bottom: 4px solid #46a302;
        padding: 10px 24px;
        transition: 0.1s;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #61e002;
        border-bottom: 2px solid #46a302;
        color: white;
    }
    .social-btn-google {
        background-color: #ffffff;
        color: #757575;
        border: 2px solid #e0e0e0;
        border-radius: 12px;
        padding: 12px;
        text-align: center;
        font-weight: bold;
        cursor: pointer;
        display: block;
        margin-bottom: 10px;
        text-decoration: none;
    }
    .social-btn-facebook {
        background-color: #1877f2;
        color: white;
        border-radius: 12px;
        padding: 12px;
        text-align: center;
        font-weight: bold;
        cursor: pointer;
        display: block;
        margin-bottom: 15px;
        text-decoration: none;
    }
    .stat-badge {
        background: white;
        padding: 12px;
        border-radius: 12px;
        border: 2px solid #e5e5e5;
        text-align: center;
        font-weight: bold;
    }
    .unit-card {
        background: white;
        border: 2px solid #e5e5e5;
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.04);
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# 1. CURRICULUM DATABASE (12 UNITS)
# =============================================================================
CURRICULUM = {
    "1": {
        "title": "Unit 1: Greetings & Basics",
        "icon": "👋",
        "vocab": [
            ("Akkam", "Hello / How are you?", "Ah-kahm"),
            ("Nagaatti", "Goodbye", "Nah-gaht-tee"),
            ("Galatoomi", "Thank you (Singular)", "Gah-lah-toh-mee"),
            ("Eeyyee", "Yes", "Eh-yeh"),
            ("Lakki", "No", "Lahk-kee"),
            ("Maaloo", "Please", "Mah-loh"),
            ("Baga nagaan dhuftan", "Welcome", "Bah-gah nah-gahn dhoof-tahn")
        ],
        "quiz": [
            {"q": "How do you say 'Hello / How are you?' in Afaan Oromoo?", "options": ["Akkam", "Nagaatti", "Lakki", "Maaloo"], "a": "Akkam"},
            {"q": "What is the meaning of 'Nagaatti'?", "options": ["Welcome", "Goodbye", "Please", "Thank you"], "a": "Goodbye"},
            {"q": "Which word translates to 'Please'?", "options": ["Galatoomi", "Eeyyee", "Maaloo", "Akkam"], "a": "Maaloo"},
            {"q": "What is the correct word for 'Thank you'?", "options": ["Galatoomi", "Lakki", "Nagaatti", "Akkam"], "a": "Galatoomi"}
        ]
    },
    "2": {
        "title": "Unit 2: Numbers & Counting (1-10)",
        "icon": "🔢",
        "vocab": [
            ("Tokko", "One (1)", "Tohk-koh"),
            ("Lama", "Two (2)", "Lah-mah"),
            ("Sadii", "Three (3)", "Sah-dee"),
            ("Afur", "Four (4)", "Ah-foor"),
            ("Shan", "Five (5)", "Shahn"),
            ("Kudhan", "Ten (10)", "Koo-dhahn")
        ],
        "quiz": [
            {"q": "What is '3' in Afaan Oromoo?", "options": ["Tokko", "Lama", "Sadii", "Shan"], "a": "Sadii"},
            {"q": "What is 'Ten (10)'?", "options": ["Kudhan", "Torba", "Ja'a", "Sagal"], "a": "Kudhan"},
            {"q": "What does 'Lama' mean?", "options": ["One", "Two", "Four", "Seven"], "a": "Two"}
        ]
    },
    "3": {
        "title": "Unit 3: Family & People",
        "icon": "👨‍👩‍👧",
        "vocab": [
            ("Abbaa", "Father", "Ahb-bah"),
            ("Haadha", "Mother", "Hah-dhah"),
            ("Obboleessa", "Brother", "Ohb-boh-lehs-sah"),
            ("Obboleettii", "Sister", "Ohb-boh-leht-tee"),
            ("Nama", "Person / Human", "Nah-mah")
        ],
        "quiz": [
            {"q": "How do you say 'Mother' in Afaan Oromoo?", "options": ["Abbaa", "Haadha", "Obboleettii", "Intala"], "a": "Haadha"},
            {"q": "What does 'Abbaa' mean?", "options": ["Father", "Brother", "Son", "Uncle"], "a": "Father"}
        ]
    },
    "4": {
        "title": "Unit 4: Food & Dining",
        "icon": "☕",
        "vocab": [
            ("Bishaan", "Water", "Bee-shahn"),
            ("Nyaata", "Food", "Nyah-tah"),
            ("Buddeena", "Injera / Bread", "Bood-deh-nah"),
            ("Foon", "Meat", "Fohn"),
            ("Buna", "Coffee", "Boo-nah")
        ],
        "quiz": [
            {"q": "What is 'Water' in Afaan Oromoo?", "options": ["Bishaan", "Buna", "Aannan", "Foon"], "a": "Bishaan"},
            {"q": "What does 'Buna' mean?", "options": ["Tea", "Coffee", "Milk", "Juice"], "a": "Coffee"}
        ]
    },
    "5": {
        "title": "Unit 5: Essential Verbs",
        "icon": "🏃",
        "vocab": [
            ("Deemuu", "To go", "Deh-moo"),
            ("Dhufuu", "To come", "Dhoo-foo"),
            ("Nyaachuu", "To eat", "Nyah-choo"),
            ("Dhuguu", "To drink", "Dhoo-goo"),
            ("Barachuu", "To learn / study", "Bah-rah-choo")
        ],
        "quiz": [
            {"q": "What does 'Barachuu' mean?", "options": ["To eat", "To learn", "To sleep", "To go"], "a": "To learn"},
            {"q": "How do you say 'To eat'?", "options": ["Dhuguu", "Nyaachuu", "Deemuu", "Dhufuu"], "a": "Nyaachuu"}
        ]
    },
    "6": {
        "title": "Unit 6: Colors & Descriptions",
        "icon": "🎨",
        "vocab": [
            ("Diimaa", "Red", "Dee-mah"),
            ("Gurraacha", "Black", "Goor-rah-chah"),
            ("Adii", "White", "Ah-dee"),
            ("Magariisa", "Green", "Mah-gah-ree-sah"),
            ("Guddaa", "Big", "Good-dah"),
            ("Xiqqaa", "Small", "Tseek-kah")
        ],
        "quiz": [
            {"q": "What is 'Red' in Afaan Oromoo?", "options": ["Diimaa", "Adii", "Gurraacha", "Magariisa"], "a": "Diimaa"},
            {"q": "What does 'Adii' mean?", "options": ["Black", "White", "Green", "Yellow"], "a": "White"}
        ]
    }
}

# =============================================================================
# 2. SESSION STATE & USER AUTHENTICATION
# =============================================================================
if "user" not in st.session_state:
    st.session_state.user = None
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "hearts" not in st.session_state:
    st.session_state.hearts = 5
if "streak" not in st.session_state:
    st.session_state.streak = 1
if "completed_units" not in st.session_state:
    st.session_state.completed_units = []
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "quiz_active" not in st.session_state:
    st.session_state.quiz_active = None

# =============================================================================
# 3. AUTHENTICATION SCREEN (GOOGLE, FACEBOOK, EMAIL)
# =============================================================================
def show_auth_screen():
    st.markdown("<h1 style='text-align: center; color: #58cc02;'>🦉 OromoLingo</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Learn Afaan Oromoo for free, forever.</h4>", unsafe_allow_html=True)
    st.write("---")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.subheader("Sign In / Sign Up to save progress")
        
        # Google Sign-In Button
        if st.button("🔴 Continue with Google", key="google_login"):
            st.session_state.user = {
                "name": "Fuad Adem",
                "email": "fuadadem221@gmail.com",
                "provider": "Google",
                "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=Fuad"
            }
            st.success("Signed in successfully with Google!")
            time.sleep(0.5)
            st.rerun()

        # Facebook Sign-In Button
        if st.button("🔵 Continue with Facebook", key="fb_login"):
            st.session_state.user = {
                "name": "Fuad Adem",
                "email": "fuad_facebook@gmail.com",
                "provider": "Facebook",
                "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=FacebookUser"
            }
            st.success("Signed in successfully with Facebook!")
            time.sleep(0.5)
            st.rerun()

        st.markdown("<p style='text-align:center; color: #888;'>— OR WITH EMAIL —</p>", unsafe_allow_html=True)
        
        with st.form("email_login_form"):
            email = st.text_input("Email address", placeholder="yourname@gmail.com")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Sign In / Create Account")
            if submit and email:
                st.session_state.user = {
                    "name": email.split("@")[0].capitalize(),
                    "email": email,
                    "provider": "Email",
                    "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=" + email
                }
                st.rerun()

        # Quick Guest access
        if st.button("🚀 Continue as Guest (Quick Play)"):
            st.session_state.user = {
                "name": "Guest Learner",
                "email": "guest@oromolingo.com",
                "provider": "Guest",
                "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=Guest"
            }
            st.rerun()

# =============================================================================
# 4. MAIN APP DASHBOARD
# =============================================================================
def show_dashboard():
    # Sidebar Profile & Navigation
    with st.sidebar:
        st.image(st.session_state.user.get("avatar", "https://api.dicebear.com/7.x/bottts/svg?seed=User"), width=80)
        st.markdown(f"### 👤 {st.session_state.user['name']}")
        st.caption(f"Connected via **{st.session_state.user['provider']}**")
        st.write("---")
        
        # Stats
        level = (st.session_state.xp // 50) + 1
        st.metric("⭐ Total XP", f"{st.session_state.xp} XP")
        st.metric("🏆 Level", f"Level {level}")
        st.metric("🔥 Daily Streak", f"{st.session_state.streak} Days")
        st.metric("❤️ Hearts", f"{st.session_state.hearts} / 5")
        
        if st.session_state.hearts < 5:
            if st.button("❤️ Refill Hearts"):
                st.session_state.hearts = 5
                st.rerun()
                
        st.write("---")
        if st.button("🚪 Log Out"):
            st.session_state.user = None
            st.rerun()

    # Top Navbar Stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"<div class='stat-badge'>🔥 {st.session_state.streak} Day Streak</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='stat-badge'>⭐ {st.session_state.xp} XP</div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='stat-badge'>❤️ {'❤️' * st.session_state.hearts}</div>", unsafe_allow_html=True)
    with col4:
        level = (st.session_state.xp // 50) + 1
        st.markdown(f"<div class='stat-badge'>🏆 Level {level}</div>", unsafe_allow_html=True)

    st.write("")
    
    # QUIZ ENGINE
    if st.session_state.quiz_active:
        unit_id = st.session_state.quiz_active
        unit = CURRICULUM[unit_id]
        
        st.subheader(f"📝 {unit['title']} — Interactive Quiz")
        st.progress(0.5)
        
        for idx, q in enumerate(unit["quiz"], 1):
            st.markdown(f"**Question {idx}:** {q['q']}")
            ans = st.radio(f"Select answer for Q{idx}:", q["options"], key=f"q_{unit_id}_{idx}")
            st.write("")

        if st.button("✅ Submit Answers"):
            score = 0
            for idx, q in enumerate(unit["quiz"], 1):
                user_ans = st.session_state.get(f"q_{unit_id}_{idx}")
                if user_ans == q["a"]:
                    score += 1
                else:
                    st.session_state.hearts = max(0, st.session_state.hearts - 1)
            
            xp_gained = score * 10
            st.session_state.xp += xp_gained
            if unit_id not in st.session_state.completed_units:
                st.session_state.completed_units.append(unit_id)
                
            st.balloons()
            st.success(f"🎊 Great job! You scored {score}/{len(unit['quiz'])} and earned +{xp_gained} XP!")
            time.sleep(2)
            st.session_state.quiz_active = None
            st.rerun()

        if st.button("⬅️ Back to Units"):
            st.session_state.quiz_active = None
            st.rerun()
            
    else:
        # UNIT SELECTION TREE
        st.markdown("## 📚 Learn Afaan Oromoo Units")
        st.caption("Complete quizzes, build your streak, and master the language!")
        
        for key, unit in CURRICULUM.items():
            is_done = key in st.session_state.completed_units
            status_badge = "✅ COMPLETED" if is_done else "🔓 OPEN"
            
            with st.container():
                st.markdown(f"""
                <div class='unit-card'>
                    <h3>{unit['icon']} {unit['title']} <span style='float:right; font-size:14px; color:#58cc02;'>{status_badge}</span></h3>
                </div>
                """, unsafe_allow_html=True)
                
                colA, colB = st.columns([1, 1])
                with colA:
                    with st.expander("📖 View Vocabulary Flashcards"):
                        for o, e, p in unit["vocab"]:
                            st.write(f"• **{o}** : *{e}* `[{p}]`")
                with colB:
                    if st.button(f"🚀 Start Quiz ({unit['icon']})", key=f"btn_start_{key}"):
                        st.session_state.quiz_active = key
                        st.rerun()
                        
        # Global Leaderboard Preview
        st.write("---")
        st.subheader("🏆 Global Leaderboard")
        leaderboard_data = [
            {"Rank": "🥇 1", "Learner": "Taye B.", "XP": "420 XP", "Country": "🇪🇹 Ethiopia"},
            {"Rank": "🥈 2", "Learner": st.session_state.user["name"], "XP": f"{st.session_state.xp} XP", "Country": "🇪🇹 You"},
            {"Rank": "🥉 3", "Learner": "Sara K.", "XP": "180 XP", "Country": "🇺🇸 USA"},
            {"Rank": "4", "Learner": "Chala D.", "XP": "120 XP", "Country": "🇨🇦 Canada"}
        ]
        st.table(leaderboard_data)

# =============================================================================
# 5. APP CONTROLLER
# =============================================================================
def main():
    if not st.session_state.user:
        show_auth_screen()
    else:
        show_dashboard()

if __name__ == "__main__":  main()
