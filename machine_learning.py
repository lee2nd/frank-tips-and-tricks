# ============================================================
# Feature Importance
# ============================================================

# get the feature importances 
from sklearn.ensemble import RandomForestRegressor
import numpy as np

regr_rf = RandomForestRegressor(n_estimators=1024, random_state=42) 
regr_rf = regr_rf.fit(df_X, df_y)

df_feature_rank = pd.DataFrame(
	{"feature": list(df_X.columns),
	 "importance": list(regr_rf.feature_importances_)
	}).sort_values(by="importance", ascending=False) 
df_feature_rank["importance"] = 100 * df_feature_rank["importance"]	

cum_pctg = np.cumsum(list(regr_rf.feature_importances_))


# ============================================================
# Model Training / Evaluation
# ============================================================

# xgb model in classification problem
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

model = XGBClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_probs = model.predict_proba(X_test)[:, 1]

cm = confusion_matrix(y_test, y_pred)
auc_score = roc_auc_score(y_test, y_probs)
accuracy_score(y_test, y_pred)
