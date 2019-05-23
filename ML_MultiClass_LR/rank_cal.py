import pandas

df = pandas.read_csv('fianl-val.csv', names=['in', 'ind', 'temp', 'score'])
df.drop(labels=['in','ind', 'score'], axis=1, inplace=True)

def assign_rank(row):
    # print(row)
    if row['temp'] >= 0.0 and row['temp'] <= 15.34:
        return '0'
    elif row['temp'] > 15.34 and row['temp'] <= 60.14:
        return '1'
    else:
        return '2'
df['rank'] = df.apply(assign_rank, axis=1)
print(df)
df.to_csv('category_data.csv', index=False)