/* Karama site behavior. Pages are static HTML; this file only adds interaction. */
(function () {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const header = $(".site-header");
  const onScroll = () => header && header.classList.toggle("scrolled", scrollY > 40);
  addEventListener("scroll", onScroll, { passive: true }); onScroll();
  $$("[data-year]").forEach(e => (e.textContent = new Date().getFullYear()));
  $$("[data-share]").forEach(b => b.addEventListener("click", async e => { e.preventDefault(); try { if (navigator.share) await navigator.share({ title: document.title, url: location.href }); else { await navigator.clipboard.writeText(location.href); b.textContent = "Link copied"; } } catch (_) {} }));

  // ---- Mega menus: hover on desktop, tap on mobile ----
  const items = $$(".main-nav > li.has-mega");
  const desktop = () => matchMedia("(min-width: 1181px)").matches;
  items.forEach(li => {
    const link = li.querySelector(":scope > a");
    let timer;
    li.addEventListener("mouseenter", () => { if (!desktop()) return; clearTimeout(timer); items.forEach(o => o !== li && o.classList.remove("open")); li.classList.add("open"); link.setAttribute("aria-expanded", "true"); });
    li.addEventListener("mouseleave", () => { if (!desktop()) return; timer = setTimeout(() => { li.classList.remove("open"); link.setAttribute("aria-expanded", "false"); }, 150); });
    link.addEventListener("click", e => {
      if (desktop()) return; // desktop: link navigates to the landing page
      if (!li.classList.contains("open")) { e.preventDefault(); li.classList.add("open"); link.setAttribute("aria-expanded", "true"); }
    });
    link.addEventListener("keydown", e => {
      if (e.key === "ArrowDown") { e.preventDefault(); li.classList.add("open"); li.querySelector(".mega a")?.focus(); }
    });
    li.addEventListener("focusout", e => { if (!li.contains(e.relatedTarget)) li.classList.remove("open"); });
  });
  document.addEventListener("keydown", e => {
    if (e.key !== "Escape") return;
    items.forEach(li => li.classList.remove("open"));
    $(".search-overlay")?.classList.remove("open");
    $(".lang")?.classList.remove("open");
  });

  // ---- Mobile menu ----
  $(".menu-toggle")?.addEventListener("click", e => {
    const open = header.classList.toggle("open");
    e.currentTarget.setAttribute("aria-expanded", open);
    e.currentTarget.querySelector("span").textContent = open ? "Close" : "Menu";
    document.body.style.overflow = open ? "hidden" : "";
  });

  // ---- Language picker (Google Translate, loaded only when a language is picked) ----
  const lang = $(".lang");
  lang?.querySelector(".lang-btn").addEventListener("click", () => lang.classList.toggle("open"));
  document.addEventListener("click", e => { if (lang && !lang.contains(e.target)) lang.classList.remove("open"); });
  $$(".lang-menu button").forEach(b => b.addEventListener("click", () => {
    const code = b.dataset.lang;
    document.cookie = code === "en" ? "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/" : `googtrans=/en/${code}; path=/`;
    location.reload();
  }));
  if (/googtrans=\/en\/\w/.test(document.cookie)) {
    window.googleTranslateElementInit = () => new google.translate.TranslateElement({ pageLanguage: "en", autoDisplay: false }, "gt");
    const s = document.createElement("script");
    s.src = "https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit";
    document.head.appendChild(s);
  }

  // ---- Search overlay ----
  const overlay = $(".search-overlay");
  $(".search-btn")?.addEventListener("click", () => { overlay.classList.add("open"); overlay.querySelector("input").focus(); });
  overlay?.querySelector(".close").addEventListener("click", () => overlay.classList.remove("open"));

  // ---- Search results page ----
  const results = $("#search-results");
  if (results && window.KARAMA_INDEX) {
    const q = new URLSearchParams(location.search).get("q") || "";
    const input = $("#search-q"); if (input) input.value = q;
    const base = results.dataset.base || "";
    const terms = q.toLowerCase().split(/\s+/).filter(Boolean);
    const hits = terms.length ? KARAMA_INDEX.map(p => {
      const hay = (p.t + " " + p.d + " " + p.k).toLowerCase();
      const score = terms.reduce((s, t) => s + (hay.includes(t) ? (p.t.toLowerCase().includes(t) ? 3 : 1) : -99), 0);
      return { p, score };
    }).filter(h => h.score > 0).sort((a, b) => b.score - a.score) : [];
    $("#search-count").textContent = terms.length ? `${hits.length} result${hits.length === 1 ? "" : "s"} for “${q}”` : "Type a word above to search the site.";
    results.innerHTML = hits.map(({ p }) => `<li><a href="${base}${p.u}">${p.t}</a><p>${p.d}</p></li>`).join("");
  }

  // ---- Interactive content pane (tabs) ----
  $$(".icp").forEach(icp => {
    const tabs = $$(".tabs button", icp), panes = $$(".pane", icp);
    const show = i => { tabs.forEach((t, j) => t.setAttribute("aria-selected", i === j)); panes.forEach((p, j) => p.classList.toggle("active", i === j)); };
    tabs.forEach((t, i) => { t.addEventListener("click", () => show(i)); t.addEventListener("mouseenter", () => show(i)); });
  });

  // ---- Secondary nav toggle (mobile) ----
  $$(".secnav .toggle").forEach(b => b.addEventListener("click", () => {
    const nav = b.closest(".secnav"); const open = nav.classList.toggle("open"); b.setAttribute("aria-expanded", open);
  }));

  // ---- Toggle groups (donation frequency / amount) ----
  $$("[data-group]").forEach(g => g.addEventListener("click", e => {
    const b = e.target.closest("button"); if (!b) return;
    $$("button", g).forEach(x => x.setAttribute("aria-pressed", x === b));
    const target = $(g.dataset.group);
    if (target) { target.value = b.dataset.value || ""; if (!b.dataset.value) target.focus(); target.dispatchEvent(new Event("input")); }
  }));
  const amt = $("#gift-amount"), freq = $("#gift-freq"), summary = $("#gift-summary");
  const updateGift = () => { if (summary && amt) summary.textContent = amt.value ? `$${amt.value}${freq && freq.value === "monthly" ? " every month" : " one time"}` : "Choose an amount"; };
  amt?.addEventListener("input", updateGift); freq?.addEventListener("input", updateGift); updateGift();

  // ---- Forms: no backend yet, so confirm locally ----
  $$("form[data-local]").forEach(f => f.addEventListener("submit", e => {
    e.preventDefault();
    const ok = f.querySelector(".success"); if (ok) { ok.classList.add("show"); ok.setAttribute("tabindex", "-1"); ok.focus(); }
    f.querySelectorAll("input:not([type=hidden]):not([type=checkbox]), textarea").forEach(i => (i.value = ""));
  }));

  // ---- Help finder: select → go ----
  $$("form[data-finder]").forEach(f => f.addEventListener("submit", e => {
    e.preventDefault(); const v = f.querySelector("select").value; if (v) location.href = v;
  }));

  // ---- Filters (events chips, news category + search) ----
  $$("[data-filter-list]").forEach(list => {
    const rows = $$("[data-cat]", list);
    const chips = $$(`[data-filter-for="${list.id}"] .chip`);
    const sel = $(`select[data-filter-for="${list.id}"]`);
    const txt = $(`input[data-filter-for="${list.id}"]`);
    const empty = $(`[data-empty-for="${list.id}"]`);
    const apply = () => {
      const chip = chips.find(c => c.getAttribute("aria-pressed") === "true");
      const cat = (chip && chip.dataset.value) || (sel && sel.value) || "";
      const q = (txt && txt.value.trim().toLowerCase()) || "";
      let shown = 0;
      rows.forEach(r => { const ok = (!cat || r.dataset.cat === cat) && (!q || r.textContent.toLowerCase().includes(q)); r.hidden = !ok; if (ok) shown++; });
      if (empty) empty.hidden = shown > 0;
    };
    chips.forEach(c => c.addEventListener("click", () => { chips.forEach(x => x.setAttribute("aria-pressed", x === c)); apply(); }));
    sel?.addEventListener("change", apply); txt?.addEventListener("input", apply);
    const pre = new URLSearchParams(location.search).get("type");
    if (pre) { const c = chips.find(x => x.dataset.value === pre); if (c) c.click(); if (sel) { sel.value = pre; apply(); } }
  });

  // ---- RSVP buttons pre-fill the event select ----
  $$("[data-rsvp]").forEach(a => a.addEventListener("click", () => { const s = $("#rsvp-event"); if (s) s.value = a.dataset.rsvp; }));

  // ---- Scroll reveal (content is only hidden once this script is running) ----
  const pending = new Set($$(".reveal"));
  const check = () => {
    const limit = innerHeight - 40;
    pending.forEach(el => { if (el.getBoundingClientRect().top < limit) { el.classList.add("in"); pending.delete(el); } });
    if (!pending.size) removeEventListener("scroll", check);
  };
  document.documentElement.classList.add("js");
  addEventListener("scroll", check, { passive: true }); addEventListener("resize", check);
  requestAnimationFrame(check);
})();
