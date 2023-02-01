import pandas as pd

import re

df = pd.read_excel('tel .xlsx')

# df


df["tel_inc"] = df['tel_inc'].replace({'"': ''}, regex=True)

df["tel_hafiza"] = df["tel_hafiza"].replace({'GB': ''}, regex=True)

df["tel_review"] = df["tel_review"].replace({'reviews': ''}, regex=True)


def convert_to_mb(x):
    value = int(re.search(r'(\d+)', x).group(1))
    if 'GB' in x:
        return value * 1024
    else:
        return value


df["tel_ram"] = df['tel_ram'].apply(convert_to_mb)

df["tel_review"] = df['tel_review'].astype(int)


# df.dtypes

def replacing_rate(x):
    if x <= 8:
        return 'Bad'
    elif x > 8:
        return 'Good'


df.tel_rate.apply(replacing_rate).value_counts()

df.tel_rate = df.tel_rate.apply(replacing_rate)


def replacing_review(x):
    if x <= 20:
        return 'Low'
    elif x > 20:
        return 'High'

df.tel_review = df.tel_review.apply(replacing_review)

#df

df.to_csv("tel_clean_data.csv", index=False, encoding="utf-8")
