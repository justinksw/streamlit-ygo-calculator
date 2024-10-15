import itertools
from math import factorial as fac

import streamlit as st


def nCr(n, r):
    return fac(n) / (fac(r) * fac(n - r))


def cal(rows):

    ls = [list(range(row.min, row.max + 1)) for row in rows]

    combs = list(itertools.product(*ls))
    combs = [c for c in combs if sum(c) <= st.session_state["Hand Size"]]

    A = 0

    for comb in combs:

        B = 1
        amt_sum = 0
        hand_count = 0

        for i, v in enumerate(comb):

            hand_count += v
            amt_sum += rows[i].amt

            B *= nCr(rows[i].amt, v)

        B *= nCr(
            st.session_state["Deck Size"] - amt_sum,
            st.session_state["Hand Size"] - hand_count,
        )

        A += B

    prob = A / nCr(st.session_state["Deck Size"], st.session_state["Hand Size"])

    return prob
