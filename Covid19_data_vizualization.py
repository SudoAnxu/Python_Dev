import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from Excel
file_path = r"C:\Users\Piya\Downloads\covid_19.xlsx"
df = pd.read_excel(file_path, sheet_name='in')

# Clean column names
df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('/', '_')

# Convert numeric columns to numbers, fill NaNs with 0
for col in ['Confirmed', 'Deaths', 'Recovered', 'Active']:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

# ========== 1. Top-N Country Bar Charts ==========
def plot_top_countries(metric='Confirmed', n=20):
    top = df.sort_values(metric, ascending=False).head(n)
    plt.figure(figsize=(14, 8))
    sns.barplot(
        x=metric, 
        y='Country_Region', 
        data=top, 
        palette='Blues_r',
        hue='Country_Region',  # Added to resolve deprecation
        legend=False
    )
    plt.title(f'Top {n} Countries by {metric}')
    plt.xlabel(metric)
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()

plot_top_countries('Confirmed', 20)

# ========== 2. Pie Chart: Global Distribution ==========
def plot_global_pie():
    totals = df[['Confirmed', 'Deaths', 'Recovered', 'Active']].sum()
    plt.figure(figsize=(8, 8))
    plt.pie(
        totals, 
        labels=totals.index, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=sns.color_palette('pastel')
    )
    plt.title('Global COVID-19 Distribution')
    plt.axis('equal')
    plt.show()

plot_global_pie()

# ========== 3. Country-Specific Analysis ==========
def plot_country_bars(country):
    row = df[df['Country_Region'] == country]
    if row.empty:
        print(f"No data for {country}")
        return
    
    # Create DataFrame for plotting
    categories = ['Confirmed', 'Deaths', 'Recovered', 'Active']
    values = row[categories].values.flatten()
    plot_df = pd.DataFrame({
        'Category': categories,
        'Value': values
    })
    
    plt.figure(figsize=(7, 5))
    sns.barplot(
        x='Category',
        y='Value',
        data=plot_df,
        hue='Category',  # Resolves deprecation warning
        palette='Set2',
        legend=False
    )
    plt.title(f'COVID-19 Status in {country}')
    plt.ylabel('Number of Cases')
    plt.show()

plot_country_bars('India')

# ========== 4. Rate Analysis ==========
def plot_rates():
    df['Death_Rate'] = (df['Deaths'] / df['Confirmed']).fillna(0) * 100
    df['Recovery_Rate'] = (df['Recovered'] / df['Confirmed']).fillna(0) * 100
    top = df.sort_values('Confirmed', ascending=False).head(20)
    
    plt.figure(figsize=(14, 8))
    sns.barplot(
        x='Death_Rate',
        y='Country_Region',
        data=top,
        color='red',
        label='Death Rate'
    )
    sns.barplot(
        x='Recovery_Rate',
        y='Country_Region',
        data=top,
        color='green',
        alpha=0.5,
        label='Recovery Rate'
    )
    plt.xlabel('Rate (%)')
    plt.title('Death and Recovery Rates in Top 20 Countries')
    plt.legend()
    plt.tight_layout()
    plt.show()

plot_rates()
