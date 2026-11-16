# BiciTierraMarket

Projecte d'anàlisi de dades i models predictius per a BiciTierra Market, una botiga de bicicletes. L'objectiu és entendre què fa augmentar les vendes i ajudar a prendre decisions de negoci.

## Pregunta de negoci

> **Què fa que venguem més unitats: el màrqueting, els descomptes, o altres factors?**

Més detall a [`preguntes.md`](preguntes.md).

## Equip

| Persona | Rama |
|---|---|
| Joel | `Joel` |
| Sofia | `Sofia` |
| Sonia | `Sonia` |

Les tasques es reparteixen al tauler de Trello.

## Estructura del repositori

| Carpeta / fitxer | Contingut |
|---|---|
| `dades/` | Fitxers CSV originals |
| `notebooks/` | Anàlisi exploratòria i neteja de dades |
| `evidencies/` | Proves dels models (un notebook per model) |
| `entregues/` | Lliuraments del projecte |
| `docs/` | Documentació |
| `preguntes.md` | Pregunta de negoci i plantejament dels models |
| `requirements.txt` | Llibreries necessàries |

## Models

| Model | Responsable |
|---|---|
| Regressió lineal | Joel |
| Regressió polinomial | Sofia |
| Regressió logística multiclasse + Gradient Boosting | Sonia |

## Com treballem

1. Cada persona treballa a la seua rama.
2. Abans de començar, baixem els canvis de `main` (`git pull origin main`).
3. Quan una tasca està acabada, fem un Pull Request a `main`.

## Instal·lació

```bash
pip install -r requirements.txt
```
