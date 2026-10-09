"""English: the source text of the site. Every other language follows the same keys."""

T = {
    "lang": "en",
    "code": "EN",
    "locale": "en_US",
    "name": "English",
    "ui": {
        "skip": "Skip to the content",
        "menu": "Main",
        "footer_menu": "Footer",
        "language": "Language",
        "nav_howto": "How to",
        "nav_support": "Support",
        "nav_privacy": "Privacy",
        "nav_terms": "Terms",
        "to_dark": "Switch to the dark theme",
        "to_light": "Switch to the light theme",
        "rights": "&copy; 2026 Board Game Log. Developed and published by Daniel Osorio.",
        "legal": "Board Game Log is a log, not a game, and is not affiliated with or endorsed by the publishers of the games it records. Game names belong to their owners.",
        "read_more": "Read more",
        "translation_note": "",
        "updated": "Last updated: October 9, 2026",
    },
    "meta": {
        "home": ("Board Game Log: score, track and see your board game stats",
                 "An iPhone app to record who played and who won, score matches live with dice and counters, and see your stats. No account needed."),
        "howto": ("How to · Board Game Log",
                  "Step-by-step guides to add a game, record or play a match, see your stats, and share groups and games with friends."),
        "support": ("Support · Board Game Log",
                    "Answers to common questions about Board Game Log (accounts, backups, sharing games and groups, watching a match) and how to contact support."),
        "privacy": ("Privacy policy · Board Game Log",
                    "What Board Game Log stores, where, and who can see it. Your matches stay on your phone unless you sign in and share."),
        "terms": ("Terms of use · Board Game Log",
                  "The terms for using Board Game Log, and a note about the game names it shows."),
        "notfound": ("Page not found · Board Game Log", ""),
    },
    "home": {
        "h1": "Keep score of every game night.",
        "lead": "Board Game Log is an iPhone app to record who played and who won, score a match as you play, and see how everyone is doing. No account needed.",
        "status": "Coming soon to the App Store",
        "cta": "See how it works",
        "logo_alt": "The Board Game Log icon: a red hexagon with the name on a gold tile",
        "does_h": "What it does",
        "does_p": "For the games you really play, from the big box to the card game on the kitchen table.",
        "features": [
            ("Any game", "Type the name of a game and start. Or say how it is won, what to track and how turns work, and the app builds the score sheet and the stats from it."),
            ("Record in three taps", "Pick the group, add the players in table order, tap the winner. Points, time and notes can come later, or never."),
            ("Play live", "Prepare the match, then start the clock. Score as you play with +X per category, counters, dice you can roll or enter, turns, undo, and an alert when someone reaches the goal."),
            ("Your stats", "Wins and win rate, streaks, head to head, scores, dice luck, time per turn, and more once you have a few matches. Each group has its own, and a person who plays in several can be seen as one."),
            ("Friends, if you want", "Sign in to share a group, a game you made, or a match in progress. Your friends play your game in your group, and can follow a match from their own phone and even roll the dice."),
        ],
        "see_h": "See it",
        "see": [
            ("15-live-scored", "A match being scored live: each player has a card with a +X for every category.", "Scoring a match live"),
            ("07-quick-log", "The Quick log form with the players and the winner chosen.", "Logging a match you played"),
            ("18-stats", "The stats page of a game with its leaderboard.", "The leaderboard of a game"),
        ],
        "keep_h": "Yours first",
        "keep_p": "Your games and matches stay on your phone. Backups are a file you keep. Sign in only if you want to share, or keep two phones in sync. There are no ads and no tracking.",
        "keep_link": "Read the privacy policy",
        "names_h": "A log, not a game",
        "names_p1": "Board Game Log is not a game and does not replace one. It is a log: you keep the records of the games you play and get statistics from them. It has no rules, art or pieces of any game. Please buy and play the official games.",
        "names_p2": "The names of the games you add are trademarks or the property of their respective owners, publishers and authors. They are used only to identify the games you play. Board Game Log is an independent app and is not affiliated with, sponsored by or endorsed by any of them.",
        "names_link": "Read the terms",
    },
    "howto": {
        "h1": "How to use Board Game Log",
        "lead": "Short guides for the things people do most. Tap a title to open it.",
        "note": "The screenshots use made-up games and players.",
        "good": "Good to know.",
        "guides": [
            {
                "id": "add-a-game", "title": "Add a game",
                "intro": "Three ways, from the quickest to the most detailed.",
                "steps": [
                    "In the <strong>Games</strong> tab, tap <strong>Add game</strong>.",
                    "Choose <strong>Just a name</strong> to type the game's name and save. You can add more later.",
                    "Or choose <strong>From an archetype</strong> for a starting shape, such as a score sheet, a team game or a co-op game. Pick one, give it a name and adjust what it tracks.",
                    "Or choose <strong>From scratch</strong> to say how the game is won and what to track: scores by category, counters, dice, turns, teams or hidden roles.",
                    "Tap <strong>Save</strong>. The game appears on the Games tab.",
                ],
                "shots": [("02-add-game", "The Add game screen with its ways to start.", "Add game"),
                          ("06-game-page", "A game's page with its Quick log and Record a match buttons.", "The page of a game")],
                "tip": "You can change a game later with <strong>Edit game</strong>. Matches you already recorded keep what they have.",
            },
            {
                "id": "quick-log", "title": "Quick log: a match you already played",
                "intro": "Three taps, then the details if you want them. The sections fold: Players and Result start open, the rest start closed.",
                "steps": [
                    "Open the game and tap <strong>Quick log</strong>.",
                    "In <strong>Players</strong>, pick the group (or let the app make one) and add the players in table order.",
                    "In <strong>Result</strong>, tap the winner, or the result that fits the game, and save.",
                    "Optional: open <strong>Colors</strong> to give each player a color, and <strong>When</strong> to set the date and the start and end time.",
                    "Optional: tap <strong>Add details</strong> for points, counters, awards, how it ended and notes. They are grouped (Players, Result, Time, Game, Rules, Notes) and each group folds. The end of the match is a date and time; the time played is worked out from it.",
                ],
                "shots": [("07-quick-log", "Quick log with the players listed and the winner chosen.", "Players and result"),
                          ("08-quick-log-colors", "The Colors section open, with a color menu for each player.", "A color for each player"),
                          ("10-add-details", "Add details with one card per player.", "Add details")],
                "tip": "<strong>Play again</strong> on a finished match starts a new one with the same group and players.",
            },
            {
                "id": "play-live", "title": "Record a match and play it live",
                "intro": "For when you want the score, the counters, the dice and the clock while the game is going. You can prepare the match first and start the clock later.",
                "steps": [
                    "Open the game and tap <strong>Record a match</strong>. Choose the group, the players, when it starts (leave it, or pick an earlier time if the game already began) and, if you like, their colors, the game's options and a photo. For a game with dice or rounds, <strong>Track</strong> lets you switch them on or off for this match. The match is saved as <strong>Ready to start</strong>.",
                    "When you begin to play, tap <strong>Start match</strong>. The clock starts then. A match that is ready waits on the game page and on the Games tab until you open it.",
                    "Score as you go: a <strong>+X</strong> for each category, counters with <strong>−</strong> and <strong>+</strong>, and one button for each condition the game has.",
                    "For games with dice, tap <strong>Roll</strong> to roll on screen, or <strong>Enter roll</strong> to type what the real dice showed.",
                    "Use <strong>End round</strong> between rounds, <strong>Undo</strong> to take back your last action and <strong>Pause</strong> to stop the clock.",
                    "When someone reaches the goal an alert asks <strong>Finish match</strong> or <strong>Keep playing</strong>. Finish suggests the result from what was played; change it if it is wrong, choose the date and time it ended if it was earlier, and save.",
                ],
                "shots": [("12-record-a-match", "The Record a match screen with the players, when it starts and the colors.", "Record a match"),
                          ("13-ready-to-start", "A match that is ready to start, with the Start match button.", "Ready to start"),
                          ("15-live-scored", "A match in progress with points entered.", "Playing live"),
                          ("16-finish", "The Finish screen with the suggested winner and the end time.", "Finish")],
                "tip": "A match in progress survives a closed app. Resume it from the card at the top of the Games tab, or <strong>Abandon</strong> it to keep it out of your stats.",
            },
            {
                "id": "stats", "title": "See your stats",
                "intro": "Every game has its own stats, for one group or for everyone you play with.",
                "steps": [
                    "Open the game and tap <strong>Stats</strong>.",
                    "The <strong>Leaderboard</strong> shows wins, win rate and matches played. Tap a player for streaks, last matches and head to head.",
                    "Use <strong>Filters</strong> to look at one group or a range of dates.",
                    "More pages appear as you add matches: scores, categories, counters, dice luck, time per turn and more.",
                ],
                "shots": [("18-stats", "The Stats page of a game with its leaderboard.", "Stats of a game")],
                "tip": "A match missing something a page needs? <strong>Add details to past matches</strong> in the Stats tab walks you through them.",
            },
            {
                "id": "sign-in", "title": "Sign in (optional)",
                "intro": "You do not need an account to keep your games. Sign in only to share with friends or to keep your games equal on every phone you use.",
                "steps": [
                    "Open the <strong>Settings</strong> tab and choose <strong>Account</strong>.",
                    "Sign in with Apple or with Google.",
                    "To keep your games on every phone you use, open <strong>Cloud</strong> and choose <strong>Upload my games</strong>. The app makes a backup first, uploads, checks both sides match and only then turns the sync on.",
                ],
                "shots": [('20-cloud-off', 'The Cloud screen before signing in.', 'Before signing in'), ('22-cloud-on', 'The Cloud screen with the sync on.', 'Sync on')],
                "tip": "Everything else works without an account. Sharing a group, a game or a match in progress needs one.",
            },
            {
                "id": "share-a-group", "title": "Share a group with friends",
                "intro": "A group is the people you play with. Friends join with a code, a QR or a link.",
                "steps": [
                    "Open the <strong>Players</strong> tab and choose the group (or <strong>New group</strong>).",
                    "Tap <strong>Invite people</strong>. You will see a code, a QR and a link; copy the code or show the QR.",
                    "Your friend signs in, opens <strong>Join a group</strong> and types the code, scans the QR or opens the link.",
                    "When they join, the app asks <strong>which player are you</strong>, so their matches and stats show as <em>You</em>.",
                ],
                "shots": [('23-groups', 'The Players tab with the groups listed first.', 'Your groups'), ('25-invite', "A group's invite with its code and QR.", 'Invite people'), ('26-join-code', 'Typing a code to join a group.', 'Join with a code'), ('27-which-player', 'Choosing which player you are.', 'Which player are you?')],
                "tip": "If a code ends up in the wrong hands, make a new one and the old one stops working.",
            },
            {
                "id": "follow-live", "title": "Let friends follow a match live",
                "intro": "Friends see the score from their own phone while you play, and can roll the dice if you let them.",
                "steps": [
                    "Start a match as usual (see <a href=\"#play-live\">Record a match and play it live</a>).",
                    "In the match, choose <strong>Share live</strong> and then <strong>Start sharing</strong>. Copy the link or show the QR code.",
                    "Friends who have an account open the link and watch. They cannot change your score. Choose <strong>Stop sharing</strong> whenever you like.",
                ],
                "shots": [('28-share-live-start', 'Starting to share a match live.', 'Share live'), ('29-share-live-qr', 'The link and QR of a match in progress.', 'Link and QR'), ('30-watching', 'A friend watching the score from their phone.', 'A friend watching')],
                "tip": "Only a match in progress can be shared, and sharing stops by itself 24 hours after the match ends.",
            },
            {
                "id": "same-person", "title": "The same person in two groups",
                "intro": "If a friend plays in two of your groups, you do not have to merge them. Link them instead.",
                "steps": [
                    "Open the <strong>Players</strong> tab and open the person's page.",
                    "Choose <strong>Link to a person in another group</strong> and pick the other profile.",
                    "The person's page now offers <strong>This group</strong> and <strong>All groups</strong>. Each group keeps its own stats.",
                    "To undo it, choose <strong>Unlink</strong>. Nothing is lost.",
                ],
                "shots": [('38-same-person-suggestion', 'The app suggesting that two people are the same.', 'A suggestion'), ('39-link-people', 'Linking a person to a profile in another group.', 'Link people')],
                "tip": "<strong>Merge</strong> is only for a duplicate inside one group, for example the same friend typed twice.",
            },
            {
                "id": "share-a-game", "title": "Share a game, duplicate it or propose a change",
                "intro": "A game you made can be shared with your groups, so their members can play it with the same rules, in matches of that group.",
                "steps": [
                    "Open the game, tap the <strong>…</strong> menu and choose <strong>Share with group…</strong>, then pick the group. Only you can share it, with as many groups as you like. Members can see the game and use it in matches of that group, but cannot change it or share it.",
                    "A member who wants their own version taps <strong>Duplicate</strong> to get a copy they can edit and use with their own groups. They can have one copy of a game at a time, a copy cannot be copied again, and it says whose game it is based on.",
                    "A member who wants the owner to change the rules opens <strong>View rules</strong> and taps <strong>Propose changes</strong>, edits and sends it with a message.",
                    "The owner sees the proposals on the game, reads what changes and chooses <strong>Accept</strong> or <strong>Reject</strong>.",
                ],
                "shots": [('31-shared-in-games', 'A shared game in the Games list.', 'A shared game'), ('32-shared-game-page', 'The page of a game shared by someone else.', 'Its page'), ('34-copy-page', 'The copy of a game, with whose game it is based on.', 'A copy'), ('35-share-with-group', 'Choosing the group to share a game with.', 'Share with a group'), ('37-proposal-review', 'The owner reviewing a proposed change.', 'Review a proposal')],
                "tip": "You cannot take a group back once a game is shared with it. If the owner leaves the group, the game stays there as it was, but nobody can share it any further.",
            },
        ],
    },
    "support": {
        "h1": "Support",
        "lead": "Something not working, or an idea? Write to <a href=\"mailto:support@boardgamelog.app\">support@boardgamelog.app</a>.",
        "h2": "Common questions",
        "faq": [
            ("Do I need an account?", "No. Everything works on your phone without one. An account is only needed to share a group, a game or a live match, and to keep two phones in sync."),
            ("How do I back up my matches?", "Settings &rarr; Data Backup &rarr; Export. You get a file you can keep anywhere and restore later."),
            ("I updated from version 1: where are my matches?", "They are on the Games tab, as a game like the others. The first time you open the new version, your matches are brought over and a backup is made first."),
            ("Can my friends use a game I made?", "Yes. Sign in and, on the game's page, open the <strong>…</strong> menu and choose <strong>Share with group…</strong>. The members of that group play the game in matches of that group. Only you can share it, and with as many groups as you like."),
            ("Why can't I use a friend's game with another group?", "A game that a friend shared with a group is played in that group. To use it somewhere else, make your own copy (the <strong>…</strong> menu, <strong>Duplicate</strong>) or ask your friend to share it with that group. You can have one copy of a game at a time, and a copy can't be copied again. The copy says whose game it is based on, and you can still propose changes to the original."),
            ("Why can't I change a match?", "Only the person who recorded a match can change it. For 7 days everything can change; after that you can only fill in what is missing."),
            ("How do I watch a friend's match?", "Open the link or scan the QR code they show you from the Live screen. You need to be signed in, and they need to have shared the match with you or turned on \"Anyone with the link\"."),
            ("How do I delete my account and data?", "The account button on the Games tab &rarr; Delete Account. See the <a href=\"{privacy}\">privacy policy</a> for what that removes."),
            ("Is the app available in my language?", "The app is in English for now. This website is in English, Spanish and French."),
        ],
        "see_also": "See also <a href=\"{howto}\">the how-to guides</a>.",
    },
    "notfound": {
        "h1": "This page is not here",
        "lead": "The address may have changed or has a typo. Go back to the home page, or read the how-to guides.",
        "home": "Home",
        "howto": "How to",
    },
}

PRIVACY_H1 = "Privacy policy"
PRIVACY_LEAD = "Board Game Log keeps your matches on your phone. It collects data only if you choose to sign in and turn on cloud sync, and it never uses it for advertising or tracking."
PRIVACY = """
<h2>Without an account</h2>
<p>Your games, players, matches and photos are stored on your phone only; none of them is ever sent anywhere. Backups are a file you create and keep.</p>
<p>The app does ask Google Firebase for a few on/off settings that say which features it offers (Firebase Remote Config). To answer, Firebase uses an installation identifier that Google gives to the app and basic information about the app and the phone, such as the app version, the system version and the language. It does not include your name or anything you recorded.</p>

<h2>With an account</h2>
<p>You can sign in with Apple or Google (optional) and turn on cloud sync. Then the app stores this in Google Firebase, in the account you signed in with:</p>
<div class="table-wrap"><table>
<tr><th>What</th><th>Why</th></tr>
<tr><td>Your email address, name and a user id from Apple or Google</td><td>To sign you in and show your name to the people you share with.</td></tr>
<tr><td>Your games and matches (players' names, scores, results, notes, events such as rolls)</td><td>To keep your phones in sync and to share with your groups.</td></tr>
<tr><td>Photos you add to a match (board, start and end photos) and a game's icon</td><td>To show them on your other phones and to the people in the group.</td></tr>
<tr><td>A small marker that says your account used an earlier version of the app, and the feature settings we may turn on for your account (they contain no personal data)</td><td>So that what you already had keeps working on a new phone, and to let us try features with a few people.</td></tr>
<tr><td>Groups you make or join: name, members, and who each player is</td><td>To share games and matches with the group.</td></tr>
</table></div>
<p>The names of the players in your matches are typed by you; they are not required to be real names, and people who are not users of the app are never contacted.</p>

<h2>Who can see it</h2>
<ul>
<li>Only you, unless you share.</li>
<li><strong>Groups:</strong> the people you invite with a code see the group's matches, players and games shared with it.</li>
<li><strong>Live matches:</strong> when you share a match live, the members of the group and the players linked to an account can follow it; if you turn on "Anyone with the link", so can anyone who has the link and an account. The shared copy is deleted 24 hours after the match ends, or when you stop sharing.</li>
</ul>

<h2>What we do not do</h2>
<ul>
<li>No advertising, no tracking across apps or websites, no analytics, no selling or renting of data.</li>
<li>No location, contacts or microphone. The camera is used only when you scan a QR code or take a photo of your board.</li>
</ul>

<h2>Deleting your data</h2>
<p>In the app, tap <strong>the account button on the Games tab &rarr; Delete Account</strong>. It removes your account. Your matches are deleted from the cloud without their notes and photos, and your games stay for the groups that use them without an owner. The small marker and the feature settings stay tied to an anonymous id; write to support if you want them removed. You can also delete a match, a game or a group at any time. Data on your phone is deleted when you delete the app.</p>

<h2>Children</h2>
<p>The app is not directed to children under 13 and does not knowingly collect data from them.</p>

<h2>Service providers</h2>
<p>Sign-in, storage and feature settings are provided by Apple, Google and Google Firebase, which process data for us under their own terms and privacy policies.</p>

<h2>Contact</h2>
<p>Questions or a request about your data: <a href="mailto:support@boardgamelog.app">support@boardgamelog.app</a>.</p>
<p>Board Game Log is developed and published by Daniel Osorio.</p>
<p>If we change this policy, the new version will be here with its date.</p>
"""

TERMS_H1 = "Terms of use"
TERMS_LEAD = "Board Game Log is a free app to keep track of the board games you play. By using it you agree to these terms."
TERMS = """
<h2>Using the app</h2>
<ul>
<li>You decide what to record. Use the app for your own games and for the groups you invite; do not record or share anything that is unlawful or that infringes the rights of others.</li>
<li>You are responsible for the account you sign in with and for the people you invite to a group.</li>
<li>The app is provided "as is", without warranties. Keep your own backups (Settings &rarr; Data Backup); we are not liable for lost data.</li>
</ul>

<h2>Your content</h2>
<p>The matches, notes, photos and names you add are yours. You allow the app to store them and to show them to the people you share them with, as described in the <a href="{privacy}">privacy policy</a>.</p>

<h2>Shared games</h2>
<p>When you share a game you made with a group, the members of that group can use it in their matches with that group. You stay its owner and are the only one who can share it. A member can make one copy for themselves; a copy cannot be copied again and says whose game it is based on. Do not share a game that infringes the rights of others.</p>

<h2 id="not-a-game">What the app is</h2>
<p>Board Game Log is not a game and does not replace one. It is a log: it keeps the records of the games you play (who played, who won, scores, time) and turns them into statistics. It does not contain the rules, art or pieces of any game, and it does not let you play them. Please buy and play the official games.</p>

<h2 id="game-names">Game names and trademarks</h2>
<p>The names of the games, expansions and scenarios shown in the app (for example the games you add and any built-in game) are trademarks or the property of their respective owners, publishers and authors. They are used only to identify the games, so you can record the ones you play.</p>
<p>Board Game Log is an independent app. It is <strong>not affiliated with, sponsored by or endorsed by</strong> any of those owners, and showing a name does not mean any such relationship. The rules summaries and numbers in the app (for example victory-point targets) are brief factual references for scorekeeping and do not replace the official rules. Please buy and play the official games.</p>
<p>If you own a name or work shown in the app and want it changed or removed, write to <a href="mailto:support@boardgamelog.app">support@boardgamelog.app</a> and it will be handled promptly.</p>

<h2>Changes</h2>
<p>We may update these terms and the app. The current version is always on this page with its date.</p>

<h2>Contact</h2>
<p><a href="mailto:support@boardgamelog.app">support@boardgamelog.app</a>. Board Game Log is developed and published by Daniel Osorio.</p>
"""
