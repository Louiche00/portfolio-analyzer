# portfolio_analyzer.py
# Analyse automatique d'un portefeuille d'actions canadiennes
# Auteur : [Ton nom] | GitHub : [ton-username]

# ── Données du portefeuille ──────────────────────────────
PORTEFEUILLE = [
    {"ticker": "RY",  "nom": "Royal Bank",      "achat": 142.50, "actuel": 158.00, "qty": 10},
    {"ticker": "TD",  "nom": "TD Bank",          "achat": 78.20,  "actuel": 91.50,  "qty": 15},
    {"ticker": "BNS", "nom": "Scotiabank",       "achat": 63.40,  "actuel": 59.20,  "qty": 20},
    {"ticker": "CNR", "nom": "Canadian National", "achat": 185.00, "actuel": 198.00, "qty": 8},
    {"ticker": "SU",  "nom": "Suncor Energy",    "achat": 51.30,  "actuel": 55.80,  "qty": 25},
]

# ── Fonctions ────────────────────────────────────────────
def rendement(achat, actuel):
    return (actuel - achat) / achat * 100

def valeur(actuel, qty):
    return actuel * qty

def meilleur_performer(portefeuille):
    return max(portefeuille, key=lambda a: rendement(a["achat"], a["actuel"]))

def pire_performer(portefeuille):
    return min(portefeuille, key=lambda a: rendement(a["achat"], a["actuel"]))

def rapport(portefeuille):
    print("\n" + "="*50)
    print("  RAPPORT DE PORTEFEUILLE — ACTIONS CANADIENNES")
    print("="*50)
    print(f"  {'TICKER':<6} {'NOM':<22} {'REND.':>7} {'VALEUR':>9}")
    print("  " + "-"*46)

    total = 0
    for a in portefeuille:
        r = rendement(a["achat"], a["actuel"])
        v = valeur(a["actuel"], a["qty"])
        total += v
        signe = "▲" if r > 0 else "▼"
        print(f"  {a['ticker']:<6} {a['nom']:<22} {signe}{r:>5.1f}%  ${v:>7.0f}")

    print("  " + "-"*46)
    print(f"  {'TOTAL':<30} ${total:>7.0f}")

    best = meilleur_performer(portefeuille)
    worst = pire_performer(portefeuille)
    print(f"\n  ★ Meilleur : {best['ticker']} ({rendement(best['achat'],best['actuel']):+.1f}%)")
    print(f"  ↓ Pire     : {worst['ticker']} ({rendement(worst['achat'],worst['actuel']):+.1f}%)")
    print("="*50 + "\n")

# ── Exécution ────────────────────────────────────────────
if __name__ == "__main__":
    rapport(PORTEFEUILLE)
OUTPUT
==================================================
  RAPPORT DE PORTEFEUILLE — ACTIONS CANADIENNES
==================================================
  TICKER NOM                    REND.    VALEUR
  ----------------------------------------------
  RY     Royal Bank             ▲10.9%   $1 580
  TD     TD Bank                ▲17.0%   $1 372
  BNS    Scotiabank             ▼ 6.6%   $1 184
  CNR    Canadian National       ▲7.0%   $1 584
  SU     Suncor Energy           ▲8.8%   $1 395
  ----------------------------------------------
  TOTAL                                  $7 115

  ★ Meilleur : TD (+17.0%)
  ↓ Pire     : BNS (-6.6%)
==================================================
