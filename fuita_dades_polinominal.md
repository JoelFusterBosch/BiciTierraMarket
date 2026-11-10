# Fuita de dades (data leakage) al model polinomial

**Projecte:** BICITIERRA · **Dataset:** `sales_history.csv` · **Objectiu:** `sales_units`

## Símptoma

El primer model polinomial (grau 2) va donar resultats impossibles a test:

| Mètrica | Valor |
|---|---|
| R² | 1.0 |
| MSE | 5.28e-27 |
| MAE | 4.91e-14 |

Un error pràcticament zero en dades reals no indica un bon model, sinó que el model "veu" la resposta.

## Causa

`num_cols` incloïa `closing_stock_units`, que es calcula a partir de les vendes (aprox. `stock_units - sales_units`). Amb `stock_units` i `closing_stock_units` el model pot reconstruir `sales_units` exactament.

`preguntes.md` ja ho advertia: `revenue`, `closing_stock_units` i `stockout` s'han de deixar fora.

També s'hi havien colat `marketing_budget` i `planned_discount`, que no estan a la llista de variables d'entrada. No són fuita, però dupliquen informació de `marketing_spend` i `avg_discount` (col·linearitat).

## Comprovació

```python
print((df["stock_units"] - df["closing_stock_units"] - df["sales_units"]).abs().describe())
```

Si el resultat és 0 o quasi 0, es confirma que la columna deriva de les vendes.

## Solució

Deixar només les variables d'entrada definides:

```python
num_cols = ["marketing_spend", "avg_discount", "website_sessions",
            "stock_units", "list_price", "month_num"]
```

## Lliçons

- Una mètrica "perfecta" (R² = 1) és un senyal d'alerta, no un èxit.
- Abans d'entrenar, revisar quines columnes es calculen a partir de l'objectiu.
- Comparar R² de train i de test per detectar també el sobreajust.

## Estat

- [x] Fuita identificada i causa documentada
- [ ] Reentrenar amb les columnes corregides i anotar els nous R², MSE i MAE
- [ ] Afegir les categòriques (`get_dummies`) i provar graus 1, 2 i 3