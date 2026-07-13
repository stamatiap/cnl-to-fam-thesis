from pathlib import Path
import streamlit as st
from src.monitoring import setup_logging
from src.run_pipeline import run_pipeline
import uuid
import json

if "session_id" not in st.session_state:
    st.session_state["session_id"] = uuid.uuid4().hex[:8]

# setup logging once per session so every translation, Petri-net build,
# and visualization is written to one log
if "logging_configured" not in st.session_state:
    setup_logging()
    st.session_state["logging_configured"] = True

st.write("Let's get to modeling!")

technique_title = st.text_input("Which technique are you modeling?")
if technique_title:
    
    file_name = f"web_app_{st.session_state['session_id']}_{technique_title.replace(' ', '_')}"

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
            svg_path = Path(result.cnl_svg_path)
            st.image(str(svg_path), caption=f"Petri Net for {technique_title}")

            has_json = result.technique_model_path is not None
            raw = Path(result.technique_model_path).read_text(encoding="utf-8") if has_json else None

            has_tree = result.parse_tree_path is not None
            tree_text = Path(result.parse_tree_path).read_text(encoding="utf-8") if has_tree else None

            col1, col2, col3 = st.columns(3)
            with col1:
                st.download_button(
                    "Save Petri net",
                    data=svg_path.read_bytes(),
                    file_name=f"{file_name}_petri_net.svg",
                    mime="image/svg+xml",
                    icon=":material/download:",
                    key="svg_dl",
                    width="stretch"
                )

            with col2:
                if has_tree:
                    st.download_button(
                        "Save Parse tree",
                        data=tree_text,
                        file_name=f"{file_name}_parse_tree.txt",
                        mime="text/plain",
                        icon=":material/download:",
                        key="parse_tree_dl",
                        width="stretch"
                    )

            with col3:
                if has_json:
                    st.download_button(
                        "Save Technique Model",
                        data=raw,
                        file_name=f"{file_name}_technique_model.json",
                        mime="application/json",
                        icon=":material/download:",
                        key="model_json_dl",
                        width="stretch"
                    )

            if has_json:
                with st.expander("View Technique Model"):
                    st.json(json.loads(raw))
            if has_tree:
                with st.expander("View Parse Tree"):
                    st.write(tree_text)

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
