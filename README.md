# 🛠 Mugie Custom Repair App – Installation & Deployment Guide

This guide outlines how to install and deploy the Mugie Custom Repair App on Mugie Odoo Enterprise via Odoo.sh.

---

## ✅ Pre-Flight Checklist

1. **Confirm Mugie repo default branch**
   - Visit: https://github.com/TMCLmugie/mugie.git
   - Note the default branch name (e.g., `main`).

2. **Confirm custom addons path**
   - Locate custom modules in `custom/` directory.

3. **Set up SSH access for private repo**
   - In Odoo.sh: `Project → Settings → Submodules`
   - Add SSH URL: `git@github.com:Brian-Ki/mugie_custom_repair_app.git`
   - Copy generated SSH key and add it to GitHub deploy keys with read access.

4. **Check `__manifest__.py`**
   - Ensure `"installable": True`
   - Include all required dependencies in `"depends": []`

5. **Add extra Python libraries**
   - Update Mugie repo’s `requirements.txt` if needed.

---

## 🖥 Local Setup

```bash
git clone https://github.com/TMCLmugie/mugie.git
cd mugie
git checkout -b client-qa origin/client-qa
git submodule add -b main git@github.com:Brian-Ki/mugie_custom_pos.git custom/mugie_custom_pos
git add .gitmodules custom/mugie_custom_pos
git commit -m "Add Mugie Custom Repair App for testing"
git push origin client-qa
```

---

## 🚧 Odoo.sh Deployment

1. Open Odoo.sh dashboard.
2. Wait for `client-qa` branch to appear.
3. Promote to Staging (optional).
4. Wait for build to complete.

---

## 📦 Module Installation

1. Open QA site for `client-qa` branch.
2. Activate Developer Mode.
3. Update Apps List.
4. Search and install **Mugie Custom Repair App**.

---

## 🔄 Updating the Module

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

## 🚀 Merge to Production

```bash
git checkout main
git merge client-qa
git push origin main
```

> Odoo.sh will deploy to production automatically.

---

## 🧾 Usage

- Access **Repair Orders** in Odoo.
- New fields: **Expense Account** and **Analytic Distribution**.
- Confirming a repair posts data to configured accounts.

---

## 🧰 Technologies Used

- Python – Backend logic
- XML – UI customizations
- Odoo.sh – Deployment platform

---

## 📜 License

MIT License – Free to use, modify, and distribute.

---

## 👤 Author

**Brian Kipkemboi Kibet**  
📧 kipkemboikibet1@gmail.com  
🔗 https://github.com/Brian-Ki
```