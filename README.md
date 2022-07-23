# sbermarket-api

<div align="center">

[![Build status](https://github.com/nov1kov/sbermarket-api/workflows/build/badge.svg?branch=master&event=push)](https://github.com/nov1kov/sbermarket-api/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/sbermarket-api.svg)](https://pypi.org/project/sbermarket-api/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/nov1kov/sbermarket-api/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/nov1kov/sbermarket-api/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/nov1kov/sbermarket-api/releases)
[![License](https://img.shields.io/github/license/nov1kov/sbermarket-api)](https://github.com/nov1kov/sbermarket-api/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

Not official python client for product market Sbermarket.

</div>

## Задачи что преследовал:

1. Поиск самого дешевого товара среди магазинов вокруг.
2. Отлеживание в целом цен на продукты.
3. Сделать алерт на дешевые товары.
4. Вести статистику на цены товаров.

## Что внутри?

Токен получается только из статического js скрипта. Где содержится JSON вида:
```json
{"api-version":"3.0","client-token":"TOKEN","is-storefront-ssr":l.sk}
```
Скорее всего он у всех одинаковый.

## Installation

```bash
pip install -U sbermarket-api
```

or install with `Poetry`

```bash
poetry add sbermarket-api
```

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/nov1kov/sbermarket-api/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

You can update it in [`release-drafter.yml`](https://github.com/nov1kov/sbermarket-api/blob/master/.github/release-drafter.yml).

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.

## 🛡 License

[![License](https://img.shields.io/github/license/nov1kov/sbermarket-api)](https://github.com/nov1kov/sbermarket-api/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/nov1kov/sbermarket-api/blob/master/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{sbermarket-api,
  author = {Nov1kov},
  title = {Not official python client for product market sbermarket API.},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/nov1kov/sbermarket-api}}
}
```

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)

## Alternatives

1. Sbermarket client on TypeScript https://github.com/x0rium/sbermarket-api
