import pandas as pd
from sklearn.preprocessing import OneHotEncoder


class DataXunhaoz002:
    def __init__(self):
        self._df = pd.read_csv('../data/raw/all.csv')
        self._data_selection()
        self._data_one_hot()

    def _data_selection(self):
        self._df = self._df[self._df['AGE'] >= 20]
        self._df = self._df[self._df['AGE'] <= 90]
        self._df = self._df[(self._df['IND'] != 2) & (self._df['IND'] != 5)]
        self._df = self._df[(self._df['OCC'] != 62) & (self._df['OCC'] != 63)]
        self._df = self._df[
            (self._df['REL'] != 9) & (self._df['REL'] != 12) & (self._df['REL'] != 13) & (self._df['REL'] != 14) &
            (self._df['REL'] != 4) & (self._df['REL'] != 6) & (self._df['REL'] != 10)
            ]
        self._df = self._df[(self._df['WKCLASS'] != 4) & (self._df['WKCLASS'] != 7)]
        self._df = self._df[
            (self._df['WORKPLACE'] != 59) & (self._df['WORKPLACE'] != 60) & (self._df['WORKPLACE'] != 61) &
            (self._df['WORKPLACE'] != 97)
            ]

        self._df['MRG'] = self._df['MRG'].apply(lambda x: 97 if 94 <= x <= 96 else x)
        self._df['MRG'] = self._df['MRG'].apply(lambda x: x if 91 <= x <= 97 else 90)

        self._df = self._df.drop(columns=['IMR', 'PERSON', 'YEAR', 'ID'])
        self._df = self._df.reset_index(drop=True)

    def _data_one_hot(self):
        one_hot_encoder = OneHotEncoder()
        res = one_hot_encoder.fit_transform(self._df.drop(columns=['ITM40', 'AGE']))
        one_hot_df = pd.DataFrame(
            res.toarray(), index=self._df.index,
            columns=one_hot_encoder.get_feature_names_out(self._df.drop(columns=['ITM40', 'AGE']).columns)
        )
        self._df = pd.concat([one_hot_df, self._df[['AGE', 'ITM40']]], axis=1)

    def get_data_label(self):
        return self._df.drop(columns=['ITM40']), self._df[['ITM40']]

