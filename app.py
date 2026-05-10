import streamlit as st

# --- SETUP ---
st.title("My Life Reset")

# Setup the save data (session state)
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "level" not in st.session_state:
    st.session_state.level = 1

# --- UI: THE STATS ---
st.header(f"Level {st.session_state.level}")
# This creates a progress bar that fills up to 100
st.progress(min(st.session_state.xp / 100.0, 1.0))
st.write(f"XP: {st.session_state.xp} / 100")

st.divider()

# --- UI: DAILY QUESTS ---
st.subheader("Daily Quests")
task1 = st.checkbox("Drink 2L Water (+10 XP)")
task2 = st.checkbox("Read 10 Pages (+20 XP)")
task3 = st.checkbox("Workout (+50 XP)")

# --- LOGIC: THE LEVEL UP SYSTEM ---
if st.button("Claim XP"):
    gained_xp = 0
    if task1: gained_xp += 10
    if task2: gained_xp += 20
    if task3: gained_xp += 50
    
    st.session_state.xp += gained_xp
    
    # Check if you leveled up!
    while st.session_state.xp >= 100:
        st.session_state.level += 1
        st.session_state.xp -= 100
        st.balloons() # Triggers a visual animation
        
    st.rerun()
