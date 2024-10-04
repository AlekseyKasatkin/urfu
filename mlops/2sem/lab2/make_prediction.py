from sklearn.cluster import KMeans
import joblib
import os
from sklearn.preprocessing import StandardScaler

project_dir = os.path.dirname(__file__)
print("Текущая рабочая директория:", os.getcwd())
df = joblib.load(os.path.join(project_dir, 'data.pkl'))
df_ = df[['review_count', 'fans', 'friends_count']]

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_)

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(df_scaled)

df_wc = df
df_wc['cluster'] = clusters


df_wc.to_pickle(os.path.join(project_dir, 'clusters.pkl'))