# 🔐 Procédure de renouvellement de licence **Confluent**




> 📄 **Objectif**  
> Renouveler les licences Confluent afin d’éviter toute perte de fonctionnalité critique, notamment l’accès à **Confluent Control Center**.

---

## 🧩 1. Renouvellement de la licence des **Brokers Kafka**

### ✅ Pré-requis
- Connexion **SSH** sur chaque broker
- Droits **root** requis

---

### 🌍 Liste des brokers par environnement

#### 🔧 Intégration
- `LI0KFB01-BROK.domedi.local`
- `LI0KFB02-BROK.domedi.local`
- `LI0KFB03-BROK.domedi.local`

#### 🧪 Recette
- `LR0KFB01-BROK.domedi.local`
- `LR0KFB02-BROK.domedi.local`
- `LR0KFB03-BROK.domedi.local`
- `LR0KFB04-BROK.domedi.local`

#### 🚀 Production
- `LP0KFB01-BROK.domedi.local`
- `LP0KFB02-BROK.domedi.local`
- `LP0KFB03-BROK.domedi.local`
- `LP0KFB04-BROK.domedi.local`

---

### ⚠️ Important
> Le paramètre `confluent.license` doit impérativement contenir **la nouvelle clé de licence** fournie par Confluent.

---

### 🖥️ Commandes à exécuter *(sur chaque broker)*

```bash
sudo su root

# Vérifier l'état du service
systemctl status confluent-server

# Arrêter le service
systemctl stop confluent-server

# Modifier le fichier de configuration
vi /etc/kafka/server.properties

# ➜ Mettre à jour la ligne suivante :
# confluent.license=VOTRE_NOUVELLE_LICENCE

# Redémarrer le service
systemctl start confluent-server

# Vérifier le statut
systemctl status confluent-server
```

---

## 🖥️ 2. Renouvellement de la licence **Control Center**

### ✅ Pré-requis
- Connexion **SSH** sur le serveur Control Center
- Droits **root** requis

---

### 🔑 Récupération de la nouvelle clé de licence

La clé de licence **Control Center** est disponible dans **Secret Server** :

🔗 https://secretserver/app/#/secrets/view/folder/944

---

### ⚠️ Important
> Le paramètre `confluent.license` doit contenir **la nouvelle clé de licence fournie par Confluent**.

---

### 🖥️ Commandes à exécuter *(sur le serveur Control Center)*

```bash
sudo su root

# Vérifier l'état du service
systemctl status confluent-control-center

# Arrêter le service
systemctl stop confluent-control-center

# Modifier le fichier de configuration
vi /etc/confluent-control-center/control-center-production.properties

# ➜ Mettre à jour la ligne suivante :
# confluent.license=VOTRE_NOUVELLE_LICENCE

# Redémarrer le service
systemctl start confluent-control-center

# Vérifier le statut
systemctl status confluent-control-center
```

---

## 🔍 3. Vérification de la validité de la licence

### 🌐 Via l’interface **Control Center**

La date d’expiration de la licence peut être consultée directement depuis l’interface web **Control Center**.

#### 📌 Exemple – Environnement **Production**

🔗 https://lp0kfb01-cont.domedi.local:9021/login/settings/license

---

## ✅ Bonnes pratiques
- Toujours effectuer l’opération **hors heures de pointe**
- Vérifier les logs en cas de problème au redémarrage
- Documenter la date de renouvellement et la date d’expiration

---

✨ *Document converti depuis PDF vers Markdown avec une mise en forme lisible, structurée et prête à être versionnée (Git).*

