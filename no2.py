import pandas as pd

def demographic_data_analyzer():
    df = pd.read_csv("adult.data.csv")
    
    race_count = df['race'].value_counts()
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)
    
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round(df[higher_education]['salary'].eq('>50K').mean() * 100, 1)
    lower_education_rich = round(df[~higher_education]['salary'].eq('>50K').mean() * 100, 1)
    
    min_work_hours = df['hours-per-week'].min()
    rich_percentage = round(df[df['hours-per-week'] == min_work_hours]['salary'].eq('>50K').mean() * 100, 1)
    
    country_earnings = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()
    highest_earning_country = country_earnings.idxmax()
    highest_earning_country_percentage = round(country_earnings.max() * 100, 1)
    
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()
    
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
