import streamlit as st

# Page settings
st.set_page_config(
    page_title="AI Eco-Life Assistant",
    page_icon="🌱",
    layout="centered"
)

# Title
st.title("🌱 AI Eco-Life Assistant")
st.write("Your smart assistant for sustainable living.")

# Question input
question = st.text_input(
    "💬 Ask your eco-friendly question:",
    placeholder="Example: How can I save water?"
)

# Button
if st.button("🌿 Get Solution"):

    if question.strip():

        q = question.lower()

        st.subheader("🤖 Eco Assistant")

        # Water
        if "water" in q:
            st.write("""
            💧 **Ways to save water:**

            • Turn off the tap while brushing your teeth.  
            • Fix leaking taps and pipes.  
            • Take shorter showers.  
            • Reuse water for plants whenever possible.  
            • Use a bucket instead of a hose for cleaning.  

            🌱 Every drop counts!
            """)

        # Plastic
        elif "plastic" in q:
            st.write("""
            ♻️ **Ways to reduce plastic use:**

            • Carry a reusable water bottle.  
            • Avoid single-use plastic bags.  
            • Use reusable food containers.  
            • Avoid disposable cups and cutlery.  
            • Choose products with less packaging.  

            🌱 Small changes can make a big difference!
            """)

        # Electricity
        elif "electricity" in q or "energy" in q or "current" in q:
            st.write("""
            ⚡ **Ways to save electricity:**

            • Switch off lights when leaving a room.  
            • Unplug chargers when not in use.  
            • Use LED bulbs.  
            • Make use of natural sunlight during the day.  
            • Turn off fans and appliances when they are not needed.  

            🌱 Save energy, protect the planet!
            """)

        # Waste
        elif "waste" in q or "garbage" in q or "trash" in q:
            st.write("""
            🗑️ **Ways to reduce waste:**

            • Separate recyclable and non-recyclable waste.  
            • Reuse items whenever possible.  
            • Compost suitable food waste.  
            • Avoid buying unnecessary items.  
            • Donate usable clothes and items.  

            ♻️ Reduce, Reuse and Recycle!
            """)

        # Trees
        elif "tree" in q or "plant" in q:
            st.write("""
            🌳 **Ways to help trees and plants:**

            • Plant native trees and plants.  
            • Take care of existing trees.  
            • Avoid unnecessary paper waste.  
            • Use both sides of paper.  
            • Support local green spaces.  

            🌱 Let's make our surroundings greener!
            """)

        # Transport
        elif "transport" in q or "travel" in q or "vehicle" in q:
            st.write("""
            🚲 **Eco-friendly transportation tips:**

            • Walk for short distances.  
            • Use a bicycle when possible.  
            • Prefer public transportation.  
            • Share rides when practical.  
            • Avoid unnecessary vehicle trips.  

            🌍 Cleaner travel means cleaner air!
            """)

        # Food
        elif "food" in q:
            st.write("""
            🍎 **Eco-friendly food habits:**

            • Avoid wasting food.  
            • Buy only what you need.  
            • Prefer local and seasonal foods when possible.  
            • Store food properly to reduce spoilage.  
            • Compost suitable food scraps.  

            🌱 Eat wisely and reduce waste!
            """)

        # General eco question
        elif "eco" in q or "environment" in q or "green" in q:
            st.write("""
            🌍 **General eco-friendly tips:**

            • Reduce plastic usage.  
            • Save water and electricity.  
            • Reuse and recycle materials.  
            • Avoid wasting food.  
            • Walk, cycle or use public transport when possible.  
            • Plant and protect trees.  

            💚 Every small action helps our planet!
            """)

        # Unknown question
        else:
            st.write("""
            🌱 **Eco-friendly suggestion:**

            Try reducing waste, saving water and electricity,
            avoiding single-use plastic, reusing materials,
            and choosing environmentally friendly options.

            💚 Small sustainable habits can create a big difference!
            """)

    else:
        st.warning("⚠️ Please enter a question first.")