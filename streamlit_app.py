import streamlit as st
from calculator import cal


st.set_page_config(page_title="YGO Calculator")

rows = []


if "Row Num" not in st.session_state:
    st.session_state["Row Num"] = 0
    st.session_state["Row Ids"] = []

    st.session_state["Deck Size"] = 40
    st.session_state["Hand Size"] = 5


class Row:
    def __init__(self, amt, min, max):
        self.amt = amt
        self.min = min
        self.max = max


def define_row(row_id):
    col0, col1, col2, col3 = st.columns([0.25] * 4)
    with col0:
        st.text_input(
            "Name", f"Card_{row_id}", key=f"{row_id}_0", label_visibility="hidden"
        )
    with col1:
        amt = st.text_input("Amt", "0", key=f"{row_id}_1", label_visibility="hidden")
    with col2:
        min = st.text_input("Min", "0", key=f"{row_id}_2", label_visibility="hidden")
    with col3:
        max = st.text_input("Max", "0", key=f"{row_id}_3", label_visibility="hidden")

    rows.append(Row(int(amt), int(min), int(max)))


def append_rows():
    st.session_state["Row Ids"].append(f"{st.session_state['Row Num']}")
    st.session_state["Row Num"] += 1


def reduce_row():
    if len(st.session_state["Row Ids"]) > 1:
        st.session_state["Row Ids"].pop(-1)


st.header("Yu-Gi-Oh Deck Probability Calculator")

st.write("")

col1, col2 = st.columns(2)
with col1:
    st.session_state["Deck Size"] = int(st.text_input("Deck Size", "40"))
with col2:
    st.session_state["Hand Size"] = int(st.text_input("Hand Size", "5"))

st.write("")

col1, col2 = st.columns(2)
with col1:
    st.button("Add Row", on_click=append_rows)
with col2:
    st.button("Redue Row", on_click=reduce_row)

st.write("")
st.write("")

col0, col1, col2, col3 = st.columns([0.25] * 4)
with col0:
    st.subheader("Name")
with col1:
    st.subheader("Amt")
with col2:
    st.subheader("Min")
with col3:
    st.subheader("Max")

for row_id in st.session_state["Row Ids"]:
    define_row(row_id)

result = cal(rows)

st.write("")

st.header(f"{round(result * 100, 2)} %")
