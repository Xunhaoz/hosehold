from dataloader.data_xunhaoz001 import DataXunhaoz001
import warnings

from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestRegressor

warnings.filterwarnings('ignore')

dl = DataXunhaoz001()
rf = RandomForestRegressor(n_jobs=-1)

train_data, train_label = dl.get_data_label()
res = cross_validate(
    rf, train_data, train_label,
    cv=5, verbose=1, return_train_score=True, scoring='neg_mean_absolute_error'
)

test_score = -res['test_score'].mean()
train_score = -res['train_score'].mean()

print(f"{test_score= :.4f}, {train_score= :.4f}")
