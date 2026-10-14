# RS TOURNAMENT Security & Bug Fixes Implementation Plan

This plan addresses code quality issues, security vulnerabilities, duplicate orphan blocks, database rules hardening, and file synchronization between the root website and Android assets.

## User Review & Critical Decisions

> [!IMPORTANT]
> - **Zero Dummy Login Fallbacks**: Fake "dummyUser" and production demo-login bypasses will be permanently removed to enforce strict Firebase Authentication integrity.
> - **Admin Authentication**: LocalStorage-alone authorization is replaced with a verified Firebase Auth user and a trusted database permission check (`isAdmin === true`).
> - **Database Rules Hardening**: Strict validation rules added to `database.rules.json` to prevent tampering with sensitive top-up orders, user balances, and chat message integrity.

- **Confirmed Decision 1**: Maintain exact synchronization between root website files (`index.html`, `admin.html`) and Android asset files (`app/src/main/assets/index.html`).
- **Open Question / Choice 2**: None remaining; executing all 6 requested stabilization and hardening tasks.

---

## 1. Overview & Core Concept

- **What It Does**: Stabilizes and secures the RS TOURNAMENT platform (Web and Android), removing fallback vulnerabilities and enforcing strict Firebase Auth, database rules, and clean code syntax.
- **Target Audience / Persona**: Esport players, tournament organizers, and administrators.
- **Key Value**: Production-grade security, zero fake authentication bypasses, robust admin access control, and clean maintainable code.

---

## 2. User Experience & Visual Design

- **Key User Flows**: Unchanged UI layouts, ensuring smooth login, tournament participation, top-ups, community chat, and admin panel management.
- **Visual Identity & Theme**: Maintains existing neon cyberpunk aesthetic (`--neon-cyan`, `--neon-green`, `--neon-amber`, `--neon-red`), dark card surfaces, and Font Awesome iconography.
- **Interactive Feedback**: Clear error banners and loading states when Firebase operations occur, with no silent fallbacks.

---

## 3. Key Product Decisions & Trade-Offs

- **Decision 1**: Removal of Demo/Dummy Login Fallbacks
  - *Chosen Approach*: Force real Firebase Auth; show precise error messages if auth fails.
  - *Why*: Eliminates security holes where unauthenticated users could access protected user actions.
- **Decision 2**: Strict Database & Admin Verification
  - *Chosen Approach*: `database.rules.json` and client checks both require `auth != null` and `root.child('users').child(auth.uid).child('isAdmin').val() === true`.
  - *Why*: Prevents privilege escalation via local storage tampering.

---

## 4. Technical Architecture & Data Strategy

```
┌────────────────────────────────────────────────────────┐
│                        Clients                         │
│       Root index.html / Android app/src/main/assets    │
│                     Root admin.html                    │
└───────────────┬────────────────────────┬───────────────┘
                │                        │
                ▼                        ▼
┌───────────────────────────────┐ ┌──────────────────────┐
│     Firebase Authentication   │ │ Firebase Realtime DB │
│ (Google / Email & Password)   │ │  (Hardened Rules)    │
└───────────────────────────────┘ └──────────────────────┘
```

- **Files to Update**:
  1. `index.html` (root user panel)
  2. `app/src/main/assets/index.html` (Android asset synchronization)
  3. `admin.html` (Admin panel security fix)
  4. `database.rules.json` (Database validation & security rules)
- **State Management & Data Strategy**:
  - Remove orphan code block around lines 6252–6280 in `index.html` and `app/src/main/assets/index.html`.
  - Enforce server-side rule validation on top-up orders, coins, roles, and chat message lengths.
