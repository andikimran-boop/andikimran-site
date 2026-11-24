{
  const WA = '6587368736';

  // mobile menu
  const btn = document.querySelector('.menu-btn');
  const nav = document.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // photos: if one is missing, hide it so the branded frame shows instead of a broken icon
  const hide = (img) => { img.style.display = 'none'; const p = img.parentElement; if (p && (p.classList.contains('pnx') || p.classList.contains('brand-pnx'))) p.classList.add('noimg'); };
  document.querySelectorAll('img').forEach((img) => {
    if (img.complete && img.naturalWidth === 0) hide(img);
    img.addEventListener('error', () => hide(img));
  });

  // label table cells for the stacked mobile layout
  document.querySelectorAll('table.stack').forEach((t) => {
    const heads = [...t.querySelectorAll('thead th')].map((th) => th.textContent.trim());
    t.querySelectorAll('tbody tr').forEach((tr) => [...tr.children].forEach((td, i) => { if (heads[i]) td.dataset.l = heads[i]; }));
  });

  // Free Sale Check -> AIMS report builder (Make webhook -> GitHub -> WhatsApp PDF from 8568 5643)
  const LEAD_WEBHOOK = 'https://hook.eu1.make.com/r2xwq6c4xa2bv7gpruswla6e7w3pw9v8';
  const areaFromPostal = (pc) => {
    const two = pc.slice(0, 2);
    if (two === '82') return 'Punggol';
    if (two === '54' || two === '79') return 'Sengkang';
    if (two === '51') return 'Pasir Ris';
    if (two === '52') return 'Tampines';
    if (two === '76') return 'Yishun';
    return 'Other';
  };
  const source = (() => {
    let q = {}; try { q = Object.fromEntries(new URLSearchParams(location.search)); } catch (x) {}
    const ref = document.referrer || '';
    if (q.gclid || q.gbraid || q.wbraid) return 'Google Ads';
    if (q.utm_source) return q.utm_source + (q.utm_campaign ? ' (' + q.utm_campaign + ')' : '');
    if (/google\./i.test(ref)) return 'Google search (not ads)';
    if (/chatgpt|openai|perplexity|claude|gemini/i.test(ref)) return 'AI assistant';
    if (/tiktok\./i.test(ref)) return 'TikTok';
    if (/instagram\./i.test(ref)) return 'Instagram';
    if (/facebook\.|fb\./i.test(ref)) return 'Facebook';
    if (ref && ref.indexOf(location.hostname) < 0) return 'Other site: ' + ref.replace(/^https?:\/\//, '').split('/')[0];
    return 'Direct / unknown';
  })();
  document.querySelectorAll('form.sale-check').forEach((form) => {
    const err = form.querySelector('.err');
    const done = form.parentElement.querySelector('.done');
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const v = (n) => (form.elements[n] ? form.elements[n].value.trim() : '');
      const fail = (msg, n) => { err.textContent = msg; if (form.elements[n]) form.elements[n].focus(); };
      const postal = v('postal').replace(/\D/g, '');
      const mobile = v('mobile').replace(/\D/g, '').replace(/^65(?=\d{8}$)/, '');
      const [property, unitType] = (v('type') || 'HDB|4-room').split('|');
      const unit = v('unit');
      if (!/^\d{6}$/.test(postal)) return fail('Postal code should be 6 digits.', 'postal');
      if (property !== 'Landed' && !unit) return fail('Please add your unit number, e.g. #08-124. It helps us price your floor.', 'unit');
      if (!v('name')) return fail('Please tell me your name.', 'name');
      if (!/^[89]\d{7}$/.test(mobile)) return fail('Please enter a Singapore mobile number (8 digits, starting with 8 or 9).', 'mobile');
      err.textContent = '';
      const stamp = new Date().toLocaleString('en-SG', { timeZone: 'Asia/Singapore', day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' });
      const body = new URLSearchParams({
        submitted_at: stamp, name: v('name'), mobile: mobile.slice(0, 4) + ' ' + mobile.slice(4), wa_link: 'https://wa.me/65' + mobile,
        postal_code: postal, address: '', unit_no: unit, property, unit_type: unitType, area: areaFromPostal(postal),
        language: 'en', situation: v('why'), page: 'andikimran.com | ' + source + ' | ' + location.href
      });
      try { fetch(LEAD_WEBHOOK, { method: 'POST', mode: 'no-cors', body }); } catch (x) {}
      if (window.gtag) { try { window.gtag('event', 'generate_lead', { method: 'property_report' }); } catch (x) {} }
      form.style.display = 'none';
      if (done) { done.classList.add('show'); done.querySelector('h3').textContent = 'On its way, ' + v('name').split(' ')[0] + '!'; }
    });
  });
}
