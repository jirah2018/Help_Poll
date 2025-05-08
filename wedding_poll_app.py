import streamlit as st


# Page config
st.set_page_config(page_title="Wedding Help Poll", layout="centered")

# Background color
st.markdown("""
    <style>
    body {
        background-color: #ffe6f0;
    }
    .stApp {
        background-color: #ffe6f0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("## Needs Help to Decorate the Reception Area of the Wedding")
st.write("📅 Please choose the **day and time** you can come to help with decorations.")

# Display couple photo
st.image("coupleimages.jpg", caption="Soon to be Mr. & Mrs.", use_column_width=True)

# Background music
st.audio("love.mp3")

# Form
with st.form("poll_form"):
    name = st.text_input("Enter your name:")
    time_slot = st.radio("When can you help?", [
        "May 22 AM",
        "May 22 PM",
        "May 23 AM",
        "May 23 PM"
    ])
    submitted = st.form_submit_button("Submit")

# Store and group responses
if submitted and name:
    if "volunteers" not in st.session_state:
        st.session_state.volunteers = {
            "May 22 AM": [],
            "May 22 PM": [],
            "May 23 AM": [],
            "May 23 PM": []
        }
    st.session_state.volunteers[time_slot].append(name)
    st.success(f"Thank you, {name}! You selected **{time_slot}**.")

# Display results grouped by time
if "volunteers" in st.session_state:
    st.markdown("### 🙌 Volunteers by Date and Time")
    for slot in ["May 22 AM", "May 22 PM", "May 23 AM", "May 23 PM"]:
        st.markdown(f"#### {slot}")
        names = st.session_state.volunteers.get(slot, [])
        if names:
            for n in names:
                st.markdown(f"- {n}")
        else:
            st.markdown("_No one has signed up yet._")

# Bible verse & thanks
st.markdown("---")
st.markdown("> _Behold, how good and how pleasant it is for brethren to dwell together in unity._")
st.markdown("**Maraming Salamat Kapamilya, Kapuso at Kapatid!** 🙏💖")
