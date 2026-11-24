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

  // Free Sale Check -> WhatsApp
  document.querySelectorAll('form.sale-check').forEach((form) => {
    const err = form.querySelector('.err');
    const done = form.parentElement.querySelector('.done');
    const link = done ? done.querySelector('a') : null;
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const v = (n) => (form.elements[n] ? form.elements[n].value.trim() : '');
      const name = v('name'), postal = v('postal'), type = v('type'), why = v('why'), note = v('note');
      if (!name) { err.textContent = 'Please tell me your name.'; form.elements.name.focus(); return; }
      if (!/^\d{6}$/.test(postal)) { err.textContent = 'Postal code should be 6 digits.'; form.elements.postal.focus(); return; }
      err.textContent = '';
      const lines = [
        'Hi Andik, I\'d like a free Sale Check.',
        'Name: ' + name,
        'Postal code: ' + postal,
        type ? 'Home: ' + type : '',
        why ? 'Situation: ' + why : '',
        note ? 'Note: ' + note : ''
      ].filter(Boolean).join('\n');
      const url = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(lines);
      if (window.gtag) { try { window.gtag('event', 'generate_lead', { method: 'sale_check' }); } catch (x) {} }
      if (link) link.href = url;
      form.style.display = 'none';
      if (done) { done.classList.add('show'); link && link.focus(); }
      try { window.open(url, '_blank', 'noopener'); } catch (x) {}
    });
  });
}
