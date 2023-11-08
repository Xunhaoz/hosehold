# 資料科學導論期末專案

## PART - 機器學習

### 環境需求

* python 3.9

### 專案架構

```
├── README.md
├── data 
│   ├── raw 存放原始 CSV 資料
│   └── result csv 存放 CSV 報告
├── dataloader - 是個放資料前處理的 class 的地方
├── predictor - 是個做預測及驗證的地方
├── requirements.txt
└── testing playground - 唯一可以亂打程式的地方

```

### REQUIREMENTS

```shell
pip install -r requirements.txt
```

### COMMIT RULE

```
ADD: what
UPDATE: what
REFACTOR: what
DELETE: what
```

### REPORT

#### **_raw data 唯讀 ！！！！！！！_**

#### **_train: valid = 0.8: 0.2_**

#### **_使用 five cross validation_**

#### **_使用 five cross valid_**

> 線性回歸 - baseline \
> dataloader data_xunhaoz001.py \
> predictor code_xunhaoz001.py \
> train mae = 250812 \
> before para finding mae = 251157 \
> after para finding mae =  \
> 資料篩選-剔除極端值, 線性回歸

> 線性回歸 - onehot \
> dataloader data_xunhaoz002.py \
> predictor code_xunhaoz001.py \
> train mae = 207481 \
> before para finding mae = 208770 \
> after para finding mae =  \
> 資料篩選-剔除極端值, 線性回歸

> xgboost - baseline \
> dataloader data_xunhaoz001.py \
> predictor code_xunhaoz002.py \
> train mae = 177721 \
> before para finding mae = 187149 \
> after para finding mae =  \
> 資料篩選-剔除極端值, xgboost

> xgboost - onehot \
> dataloader data_xunhaoz002.py \
> predictor code_xunhaoz002.py \
> train mae = 177394 \
> before para finding mae = 187351 \
> after para finding mae =  \
> 資料篩選-剔除極端值, xgboost

> random_forest - baseline \
> dataloader data_xunhaoz001.py \
> predictor code_xunhaoz003.py \
> train mae = 108679 \
> before para finding mae = 207795 \
> after para finding mae =  \
> 資料篩選-剔除極端值, random_forest

> random_forest - onehot \
> dataloader data_xunhaoz002.py \
> predictor code_xunhaoz003.py \
> train mae = 107572 \
> before para finding mae = 204512 \
> after para finding mae =  \
> 資料篩選-剔除極端值, random_forest

> extra_trees_regressor - baseline \
> dataloader data_xunhaoz001.py \
> predictor code_xunhaoz004.py \
> train mae = 64263 \
> before para finding mae = 217228 \
> after para finding mae =  \
> 資料篩選-剔除極端值, extra_trees_regressor

> extra_trees_regressor - onehot \
> dataloader data_xunhaoz001.py \
> predictor code_xunhaoz004.py \
> train mae = 64263 \
> before para finding mae = 221386 \
> after para finding mae =  \
> 資料篩選-剔除極端值, extra_trees_regressor

> lgbm_regressor - baseline \
> dataloader data_xunhaoz001.py \
> predictor code_xunhaoz005.py \
> train mae = 185391 \
> before para finding mae = 189237 \
> after para finding mae =  \
> 資料篩選-剔除極端值, lgbm_regressor

> lgbm_regressor - onehot \
> dataloader data_xunhaoz001.py \
> predictor code_xunhaoz005.py \
> train mae = 184285 \
> before para finding mae = 188149 \
> after para finding mae =  \
> 資料篩選-剔除極端值, lgbm_regressor

> catboost - baseline \
> dataloader data_xunhaoz001.py \
> predictor code_xunhaoz006.py \
> train mae = 178968 \
> before para finding mae = 185636 \
> after para finding mae =  \
> 資料篩選-剔除極端值, catboost

> catboost - onehot \
> dataloader data_xunhaoz001.py \
> predictor code_xunhaoz006.py \
> train mae = 178380 \
> before para finding mae = 185716 \
> after para finding mae =  \
> 資料篩選-剔除極端值, catboost