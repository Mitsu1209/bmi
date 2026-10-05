import streamlit as st

st.title("BMI計算アプリ")

# input() の代わりに st.number_input() を使ってWebの入力枠を作る
height = st.number_input("身長をメートル(m)で入力してください", value=1.70)
weight = st.number_input("体重をキログラム(kg)で入力してください", value=60.0)

# 計算式は全く同じ！
if height > 0:  # 身長が0の時にエラーになるのを防ぐ安全対策
    bmi = weight / (height * height)
    
    # print() の代わりに st.write() を使ってWebに文字を出す
    st.write("あなたのBMIは：", bmi)
