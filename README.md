# 🛡️ Password Strength Checker

A lightweight Python tool designed to evaluate the security of user passwords based on standard complexity requirements. This script provides real-time feedback to help users create stronger, more resilient credentials.



## ✨ Features

* **Length Check:** Ensures passwords are at least 8 characters long.
* **Complexity Analysis:** Validates the presence of:
    * Numbers (`0-9`)
    * Uppercase letters (`A-Z`)
    * Lowercase letters (`a-z`)
    * Special characters (e.g., `!@#$%^&*`)
* **Interactive Loop:** Test multiple passwords in one session without restarting the script.

## 🚀 How It Works

The tool uses a series of conditional checks and **Regular Expressions (Regex)** to verify that the input meets specific security thresholds.

### Strength Levels:
| Status | Requirement |
| :--- | :--- |
| **Weak** | Fails basic length or character variety checks. |
| **Medium** | Meets length and alphanumeric requirements but lacks special characters. |
| **Strong** | Meets all security criteria. |

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mansi-Kulkarni12/Password_Strength_Checker.git
