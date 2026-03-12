import matplotlib.pyplot as plt

# נתונים לדוגמה לגרף
products = ['תפוח', 'בננה', 'אגס', 'תפוז']
quantities = [50, 80, 30, 60]

plt.bar(products, quantities, color='skyblue')
plt.title('כמות פירות')
plt.xlabel('מוצר')
plt.ylabel('כמות')
plt.tight_layout()
plt.show()