<div align="center">

# 🏆 GitHub Achievement Atlas

**A catalogue of the badges you can earn, the ones you missed, and the ones GitHub keeps internal.**

<img src="assets/badges/starstruck-default.png" width="86" alt="Starstruck">
<img src="assets/badges/pull-shark-default.png" width="86" alt="Pull Shark">
<img src="assets/badges/proxima-pioneer-default.png" width="86" alt="Proxima Pioneer">
<img src="assets/badges/proxima-staffshipper-default.png" width="86" alt="Proxima Staffshipper">
<img src="assets/badges/proxima-staffuser-default.png" width="86" alt="Proxima Staffuser">

[**Explore in English →**](catalog/english.md) · [**Открыть на русском →**](catalog/russian.md) · [**Українською →**](catalog/ukrainian.md)

**14 documented achievements · 7 profile highlights · 25 languages**

Last researched: **30 September 2026**

</div>

---

## Choose a collection

| Collection | Count | What it covers |
| --- | ---: | --- |
| 🟢 [Earnable](catalog/english.md#active) | 7 | Contributions, collaboration, Discussions, stars and sponsorship |
| 🕰️ [Retired](catalog/english.md#retired) | 2 | Arctic Code Vault Contributor and Mars 2020 Contributor |
| 🧪 [Experimental / disabled](catalog/english.md#experimental) | 2 | Heart On Your Sleeve and Open Sourcerer |
| 🔒 [Internal GitHub awards](catalog/english.md#internal) | 3 | Proxima Pioneer, Proxima Staffshipper and Proxima Staffuser |
| ✨ [Profile highlights](catalog/english.md#highlights) | 7 | Program/account labels, including the former Discussion answered highlight |

The catalogue includes tier artwork, skin-tone variants, historical names and designs, examples of awarded badges, and a source trail. Original names remain in English so they match the GitHub interface.

> **Scope:** these are publicly documented GitHub-native profile badges. GitHub has no complete public eligibility specification, so unknown internal experiments cannot be enumerated with certainty. Historical names, tier multipliers and visual variants are not counted as separate achievements. See the [research and its limits](docs/research.en.md).

## What changed in this edition

- **Proxima:** the two unusual badges on [@JakubOleksy’s profile](https://github.com/JakubOleksy?tab=achievements) are awards for internal work: an M0 proof of concept and an M8 Staffship instance. A third badge, **Proxima Staffuser**, records team onboarding. [Evidence and dates](docs/research.en.md#proxima).
- **Disabled experiments:** GitHub confirmed that the March 2026 return of **Heart On Your Sleeve** and **Open Sourcerer** was accidental and reversed it. [Staff response](https://github.com/orgs/community/discussions/190746).
- **Current display behavior:** profiles show the highest earned tier since September 2026. [GitHub changelog](https://github.blog/changelog/2026-09-11-profiles-now-show-your-highest-achievement-badge-tier/).
- **Award delays:** the latest staff update, dated 23 September 2026, reports delays of several days for some users without a fix timeline. A missing badge does not establish retirement. [Incident discussion](https://github.com/orgs/community/discussions/203416).
- **Historical archive:** the original 2021 designs and former names are preserved separately. [Artwork and aliases](catalog/english.md#history).

## Read in your language

| | | | | |
| --- | --- | --- | --- | --- |
| [English](catalog/english.md) | [Русский](catalog/russian.md) | [Українська](catalog/ukrainian.md) | [简体中文](catalog/chinese.md) | [正體中文](catalog/traditional-chinese.md) |
| [Nederlands](catalog/dutch.md) | [Français](catalog/french.md) | [Deutsch](catalog/german.md) | [Ελληνικά](catalog/greek.md) | [हिन्दी](catalog/hindi.md) |
| [Bahasa Indonesia](catalog/indonesian.md) | [Italiano](catalog/italian.md) | [ಕನ್ನಡ](catalog/kannada.md) | [한국어](catalog/korean.md) | [ଓଡ଼ିଆ](catalog/odia.md) |
| [Naijá](catalog/pidgin.md) | [Polski](catalog/polish.md) | [Português](catalog/portuguese.md) | [Español](catalog/spanish.md) | [Kiswahili](catalog/swahili.md) |
| [தமிழ்](catalog/tamil.md) | [తెలుగు](catalog/telugu.md) | [Türkçe](catalog/turkish.md) | [Tiếng Việt](catalog/vietnamese.md) | [isiZulu](catalog/zulu.md) |

## Repository map

```text
README.md                 Entry point and language navigation
catalog/                  Complete catalogue in each of 25 languages
data/achievements.json    Shared records, tiers, status, evidence and sources
i18n/                     Translated descriptions and interface text
assets/badges/            Default badges and tier artwork
assets/variants/          Skin-tone variants
assets/legacy/            Historical artwork
assets/evidence/          Supplied Proxima screenshots
assets/manifest.json      Image origins and retrieval dates
docs/                     Research in English and Russian; historical appendix
scripts/                  Build and consistency checks (Python standard library)
lang/                     Compatibility links for the previous translations
CONTRIBUTING.md           How to maintain the catalogue and its translations
LICENSE                   Original CC0 license for repository text
```

## Keep it current

Edit the records in `data/` and the translations in `i18n/`, then rebuild:

```bash
python scripts/build_catalog.py
python scripts/check_catalog.py
```

No dependencies are required. All translated catalogues share the same counts, section order, thresholds, images and sources. The checker detects incomplete translations, inconsistent generated pages, broken local links and missing artwork. See [contributing](CONTRIBUTING.md).

The starting text and translations come from [gomzyakov/github-achievements](https://github.com/gomzyakov/github-achievements). Additional observations and historical artwork are credited to [Schweinepriester/github-profile-achievements](https://github.com/Schweinepriester/github-profile-achievements). GitHub artwork retains its original ownership; see [asset provenance](assets/README.md).
