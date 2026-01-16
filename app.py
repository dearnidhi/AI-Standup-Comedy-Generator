import streamlit as st
from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents.joke_writer import joke_writer_node
from agents.roast_controller import roast_controller_node
from agents.delivery_agent import delivery_node

# ---------- STATE ----------
class ComedyState(TypedDict):
    name: str
    traits: str
    level: str
    jokes: str
    controlled_jokes: str
    final_script: str

# ---------- GRAPH ----------
graph = StateGraph(ComedyState)
graph.add_node("joke_writer", joke_writer_node)
graph.add_node("roast_controller", roast_controller_node)
graph.add_node("delivery", delivery_node)
graph.set_entry_point("joke_writer")
graph.add_edge("joke_writer", "roast_controller")
graph.add_edge("roast_controller", "delivery")
graph.add_edge("delivery", END)
comedy_app = graph.compile()

# ---------- STYLED UI ----------
st.set_page_config(
    page_title="🎤 Comedy Roast Generator",
    page_icon="🎭",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&family=Montserrat:wght@400;600&display=swap');

/* Whole page background */
.main {
    background: linear-gradient(135deg, #ffc0cb 0%, #87ceeb 100%); /* baby pink to sky blue */
    color: #000; /* default text black, readable */
}

/* Input and textarea fields */
.stTextInput input, .stTextArea textarea {
    background-color: rgba(0,0,0,0.5) !important; /* dark translucent so white text is readable */
    border: 2px solid #ff6b6b !important;
    border-radius: 10px !important;
    color: #fff !important; /* input text white */
    font-family: 'Montserrat', sans-serif;
    padding: 8px;
}

/* Selectbox */
.stSelectbox select {
    background-color: rgba(0,0,0,0.5) !important; /* match input style */
    border: 2px solid #4ecdc4 !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 6px;
}

/* Buttons */
.stButton button {
    background: linear-gradient(90deg, #ff6b6b 0%, #ff8e53 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 25px !important;
    padding: 12px 30px !important;
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    transition: all 0.3s ease !important;
    width: 100%;
}

.stButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(255, 107, 107, 0.4) !important;
}

/* Titles */
.title-text {
    font-family: 'Comic Neue', cursive;
    font-weight: 700;
    background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 10px;
}

.subtitle {
    font-family: 'Montserrat', sans-serif;
    text-align: center;
    color: #333; 
    margin-bottom: 30px;
}

/* Script output box */
.script-box {
    background: rgba(0,0,0,0.7); /* dark translucent box */
    color: #fff; /* text white */
    border-left: 4px solid #ff6b6b;
    border-radius: 8px;
    padding: 20px;
    margin-top: 20px;
    font-family: 'Courier New', monospace;
    line-height: 1.6;
    white-space: pre-wrap;
}

/* Steps indicator */
.step-indicator {
    display: flex;
    justify-content: space-between;
    margin: 30px 0;
    padding: 0 20px;
}

.step {
    text-align: center;
    flex: 1;
    color: #666;
    font-family: 'Montserrat', sans-serif;
}

.step.active {
    color: #ff6b6b;
    font-weight: 600;
}

.step-icon {
    font-size: 24px;
    margin-bottom: 5px;
}

.divider {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #ff6b6b, transparent);
    margin: 30px 0;
}
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<h1 class='title-text'>🎤 COMEDY ROAST GENERATOR</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>AI-powered roast comedy crafted by your virtual comedy team</p>", unsafe_allow_html=True)

# Step Indicator
st.markdown("""
<div class='step-indicator'>
    <div class='step active'>
        <div class='step-icon'>📝</div>
        <div>Input</div>
    </div>
    <div class='step">
        <div class='step-icon'>🤖</div>
        <div>Agents Working</div>
    </div>
    <div class='step'>
        <div class='step-icon'>🎭</div>
        <div>Roast Ready</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Input Section with better spacing
col1, col2 = st.columns(2)
with col1:
    name = st.text_input(
        "🎯 **TARGET NAME**",
        placeholder="Enter the name to roast...",
        help="Who's getting roasted today?"
    )

with col2:
    level = st.selectbox(
        "🔥 **ROAST INTENSITY**",
        ["light", "medium", "savage"],
        help="How spicy should the roast be?"
    )

traits = st.text_area(
    "🎭 **PERSONALITY TRAITS**",
    placeholder="Describe their quirks, habits, or funny traits...",
    height=100,
    help="What makes them uniquely roast-worthy?"
)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# Generate Button with better placement
if st.button("🎭 GENERATE ROAST"):
    if not name or not traits:
        st.warning("⚠️ Please fill in both the name and traits!")
    else:
        # Progress animation
        with st.spinner("🤖 Comedy agents are at work..."):
            progress_bar = st.progress(0)
            
            # Simulate progress for better UX
            for i in range(100):
                progress_bar.progress(i + 1)
            
            # Actual processing
            result = comedy_app.invoke({
                "name": name,
                "traits": traits,
                "level": level,
            })
        
        # Success message
        st.balloons()
        st.success("✅ Roast generated successfully!")
        
        # Display results in styled container
        st.markdown("<div class='script-box'>", unsafe_allow_html=True)
        st.markdown("### 🎤 **YOUR CUSTOM ROAST SCRIPT**")
        st.markdown("---")
        st.markdown(result["final_script"])
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Download button for the script
        st.download_button(
            label="📥 Download Script",
            data=result["final_script"],
            file_name=f"roast_{name.replace(' ', '_')}.txt",
            mime="text/plain"
        )

# Footer
st.markdown("<hr class='divider'>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: #666; font-size: 12px; margin-top: 30px;'>
    <p>🎭 Generated with AI • All roasts are in good fun • Made for comedy lovers</p>
</div>
""", unsafe_allow_html=True)