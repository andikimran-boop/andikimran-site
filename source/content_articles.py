# Weekly articles. Newest FIRST. Each entry becomes /guides/<slug> and appears on /guides under "Latest articles".
# Add one dict per article — see ARTICLES.md for the weekly routine and the rules.
#
# dict(
#     slug="how-much-cash-to-upgrade-from-4-room",        # URL: /guides/<slug>
#     published="2026-12-02",                              # YYYY-MM-DD
#     title="How Much Cash Do You Need to Upgrade From a 4-Room HDB?",   # <title>, ~50-60 chars
#     desc="One or two sentences for Google, 140-160 chars.",
#     h1="How much cash do you need to upgrade from a 4-room HDB?",
#     crumb="Cash to upgrade",                             # short breadcrumb label
#     intro="One-sentence lede under the headline.",
#     toc=[("answer", "Short answer"), ("section-id", "Section label")],
#     body="""<div class="answer"><b>Short answer</b>...</div> <h2 id="section-id">...</h2><p>...</p>""",
#     faq=[("Question?", "Answer.")],
#     related=[("g-upgrade", "Upgrading after MOP"), ("calculator", "Loan calculator")],
# )

ARTICLES = [
    dict(
        slug="bigger-share-hdb-flat-divorce",
        published="2026-11-25",
        title="Should I Fight for a Bigger Share of Our HDB Flat in a Divorce?",
        desc="A friend wanted 70% of the matrimonial HDB flat. What I told him: how the split is decided, the cost of a long fight, and planning the next home.",
        h1="Should I fight for a bigger share of our HDB flat in a divorce?",
        crumb="Bigger share in a divorce",
        intro="A friend in the middle of a divorce wanted 70% of the matrimonial flat. Here's what I told him.",
        toc=[("answer", "Short answer"), ("why", "Why he wanted 70%"), ("snake", "The snake and the saw"),
             ("instead", "What I suggested instead"), ("next-hdb", "Planning his next HDB"), ("help", "If you're going through this")],
        body="""<div class="answer" id="answer"><b>Short answer</b>You can, but count what the fight costs first. The court doesn't hand anyone 70% by default. It looks at what each of you contributed, in money and in caring for the family, and at the children's needs. In my experience, couples who agree on a fair split and sell together move on sooner, with more of their money and their peace intact.</div>
  <p>A friend called me recently. He and his wife are divorcing, the case is still going, and they're still living under the same roof in their HDB flat. He told me he wanted 70% of the matrimonial home. He felt deeply wronged, and he wanted to fight.</p>
  <p>I'm not a lawyer, and I told him so. But I've seen how property and divorce play out, so I told him what I'd tell anyone in his spot. I've kept him anonymous here, because I know many people are quietly going through the same thing.</p>
  <h2 id="why">Why he wanted 70%</h2>
  <p>He was hurt, and the flat felt like the one thing he could still win. That's very human. When someone feels betrayed, the home stops being a home and becomes a scoreboard.</p>
  <p>But the court doesn't divide matrimonial assets to decide who was hurt more. It looks at what each person put in: money towards the flat, and indirect contributions such as looking after the children and running the household. It also weighs things like the children's needs. Your lawyer can tell you what's realistic for your case.</p>
  <h2 id="snake">The snake and the saw</h2>
  <p>I told him an old story. A snake slid into a carpenter's workshop at night and brushed against a saw. It got a small cut. Angry, it bit the saw, and cut its own mouth. Now furious, it wrapped itself around the saw and squeezed with all its strength to crush it. By morning the saw was fine. The snake was dead.</p>
  <p>Sometimes the fight hurts you more than the other person. Every extra month in court means more legal fees, more stress at home and more time you can't plan your life. Some divorces I've seen dragged on for two to three years. The saw doesn't feel anything. You do.</p>
  <h2 id="instead">What I suggested instead</h2>
  <ul>
    <li><b>Try to agree on 50/50 if you can.</b> A fair split you both accept now beats a bigger number you may or may not win years later, after the fees.</li>
    <li><b>Sell quickly once you agree.</b> They're still living together, and every day under the same roof hurts. A quick, clean sale lets both of them go their separate ways.</li>
    <li><b>Plan your next home on the conservative number.</b> Don't build your plans around the share you hope for. If the outcome is better, that's a bonus.</li>
  </ul>
  <h2 id="next-hdb">Planning his next HDB</h2>
  <p>He wants to buy another HDB flat afterwards. Which flat and scheme he can buy depends on HDB's eligibility rules, including who gets care and control of the children and his age. For him, care and control isn't decided yet, so we're keeping his options open.</p>
  <p>One more thing people forget: when the flat is sold, the CPF each of you used goes back to your own CPF account first, with accrued interest. So the cash you split is less than the sale price suggests. Get those numbers worked out before you commit to anything. My <a href="{{L:g-divorce}}">guide to selling your HDB flat during a divorce</a> covers the steps, MOP and documents.</p>
  <h2 id="help">If you're going through this</h2>
  <p>You don't have to work it all out alone. Talk to your lawyer about the split and the timeline. Then talk to an agent about what your flat is worth and what you can realistically afford next.</p>
  <div class="note"><b>A quiet, no-pressure chat:</b> get a free <a href="{{L:salecheck}}">Sale Check</a> on WhatsApp to see what your flat could sell for and the cash you'd keep. Everything stays confidential.</div>""",
        faq=[
            ("Is the matrimonial flat always split 50/50?", "No. The court looks at each person's direct and indirect contributions and other factors, such as the children's needs. Couples can also agree on a split themselves, which the court can record in its order."),
            ("How long does a contested divorce take?", "It varies. In my experience, contested ones can drag on for two to three years."),
            ("Can I buy another HDB flat after my divorce?", "Often yes, but it depends on HDB's eligibility rules, including your age and who has care and control of the children. Check your eligibility with HDB before you plan."),
        ],
        related=[("g-divorce", "Selling your HDB flat during a divorce"), ("salecheck", "Free Sale Check"), ("safe", "The SAFE plan")],
    ),
]
