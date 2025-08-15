# 🛠 Installation & Deployment Guide  
**For `Mugie Custom Repair App` on Mugie Odoo Enterprise (Odoo.sh)**  

---

## 0️⃣ Pre-Flight Checklist (Do This Before Any Commands)

### 1. Confirm Mugie repo default branch
- Visit [Mugie Repo](https://github.com/TMCLmugie/mugie.git)  
- Check the branch selector → **Note the name** (likely `main`, but confirm).

### 2. Confirm Mugie custom addons path
- Open Mugie repo and locate existing custom modules.
- Custom modules live in: `custom/`  
- Replace in commands below if different.

### 3. Setup SSH access for private repo
- On **Odoo.sh dashboard**:  
  `Project → Settings → Submodules`  
  Add SSH URL:  
  ```bash
  git@github.com:Brian-Ki/mugie_custom_repair_app.git
````

Copy the generated SSH public key.

* On **GitHub** (`mugie_custom_repair_app` repo):
  `Settings → Deploy Keys → Add key`
  Paste the key, check **Allow read access**, and save.

> 📌 *Optional*: Insert screenshot of Odoo.sh SSH key setup.

### 4. Ensure `__manifest__.py` is correct

* `"installable": True`
* `"depends": []` contains all dependencies.

### 5. If extra Python libs are needed

* Add them to **Mugie repo’s `requirements.txt`**.

---

## 1️⃣ Local Machine Steps

```bash
# 1. Clone Mugie repo
git clone https://github.com/TMCLmugie/mugie.git
cd mugie

# 2. Checkout the testing branch
git checkout -b client-qa origin/client-qa

# 3. Add mugie_custom_pos as submodule (custom repair app)
git submodule add -b main git@github.com:Brian-Ki/mugie_custom_pos.git custom/mugie_custom_pos

# 4. Commit and push changes
git add .gitmodules custom/mugie_custom_pos
git commit -m "Add Mugie Custom Repair App for testing"
git push origin client-qa
```

---

## 2️⃣ Odoo.sh Dashboard Steps

1. Go to **Odoo.sh dashboard** for Mugie project.
2. Wait for `client-qa` branch to appear.
3. Click **Promote to Staging** (optional if you want staging environment).
4. Wait for build to complete (check logs for errors).

---

## 3️⃣ Install the Module in Staging/Client QA DB

1. Open Mugie QA site for the branch (`client-qa`).
2. Go to **Settings → Activate Developer Mode**.
3. Go to **Apps → Update Apps List**.
4. Search for **"Mugie Custom Repair App"** → Install.

---

## 4️⃣ Updating the Module (Local Machine)

```bash
cd custom/mugie_custom_pos
git pull origin main
cd ../../..
git add custom/mugie_custom_pos
git commit -m "Update Mugie Custom Repair App to latest version"
git push origin client-qa
```

> Odoo.sh will rebuild automatically.

---

## 5️⃣ Merging to Production

```bash
# Local machine:
git checkout main     # Or Mugie’s default production branch
git merge client-qa
git push origin main
```

* **Dashboard**: Odoo.sh will deploy to production automatically once `main` is updated.

---

## 🚀 Usage

1. Open **Repair Orders** in Odoo.
2. You will see **Expense Account** and **Analytic Distribution** fields in the form & tree views.
3. Confirm a repair → data will post according to configured accounts.

---

## 💻 Technologies Used

* **Python** – Backend module logic
* **XML** – Form & tree view customizations
* **Odoo.sh** – Deployment & module management

---

## 📜 License

Licensed under the **MIT License** – free to use, modify, and distribute.

---

## 👤 Author

**Brian Kipkemboi Kibet**
📧 [kipkemboikibet1@gmail.com](mailto:kipkemboikibet1@gmail.com)
🔗 [GitHub Profile](https://github.com/Brian-Ki)

```
