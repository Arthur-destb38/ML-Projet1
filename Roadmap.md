


#  Roadmap – Projet de Machine Learning Supervisé en Économétrie Quantitative

## 👥 Équipe
**Groupe de 5 étudiants**

---

## 🎯 Objectif du projet
Proposer et implémenter un **projet de machine learning supervisé** appliqué à un problème d’économétrie quantitative.  
Le but est de montrer **dans quel cadre le ML peut être utile** pour modéliser, prévoir ou expliquer un phénomène économique ou financier.

Exemples :
- Prévision macroéconomique (PIB, inflation, chômage)
- Modélisation des rendements financiers (automatic trading)
- Scoring de crédit ou risque de défaut
- Prévision de la consommation énergétique
- Estimation de la demande / offre sur un marché

---

## 🧮 Étape 1 – Définition du cadre et des données

### 1.1. Choix du thème et de la problématique
- Identifier une question économétrique ou financière où le ML apporte une valeur ajoutée.
- Exemples :
  - Peut-on prédire l’évolution du taux d’inflation à partir d’indicateurs macroéconomiques ?
  - Peut-on estimer le rendement journalier d’un actif à partir de données de marché ?

# Roadmap — Projet : Automatic trading (style clair et humain)

Salut l'équipe — voici une feuille de route faite pour qu'on avance vite et propre sur un projet d'automatic trading. J'ai gardé les étapes classiques de machine learning, mais réorientées vers le trading : data, features, backtest, modèles, métriques financières et déploiement.

Objectif rapide
- Construire un pipeline reproductible qui prend des prix (ex. SPY), génère des features techniques, entraîne des modèles, backteste des signaux, et produit un rapport + notebook.

Pourquoi ça marche
- On commence simple (indicateurs classiques, modèles linéaires), puis on complexifie (boosting, LSTM) si besoin. On évalue non seulement sur métriques ML, mais surtout en performance de trading (Sharpe, drawdown, PnL).

Plan en 6 étapes (concret)
1) Définir la question
  - Qu'est-ce qu'on prédit ? le signe du rendement (classification) ou la valeur du rendement (régression) ?
  - Horizon : daily (recommandé pour commencer) ou intraday ?
  - Univers : SPY / top US stocks / crypto ? (on démarre sur SPY pour un proof-of-concept)

2) Collecte et qualité des données
  - Sources : Yahoo Finance (`yfinance`) pour l'historique; possibilité d'ajouter AlphaVantage / CCXT plus tard.
  - Nettoyage : gérer missing, splits, divs, timezone, resampling si nécessaire.
  - Stockage : `data/raw/` pour brut, `data/processed/` pour datasets prêts à l'entraînement.

3) Features & preprocessing
  - Features de base : returns, log-returns, rolling mean/std, RSI, MACD, ATR, volumes normalisés, lags de rendement.
  - Préprocessing : standardisation, création de fenêtres temporelles, éviter look-ahead.

4) Modélisation & validation
  - Baselines : régression/logistique, arbres, RandomForest.
  - Avancés : LightGBM/XGBoost, LSTM/1D-CNN si on veut capter séquence.
  - Validation : split temporel, backtest rolling (walk-forward). Pas de CV aléatoire.

5) Backtest & évaluation financière
  - Backtester avec coûts de transaction et slippage simples.
  - Metrics : PnL cumulée, Sharpe ratio, CAGR, max drawdown, hit rate, turnover.
  - Comparer à un benchmark (buy-and-hold). Faire tests sur périodes différentes (bull/bear).

6) Packaging & présentation
  - Notebook reproducible + script pour rejouer le pipeline.
  - Petite API pour exposer signaux (optionnel) via `uvicorn`.
  - Slides + rapport synthétique.

Livrables finaux
- Notebook Jupyter complet
- Scripts pour download/preprocess/features
- Backtest reproduisible avec métriques
- Slides + README d'utilisation

Timeline suggérée (6 semaines)
- Semaine 1 : choix du sujet précis, collecte SPY, nettoyage, premières features.
- Semaine 2 : EDA, features supplémentaires, baseline models.
- Semaine 3 : Modèles avancés et tuning, backtest initial.
- Semaine 4 : Robustesse (stress tests, different periods), métriques trading.
- Semaine 5 : Packaging, notebook final, slides.
- Semaine 6 : Révisions, présentation orale, livraison.

Prochaines petites actions immédiates
1. Choisir : classification du signe (recommandé) vs régression.
2. Confirmer horizon : daily ?
3. Si ok, je génère automatiquement des features de base pour `data/raw/SPY.csv` et je crée `data/processed/spy_features.csv`.

Dis-moi ce que tu veux choisir (signe vs rendement, horizon daily vs intraday). Je lance la génération des features dès que t'as validé.
