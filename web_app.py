import streamlit as st
from src.translation.translator import Translator
from src.petri_net.petri_net_builder import PetriNetBuilder

st.write("Let's get to modeling!")
# get all example
technique_title = st.text_input("Which technique are you modeling?")
if technique_title:
    file_path = f"streamlit_testing_{technique_title.replace(" " ,"_")}"

    description_text = st.text_area("Please write a MITRE ATT&CK technique in CNL:", height="content")

    if description_text:
        path = "data/example_descriptions/"+ file_path + ".txt"
        with open(path, "w+") as text_file:
            text_file.write(description_text)

            
        translator = Translator()
        model = translator.translate(path)
        petri_net_builder = PetriNetBuilder()
        petri_net_builder.visualize(*petri_net_builder.build(model), "testing_streamlit")

        st.image("testing_streamlit.png", caption=f"Petri Net for {" ".join(path.split('/')[-1][:-4].split("_")[2:])}")
