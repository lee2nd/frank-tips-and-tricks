# ============================================================
# Column / String Operations
# ============================================================

# Split strings into two Columns
new = data["Name"].str.split(" ", n = 1, expand = True)
data["First Name"]= new[0]
data["Last Name"]= new[1]

# Drop columns whose name contains a specific string (_id,_time)
# ex : ['scan_report_time', 'scan_sheet_id', 'scan_tool_id', 'scan_lot_id',
#       'scan_cst_id', 'scan_operation_id', 'scan_mes_id', 'track_report_time',
#       'track_sheet_id', 'track_tool_id', 'track_lot_id', 'track_cst_id',
#       'track_operation_id', 'track_mes_id', 'meth_report_time',
#       'meth_sheet_id', 'meth_tool_id', 'meth_lot_id', 'meth_cst_id',
#       'meth_operation_id', 'meth_mes_id']
df = df[df.columns.drop(list(df.filter(regex='_id|_time')))]

# 選包含某 string 的 columns to list
target_col = df.columns[df.columns.str.contains("Ylabel_")].to_list()


# ============================================================
# Missing Values
# ============================================================

# Check if any value is NaN in a Pandas DataFrame
df.isnull().any().any()

# Drop NAN
https://www.digitalocean.com/community/tutorials/pandas-dropna-drop-null-na-values-from-dataframe


# ============================================================
# Multi-level Columns
# ============================================================

# Giving a column multiple indexes/headers
header = pd.MultiIndex.from_product([['location1','location2'],
                                     ['S1','S2','S3']],
                                    names=['loc','S'])
df = pd.DataFrame(np.random.randn(5, 6), 
                  index=['a','b','c','d','e'], 
                  columns=header)
# loc location1                     location2                    
# S          S1        S2        S3        S1        S2        S3
# a   -1.245988  0.858071 -1.433669  0.105300 -0.630531 -0.148113
# b    1.132016  0.318813  0.949564 -0.349722 -0.904325  0.443206
# c   -0.017991  0.032925  0.274248  0.326454 -0.108982  0.567472
# d    2.363533 -1.676141  0.562893  0.967338 -1.071719 -0.321113
# e    1.921324  0.110705  0.023244 -0.432196  0.172972 -0.50368

# Drop a column from a multi-level column index
# https://stackoverflow.com/questions/25135578/python-pandas-drop-a-column-from-a-multi-level-column-index
#    a         x   
#    b  c  f   c  f
# 0  1  3  7  21  8
# 1  2  4  9  21  8

df.drop(('a', 'c'), axis = 1)
#    a      x   
#    b  f   c  f
# 0  1  7  21  8
# 1  2  9  21  8


# ============================================================
# DataFrame Construction & Conversion
# ============================================================

# Create multiple dataframes in loop
# https://stackoverflow.com/questions/30635145/create-multiple-dataframes-in-loop
## method1
dfs = ['df1', 'df2', 'df3', 'df4']
for df in dfs:
     exec('{} = pd.DataFrame()'.format(df))

## method2 --> a better way     
dfs = ['df5', 'df6']     
d = {}
for name in dfs:
    d[name] = pd.DataFrame()    
for name, df in d.items():
    # operate on DataFrame 'df' for company 'name'   

# Construct dataframe from dict
data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
df = pd.DataFrame.from_dict(data)

#    col_1 col_2
# 0      3     a
# 1      2     b
# 2      1     c
# 3      0     d

# Convert dataframe to 2d Array
df.values
# array([[3, 'a'],
#        [2, 'b'],
#        [1, 'c'],
#        [0, 'd']]

# flatten multi columns to one column
data = {
    "priceA": [17, 35, 87],
    "priceB": [47, 45, 65],
    "priceC": [pd.NA, 15, 64],
}
df = pd.DataFrame(data)
data_trans = (df
             .values  # to_numpy()
             .T       # transpose
             .ravel() # flatten
              )
df_trans = pd.DataFrame(data_trans, copy=False)

# dataframe to dictionary
temp = [["a",1], 
        ["b",2], 
        ["c",3], 
        ["d",4], 
        ["e",5]
        ]
df=pd.DataFrame(temp)
print(dict(df.values))
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


# ============================================================
# Filtering Rows
# ============================================================

# filter rows containing a string pattern
# https://stackoverflow.com/questions/27975069/how-to-filter-rows-containing-a-string-pattern-from-a-pandas-dataframe
# ids    vals
# aball   1
# bball   2
# cnut    3
# fball   4
# filter rows which contain the key word "ball"
# ids    vals
# aball   1
# bball   2
# fball   4
df[df['ids'].str.contains("ball")]


# ============================================================
# Feature Engineering / Preprocessing
# ============================================================

# drop columns with missing value > 0.60
df_X = df_X.loc[:, df_X.isnull().mean()<.60]

# sort
df.sort_values(by='col1', ascending=False)

# impute with MICE
X_size_row, X_size_column = df_X.shape
X_features_list = df_X.columns.tolist()

imp = IterativeImputer(
	estimator=ExtraTreesRegressor(random_state=42),
	missing_values=np.nan,
	max_iter=1,
	verbose=2,
	n_nearest_features=int(np.log(X_size_column+1)),
	random_state=42)
df_X = imp.fit_transform(df_X)
df_X = pd.DataFrame(df_X, columns=X_features_list)

# drop unique value columns
df_X = df_X[[col for col in list(df_X) if len(df_X[col].unique())>1]]

# label encoding
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
data.loc[:,"xxx"] = label_encoder.fit_transform(data.loc[:,"xxx"]).astype('float64')

# one-hot encoding
df_one_hot = pd.get_dummies(df_X['xxx'],prefix='xxx')
df_X = df_X.drop(columns='xxx')
df_X = pd.concat([df_X,df_one_hot],axis=1)

# correlation
import seaborn as sns
corr = df_X.corr()
sns.heatmap(corr)
columns = np.full((corr.shape[0],), True, dtype=bool)
for i in range(corr.shape[0]):
    for j in range(i+1, corr.shape[0]):
        if corr.iloc[i,j] >= 0.9:
            if columns[j]:
                columns[j] = False
selected_columns = df_X.columns[columns]
df_X = df_X[selected_columns]
