# Extra pages: first-timer guide, three upgrade timelines, SSD guide, loan calculator.
from content import article_shell, sale_check_form, CHAT, UPDATED

GUIDE_META = dict(published="2026-11-24", modified="2026-11-24")


def tl(items):
    out = ['<ol class="tl">']
    for it in items:
        when, title, lane, text, pays = it[:5]
        key = len(it) > 5 and it[5]
        lane_html = ('<span class="lane ' + lane + '">' + ("Selling" if lane == "sell" else "Buying") + "</span>") if lane else ""
        pay_html = ""
        if pays:
            pay_html = '<div class="pay">' + "".join('<span' + (' class="cash"' if c else "") + ">" + t + "</span>" for t, c in pays) + "</div>"
        out.append('<li' + (' class="key"' if key else "") + '><p class="when">' + when + "</p><h3>" + lane_html + title + "</h3><p>" + text + "</p>" + pay_html + "</li>")
    out.append("</ol>")
    return "".join(out)


def table(head, rows, num_cols=()):
    h = "".join('<th' + (' class="num"' if i in num_cols else "") + ">" + c + "</th>" for i, c in enumerate(head))
    b = "".join("<tr>" + "".join('<td' + (' class="num"' if i in num_cols else "") + ">" + c + "</td>" for i, c in enumerate(r)) + "</tr>" for r in rows)
    return '<table class="tbl stack"><thead><tr>' + h + "</tr></thead><tbody>" + b + "</tbody></table>"


SSD_TABLE = table(
    ["If you sell within", "Bought on/after 4 Jul 2025", "Bought 11 Mar 2017 – 3 Jul 2025"],
    [["1 year", "16%", "12%"], ["2 years", "12%", "8%"], ["3 years", "8%", "4%"], ["4 years", "4%", "No SSD"], ["After 4 years", "No SSD", "No SSD"]],
    num_cols=(1, 2),
)

PPS_TABLE = table(
    ["Stage", "% of price", "Typical timing", "Paid with"],
    [
        ["Booking fee (Option to Purchase)", "5%", "Day 0", "Cash only"],
        ["Exercise S&amp;P, balance downpayment", "15%", "Within 8 weeks of booking", "Cash and/or CPF OA"],
        ["Foundation completed", "10%", "Around 6–12 months", "CPF / loan"],
        ["Reinforced concrete framework", "10%", "Following months", "CPF / loan"],
        ["Partition walls", "5%", "During construction", "CPF / loan"],
        ["Roofing and ceiling", "5%", "During construction", "CPF / loan"],
        ["Doors, windows, electrical, plumbing", "5%", "During construction", "CPF / loan"],
        ["Car park, roads, drains", "5%", "During construction", "CPF / loan"],
        ["TOP (keys)", "25%", "Usually 3–4+ years", "CPF / loan"],
        ["CSC (legal completion)", "15%", "Often about a year after TOP", "CPF / loan"],
    ],
    num_cols=(1,),
)

# ------------------------------------------------------------ FIRST-TIMER
FIRST_FAQ = [
    ("Should we go BTO or resale?", "BTO is cheaper but you wait several years and pick from where HDB is building. Resale costs more but you can move in within months, choose the exact estate (near parents, schools, work), and stack up to three grants. Many couples who need space now, or want to be near family, find resale makes more sense."),
    ("How long does it take to buy a resale flat?", "Plan for about three to four months: up to a month for the HFE letter, a few weeks to find the flat, 21 days on the Option, then about 8 weeks from HDB's acceptance of the resale application to completion."),
    ("Do we need cash, or can we use CPF?", "You'll need some cash: the option fee and deposit (up to $5,000 in total), plus at least 5% of the price in cash if you take a bank loan. With an HDB loan, the downpayment can be paid fully from CPF. Stamp duty and legal fees can usually be paid or reimbursed from CPF. Your lawyer confirms the details."),
    ("Do we have to pay back the grants if we sell?", "When you eventually sell, the grants (with the interest they would have earned) go back into your CPF accounts, not to the government. It's still your money, for your next home or retirement."),
    ("How much can we borrow?", "Use my <a href=\"{{L:calculator}}\">loan calculator</a> for a quick estimate. Your HFE letter will confirm your HDB loan eligibility."),
]
FIRST_BODY = '''
  <div class="answer"><b>Short answer</b>Start with the HDB Flat Eligibility (HFE) letter. It tells you whether you can buy, which grants you get, and how much HDB will lend you. With it in hand, you know your real budget before you fall in love with a flat. Eligible first-timer families buying a resale flat can receive up to $230,000 in CPF housing grants.</div>
  <p>Buying your first home is exciting and a little terrifying. The good news: the process is well-defined, and as a first-timer you get the most help the government gives. Here's how it works, in order.</p>
  <h2 id="bto-resale">BTO or resale?</h2>
  ''' + table(["", "BTO (new flat)", "Resale flat"], [
      ["Price", "Lower, subsidised", "Market price"],
      ["Wait", "Several years", "About 3–4 months"],
      ["Location", "Where HDB is building", "Any estate you like"],
      ["Grants", "Enhanced CPF Housing Grant (EHG)", "EHG + CPF Housing Grant + Proximity Housing Grant"],
      ["MOP", "5 years (10 for Plus/Prime)", "5 years"],
  ]) + '''
  <h2 id="grants">The grants first-timers can get (resale)</h2>
  ''' + table(["Grant", "Up to", "Key condition"], [
      ["CPF Housing Grant", "$80,000 (2–4 room) / $50,000 (5-room+)", "First-timer SC couple; income ceiling applies"],
      ["Enhanced CPF Housing Grant (EHG)", "$120,000", "Average household income up to $9,000; less as income rises"],
      ["Proximity Housing Grant", "$30,000 living with parents / $20,000 within 4km", "Buying with or near parents or children"],
  ], num_cols=()) + '''
  <p>Grant amounts depend on your citizenship, income and flat type. Your HFE letter states exactly what you qualify for.</p>
  <h2 id="steps">The steps, in order</h2>
  ''' + tl([
      ("Week 0", "Check your eligibility and apply for the HFE letter", None, "Done on the HDB Flat Portal. It can take up to a month once your documents are in, so start early.", None),
      ("While you wait", "Set your budget", None, "Your HDB loan or bank in-principle approval, your CPF OA, your cash and the grants. Try my <a href=\"{{L:calculator}}\">loan calculator</a>. Leave a buffer for renovation.", None),
      ("Weeks 4–8", "View flats and agree a price", None, "Check the remaining lease, the block's recent transactions, and what's nearby: schools, parents, MRT.", None),
      ("Option date", "The seller grants you an Option to Purchase", "buy", "You need a valid HFE letter at this point. You then have 21 calendar days to decide.", [("Option fee up to $1,000 · cash", True)], True),
      ("Within 21 days", "Exercise the Option", "buy", "You commit to the purchase.", [("Option exercise fee · cash (deposit up to $5,000 in total)", True)]),
      ("Within 14 days of exercising", "Pay Buyer's Stamp Duty", "buy", "Usually handled through your lawyer.", [("Buyer's Stamp Duty", False)]),
      ("After exercising", "Submit the resale application with the seller", None, "HDB reviews it and issues its acceptance.", None),
      ("About 8 weeks after HDB's acceptance", "Completion and keys", "buy", "Your downpayment, legal fees and loan are settled, and the grants are credited towards the purchase. Your monthly instalment starts.", [("Downpayment balance · CPF/cash", False), ("Legal fees", False)], True),
  ]) + '''
  <h2 id="costs">Costs first-timers forget</h2>
  <ul><li>Renovation and furniture, usually the biggest surprise</li><li>Legal and conveyancing fees</li><li>Home and fire insurance</li><li>A buffer of a few months' expenses that you don't touch</li></ul>
  <div class="note"><b>My advice to first-timers:</b> buy for the next 5–10 years, not just the next 2. If kids are coming, think about schools and grandparents nearby. The Proximity Housing Grant can make "near Mak" the cheaper choice too.</div>
'''

# ------------------------------------------------------------ HDB -> HDB
H2H_FAQ = [
    ("Can I buy the new flat before selling my current one?", "Most families sell and buy in parallel, timing both completions close together. HDB does allow some owners to buy first and sell within a set period, subject to conditions. We'll check what applies to you."),
    ("Where does my sale money go?", "At completion, your outstanding loan is paid off and the CPF you used (plus accrued interest) is refunded to your CPF account. The cash balance comes to you. Both can fund your next flat."),
    ("What if my new flat isn't ready when I sell?", "You can ask your buyer for a temporary extension of stay after completion. I usually agree this upfront in the deal so nobody is surprised."),
    ("Do I pay ABSD buying another HDB flat?", "No. ABSD isn't payable on HDB flats when a Singapore Citizen is among the buyers, because HDB rules already require the existing flat to be sold."),
]
H2H_BODY = '''
  <div class="answer"><b>Short answer</b>Plan for about 3 to 5 months from listing to moving, depending on how fast your flat sells. The usual approach is to sell and buy in parallel, with both completions about 8 weeks after HDB accepts the resale applications, so your sale proceeds and CPF refund fund the next flat.</div>
  <p>Moving from one HDB flat to another (bigger, nearer parents, nearer school) is the most common upgrade I handle. The rules are clear; the trick is timing two transactions so you move once.</p>
  <h2 id="timeline">The timeline</h2>
  ''' + tl([
      ("Before you start", "Check MOP, get your HFE letter and run the numbers", None, "Confirm your MOP date, apply for the HFE letter for the next flat (up to a month), and know your sale proceeds and loan before listing.", None),
      ("Week 0", "Register your Intent to Sell", "sell", "You must register it at least 7 days before you can grant an Option to a buyer.", None),
      ("Weeks 1–6 (varies)", "Market your flat and hold viewings", "sell", "Pricing right is what makes this quick.", None),
      ("Same weeks", "Shortlist and negotiate your next flat", "buy", "Ideally you've agreed terms on your next flat around the time your own sale is agreed.", None),
      ("Option date", "Grant an Option to your buyer; get an Option on your next flat", "sell", "Each Option lasts 21 calendar days.", [("You receive: option fee", False), ("You pay: option fee up to $1,000 · cash", True)], True),
      ("Within 21 days", "Both Options exercised", "buy", "The buyer exercises on your flat; you exercise on your next flat.", [("You pay: exercise fee (deposit up to $5,000 total) · cash", True)]),
      ("Within 14 days of exercising", "Stamp duty on your purchase", "buy", "", [("Buyer's Stamp Duty", False)]),
      ("Next", "Submit both resale applications", None, "HDB reviews and accepts them. We align both so the completion dates sit together.", None),
      ("About 8 weeks after HDB's acceptance", "Completion of both: sell, then buy", None, "Your loan is paid off, your CPF is refunded with interest, the cash comes to you, and the purchase is paid with CPF, cash and the new loan.", [("Downpayment · CPF/cash", False), ("Legal fees", False), ("New loan starts", False)], True),
      ("If needed", "Temporary extension of stay", "sell", "Agreed with your buyer, if you need a short bridge before moving.", None),
  ]) + '''
  <h2 id="payments">What you pay, and when</h2>
  ''' + table(["When", "Payment", "Paid with"], [
      ["Option date", "Option fee up to $1,000", "Cash"],
      ["Exercise (within 21 days)", "Option exercise fee (deposit up to $5,000 total)", "Cash"],
      ["Within 14 days of exercise", "Buyer's Stamp Duty", "Cash first; CPF can often reimburse it"],
      ["Completion", "Downpayment: 25% with an HDB loan (CPF/cash), or 25% with at least 5% cash with a bank loan", "CPF / cash"],
      ["Completion", "Legal fees", "CPF / cash"],
  ]) + '''
  <div class="note"><b>Where families get caught:</b> forgetting that the CPF refund goes back to CPF, not to cash. If your next flat needs more cash than you think, the deal can wobble at the last step. We check this before you list.</div>
'''

# ------------------------------------------------------------ HDB -> PRIVATE RESALE
H2P_FAQ = [
    ("Do I have to sell my HDB before buying a condo?", "No. After MOP you can buy private property while keeping your HDB flat. But as a Singapore Citizen couple, the condo would be your second property, so ABSD applies up front."),
    ("How does the ABSD refund work?", "A married couple, with at least one Singapore Citizen, buying the condo jointly can claim back the ABSD if they sell their HDB within 6 months of buying a completed property. You must pay the ABSD first, and the refund isn't automatic. Your lawyer applies for it."),
    ("Can I use an HDB loan for a condo?", "No. Private property uses a bank loan. The TDSR limit (55% of income for all debts) applies, but not the 30% MSR that applies to HDB flats."),
    ("What is SSD and does it affect me?", "Seller's Stamp Duty applies if you sell the condo within 4 years of buying it (for purchases from 4 July 2025). It doesn't affect selling your HDB, because the MOP is longer. See my <a href=\"{{L:g-ssd}}\">SSD guide</a>."),
]
H2P_BODY = '''
  <div class="answer"><b>Short answer</b>The usual path takes about 4 to 6 months. Most families sell the HDB first and time the condo purchase so it completes after the HDB does, avoiding ABSD up front. The other path is buying first: you pay 20% ABSD on the condo, then claim it back if the HDB is sold within 6 months.</div>
  <p>Going from HDB to a resale condo means juggling two different systems: HDB's resale process and the private-property process. The order you do them in decides how much cash you need upfront.</p>
  <h2 id="paths">Two ways to do it</h2>
  ''' + table(["", "Sell HDB first (most common)", "Buy condo first"], [
      ["ABSD up front", "No, if the HDB is sold before you buy", "Yes, 20% (SC couple's 2nd property), refundable if conditions are met"],
      ["Budget certainty", "High: you know your proceeds", "Lower: depends on your HDB sale"],
      ["Moving", "May need a short bridge (extension of stay or family)", "One move, straight into the condo"],
      ["Risk", "Finding the right condo in time", "Big cash outlay; must sell the HDB within 6 months"],
  ]) + '''
  <h2 id="timeline">Timeline: sell HDB first</h2>
  ''' + tl([
      ("Before you start", "SAFE check and bank in-principle approval", None, "Know your HDB proceeds, CPF refund and what the bank will lend for private property.", None),
      ("Week 0", "Register your Intent to Sell", "sell", "At least 7 days before granting an Option.", None),
      ("Weeks 1–6", "Market the HDB; shortlist condos", "sell", "We line up two or three condo options while your flat is on the market.", None),
      ("Option date", "Grant an Option to your HDB buyer", "sell", "21 calendar days for your buyer to exercise.", [("You receive: option fee", False)], True),
      ("Next", "Resale application; HDB acceptance", "sell", "", None),
      ("While HDB processes", "Secure the condo with an Option to Purchase", "buy", "We negotiate an Option period and completion date that land after your HDB completion.", [("Option fee, typically 1% · cash", True)], True),
      ("About 8 weeks after HDB's acceptance", "HDB completion", "sell", "Loan paid off, CPF refunded with interest, cash proceeds to you. You no longer own a residential property.", [("You receive: sale proceeds", False)]),
      ("Usually within 14 days of the Option", "Exercise the condo Option", "buy", "Exercising after your HDB has completed is what keeps you clear of ABSD.", [("Exercise fee, typically 4% · cash/CPF", True)]),
      ("Within 14 days of exercising", "Stamp duty on the condo", "buy", "", [("Buyer's Stamp Duty", False)]),
      ("Typically 8–12 weeks after exercising", "Condo completion and keys", "buy", "Balance downpayment paid, bank loan disbursed, monthly instalments start.", [("Balance downpayment · CPF/cash", False), ("Legal fees", False)], True),
  ]) + '''
  <h2 id="payments">Condo payments at a glance</h2>
  ''' + table(["When", "Payment", "Paid with"], [
      ["Option", "Option fee, usually 1%", "Cash"],
      ["Exercise", "Usually 4% more, making 5%", "Cash (CPF can be used for part of the downpayment)"],
      ["Within 14 days of exercise", "Buyer's Stamp Duty (+ ABSD if you still own the HDB)", "Cash first; CPF may reimburse BSD"],
      ["Completion", "Balance of the 25% downpayment", "CPF / cash"],
      ["Completion", "75% bank loan disbursed (55% if tenure is over 30 years or runs past age 65)", "Loan"],
  ]) + '''
  <p>With a 75% bank loan, at least 5% of the price must be paid in cash. The rest of the downpayment can come from CPF.</p>
  <h2 id="ssd">If you sell the condo early: SSD</h2>
  <p>Plan to hold for at least 4 years. Selling a private home bought from 4 July 2025 within 4 years attracts Seller's Stamp Duty:</p>
  ''' + SSD_TABLE + '''
  <div class="note"><b>The timing trick:</b> the dates in the condo Option are negotiable. Getting the exercise date to fall after your HDB completes is often the difference between needing $0 or $200,000+ in ABSD cash. Agree this before you sign anything.</div>
'''

# ------------------------------------------------------------ HDB -> NEW LAUNCH
H2N_FAQ = [
    ("Can I stay in my HDB while the condo is being built?", "Yes. That's the main reason families buy first. But as a Singapore Citizen couple, you pay 20% ABSD upfront on the new launch, and claim it back if you sell the HDB within 6 months of the condo's TOP or CSC, whichever is earlier."),
    ("When do the monthly instalments start?", "The bank loan is drawn down as construction progresses, so instalments start small after the early stages and grow until TOP and CSC. Make sure you can carry your HDB loan and the rising condo instalments together."),
    ("Do I pay an agent fee for a new launch?", "No. For new launch projects, the developer pays the agent's fee."),
    ("What happens if I don't exercise after booking?", "If you don't exercise the Option, the developer can keep a quarter of the 5% booking fee and refunds the rest. Do your sums before you book, not after."),
    ("When does the SSD clock start for a new launch?", "From when you buy, not when you collect the keys. A 4-year SSD window from booking largely overlaps the construction period."),
]
H2N_BODY = '''
  <div class="answer"><b>Short answer</b>Most HDB upgraders book the new launch first and stay in their flat during construction, which typically takes 3–4 years. You pay 5% at booking, 15% within 8 weeks, and the rest progressively as the building goes up. Singapore Citizen couples pay 20% ABSD upfront, refundable if the HDB is sold within 6 months of TOP or CSC, whichever is earlier.</div>
  <p>New launches suit HDB upgraders because you don't have to move twice: you live in your flat until your new home is ready. The catch is cash flow, both the ABSD upfront and carrying two homes for a while.</p>
  <h2 id="paths">Two ways to do it</h2>
  ''' + table(["", "Book first, sell later (most common)", "Sell HDB first, then book"], [
      ["ABSD", "20% upfront, refundable if the HDB is sold within 6 months of TOP/CSC", "None"],
      ["Where you live", "Your HDB, until the condo is ready", "Rent or stay with family for 3–4 years"],
      ["Cash needed early", "5% cash + 15% + ABSD + BSD", "5% cash + 15% + BSD"],
      ["Watch out for", "Carrying both loans; the HDB sale deadline", "Rent costs; the market moving while you wait"],
  ]) + '''
  <h2 id="timeline">Timeline: book first, sell later</h2>
  ''' + tl([
      ("Before you book", "SAFE check, bank in-principle approval, ABSD plan", None, "Confirm you can pay 5% cash, 15% within 8 weeks, plus BSD and ABSD, while still paying your HDB loan.", None),
      ("Day 0", "Book the unit (Option to Purchase)", "buy", "The developer issues the Sale &amp; Purchase agreement, usually within about 2 weeks.", [("5% booking fee · cash", True)], True),
      ("About 3 weeks after you receive the S&amp;P", "Exercise the S&amp;P", "buy", "", None),
      ("Within 14 days of exercising", "Stamp duties", "buy", "Buyer's Stamp Duty, plus ABSD because you still own your HDB.", [("BSD", False), ("ABSD 20% · refundable later", True)]),
      ("Within 8 weeks of booking", "Balance downpayment", "buy", "", [("15% · cash/CPF", False)], True),
      ("Months 6 onward", "Progressive payments begin", "buy", "Foundation, framework, walls, ceiling, fittings, car park: each stage triggers the next drawdown. Your instalment grows with each one.", [("Paid by CPF / bank loan", False)]),
      ("Usually 3–4+ years", "TOP: keys to your new home", "buy", "25% is drawn down. The 6-month clock to sell your HDB starts at TOP or CSC, whichever is earlier.", [("25% · CPF/loan", False)], True),
      ("Around TOP", "Sell your HDB", "sell", "Register your Intent to Sell, market, grant the Option, resale application, completion about 8 weeks after HDB accepts it. Start before TOP so it completes in time.", None, True),
      ("Within 6 months of TOP/CSC", "Claim the ABSD refund", "sell", "Your lawyer applies once the HDB sale completes.", [("ABSD refunded", False)]),
      ("Often about a year after TOP", "CSC: final 15%", "buy", "", [("15% · CPF/loan", False)]),
  ]) + '''
  <h2 id="payments">The progressive payment schedule</h2>
  ''' + PPS_TABLE + '''
  <p>Timings vary by project. The developer's payment schedule in the S&amp;P is the one that counts.</p>
  <h2 id="ssd">SSD on new launches</h2>
  <p>For homes bought from 4 July 2025, selling within 4 years of purchase attracts SSD of up to 16%. The clock starts when you buy, so if you're thinking of selling soon after TOP, check the dates first.</p>
  ''' + SSD_TABLE + '''
  <div class="note"><b>Plan the HDB sale backwards from TOP:</b> list a few months before TOP so your HDB completes inside the 6-month window. Miss it and the ABSD stays with the taxman. I track this date for every client.</div>
'''

# ------------------------------------------------------------ SSD
SSD_FAQ = [
    ("Does SSD apply when I sell my HDB flat?", "In practice, no. The revised SSD doesn't affect HDB owners, because the HDB Minimum Occupation Period is longer than the SSD holding period."),
    ("Is SSD calculated on my selling price?", "On the selling price or the market value, whichever is higher."),
    ("When does the holding period start and end?", "Generally from the date you bought (when you exercised the Option or signed the S&amp;P) to the date you sell (when you grant the Option or sign the sale agreement). Your lawyer confirms the exact dates."),
    ("Who pays SSD, buyer or seller?", "The seller."),
]
SSD_BODY = '''
  <div class="answer"><b>Short answer</b>Seller's Stamp Duty (SSD) is a tax on selling a residential property soon after buying it. For properties bought on or after 4 July 2025, it applies if you sell within 4 years: 16% in the first year, 12% in the second, 8% in the third and 4% in the fourth. It doesn't affect HDB flats, because their MOP is longer.</div>
  <p>SSD matters most to upgraders who buy a condo or new launch and might need to sell within a few years: a job move, a family change, or a better opportunity. Know the date you're "free" before you buy.</p>
  <h2 id="rates">SSD rates</h2>
  ''' + SSD_TABLE + '''
  <p>SSD is charged on the higher of the selling price or market value.</p>
  <h2 id="calc">Quick SSD check</h2>
  <form class="mini" id="ssd-calc" novalidate>
    <div class="row2">
      <div class="field"><label for="s-buy">Date you bought</label><input type="date" id="s-buy" value="2025-08-01"></div>
      <div class="field"><label for="s-sell">Date you plan to sell</label><input type="date" id="s-sell" value="2027-03-01"></div>
    </div>
    <div class="field"><label for="s-price">Selling price</label><div class="money"><input id="s-price" inputmode="numeric" value="1500000"></div></div>
    <p class="hint" style="margin:0">Estimated SSD</p>
    <p class="out" id="s-out" aria-live="polite">–</p>
    <p class="fine" id="s-note" style="margin:6px 0 0"></p>
  </form>
  <p class="fine">An estimate only. Exact dates and amounts are confirmed by your lawyer against IRAS rules.</p>
  <h2 id="who">Who should think about SSD</h2>
  <ul>
    <li><b>New launch buyers:</b> the clock starts when you buy, not at TOP.</li>
    <li><b>Resale condo buyers</b> who might relocate, upgrade again or downsize within 4 years.</li>
    <li><b>Investors</b> planning a short holding period.</li>
  </ul>
  <div class="note"><b>Before you buy private:</b> I write down your SSD-free date alongside your SAFE plan, so a future decision is never made without it.</div>
'''

# ------------------------------------------------------------ CALCULATOR
CALC_FAQ = [
    ("Why is my maximum loan lower than I expected?", "Banks don't test your loan at today's interest rate. MAS requires them to use at least 4% (HDB uses 3% for its own loans) to check you could still afford it if rates rise. That stress test is what shrinks the number."),
    ("What's the difference between TDSR and MSR?", "TDSR caps all your monthly debt repayments (home, car, other loans) at 55% of income. MSR caps the home loan alone at 30% of income, and applies only to HDB flats and ECs bought from developers."),
    ("Why did my LTV drop to 55%?", "For bank loans, the 75% LTV applies only if the tenure is within 25 years (HDB flats) or 30 years (private), and the loan ends by age 65. Otherwise it's 55%, and you need at least 10% in cash."),
    ("I'm self-employed or earn commission. Does this work for me?", "Banks usually count only part of variable income such as commission, bonuses and self-employed income. Your actual figure may be lower. Talk to a mortgage banker for an in-principle approval."),
]
CALCULATOR = '''<section class="article-head"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="{{L:home}}">Home</a> / Loan calculator</nav>
  <h1>How much can you borrow, and what can you afford?</h1>
  <p class="lede">Enter your income and savings. This calculator applies Singapore's loan rules (TDSR, MSR, LTV and the stress-test rate) to estimate your maximum loan, your affordable price, and your monthly instalment.</p>
</div></section>
<section class="band paper" style="padding-top:40px"><div class="wrap calc">
  <form id="loan-calc" novalidate>
    <fieldset><legend>What are you buying?</legend>
      <div class="seg" role="radiogroup" aria-label="Property type">
        <label><input type="radio" name="ptype" value="hdb" checked><span>HDB flat</span></label>
        <label><input type="radio" name="ptype" value="ec"><span>EC (from developer)</span></label>
        <label><input type="radio" name="ptype" value="pvt"><span>Condo / private</span></label>
      </div>
      <div class="seg" role="radiogroup" aria-label="Loan type">
        <label><input type="radio" name="lender" value="bank" checked><span>Bank loan</span></label>
        <label><input type="radio" name="lender" value="hdb"><span>HDB loan</span></label>
      </div>
    </fieldset>
    <fieldset><legend>Your income</legend>
      <div class="row2">
        <div class="field"><label for="c-inc1">Buyer 1 gross monthly income</label><div class="money"><input id="c-inc1" inputmode="numeric" value="6000"></div></div>
        <div class="field"><label for="c-age1">Buyer 1 age</label><input id="c-age1" inputmode="numeric" value="32"></div>
      </div>
      <div class="row2">
        <div class="field"><label for="c-inc2">Buyer 2 gross monthly income <span class="hint">(optional)</span></label><div class="money"><input id="c-inc2" inputmode="numeric" value="5000"></div></div>
        <div class="field"><label for="c-age2">Buyer 2 age</label><input id="c-age2" inputmode="numeric" value="31"></div>
      </div>
      <div class="field"><label for="c-debts">Other monthly debt repayments <span class="hint">(car loan, personal loans, etc.)</span></label><div class="money"><input id="c-debts" inputmode="numeric" value="0"></div></div>
    </fieldset>
    <fieldset><legend>Your savings</legend>
      <div class="row2">
        <div class="field"><label for="c-cash">Cash available for the purchase</label><div class="money"><input id="c-cash" inputmode="numeric" value="60000"></div></div>
        <div class="field"><label for="c-cpf">CPF OA available <span class="hint">(incl. sale proceeds &amp; refunds)</span></label><div class="money"><input id="c-cpf" inputmode="numeric" value="120000"></div></div>
      </div>
      <div class="field"><label for="c-other">Legal and other costs</label><div class="money"><input id="c-other" inputmode="numeric" value="3000"></div></div>
    </fieldset>
    <fieldset><legend>The loan</legend>
      <div class="row2">
        <div class="field"><label for="c-tenure">Loan tenure (years) <span class="hint" id="ten-hint"></span></label><input id="c-tenure" inputmode="numeric" value="25"></div>
        <div class="field"><label for="c-rate">Your interest rate (% a year)</label><input id="c-rate" inputmode="decimal" value="2.6"></div>
      </div>
      <div class="field" id="lease-field" style="display:none"><label for="c-lease">Remaining lease of the flat (years) <span class="hint">(HDB loan tenure is capped at lease minus 20)</span></label><input id="c-lease" inputmode="numeric" value="80"></div>
      <div class="field"><label for="c-price">Price of the home you're looking at <span class="hint">(optional)</span></label><div class="money"><input id="c-price" inputmode="numeric" value="650000"></div></div>
    </fieldset>
  </form>
  <aside class="result" aria-live="polite">
    <h2>Your estimate</h2>
    <p class="big-label">Maximum loan based on income</p>
    <p class="big" id="r-loan">–</p>
    <ul class="rows">
      <li><span id="r-capname">Max instalment allowed</span><b id="r-cap">–</b></li>
      <li><span>Stress-test rate used</span><b id="r-stress">–</b></li>
      <li><span>LTV &amp; tenure applied</span><b id="r-ltv">–</b></li>
      <li><span>Income-weighted age</span><b id="r-age">–</b></li>
      <li><span>Highest price your savings + loan can support</span><b id="r-maxprice">–</b></li>
    </ul>
    <div id="r-price-block">
      <h2 style="margin-top:26px">At your chosen price</h2>
      <ul class="rows">
        <li><span>Loan</span><b id="r-p-loan">–</b></li>
        <li><span>Downpayment</span><b id="r-p-down">–</b></li>
        <li><span>of which minimum cash</span><b id="r-p-cash">–</b></li>
        <li><span>Buyer's Stamp Duty</span><b id="r-p-bsd">–</b></li>
        <li><span>Monthly instalment at your rate</span><b id="r-p-monthly">–</b></li>
        <li><span>Share of income</span><b id="r-p-share">–</b></li>
      </ul>
      <div class="flag" id="r-flag"></div>
    </div>
    <a class="btn primary" style="width:100%;margin-top:20px" href="{{WA:Hi Andik, I used your loan calculator and would like you to check my numbers.}}">''' + CHAT + '''Ask Andik to check my numbers</a>
  </aside>
</div>
<div class="wrap">
  <div class="disclaimer">
    <b>Important: please read</b>
    <ul>
      <li>This calculator gives <b>estimates for planning only</b>. It is not a loan offer, an approval, or financial advice. Banks and HDB decide your actual loan amount.</li>
      <li>It applies the rules as at ''' + UPDATED + ''': TDSR 55% of gross income; MSR 30% for HDB flats and ECs; a stress-test rate of at least 4% for bank loans and 3% for HDB loans; LTV 75% (55% if tenure exceeds 25 years for HDB flats or 30 years for private property, or the loan runs past age 65); and minimum cash of 5% (10% at 55% LTV) for bank loans.</li>
      <li>It assumes no other outstanding housing loans. A second housing loan has much lower LTV limits. ABSD, renovation, and property tax aren't included.</li>
      <li>Banks typically count only part of variable or self-employed income. HDB loan eligibility also depends on household income ceilings, citizenship and other conditions not modelled here.</li>
      <li>Before committing, get an HFE letter (for HDB) or an in-principle approval from a bank, and check the latest rules with MAS, HDB, CPF and IRAS.</li>
    </ul>
  </div>
  <div class="prose" style="max-width:860px;margin-top:30px">
    <h2 id="faq">About these numbers</h2>
    [[FAQ]]
  </div>
</div></section>
<section class="band dark"><div class="wrap split">
  <div><h2>Your loan is only half the picture</h2><p class="lede">What you'll get from selling your current flat decides the rest. Send your postal code and I'll do the other half.</p></div>
  <div>''' + sale_check_form() + '''</div>
</div></section>'''

_ctx = [("guides", "Guides")]
EXTRA_PAGES = [
    dict(key="g-first", url="/guides/first-time-home-buyer-guide", file="guides/first-time-home-buyer-guide.html",
         h1_short="First-time home buyer guide (Singapore HDB)", crumbs=_ctx,
         title="First-Time Home Buyer Guide Singapore 2026: HFE, Grants & Steps",
         desc="Buying your first HDB flat? HFE letter, BTO vs resale, up to $230,000 in grants, the step-by-step resale timeline and what you pay at each stage.",
         article=GUIDE_META, faq=FIRST_FAQ,
         body=article_shell("First-time buyers", "First-time home buyer guide: from HFE letter to keys",
                            "Everything a first-timer couple needs, in the order you'll need it: eligibility, grants, budget, the resale steps and what you pay at each one.",
                            [("bto-resale", "BTO or resale?"), ("grants", "Grants you can get"), ("steps", "The steps, in order"), ("costs", "Costs first-timers forget")],
                            FIRST_BODY, [("calculator", "Loan calculator"), ("g-hdb2hdb", "HDB to HDB timeline"), ("g-upgrade", "Upgrading after MOP")])),
    dict(key="g-hdb2hdb", url="/guides/hdb-to-hdb-upgrade-timeline", file="guides/hdb-to-hdb-upgrade-timeline.html",
         h1_short="HDB to HDB upgrade timeline", crumbs=_ctx,
         title="HDB to HDB Upgrade Timeline: Sell & Buy in Parallel (2026)",
         desc="Step-by-step timeline for selling your HDB and buying another: Intent to Sell, Options, resale applications, completion, and exactly what you pay at each stage.",
         article=GUIDE_META, faq=H2H_FAQ,
         body=article_shell("HDB to HDB timeline", "HDB to HDB: the upgrade timeline and payment schedule",
                            "How to sell your flat and buy the next one in parallel, so you move once and your sale funds the purchase.",
                            [("timeline", "The timeline"), ("payments", "What you pay, and when")],
                            H2H_BODY, [("g-hdb2pvt", "HDB to private resale"), ("g-hdb2nl", "HDB to new launch"), ("calculator", "Loan calculator")])),
    dict(key="g-hdb2pvt", url="/guides/hdb-to-private-resale-timeline", file="guides/hdb-to-private-resale-timeline.html",
         h1_short="HDB to private resale condo timeline", crumbs=_ctx,
         title="HDB to Resale Condo Timeline: Sell First or Buy First? ABSD & SSD (2026)",
         desc="Upgrading from HDB to a resale condo: the sell-first vs buy-first timelines, condo payment schedule (1% + 4%), ABSD refund rules and SSD.",
         article=GUIDE_META, faq=H2P_FAQ,
         body=article_shell("HDB to private resale", "HDB to private resale: the upgrade timeline and payment schedule",
                            "The two ways to sequence it, what each costs upfront, and the timing that keeps ABSD off your bill.",
                            [("paths", "Two ways to do it"), ("timeline", "Timeline: sell first"), ("payments", "Condo payments"), ("ssd", "SSD if you sell early")],
                            H2P_BODY, [("g-hdb2nl", "HDB to new launch"), ("g-ssd", "Seller's Stamp Duty"), ("calculator", "Loan calculator")])),
    dict(key="g-hdb2nl", url="/guides/hdb-to-new-launch-timeline", file="guides/hdb-to-new-launch-timeline.html",
         h1_short="HDB to new launch condo timeline", crumbs=_ctx,
         title="HDB to New Launch Condo Timeline: Progressive Payments, ABSD & SSD",
         desc="Upgrading from HDB to a new launch: the book-first timeline, progressive payment schedule from 5% booking to CSC, ABSD refund within 6 months of TOP, and SSD.",
         article=GUIDE_META, faq=H2N_FAQ,
         body=article_shell("HDB to new launch", "HDB to new launch: the upgrade timeline and payment schedule",
                            "Book, stay in your flat while it's built, then sell at the right moment. Here's every payment and deadline along the way.",
                            [("paths", "Two ways to do it"), ("timeline", "Timeline: book first"), ("payments", "Progressive payments"), ("ssd", "SSD on new launches")],
                            H2N_BODY, [("newlaunch", "New launch for upgraders"), ("g-ssd", "Seller's Stamp Duty"), ("calculator", "Loan calculator")])),
    dict(key="g-ssd", url="/guides/sellers-stamp-duty-ssd", file="guides/sellers-stamp-duty-ssd.html",
         h1_short="Seller's Stamp Duty (SSD) explained", crumbs=_ctx, scripts=["calc.js"],
         title="Seller's Stamp Duty (SSD) 2026: Rates, 4-Year Rule & Calculator",
         desc="SSD rates for homes bought from 4 July 2025: 16%, 12%, 8%, 4% within 4 years. Who pays, how it's calculated, and a quick SSD calculator.",
         article=GUIDE_META, faq=SSD_FAQ,
         body=article_shell("Seller's Stamp Duty", "Seller's Stamp Duty (SSD): rates, the 4-year rule, and a quick check",
                            "What SSD is, when it applies, and how to know your SSD-free date before you buy.",
                            [("rates", "SSD rates"), ("calc", "Quick SSD check"), ("who", "Who should think about it")],
                            SSD_BODY, [("g-hdb2pvt", "HDB to private resale"), ("g-hdb2nl", "HDB to new launch"), ("calculator", "Loan calculator")])),
    dict(key="calculator", url="/loan-calculator", file="loan-calculator.html", h1_short="Home loan calculator",
         title="Home Loan Calculator Singapore 2026: TDSR, MSR & Affordability | Andik Imran",
         desc="Estimate your maximum home loan from your income using Singapore's TDSR, MSR, LTV and 4% stress-test rules. See your affordable price, downpayment, stamp duty and monthly instalment.",
         faq=CALC_FAQ, scripts=["calc.js"], body=CALCULATOR),
]
