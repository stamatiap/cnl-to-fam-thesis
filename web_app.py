from pathlib import Path
import streamlit as st
from src.monitoring import setup_logging
from src.run_pipeline import run_pipeline

# setup logging once per session so every translation, Petri-net build,
# and visualization is written to one log
if "logging_configured" not in st.session_state:
    setup_logging()
    st.session_state["logging_configured"] = True

st.write("Let's get to modeling!")

technique_title = st.text_input("Which technique are you modeling?")
if technique_title:
    file_name = "web_app_" + technique_title.replace(" ", "_")

    description_text = st.text_area("Please write a MITRE ATT&CK technique in CNL:", height="content")

    if description_text:
        # save the description so the translator (which reads from a file) can parse it.
        input_path = Path("data/web_app_descriptions") / f"{file_name}.txt"
        input_path.parent.mkdir(parents=True, exist_ok=True)
        input_path.write_text(description_text, encoding="utf-8")

        result = run_pipeline(
            input_path,
            validate=False,
            build_domain=False,
            petri_net_dir=Path("data/web_app_pn_models"),
            parsed_prefix="",
        )

        if result.ok and result.cnl_svg_path is not None:
            print(result.cnl_svg_path)
            st.image(str(result.cnl_svg_path), caption=f"Petri Net for {technique_title}")
        elif result.grammar_errors:
            st.error("Your description couldn't be parsed. Fix the following grammar issue(s):")
            for err in result.grammar_errors:
                st.markdown(f"- **Line {err['line']}, column {err['column']}** — {err['message']}")
        elif result.translation_errors:
            st.error("Your description was parsed, but the translation was not successful.")
            for msg in result.translation_errors:
                st.markdown(f"- {msg}")
        else:
            st.error("Petri net could not be built. See the logs for details.")
