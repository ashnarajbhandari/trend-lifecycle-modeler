import pandas as pd
import os

FILES = {
    "Clean Girl Aesthetic": "clean_girl.csv",
    "Mob Wife Aesthetic": "mob_wife.csv",
    "Quiet Luxury": "quiet_luxury.csv",
    "Glazed Donut Nails": "glazed_donut_nails.csv",
    "Coastal Grandmother": "coastal_grandmother.csv",
    "Indie Sleaze": "indie_sleaze.csv",
    "Cottagecore": "cottagecore.csv",
    "Dark Academia": "dark_academia.csv",
    "E-Girl Aesthetic": "e_girl.csv",
    "Y2K": "y2k.csv",
    "Balletcore": "balletcore.csv",
    "VSCO Girl": "vsco_girl.csv",
    "Coquette Aesthetic": "coquette.csv",
    "Rockstar Girlfriend": "rockstar_girlfriend.csv",
    "Opium Aesthetic": "opium_aesthetic.csv",
    "Pilates Princess": "pilates_princess.csv",
    "Office Siren": "office_siren.csv",
    "Latte Makeup": "latte_makeup.csv",
    "Soap Brows": "soap_brows.csv",
}

for name, file in FILES.items():
    if os.path.exists(file):
        df = pd.read_csv(file, skiprows=1)
        print(f"\n✅ {name} ({file})")
        print(df.head(3))
    else:
        print(f"\n❌ Missing: {file}")
