{
  // ---- Rules as at 24 Nov 2026 (MAS, HDB, IRAS). Update here if rules change. ----
  const RULES = {
    tdsr: 0.55,            // Total Debt Servicing Ratio (all property loans from banks)
    msr: 0.30,             // Mortgage Servicing Ratio (HDB flats and ECs bought from developers)
    bankStress: 0.04,      // MAS medium-term interest rate floor for residential loans
    hdbStress: 0.03,       // HDB interest-rate floor used to compute HDB loan amount
    ltvHigh: 0.75, ltvLow: 0.55,
    cashHigh: 0.05, cashLow: 0.10,
    bankMaxTenureHDB: 30, bankMaxTenurePvt: 35,
    ltvTenureHDB: 25, ltvTenurePvt: 30, ltvAge: 65,
    hdbLoanMaxTenure: 25
  };

  const $ = (id) => document.getElementById(id);
  const num = (id) => { const el = $(id); if (!el) return 0; const v = parseFloat(String(el.value).replace(/[^0-9.]/g, '')); return isFinite(v) ? v : 0; };
  const fmt = (n) => (n < 0 ? '-' : '') + '$' + Math.round(Math.abs(n)).toLocaleString('en-SG');
  const pct = (n) => (Math.round(n * 1000) / 10) + '%';
  const pv = (rate, years, pmt) => { const r = rate / 12, n = years * 12; return r === 0 ? pmt * n : pmt * (1 - Math.pow(1 + r, -n)) / r; };
  const pmt = (rate, years, loan) => { const r = rate / 12, n = years * 12; return r === 0 ? loan / n : loan * r / (1 - Math.pow(1 + r, -n)); };

  function bsd(p) {
    const bands = [[180000, .01], [180000, .02], [640000, .03], [500000, .04], [1500000, .05], [Infinity, .06]];
    let left = p, d = 0;
    for (const [w, r] of bands) { const x = Math.min(left, w); d += x * r; left -= x; if (left <= 0) break; }
    return Math.floor(d);
  }

  const form = $('loan-calc');
  if (form) {
    const typeOf = () => (form.querySelector('input[name=ptype]:checked') || {}).value || 'hdb';
    const lenderOf = () => (form.querySelector('input[name=lender]:checked') || {}).value || 'bank';
    let tenureTouched = false;
    $('c-tenure').addEventListener('input', () => { tenureTouched = true; });

    function calc() {
      const type = typeOf();
      const hdbLoanRadio = form.querySelector('input[name=lender][value=hdb]');
      hdbLoanRadio.disabled = type !== 'hdb';
      if (type !== 'hdb' && hdbLoanRadio.checked) form.querySelector('input[name=lender][value=bank]').checked = true;
      const lender = type === 'hdb' ? lenderOf() : 'bank';
      $('lease-field').style.display = (type === 'hdb' && lender === 'hdb') ? '' : 'none';

      const rows = [...form.querySelectorAll('.buyer')].map((r) => {
        const v = (el) => { const x = parseFloat(String(el.value).replace(/[^0-9.]/g, '')); return isFinite(x) ? x : 0; };
        return { inc: v(r.querySelector('.b-inc')), age: v(r.querySelector('.b-age')) };
      });
      const a1 = rows[0].age || 30;
      rows.forEach((r) => { if (!r.age) r.age = a1; });
      const income = rows.reduce((s, r) => s + r.inc, 0);
      const age = income > 0 ? rows.reduce((s, r) => s + r.age * r.inc, 0) / income : a1;
      const debts = num('c-debts');
      const cash = num('c-cash'), cpf = num('c-cpf'), other = num('c-other');
      const price = num('c-price');
      const actual = (num('c-rate') || (lender === 'hdb' ? 2.6 : 2.5)) / 100;

      // tenure
      let maxTen, autoTen;
      if (lender === 'hdb') {
        const lease = num('c-lease');
        maxTen = Math.min(RULES.hdbLoanMaxTenure, Math.floor(65 - age), lease ? lease - 20 : 99);
        autoTen = maxTen;
      } else {
        const capT = type === 'hdb' ? RULES.bankMaxTenureHDB : RULES.bankMaxTenurePvt;
        const ltvT = type === 'hdb' ? RULES.ltvTenureHDB : RULES.ltvTenurePvt;
        maxTen = capT;
        autoTen = Math.min(ltvT, Math.floor(RULES.ltvAge - age));
        if (autoTen < 5) autoTen = Math.min(capT, 25);
      }
      maxTen = Math.max(1, maxTen);
      const tenEl = $('c-tenure');
      if (!tenureTouched || !num('c-tenure')) tenEl.value = Math.max(1, Math.min(autoTen, maxTen));
      let ten = Math.max(1, Math.min(num('c-tenure'), maxTen));
      $('ten-hint').textContent = 'Max ' + maxTen + ' years for this loan';

      // LTV + min cash
      let ltv, cashPct;
      if (lender === 'hdb') { ltv = RULES.ltvHigh; cashPct = 0; }
      else {
        const ltvT = type === 'hdb' ? RULES.ltvTenureHDB : RULES.ltvTenurePvt;
        const ok = ten <= ltvT && age + ten <= RULES.ltvAge;
        ltv = ok ? RULES.ltvHigh : RULES.ltvLow;
        cashPct = ok ? RULES.cashHigh : RULES.cashLow;
      }

      // max instalment
      let capInst, capName;
      if (lender === 'hdb') { capInst = RULES.msr * income; capName = 'MSR 30%'; }
      else if (type === 'pvt') { capInst = RULES.tdsr * income - debts; capName = 'TDSR 55%'; }
      else {
        const m = RULES.msr * income, t = RULES.tdsr * income - debts;
        capInst = Math.min(m, t); capName = m <= t ? 'MSR 30%' : 'TDSR 55%';
      }
      capInst = Math.max(0, capInst);
      const stress = lender === 'hdb' ? RULES.hdbStress : Math.max(RULES.bankStress, actual);
      const loanIncome = pv(stress, ten, capInst);

      // max price with funds
      const funds = cash + cpf;
      const feasible = (P) => {
        const loan = Math.min(ltv * P, loanIncome);
        const need = P - loan + bsd(P) + other;
        return funds >= need && cash >= cashPct * P;
      };
      let lo = 0, hi = 8000000;
      if (funds > 0) { for (let k = 0; k < 60; k++) { const mid = (lo + hi) / 2; if (feasible(mid)) lo = mid; else hi = mid; } }
      const maxPrice = funds > 0 ? Math.floor(lo / 1000) * 1000 : 0;

      // outputs
      $('r-loan').textContent = fmt(loanIncome);
      $('r-cap').textContent = fmt(capInst) + ' /mth';
      $('r-capname').textContent = 'Max instalment allowed (' + capName + ')';
      $('r-stress').textContent = pct(stress);
      $('r-ltv').textContent = pct(ltv) + ' · ' + ten + ' yrs';
      $('r-age').textContent = Math.round(age) + ' yrs';
      $('r-maxprice').textContent = funds > 0 ? fmt(maxPrice) : 'Add your cash & CPF';

      const pr = $('r-price-block');
      if (price > 0) {
        const loan = Math.min(ltv * price, loanIncome);
        const down = price - loan;
        const minCash = cashPct * price;
        const duty = bsd(price);
        const need = down + duty + other;
        const monthly = pmt(actual, ten, loan);
        $('r-p-loan').textContent = fmt(loan);
        $('r-p-down').textContent = fmt(down);
        $('r-p-cash').textContent = fmt(minCash);
        $('r-p-bsd').textContent = fmt(duty);
        $('r-p-monthly').textContent = fmt(monthly) + ' /mth';
        $('r-p-share').textContent = income ? pct(monthly / income) + ' of income' : '–';
        const gap = funds - need;
        const fl = $('r-flag');
        const issues = [];
        if (gap < 0) issues.push('You are short by about ' + fmt(-gap) + ' for the downpayment, stamp duty and costs at this price.');
        if (cash < minCash) issues.push('You need at least ' + fmt(minCash) + ' in cash for this price. You have ' + fmt(cash) + '.');
        if (loan < ltv * price - 1) issues.push('Your income limits the loan to ' + fmt(loan) + ', below the ' + pct(ltv) + ' LTV maximum, so the downpayment is larger.');
        if (funds <= 0) { fl.className = 'flag'; fl.textContent = 'Add your cash and CPF OA to see if your savings cover the downpayment and stamp duty.'; }
        else if (!issues.length) { fl.className = 'flag'; fl.textContent = 'Your cash and CPF cover the downpayment and stamp duty, with ' + fmt(gap) + ' to spare. Under SAFE, part of that should stay aside as your buffer.'; }
        else { fl.className = 'flag warn'; fl.textContent = issues.join(' '); }
        pr.style.display = '';
      } else { pr.style.display = 'none'; }
    }
    // add / remove owners (up to 4)
    const box = $('buyers'), addBtn = $('add-buyer');
    const renumber = () => {
      [...box.querySelectorAll('.buyer')].forEach((r, k) => {
        const n = k + 1;
        r.querySelector('.b-inc').id = 'c-inc' + n; r.querySelector('.b-age').id = 'c-age' + n;
        const ls = r.querySelectorAll('label');
        ls[0].htmlFor = 'c-inc' + n; ls[0].firstChild.textContent = 'Owner ' + n + ' gross monthly income';
        ls[1].htmlFor = 'c-age' + n; ls[1].firstChild.textContent = 'Owner ' + n + ' age';
      });
      addBtn.style.display = box.querySelectorAll('.buyer').length >= 4 ? 'none' : '';
    };
    addBtn.addEventListener('click', () => {
      const r = document.createElement('div');
      r.className = 'row2 buyer';
      r.innerHTML = '<div class="field"><label>Owner</label><div class="money"><input class="b-inc" inputmode="numeric" value="0"></div></div>' +
        '<div class="field"><label>Owner</label><div class="age-row"><input class="b-age" inputmode="numeric" value="0"><button type="button" class="rm-buyer" aria-label="Remove this owner">✕</button></div></div>';
      r.querySelector('.rm-buyer').addEventListener('click', () => { r.remove(); renumber(); calc(); });
      box.appendChild(r); renumber(); calc();
      r.querySelector('.b-inc').focus(); r.querySelector('.b-inc').select();
    });
    form.addEventListener('input', calc);
    form.addEventListener('change', calc);
    form.addEventListener('submit', (e) => e.preventDefault());
    calc();
  }

  // ---- SSD mini calculator ----
  const ssd = $('ssd-calc');
  if (ssd) {
    const run = () => {
      const p = num('s-price');
      const b = new Date($('s-buy').value), s = new Date($('s-sell').value);
      const out = $('s-out'), note = $('s-note');
      if (!p || isNaN(b) || isNaN(s) || s <= b) { out.textContent = '–'; note.textContent = 'Enter the price and both dates.'; return; }
      const newRules = b >= new Date('2025-07-04');
      const addY = (d, y) => { const x = new Date(d); x.setFullYear(x.getFullYear() + y); return x; };
      const tiers = newRules ? [.16, .12, .08, .04] : [.12, .08, .04];
      let rate = 0, yr = 0;
      for (let i = 0; i < tiers.length; i++) { if (s <= addY(b, i + 1)) { rate = tiers[i]; yr = i + 1; break; } }
      out.textContent = rate ? fmt(p * rate) + ' (' + Math.round(rate * 100) + '%)' : 'No SSD';
      note.textContent = rate
        ? 'Sold within year ' + yr + ' of purchase. ' + (newRules ? 'Bought on/after 4 Jul 2025: 4-year holding period.' : 'Bought 11 Mar 2017 – 3 Jul 2025: 3-year holding period.') + ' SSD is on the higher of price or market value.'
        : 'Held beyond the SSD holding period' + (newRules ? ' (4 years).' : ' (3 years).');
    };
    ssd.addEventListener('input', run);
    ssd.addEventListener('submit', (e) => e.preventDefault());
    run();
  }
}
