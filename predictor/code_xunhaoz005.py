from dataloader.data_xunhaoz002 import DataXunhaoz002
import warnings

from sklearn.model_selection import cross_validate
from lightgbm import LGBMRegressor

warnings.filterwarnings('ignore')

dl = DataXunhaoz002()
lgbm = LGBMRegressor(n_jobs=-1, verbose=0)

train_data, train_label = dl.get_data_label()
res = cross_validate(
    lgbm, train_data, train_label, n_jobs=-1,
    cv=5, verbose=1, return_train_score=True, scoring='neg_mean_absolute_error'
)

test_score = -res['test_score'].mean()
train_score = -res['train_score'].mean()

print(f"{test_score= :.4f}, {train_score= :.4f}")
