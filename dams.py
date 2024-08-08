import streamlit as st
from PIL import Image

# Charger l'image
image_path = "carte_de_visite.jpeg"
image = Image.open(image_path)

# Afficher l'image en haut du site
st.image(image, use_column_width=True)

# Titre de l'application
st.title("Dam's Multi services")

# Barre latérale pour les informations de l'entreprise
st.sidebar.title("Informations")

# Informations de l'entreprise dans la sidebar
st.sidebar.header("Informations de l'entreprise")
st.sidebar.write("""
**Nom** : Dam's Multi services 
**Adresse** : Territoire de Belfort et alentour   
**Téléphone** : 06.03.50.85.52  
**Email** : damsmultiservice90@gmail.com 
**Horaires** : Lundi - Samedi, 8h - 18h  
""")
st.sidebar.write("N'hésitez pas à me joindre pour plus de renseignement.")

# Contenu principal
st.header("Mes Services")
st.write("""
### Désinfection des cafards
J'utilise des techniques efficaces et respectueuses de l'environnement pour éliminer les cafards de votre domicile ou de votre entreprise.

### Élimination des punaises de lit
J'élimine les punaises de lit de votre domicile en garantissant des résultats rapides et durables.

         
### Enlèvement de nids de guêpes
Intervention rapide pour retirer en toute sécurité les nids de guêpes ou de frelons de votre propriété, afin de garantir votre sécurité.

### Débarras
Je vous aide à vous débarrasser de vos encombrants rapidement et efficacement.
         
### Pelouse
Je vous aide à tailler vos haies et à prendre soin de vos extérieurs.
""")

# Séparateur
st.markdown("---")

# FAQ
st.header("FAQ")
st.write("""
**Comment savoir si j'ai des cafards ou des punaises de lit ?**
Les signes courants incluent des taches, des traces de morsures, et des odeurs inhabituelles. Contactez-moi pour un diagnostic.

**Combien de temps prend une intervention ?**
Cela dépend du service, mais j'essaie de compléter chaque intervention le jour même.

**Quels produits utilisez-vous ?**
J'utilise des produits respectueux de l'environnement qui sont efficaces et sûrs pour votre maison et vos animaux domestiques.
""")
