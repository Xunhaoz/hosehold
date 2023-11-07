import pandas as pd


class DataXunhaoz001:
    def __init__(self):
        self._df = pd.read_csv('../data/raw/all.csv')
        self._data_selection()

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

        self._df = self._df.drop(columns=['IMR', 'PERSON'])

    def get_data_label(self):
        return self._df.drop(columns=['ITM40']), self._df[['ITM40']]
