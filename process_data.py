import pandas as pd

fake = pd.read_csv("fake.csv")
true = pd.read_csv("true.csv")


fake['label'] = 'fake'
true['label'] = 'true'

frames = [fake, true]
news_dataset = pd.concat(frames)
final_data = news_dataset.dropna()


final_data.drop(['title','subject','date'], axis=1, inplace=True)


final_data.to_csv("data_processed.csv")

