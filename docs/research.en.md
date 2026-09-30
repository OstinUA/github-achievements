# Research: GitHub profile achievements

[English catalogue](../catalog/english.md) · [Исследование на русском](research.ru.md)

Checked **30 September 2026**. The documented set contains **14 achievement types**: 7 earnable, 2 retired, 2 disabled experiments and 3 internal awards. Seven separate entries cover profile highlights. Tier artwork, skin tones and historical aliases do not increase these counts.

## Scope and method

GitHub does not publish a complete eligibility specification. Its [2022 announcement](https://github.blog/news-insights/product-news/introducing-achievements-recognizing-the-many-stages-of-a-developers-coding-journey/) encourages discovery through awarded profile cards. This catalogue therefore distinguishes official status announcements, observed awarded events and community observations.

The supplied repository and every translation, GitHub Docs, GitHub blog and changelog, staff announcements, live profile cards and the [community archive](https://github.com/Schweinepriester/github-profile-achievements) were checked. No additional substantiated achievement types were found. This is coverage of public evidence, not a claim to know every undisclosed internal experiment. A third-party name or image alone is insufficient evidence of an obtainable award.

<a id="proxima"></a>
## The two unusual badges on JakubOleksy’s profile

His [public profile](https://github.com/JakubOleksy) identifies GitHub as his employer. The awarded cards show:

| Award | Card label | Recorded event | Awarded at, UTC |
| --- | --- | --- | --- |
| [Proxima Pioneer](https://github.com/JakubOleksy?achievement=proxima-pioneer&tab=achievements) | M0 Participant | Contributed to the Proxima proof of concept | 2023-06-01 17:34:35 |
| [Proxima Staffshipper](https://github.com/JakubOleksy?achievement=proxima-staffshipper&tab=achievements) | M8 Participant | Shipped a Proxima Staffship instance | 2024-08-21 22:28:27 |
| [Proxima Staffuser](https://github.com/timrogers?achievement=proxima-staffuser&tab=achievements) | When your team is on Proxima | Team onboarded to Proxima; example from @timrogers | 2023-08-16 18:28:07 |

These support the inference that the awards recognize internal Proxima development and adoption by GitHub staff. There is no published public earning procedure. The public profiles and milestone events establish the internal context; they do not reveal the full internal award policy or every M0/M8 task. **They are not demonstrably retired:** they remain visible, and no confirmed end of internal awarding was found. Ordinary public repository activity is not a documented path to them.

GitHub’s [profile reference](https://docs.github.com/en/account-and-profile/reference/profile-reference#earning-achievements) explains that event links become inaccessible to viewers without access to the relevant repository or organization. This is a visibility restriction, not evidence that an award or event was deleted.

The Staffshipper screenshot displays 22 August 2024; the live card returns 21 August in UTC. A different viewer time zone is consistent with that difference, but the original screenshot’s time zone is unknown. A recipient’s award date is not the badge’s public release date.

The supplied [Pioneer](../assets/evidence/jakub-proxima-pioneer.png) and [Staffshipper](../assets/evidence/jakub-proxima-staffshipper.png) screenshots are preserved unchanged. Exact event strings, detail URLs and timestamps are in `proxima_evidence` in [the data file](../data/achievements.json). Reading the public detail fragments required `Accept: text/fragment+html`; a normal request returned HTTP 406.

The [GitHub engineering article about Enterprise Cloud data residency](https://github.blog/engineering/engineering-principles/github-enterprise-cloud-with-data-residency/) provides related infrastructure context, but does not name Proxima or define these awards. It is not sufficient by itself to establish a specific product-to-badge relationship. Closed project documentation was not accessible.

## Retired awards

**Arctic Code Vault Contributor** recognizes contributions to qualifying repositories in the **2 February 2020** snapshot. GitHub [documented the repository selection criteria](https://github.blog/open-source/maintainers/the-arctic-code-vault-starts-production-and-your-open-source-projects-are-being-archived/): recent activity after the November 2019 announcement; or at least one star with activity during the preceding year; or at least 250 stars regardless of recent activity. These are snapshot inclusion criteria, not a present-day earning procedure. The [Archive Program](https://archiveprogram.github.com/) remains a preservation initiative, but new commits do not enter that old snapshot.

**Mars 2020 Contributor** recognizes commits in specific project versions used by NASA/JPL Ingenuity. GitHub [explicitly says that the event ended](https://docs.github.com/en/account-and-profile/reference/profile-reference#list-of-qualifying-repositories-for-mars-2020-helicopter-contributor-achievement). Contributing to modern Linux or Python does not recreate eligibility for those historical versions. The complete repository/version/tag list is preserved in the [historical appendix](mars-2020-repositories.md).

## Disabled experiments

**Heart On Your Sleeve** is associated in community observations with heart reactions. **Open Sourcerer** is associated with merged PRs across public repositories. Default, bronze, silver and gold artwork exists for both. Image availability proves a design exists, not public availability or an eligibility threshold.

On 27 March 2026, GitHub staff [confirmed that a temporary reactivation was an error](https://github.com/orgs/community/discussions/190746). These experiments were not meant to be enabled broadly and were removed again. No public release date was found. The catalogue labels them experimental/disabled, without promising a release or asserting permanent cancellation.

The [community archive](https://github.com/Schweinepriester/github-profile-achievements) reports provisional bronze/silver thresholds of 16/128 heart reactions and bronze/silver/gold thresholds of 8/16/64 for Open Sourcerer. That source does not establish the base thresholds or Heart On Your Sleeve’s gold threshold. Open Sourcerer’s counting method is also unconfirmed: PR count and distinct repository count are not interchangeable. These figures remain explicitly separated from the earnable tier table.

## Earnable awards and counting

| Award | Default → bronze → silver → gold | Activity |
| --- | --- | --- |
| Starstruck | 16 → 128 → 512 → 4096 | Stars of a created repository |
| Pull Shark | 2 → 16 → 128 → 1024 | Authored PRs that were merged |
| Pair Extraordinaire | 1 → 10 → 24 → 48 | Merged PRs with coauthored commits |
| Galaxy Brain | 2 → 8 → 16 → 32 | Accepted Discussion answers |

These are observed thresholds. Examples include [torvalds](https://github.com/torvalds?achievement=starstruck&tab=achievements), [ljharb’s Pull Shark](https://github.com/ljharb?achievement=pull-shark&tab=achievements) and [Galaxy Brain](https://github.com/ljharb?achievement=galaxy-brain&tab=achievements), and [Rongronggg9](https://github.com/Rongronggg9?achievement=pair-extraordinaire&tab=achievements). Correct attribution matters for coauthorship; see [GitHub’s commit trailer documentation](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors).

Quickdraw records closing an issue or PR within five minutes. YOLO is associated with merging one’s own PR without review. Public Sponsor records public support through [GitHub Sponsors](https://github.com/sponsors). No bronze/silver/gold sequence is confirmed for those three. All exceptions, bot behavior, historical reprocessing and exact award timing are not officially specified; the minimum observed condition does not guarantee immediate display.

Galaxy Brain is not globally retired. The [6 February 2024 announcement](https://github.com/orgs/community/discussions/106536) disables achievements in GitHub’s own `github.com/orgs/community`; it does not disable every repository’s Discussions.

x2/x3/x4 mean bronze/silver/gold, not arithmetic multiplication of the base requirement. Their label colors are `#F9BFA7`, `#E1E4E4` and `#FAE57E`. Starstruck and Quickdraw skin-tone images alter appearance, not the achievement count. [Appearance settings](https://github.com/settings/appearance).

## Historical names and adjacent labels

GitHub [introduced the Achievements section on 19 April 2021](https://github.blog/news-insights/company-news/open-source-goes-to-mars/) and [expanded it on 9 June 2022](https://github.blog/news-insights/product-news/introducing-achievements-recognizing-the-many-stages-of-a-developers-coding-journey/). The original artwork and aliases are preserved:

- **GitHub Sponsor** became **Public Sponsor**.
- **Mars 2020 Helicopter Contributor** / **Mars 2020 Helicopter Mission** correspond to **Mars 2020 Contributor**.
- **Arctic Code Vault Contributor** retained its name with revised artwork; “2020 GitHub Archive Program” identifies the same event.

Award histories can refer to activity before the badge system existed. An old event date does not establish when a modern badge design launched.

[GitHub Docs](https://docs.github.com/en/account-and-profile/reference/profile-reference#displaying-badges-on-your-profile) documents Pro, Developer Program Member, Security Bug Bounty Hunter, GitHub Campus Expert and Security Advisory Credit. [GitHub Stars](https://stars.github.com/) is listed as a program distinction, not a star-count medal. The former **Discussion answered** highlight is historical: its replacement by Galaxy Brain was [reported by a user relaying a support response](https://github.com/orgs/community/discussions/31629), not announced in a new official changelog.

GitHub certifications, Hacktoberfest participation, Shields.io graphics, README pictures, organization roles, verified commits and employer fields belong to different systems. They are outside the native Achievements count. Undisclosed internal tests remain unknown.

## Current display limitations

GitHub [changed profiles to show the highest earned tier on 11 September 2026](https://github.blog/changelog/2026-09-11-profiles-now-show-your-highest-achievement-badge-tier/). The [staff update dated 23 September](https://github.com/orgs/community/discussions/203416) reports award/display delays sometimes lasting days, without a fix timeline. An absent badge therefore cannot automatically be classified as retired.

[Visibility settings](https://docs.github.com/en/account-and-profile/how-tos/contribution-settings/manage-visibility-settings-for-private-contributions-and-achievements) control public display and private contributions. A recipient may hide a badge or the entire section. Repository checks validate local files and links; the research date is not a promise that external sources will remain unchanged.
