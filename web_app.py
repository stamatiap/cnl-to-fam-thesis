from pathlib import Path
import streamlit as st
import streamlit.components.v1 as comp
from src.monitoring import setup_logging
from src.run_pipeline import run_pipeline
import uuid
import json

st.set_page_config(layout="wide")

if "session_id" not in st.session_state:
    st.session_state["session_id"] = uuid.uuid4().hex[:8]

# setup logging once per session so every translation, Petri-net build,
# and visualization is written to one log
if "logging_configured" not in st.session_state:
    setup_logging()
    st.session_state["logging_configured"] = True


col1, col2 = st.columns([3, 2])


col1.subheader("Let's model MITRE ATT&CK Techniques!")

EXAMPLE_NAME = """Ex. Content Injection"""
technique_title = col1.text_input("Which Technique are you modeling?", placeholder=EXAMPLE_NAME)
    
file_name = f"web_app_{st.session_state['session_id']}_{technique_title.replace(' ', '_')}"

SKELETON = """Tactic: <ID> <Name>
Technique: <ID> <Name>

Background
Given <asset_type> as <name>

Event <n>
Given <the state before>
When <actor> <verb> <object>
Then <the state after>

Completion
Event <n>"""

description_text = col1.text_area("Describe the Technique using the CNL:", height="content", placeholder= SKELETON)

with col2:
    show_guide = st.toggle("📖 Show CNL Guide", value=False)

    if show_guide:
        st.subheader("CNL Syntax Guide")

        st.markdown(
            """
            <style>
            [data-testid="stMarkdownContainer"] p code,
            [data-testid="stMarkdownContainer"] li code {
                color: #1f77b4;
                background-color: rgba(31, 119, 180, 0.10);
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("A technique description is made of four blocks: `Header`, `Background`, `Event`, `Completion`.")

        BLOCKS = {
            "Header": {
                "note": "Declares the Tactic and Technique being modeled.",
                "code": 'Tactic: <ID> <Name>\n'
                        'Technique: <ID> <Name>',
                "examples":[ 'Tactic: TA0006 Credential_Access\n'
                        'Technique: T1003.001 OS_Credential_Dumping_LSASS_Memory',
                    'Tactics: TA0112 Defense_Impairment, TA0003 Persistence, TA0006 Credential_Access \n'
                        'Technique: T1556 Modify Authentication_Process'
                        ],
                "notes": [
                        "The keyword `Tactics` can be used to declare multiple Tactics.",
                        "Multiple tactics can be joined with commas."
                    ],
            },
            "Background": {
                "note": "Declares all assets and their properties, once, up front.",
                "code": 'Background\n'
                        'Given <asset_type> as <name> (with <property_type> = "<property_value>")?',
                "examples": ['Background\n'
                            'Given process as abnormal_process\n'
                            'And process as lsass_exe with command_line = "lsass.exe", signed = "true"\n'
                            'And handle as lsass_handle with hexadecimal_number = "0x1F0FFF", target = "lsass_exe"\n'
                            'And file as lsass_dump\n'
                            'And registry as registry_keys',
                            'Background\n'
                            'Given process as Browser\n'
                            'And registry as R'],
                "notes": [
                        "Multiple assets can be joined with `And`.",
                        "Multiple properties can be joined with commas after the keyword `with`.",
                    ],
            },
            "Event": {
                "note": "One attack step: preconditions → action → postconditions. "
                        "Repeat for each step.",
                "code": 'Event <n>\n'
                        'Given <subject_asset> <state_verb> ((in|to|from|by) <asset>)*\n'
                        'When <actor_asset> <verb> <object_asset> ((in|to|from|by) <asset>)*\n'
                        'Then <subject_asset> <state_verb> ((in|to|from|by) <asset>)*\n'
                        '(Repeated <x> times (within <t> <time_unit>)?)?\n'
                        '((During|Outside) <time_period>)?\n',
                "examples": ['Event 1\n'
                            'Given abnormal_process is activated And lsass_exe is activated\n'
                            'When abnormal_process requests lsass_handle\n'
                            'Then lsass_handle acquired by abnormal_process\n',
                            'Event 1\n'
                            'Given AuthenticationService is awaiting_input\n'
                            'When AuthenticationService receives IncorrectCredentials to TargetAccount\n'
                            'Then IncorrectCredentials is rejected\n'
                            'Repeated 5 times within 1 sec\n',
                            'Event 5\n'
                            'Given unusual_privileged_process is active in domain_controller\n'
                            'When unusual_privileged_process loads authentication_DLL\n'
                            'Then authentication_DLL is active\n'
                            'Outside business_hours'
                            ],
                "notes": [
                        "Multiple `Given` preconditions can be joined with `And`, `Or`, or `Xor` "
                        "(only one in each clause).",
                        "Multiple `Then` postconditions can be joined with `And` only.",
                        "The `When` action takes one verb and one object; modifiers "
                        "(`in`/`to`/`from`/`by`) are optional and repeatable.",
                    ],
            },
            "Completion": {
                "note": "Declares which event(s) mark the end of the Technique.",
                "code": 'Completion\n'
                        'Event <n>',
                "examples": [
                    'Completion\n'
                    'Event 4',
                    'Completion\n'
                    'Event 2 Xor Event 3\n'],
                "notes": [
                        "Multiple events can be joined with `And`, `Or`, or `Xor`."
                    ],
            },
        }

        block = st.selectbox("Which block do you need help with?", list(BLOCKS.keys()),
                            index=None,
                            placeholder="Pick a block…",)

        if block:
            data = BLOCKS[block]

            st.caption(data["note"])

            st.markdown("**Syntax**")
            st.code(data["code"], language=None)

            if data.get("notes"):
                for n in data["notes"]:
                    st.markdown(f"- {n}")

            if "examples" in data.keys():
                st.markdown("**Examples**")
                for ex in data["examples"]:
                    st.code(ex, language=None)

col2.subheader("Example CNL Descriptions")
with col2.expander("OS Credential Dumping: LSASS Memory"):
    description = Path("data/example_descriptions/lsass_memory.txt").read_text(encoding="utf-8")
    st.code(description, language=None)

with col2.expander("Brute Force: Password Guessing"):
    description = Path("data/example_descriptions/password_guessing.txt").read_text(encoding="utf-8")
    st.code(description, language=None)

with col2.expander("Content Injection"):
    description = Path("data/example_descriptions/content_injection.txt").read_text(encoding="utf-8")
    st.code(description, language=None)

with col2.expander("Scheduled Task/Job: At"):
    description = Path("data/example_descriptions/scheduled_task_job_at.txt").read_text(encoding="utf-8")
    st.code(description, language=None)


if description_text:
    print(technique_title)
    if technique_title != '':
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
            with open(str(svg_path)) as f:
                svg_code = f.read()

            import re

            # --- prep the SVG so it fills the container ---
            # ensure there's a viewBox (needed for correct fitting)
            if "viewBox" not in svg_code:
                w = re.search(r'width="([\d.]+)', svg_code)
                h = re.search(r'height="([\d.]+)', svg_code)
                if w and h:
                    svg_code = svg_code.replace(
                        "<svg", f'<svg viewBox="0 0 {w.group(1)} {h.group(1)}"', 1
                    )

            # strip Graphviz's fixed width/height so it can scale to the wrapper
            svg_code = re.sub(r'(<svg[^>]*?)\s+width="[^"]*"', r'\1', svg_code, count=1)
            svg_code = re.sub(r'(<svg[^>]*?)\s+height="[^"]*"', r'\1', svg_code, count=1)
            svg_code = svg_code.replace("<svg", '<svg style="width:100%; height:100%;"', 1)

            html_code = f"""
            <div id="vz-container"
            style="width:100%; height:200px; border:1px solid #ddd; overflow:hidden;
                    background:#fff; position:relative; cursor:grab;">
            <div id="vz-inner" style="transform-origin:0 0; width:100%; height:100%;">
                {svg_code}
            </div>
            <div id="vz-controls"
                style="position:absolute; top:8px; right:8px; display:flex; gap:4px;">
                <button id="vz-in"    style="width:30px; height:30px; font-size:16px; cursor:pointer;">+</button>
                <button id="vz-out"   style="width:30px; height:30px; font-size:16px; cursor:pointer;">&minus;</button>
                <button id="vz-reset" style="width:30px; height:30px; font-size:14px; cursor:pointer;">&#9634;</button>
            </div>
            </div>
            <script>
            (function() {{
            var container = document.getElementById('vz-container');
            var inner = document.getElementById('vz-inner');
            var scale = 1, tx = 0, ty = 0;
            var dragging = false, sx = 0, sy = 0;

            function apply() {{
                inner.style.transform = 'translate(' + tx + 'px,' + ty + 'px) scale(' + scale + ')';
            }}

            // zoom toward the cursor
            container.addEventListener('wheel', function(e) {{
                e.preventDefault();
                var rect = container.getBoundingClientRect();
                var mx = e.clientX - rect.left, my = e.clientY - rect.top;
                var f = e.deltaY < 0 ? 1.1 : 1/1.1;
                tx = mx - (mx - tx) * f;
                ty = my - (my - ty) * f;
                scale *= f;
                apply();
            }}, {{ passive: false }});

            // drag to pan
            container.addEventListener('mousedown', function(e) {{
                dragging = true; sx = e.clientX - tx; sy = e.clientY - ty;
                container.style.cursor = 'grabbing';
            }});
            window.addEventListener('mousemove', function(e) {{
                if (!dragging) return;
                tx = e.clientX - sx; ty = e.clientY - sy;
                apply();
            }});
            window.addEventListener('mouseup', function() {{
                dragging = false; container.style.cursor = 'grab';
            }});

            // don't start a drag when clicking the buttons
            document.getElementById('vz-controls')
                    .addEventListener('mousedown', function(e) {{ e.stopPropagation(); }});
            document.getElementById('vz-in').onclick    = function() {{ scale *= 1.2; apply(); }};
            document.getElementById('vz-out').onclick   = function() {{ scale /= 1.2; apply(); }};
            document.getElementById('vz-reset').onclick = function() {{ scale = 1; tx = 0; ty = 0; apply(); }};

            apply();
            }})();
            </script>
            """

            with col1:
                comp.html(html_code, height=210)
                st.markdown(
                    f"<p style='text-align:center; color:#808495; font-size:14px;'>Petri net for {technique_title}</p>",
                    unsafe_allow_html=True,
                )


            has_json = result.technique_model_path is not None
            raw = Path(result.technique_model_path).read_text(encoding="utf-8") if has_json else None

            has_tree = result.parse_tree_path is not None
            tree_text = Path(result.parse_tree_path).read_text(encoding="utf-8") if has_tree else None

            left, center, right = col1.columns(3)
            with left:
                st.download_button(
                    "Save Petri net",
                    data=svg_path.read_bytes(),
                    file_name=f"{file_name}_petri_net.svg",
                    mime="image/svg+xml",
                    icon=":material/download:",
                    key="svg_dl",
                    width="stretch"
                )

            with center:
                if has_tree:
                    st.download_button(
                        "Save Parse Tree",
                        data=tree_text,
                        file_name=f"{file_name}_parse_tree.txt",
                        mime="text/plain",
                        icon=":material/download:",
                        key="parse_tree_dl",
                        width="stretch"
                    )

            with right:
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
                with col1.expander("View Technique Model"):
                    st.json(json.loads(raw))
            if has_tree:
                with col1.expander("View Parse Tree"):
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
    else:
        st.error("Please, provide a name for the Technique.")
