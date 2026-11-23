# Pregunta de negoci

> **Què fa que venguem més unitats: el màrqueting, els descomptes, o altres factors?**

Dataset: `sales_history.csv` (1188 registres, 17 columnes).
Objectiu: `sales_units` (unitats venudes).

## Com la respon cada model

| Model | Pregunta | Pregunta secundària |
|---|---|---|
| **Regressió lineal** | Quant augmenten les vendes per cada euro de màrqueting o punt de descompte? | Quin factor pesa més? |
| **Regressió polinomial** | L'augment és constant, o hi ha un punt a partir del qual deixa de compensar? | A partir de quin gasto en màrqueting guanyem poc? |
| **Regressió logística multiclasse** | Amb quines condicions tenim vendes altes en lloc de baixes o mitjanes? | Quin factor fa pujar més la probabilitat de vendes altes? |

## Dades comunes

**Variables d'entrada**

- Numèriques: `marketing_spend`, `avg_discount`, `website_sessions`, `stock_units`, `list_price`, `month_num`.
- Categòriques (amb `get_dummies`): `channel`, `product_line`, `region`, `campaign`.

**Deixar fora** (es calculen a partir de les vendes i farien trampa): `revenue`, `closing_stock_units`, `stockout`.

**Objectiu de la logística**: columna nova `nivell_vendes`.

```python
df["nivell_vendes"] = pd.qcut(df["sales_units"], 3, labels=["baix", "mitjà", "alt"])
```

## Per a Power BI

Cada persona exporta un CSV amb els resultats i el carrega amb *Obtindre dades → Text/CSV*:

```python
resultat = X_test.copy()
resultat["real"] = y_test
resultat["prediccio"] = model.predict(X_test)
resultat.to_csv("resultats_nom_model.csv", index=False)
```

Gràfics suggerits (senzills):

- **Lineal**: barres amb els coeficients, de més a menys pes.
- **Polinomial**: dispersió amb els punts reals i la línia predita.
- **Logística**: taula o matriu amb encerts i errors per classe (baix, mitjà, alt).

La conclusió final de l'informe uneix els tres models en una sola resposta a la pregunta.