import streamlit as st
import pandas as pd

# כותרת הדאשבורד
st.title("ron's dashboard")

# יצירת נתונים לדוגמה
data = {
    'מוצר': ['תפוח', 'בננה', 'אגס', 'תפוז'],
    'כמות': [50, 80, 30, 60],
    'מחיר ליחידה': [2.5, 1.8, 3.0, 2.2]
}
df = pd.DataFrame(data)

# הצגת הטבלה
st.subheader("טבלת מוצרים")
st.dataframe(df)

# הצגת גרף
st.subheader("סך הכל כמות לפי מוצר")
st.bar_chart(df.set_index('מוצר')['כמות'])

# הצגת מדד סכום כולל
st.metric("סך הכל הכנסה", f"{(df['כמות'] * df['מחיר ליחידה']).sum()} ₪")