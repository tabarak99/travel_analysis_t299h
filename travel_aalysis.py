# ============================================================
# ✈️ TRAVEL PLANNER - STATISTICAL ANALYSIS
# تحليل إحصائي لبيانات الرحلات
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1. إنشاء بيانات الرحلات (DataFrame)
# ------------------------------------------------------------
travel_data = {
    "Destination": ["Paris", "Baghdad", "Tokyo", "Istanbul", "Dubai", "Cairo"],
    "Country": ["France", "Iraq", "Japan", "Turkey", "UAE", "Egypt"],
    "Currency": ["Euro", "Iraqi Dinar", "Japanese Yen", "Turkish Lira", "Dirham", "Egyptian Pound"],
    "Language": ["French", "Arabic", "Japanese", "Turkish", "Arabic", "Arabic"],
    "Best_Time": ["April to June", "Nov to March", "March to May", 
                  "April to May", "Nov to March", "Oct to April"],
    "Attractions_Count": [3, 3, 3, 3, 3, 3],
    "Daily_Budget_Min": [150, 50, 120, 80, 200, 60],
    "Daily_Budget_Max": [250, 100, 200, 150, 350, 120]
}

df = pd.DataFrame(travel_data)

# ------------------------------------------------------------
# 2. عرض البيانات
# ------------------------------------------------------------
print("="*60)
print("✈️  TRAVEL PLANNER - STATISTICAL ANALYSIS")
print("="*60)
print("\n--- Travel Data ---")
print(df)

# ------------------------------------------------------------
# 3. الإحصاءات الوصفية
# ------------------------------------------------------------
print("\n--- Descriptive Statistics ---")
print(df[['Daily_Budget_Min', 'Daily_Budget_Max']].describe())

# ------------------------------------------------------------
# 4. حساب المتوسطات
# ------------------------------------------------------------
df['Average_Daily_Budget'] = (df['Daily_Budget_Min'] + df['Daily_Budget_Max']) / 2

print("\n--- Average Daily Budget per Destination ---")
print(df[['Destination', 'Average_Daily_Budget']].sort_values(
    by='Average_Daily_Budget', ascending=True
))

# ------------------------------------------------------------
# 5. حساب إجمالي التكلفة لرحلة 7 أيام
# ------------------------------------------------------------
df['Total_Cost_7_Days'] = df['Average_Daily_Budget'] * 7

print("\n--- Total Cost for 7 Days Trip ---")
print(df[['Destination', 'Total_Cost_7_Days']].sort_values(
    by='Total_Cost_7_Days', ascending=True
))

# ------------------------------------------------------------
# 6. ترتيب الوجهات حسب التكلفة (الأرخص أولاً)
# ------------------------------------------------------------
cheapest = df.sort_values(by='Average_Daily_Budget', ascending=True)
print("\n--- Cheapest Destinations ---")
print(cheapest[['Destination', 'Average_Daily_Budget']])

most_expensive = df.sort_values(by='Average_Daily_Budget', ascending=False)
print("\n--- Most Expensive Destinations ---")
print(most_expensive[['Destination', 'Average_Daily_Budget']])

# ------------------------------------------------------------
# 7. الرسم البياني: متوسط الميزانية اليومية
# ------------------------------------------------------------
plt.figure(figsize=(10, 6))
plt.bar(df['Destination'], df['Average_Daily_Budget'], color='skyblue', edgecolor='black')
plt.title('Average Daily Budget per Destination', fontsize=14)
plt.xlabel('Destination', fontsize=12)
plt.ylabel('Average Daily Budget ($)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 8. الرسم البياني: إجمالي التكلفة لرحلة 7 أيام
# ------------------------------------------------------------
plt.figure(figsize=(10, 6))
plt.bar(df['Destination'], df['Total_Cost_7_Days'], color='salmon', edgecolor='black')
plt.title('Total Cost for 7 Days Trip per Destination', fontsize=14)
plt.xlabel('Destination', fontsize=12)
plt.ylabel('Total Cost ($)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 9. الرسم البياني الدائري: نسبة التكلفة لكل وجهة
# ------------------------------------------------------------
plt.figure(figsize=(8, 8))
plt.pie(df['Total_Cost_7_Days'], labels=df['Destination'], autopct='%1.1f%%', 
        colors=plt.cm.Pastel1.colors, startangle=140)
plt.title('Percentage of Total Cost (7 Days Trip) by Destination', fontsize=14)
plt.show()

# ------------------------------------------------------------
# 10. تحليل حسب اللغة
# ------------------------------------------------------------
print("\n--- Destinations by Language ---")
language_groups = df.groupby('Language')['Destination'].count()
print(language_groups)

plt.figure(figsize=(8, 6))
language_groups.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Number of Destinations by Language', fontsize=14)
plt.xlabel('Language', fontsize=12)
plt.ylabel('Number of Destinations', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("✅ Analysis Completed Successfully!")
print("="*60)