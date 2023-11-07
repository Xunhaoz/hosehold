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
> train mse = 207961125186.6589 \
> before para finding mse = 208235595500.1610 \
> after para finding mse =  \
> 資料篩選-剔除極端值, 線性回歸

> xgboost - baseline \
> dataloader data_xunhaoz001.py \
> predictor code_xunhaoz002.py \
> train mse = 116527097296.6626 \
> before para finding mse = 160159458723.4670 \
> after para finding mse =  \
> 資料篩選-剔除極端值, xgboost

> random_forest - baseline \
> dataloader data_xunhaoz001.py \
> predictor code_xunhaoz003.py \
> train mse = 188255005038.0431 \
> before para finding mse = 48022261133.9113 \
> after para finding mse =  \
> 資料篩選-剔除極端值, random_forest

> extra_trees_regressor - baseline \
> dataloader data_xunhaoz001.py \
> predictor code_xunhaoz004.py \
> train mse = 205836012057.1338 \
> before para finding mse = 30237992697.9192 \
> after para finding mse =  \
> 資料篩選-剔除極端值, extra_trees_regressor

> lgbm_regressor - baseline \
> dataloader data_xunhaoz001.py \
> predictor code_xunhaoz005.py \
> train mse = 149967668729.3877 \
> before para finding mse = 135916482312.5306 \
> after para finding mse =  \
> 資料篩選-剔除極端值, lgbm_regressor

> catboost - baseline \
> dataloader data_xunhaoz001.py \
> predictor code_xunhaoz006.py \
> train mse = 152864670413.1408 \
> before para finding mse = 120433189517.8904 \
> after para finding mse =  \
> 資料篩選-剔除極端值, catboost