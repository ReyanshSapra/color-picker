import streamlit as st
from PIL import ImageColor

st.title("Color Picker")

selected_color = st.color_picker("Click the box below to select", value="#FFFFFF")

st.write("---")

if selected_color:
    try:
        color_name = ImageColor.getcolor(selected_color, "RGB")
        st.subheader(f"You selected:")
        st.markdown(
            f"<div style='background-color: {selected_color}; padding: 20px; border-radius: 5px;'>"
            f"</div>",
            unsafe_allow_html=True,
        )
        st.write(f"**Hex Code:** `{selected_color}`")

    except ValueError:
        st.error("Invalid color format.")
