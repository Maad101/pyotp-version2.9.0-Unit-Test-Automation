## Group Members
| Name | Roll No. |
|---|---|
| Maad Ashraf | 24F-3091 |
| Ali Hassan | 24F-3066 |

---

## Application Under Test
| Item | Details |
|---|---|
| Project | pyotp |
| Version | 2.9.0 |
| Language | Python |
| Source | https://github.com/pyauth/pyotp |
| License | MIT (see `LICENSE-pyotp`) |

### Modules Selected for Testing
| Module | Files | Classes / Functions |
|---|---|---|
| M1 – HOTP (counter-based OTP) | `otp.py`, `hotp.py` | `OTP`, `HOTP` – `at()`, `verify()`, `provisioning_uri()`, `generate_otp()` |
| M2 – TOTP (time-based OTP) | `totp.py` | `TOTP` – `at()`, `now()`, `verify()`, `timecode()` |
| M3 – Utilities and URI parsing | `utils.py`, `__init__.py` | `build_uri()`, `strings_equal()`, `random_base32()`, `parse_uri()` |

---

## Task Allocation
| Task | Owner |
|---|---|
| Task 1 – Project setup and setup video | Maad Ashraf, Ali Hassan |
| Task 2 – Test notes (ECP, BVA) and unit tests for own functions in all 3 modules | Maad Ashraf, Ali Hassan |
| Task 3 – Excel test cases with CSV test data | Maad Ashraf, Ali Hassan |
| Task 4 – Configuration (parallel execution, suites, groups, order) | Maad Ashraf, Ali Hassan |

## Tools and Frameworks
| Tool | Purpose |
|---|---|
| Python 3.12 | Programming language |
| pytest | Unit testing framework |
| pytest-xdist | Running tests in parallel |
| pytest-order | Setting the execution order of tests |
| CSV files | External test data for data-driven tests |
| Git / GitHub | Version control and collaboration |
| VS Code | Development environment |

