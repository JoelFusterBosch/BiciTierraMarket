"""
Genera customers_segmented.csv a partir de customers_out.csv
(mateixa lògica que el notebook cp3.ipynb: K-Means amb k = 5).

Ús:  python genera_customers_segmented.py
Requereix: pandas, numpy, scikit-learn
"""
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.preprocessing import StandardScaler

# ---- Rutes (canvia-les si cal) ----
RUTA_ENTRADA = "customers_out.csv"
RUTA_EIXIDA = "customers_segmented.csv"

# ---- 1. Llegim les dades netes ----
df = pd.read_csv(RUTA_ENTRADA)

# ---- 2. Segmentació per regles (referència) ----
def regla(fila):
    if fila["returns_ratio"] >= 0.25:
        return "Devolucions altes"
    if fila["days_since_last_order"] > 180:
        return "Inactius"
    if fila["orders_last_12m"] >= 7 and fila["avg_order_value"] >= 150:
        return "Valuosos"
    return "Resta"

# ---- 3. K-Means (k = 5) ----
df["log_avg_order_value"] = np.log(df["avg_order_value"])
vars_cluster = ["days_since_last_order", "orders_last_12m",
                "log_avg_order_value", "returns_ratio"]

# Excloem els clients sense recència (20 files), com al notebook
d = df.dropna(subset=["days_since_last_order"]).copy()
X = StandardScaler().fit_transform(d[vars_cluster])

km = KMeans(n_clusters=5, n_init=10, random_state=42).fit(X)
d["cluster"] = km.labels_
d["silhouette"] = silhouette_samples(X, km.labels_)
print("Silhouette global:", round(silhouette_score(X, km.labels_), 3))  # ha de donar 0.339

# ---- 4. Noms dels perfils ----
# No fiem el nom al número del cluster (pot canviar segons la versió de
# scikit-learn). Els assignem per les característiques de cada grup.
p = d.groupby("cluster").agg(
    rec=("days_since_last_order", "median"),
    com=("orders_last_12m", "median"),
    tiq=("avg_order_value", "median"),
    dev=("returns_ratio", "mean"),
)
noms = {}
noms[p["dev"].idxmax()] = "Devolucions altes"
resta = p.drop(index=list(noms))
noms[resta["rec"].idxmax()] = "Inactius"
resta = p.drop(index=list(noms))
noms[resta["tiq"].idxmax()] = "Tiquet alt"
resta = p.drop(index=list(noms))
noms[resta["com"].idxmax()] = "Fidels freqüents"
resta = p.drop(index=list(noms))
noms[resta.index[0]] = "Ocasionals de tiquet baix"

d["perfil"] = d["cluster"].map(noms)
d["segment_regles"] = d.apply(regla, axis=1)
print(d["perfil"].value_counts())  # 607 / 540 / 403 / 216 / 214

# ---- 5. Tornem a unir amb els 2.000 clients ----
out = df.merge(
    d[["customer_id", "cluster", "perfil", "silhouette", "segment_regles"]],
    on="customer_id", how="left",
)
out["perfil"] = out["perfil"].fillna("Sense recència (excl.)")
out["segment_regles"] = out["segment_regles"].fillna("Sense recència (excl.)")

# ---- 6. Segmentació comercial (valor + risc) ----
out["segment_valor"] = pd.qcut(
    out["annual_spend"], q=3, labels=["Baix", "Mitjà", "Alt"]
).astype(str)
out["estat_client"] = np.where(out["days_since_last_order"] > 90, "Risc", "Actiu")
out.loc[out["days_since_last_order"].isna(), "estat_client"] = "Sense dades"
out["segment_comercial"] = out["segment_valor"] + "_" + out["estat_client"]

# ---- 7. Columnes auxiliars per a Power BI ----
out["frontera"] = np.where(out["silhouette"] < 0, "Frontera (silhouette<0)", "Clar")
out.loc[out["silhouette"].isna(), "frontera"] = "Sense dades"
out["tram_edat"] = pd.cut(
    out["age"], [0, 29, 39, 49, 59, 120],
    labels=["<30", "30-39", "40-49", "50-59", "60+"],
).astype(str)

# ---- 8. Guardem ----
out.to_csv(RUTA_EIXIDA, index=False)
print("Guardat:", RUTA_EIXIDA, out.shape)  # (2000, 24)