import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta


# -----------------------------------------------------------------------------
# Sayfa ayarları ve kurumsal görünüm
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Lufthansa TRN Takip Portalı",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root { --navy:#05164D; --yellow:#FFAC00; --bg:#F4F6F9; --green:#16845B; }
    html, body, [class*="css"] { font-family:'Inter', sans-serif; }
    .stApp { background:var(--bg); color:#14213d; }
    .block-container { max-width:1450px; padding-top:1.4rem; padding-bottom:3rem; }
    #MainMenu, footer { visibility:hidden; }

    .hero {
        background:linear-gradient(125deg,#05164D 0%,#0A2B70 72%,#153A83 100%);
        border-radius:18px; padding:25px 28px; color:white; margin-bottom:20px;
        box-shadow:0 12px 30px rgba(5,22,77,.18); position:relative; overflow:hidden;
    }
    .hero:after { content:""; position:absolute; width:180px; height:180px;
        border:30px solid rgba(255,172,0,.14); border-radius:50%; right:-55px; top:-75px; }
    .hero-row { display:flex; gap:18px; align-items:center; position:relative; z-index:2; }
    .brand-badge { width:58px; height:58px; min-width:58px; border-radius:50%;
        display:flex; align-items:center; justify-content:center; background:#FFAC00;
        color:#05164D; font-size:28px; box-shadow:0 5px 16px rgba(0,0,0,.18); }
    .hero h1 { margin:0; font-size:clamp(1.35rem,3vw,2.15rem); letter-spacing:-.03em; }
    .hero p { margin:6px 0 0; opacity:.82; font-size:.94rem; }

    .metric-card { background:white; border-radius:14px; padding:18px 19px; min-height:125px;
        box-shadow:0 5px 18px rgba(15,33,65,.07); border-top:4px solid var(--accent); }
    .metric-label { color:#697386; font-size:.78rem; font-weight:700; text-transform:uppercase;
        letter-spacing:.055em; min-height:36px; }
    .metric-value { color:#05164D; font-size:2rem; font-weight:800; margin-top:8px; }
    .metric-note { color:#8b95a7; font-size:.73rem; margin-top:1px; }

    .section-title { color:#05164D; font-size:1.12rem; font-weight:800; margin:18px 0 10px; }
    .person-card { background:white; border:1px solid #e6eaf0; border-radius:14px;
        padding:17px 19px; margin:9px 0; box-shadow:0 3px 12px rgba(20,33,61,.05); }
    .person-head { display:flex; justify-content:space-between; gap:12px; align-items:flex-start; }
    .person-name { color:#05164D; font-size:1.04rem; font-weight:800; }
    .person-id { color:#7d8797; font-size:.78rem; margin-top:2px; }
    .status { display:inline-block; border-radius:999px; padding:5px 10px; font-size:.72rem;
        font-weight:700; white-space:nowrap; background:#eef1f6; color:#39445a; }
    .status.ok { background:#e3f5ed; color:#087348; }
    .status.warn { background:#fff0d1; color:#9b5c00; }
    .status.done { background:#e7edff; color:#173b94; }
    .detail-grid { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:11px;
        margin-top:15px; padding-top:14px; border-top:1px solid #edf0f4; }
    .detail-label { color:#8992a2; font-size:.69rem; font-weight:700; text-transform:uppercase; }
    .detail-value { color:#24304a; font-size:.83rem; font-weight:600; margin-top:3px; }
    div[data-testid="stForm"], div[data-testid="stFileUploader"] {
        background:white; border:1px solid #e5e9ef; border-radius:14px; padding:16px;
    }
    div[data-baseweb="tab-list"] { gap:8px; }
    button[data-baseweb="tab"] { background:white; border-radius:10px; padding:10px 16px; }
    .stButton > button, .stDownloadButton > button { border-radius:10px; font-weight:700; min-height:43px; }
    .stButton > button[kind="primary"] { background:#05164D; border-color:#05164D; }
    [data-testid="stDataFrame"] { background:white; border-radius:12px; overflow:hidden; }
    .hint { background:#eef3ff; border-left:4px solid #315aab; border-radius:8px;
        padding:10px 13px; color:#2a3d65; font-size:.83rem; }

    @media (max-width: 768px) {
        .block-container { padding:12px 12px 35px; }
        .hero { padding:20px 17px; border-radius:14px; }
        .brand-badge { width:48px; height:48px; min-width:48px; font-size:23px; }
        .hero p { font-size:.8rem; }
        .metric-card { min-height:104px; padding:14px; margin-bottom:4px; }
        .metric-value { font-size:1.65rem; }
        .detail-grid { grid-template-columns:repeat(2,minmax(0,1fr)); }
        .person-head { flex-direction:column; }
        .stButton > button, .stDownloadButton > button { width:100%; }
        div[data-testid="stHorizontalBlock"] { gap:.55rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------------------------------------------------------
# Veri motoru ve yardımcı fonksiyonlar
# -----------------------------------------------------------------------------
STATUSES = [
    "Sınıf Eğitimi",
    "Kontuar TRN (Devam Ediyor)",
    "Değerlendirme Aşaması",
    "Release Verildi",
    "Aksiyon Gerekiyor",
]


def calculate_dates(start_value):
    """Başlangıçtan itibaren hedef tarihi ve bugüne göre kalan günü hesaplar."""
    if isinstance(start_value, datetime):
        start_value = start_value.date()
    elif isinstance(start_value, str):
        start_value = pd.to_datetime(start_value).date()
    target = start_value + timedelta(days=60)
    return target, (target - date.today()).days


def sample_records():
    """Sunumda ilk açılışı dolu gösterecek, farklı aşamalardaki örnek kayıtlar."""
    today = date.today()
    seeds = [
        ("TR1042", "Ahmet Yılmaz", "Selin Kaya", 18, True, "Kontuar TRN (Devam Ediyor)", "İletişimi güçlü, DCS ekranlarına hızlı adapte oluyor.", ""),
        ("TR1087", "Elif Demir", "Murat Aksoy", 63, True, "Değerlendirme Aşaması", "Bagaj ve doküman kontrolünde bağımsız çalışabiliyor.", "Final gözlem vardiyası planlanacak."),
        ("TR1115", "Can Eren", "Selin Kaya", 41, False, "Aksiyon Gerekiyor", "Mentorla yalnızca iki ortak vardiya gerçekleşti.", "Vardiya eşleşmesi revize edilmeli."),
        ("TR1168", "Zeynep Arslan", "Burak Şahin", 76, True, "Release Verildi", "Tüm işlem adımlarında yeterli performans gösterdi.", "Release onayı tamamlandı."),
        ("TR1203", "Mert Çelik", "Murat Aksoy", 7, True, "Sınıf Eğitimi", "Sınıf eğitimine katılımı düzenli.", ""),
        ("TR1249", "Derya Koç", "Burak Şahin", 58, True, "Kontuar TRN (Devam Ediyor)", "Yoğun uçuşlarda hız ve doğruluk gelişiyor.", "60. gün değerlendirmesi bekleniyor."),
    ]
    records = []
    for sicil, name, mentor, elapsed, compatible, status, note, comment in seeds:
        start = today - timedelta(days=elapsed)
        class_start = start - timedelta(days=5)
        target, remaining = calculate_dates(start)
        records.append({
            "sicil_no": sicil,
            "ad_soyad": name,
            "sinif_egitimi_tarihleri": f"{class_start:%d.%m.%Y} - {(class_start + timedelta(days=2)):%d.%m.%Y}",
            "mentor_ad_soyad": mentor,
            "vardiya_uyumu": compatible,
            "kontuar_trn_baslangic": start,
            "hedef_release_tarihi": target,
            "kalan_gun": remaining,
            "mentor_notu": note,
            "lufthansa_release_aciklama": comment,
            "durum": status,
        })
    return records


def refresh_calculated_fields():
    for record in st.session_state.personnel:
        target, remaining = calculate_dates(record["kontuar_trn_baslangic"])
        record["hedef_release_tarihi"] = target
        record["kalan_gun"] = remaining


def dataframe_for_export(records):
    export_df = pd.DataFrame(records).copy()
    if export_df.empty:
        return export_df
    export_df["vardiya_uyumu"] = export_df["vardiya_uyumu"].map({True: "Uyumlu", False: "Aksiyon Gerekiyor"})
    for col in ["kontuar_trn_baslangic", "hedef_release_tarihi"]:
        export_df[col] = export_df[col].apply(lambda x: x.strftime("%d.%m.%Y") if hasattr(x, "strftime") else x)
    return export_df


if "personnel" not in st.session_state:
    st.session_state.personnel = sample_records()
refresh_calculated_fields()


# -----------------------------------------------------------------------------
# Üst panel ve KPI kartları
# -----------------------------------------------------------------------------
st.markdown(
    """
    <div class="hero"><div class="hero-row">
      <div class="brand-badge">✈</div>
      <div><h1>Lufthansa TRN Takip ve Yönetim Portalı</h1>
      <p>Yer hizmetleri personelinin sınıf eğitimi, mentorluk, kontuar TRN ve release süreçlerini tek noktadan yönetin.</p></div>
    </div></div>
    """,
    unsafe_allow_html=True,
)

records = st.session_state.personnel
total = len(records)
active = sum(r["durum"] == "Kontuar TRN (Devam Ediyor)" for r in records)
due = sum(r["kalan_gun"] <= 0 and r["durum"] != "Release Verildi" for r in records)
action = sum((not r["vardiya_uyumu"]) or r["durum"] == "Aksiyon Gerekiyor" for r in records)

metric_data = [
    ("Toplam Menti", total, "Kayıtlı personel", "#315AAB"),
    ("Aktif Kontuar TRN", active, "Eğitimi devam eden", "#FFAC00"),
    ("Süresi Dolan / Değerlendirmede", due, "60 gününü tamamlayan", "#16845B"),
    ("Aksiyon Gereken", action, "Vardiya veya süreç", "#D64545"),
]
metric_cols = st.columns(4)
for col, (label, value, note, color) in zip(metric_cols, metric_data):
    col.markdown(
        f'<div class="metric-card" style="--accent:{color}"><div class="metric-label">{label}</div>'
        f'<div class="metric-value">{value}</div><div class="metric-note">{note}</div></div>',
        unsafe_allow_html=True,
    )


# -----------------------------------------------------------------------------
# Filtreler ve yönetim araçları
# -----------------------------------------------------------------------------
st.markdown('<div class="section-title">Personel ve Süreç Kontrolü</div>', unsafe_allow_html=True)
f1, f2, f3 = st.columns([1.5, 1.25, 1])
with f1:
    search_text = st.text_input("Arama", placeholder="Sicil no, personel veya mentor...", label_visibility="collapsed")
with f2:
    selected_statuses = st.multiselect("Durum", STATUSES, placeholder="Tüm durumlar", label_visibility="collapsed")
with f3:
    only_actions = st.toggle("Yalnızca aksiyon gerekenler")

q = search_text.casefold().strip()
filtered = []
for r in records:
    searchable = f'{r["sicil_no"]} {r["ad_soyad"]} {r["mentor_ad_soyad"]}'.casefold()
    if q and q not in searchable:
        continue
    if selected_statuses and r["durum"] not in selected_statuses:
        continue
    if only_actions and r["vardiya_uyumu"] and r["durum"] != "Aksiyon Gerekiyor":
        continue
    filtered.append(r)

toolbar1, toolbar2, toolbar3 = st.columns([1.3, 1, 1])
with toolbar1:
    st.caption(f"{len(filtered)} kayıt gösteriliyor · Son kontrol: {datetime.now():%d.%m.%Y %H:%M}")
with toolbar2:
    csv_bytes = dataframe_for_export(records).to_csv(index=False, sep=";", encoding="utf-8-sig").encode("utf-8-sig")
    st.download_button(
        "⬇ CSV / Excel Uyumlu İndir",
        data=csv_bytes,
        file_name=f"lufthansa_trn_{date.today():%Y%m%d}.csv",
        mime="text/csv",
        use_container_width=True,
    )
with toolbar3:
    if st.button("↻ Verileri Sıfırla / Örnek Yükle", use_container_width=True):
        st.session_state.personnel = sample_records()
        st.toast("Örnek veriler yeniden yüklendi.", icon="✅")
        st.rerun()


# -----------------------------------------------------------------------------
# Modern personel kartları
# -----------------------------------------------------------------------------
if not filtered:
    st.info("Seçili filtrelere uyan personel bulunamadı.")

for r in filtered:
    elapsed = max(0, 60 - r["kalan_gun"])
    eligible = r["kalan_gun"] <= 0
    if r["durum"] == "Release Verildi":
        badge_text, badge_class = "✓ Release Verildi", "done"
    elif eligible:
        badge_text, badge_class = "✓ Release İçin Uygun", "ok"
    elif not r["vardiya_uyumu"] or r["durum"] == "Aksiyon Gerekiyor":
        badge_text, badge_class = "! Aksiyon Gerekiyor", "warn"
    else:
        badge_text, badge_class = f"{r['kalan_gun']} Gün Kaldı", ""

    st.markdown(
        f"""
        <div class="person-card">
          <div class="person-head"><div><div class="person-name">{r['ad_soyad']}</div>
          <div class="person-id">{r['sicil_no']} · {r['durum']}</div></div>
          <span class="status {badge_class}">{badge_text}</span></div>
          <div class="detail-grid">
            <div><div class="detail-label">Mentor</div><div class="detail-value">{r['mentor_ad_soyad']}</div></div>
            <div><div class="detail-label">Vardiya Uyumu</div><div class="detail-value">{'✓ Uyumlu' if r['vardiya_uyumu'] else '⚠ Aksiyon Gerekli'}</div></div>
            <div><div class="detail-label">TRN Başlangıcı</div><div class="detail-value">{r['kontuar_trn_baslangic']:%d.%m.%Y}</div></div>
            <div><div class="detail-label">Hedef Release</div><div class="detail-value">{r['hedef_release_tarihi']:%d.%m.%Y} · {elapsed}. gün</div></div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------------------------------------------------------
# Hızlı işlem sekmeleri
# -----------------------------------------------------------------------------
st.markdown('<div class="section-title">Hızlı İşlemler</div>', unsafe_allow_html=True)
tab_new, tab_review, tab_bulk = st.tabs([
    "＋ Yeni Personel Kaydı",
    "✓ Mentor & Release Değerlendirme",
    "⇧ Toplu Veri Yükleme",
])

with tab_new:
    mentor_options = sorted({r["mentor_ad_soyad"] for r in records}) or ["Mentor Atanmadı"]
    with st.form("new_person_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            new_id = st.text_input("Sicil No *", placeholder="TR1250")
            new_name = st.text_input("Ad Soyad *", placeholder="Ad Soyad")
            class_start = st.date_input("3 Günlük Sınıf Eğitimi Başlangıcı", value=date.today())
        with c2:
            new_mentor = st.selectbox("Mentor", mentor_options)
            new_compatible = st.checkbox("Mentor–menti vardiyası uyumlu", value=True)
            new_start = st.date_input("Kontuar TRN Başlangıç Tarihi", value=date.today())
        auto_target = new_start + timedelta(days=60)
        st.markdown(f'<div class="hint">Otomatik hedef release tarihi: <b>{auto_target:%d.%m.%Y}</b></div>', unsafe_allow_html=True)
        submitted = st.form_submit_button("Personeli Kaydet", type="primary", use_container_width=True)

    if submitted:
        clean_id, clean_name = new_id.strip().upper(), new_name.strip()
        if not clean_id or not clean_name:
            st.error("Sicil no ve ad soyad alanları zorunludur.")
        elif any(r["sicil_no"].upper() == clean_id for r in records):
            st.error("Bu sicil numarasıyla daha önce kayıt oluşturulmuş.")
        else:
            target, remaining = calculate_dates(new_start)
            status = "Kontuar TRN (Devam Ediyor)" if new_compatible else "Aksiyon Gerekiyor"
            st.session_state.personnel.append({
                "sicil_no": clean_id,
                "ad_soyad": clean_name,
                "sinif_egitimi_tarihleri": f"{class_start:%d.%m.%Y} - {(class_start + timedelta(days=2)):%d.%m.%Y}",
                "mentor_ad_soyad": new_mentor,
                "vardiya_uyumu": new_compatible,
                "kontuar_trn_baslangic": new_start,
                "hedef_release_tarihi": target,
                "kalan_gun": remaining,
                "mentor_notu": "",
                "lufthansa_release_aciklama": "",
                "durum": status,
            })
            st.toast(f"{clean_name} başarıyla kaydedildi.", icon="✅")
            st.rerun()

with tab_review:
    if not records:
        st.info("Değerlendirilecek personel bulunmuyor.")
    else:
        labels = {f'{r["sicil_no"]} — {r["ad_soyad"]}': i for i, r in enumerate(records)}
        selection = st.selectbox("Personel Seçimi", list(labels.keys()))
        selected_index = labels[selection]
        selected = records[selected_index]
        eligible = selected["kalan_gun"] <= 0

        i1, i2, i3 = st.columns(3)
        i1.metric("TRN Başlangıcı", selected["kontuar_trn_baslangic"].strftime("%d.%m.%Y"))
        i2.metric("Hedef Tarih", selected["hedef_release_tarihi"].strftime("%d.%m.%Y"))
        i3.metric("Süre", "Uygun" if eligible else f'{selected["kalan_gun"]} gün kaldı')

        with st.form("review_form"):
            mentor_note = st.text_area("Mentor Notu", value=selected["mentor_notu"], height=110)
            station_comment = st.text_area(
                "Lufthansa İstasyon / Release Açıklaması",
                value=selected["lufthansa_release_aciklama"],
                height=110,
            )
            new_shift_fit = st.checkbox("Mentor–menti vardiyası uyumlu", value=selected["vardiya_uyumu"])
            save_notes = st.form_submit_button("Değerlendirmeyi Kaydet", use_container_width=True)

        if save_notes:
            selected["mentor_notu"] = mentor_note.strip()
            selected["lufthansa_release_aciklama"] = station_comment.strip()
            selected["vardiya_uyumu"] = new_shift_fit
            if not new_shift_fit and selected["durum"] != "Release Verildi":
                selected["durum"] = "Aksiyon Gerekiyor"
            st.toast("Değerlendirme güncellendi.", icon="✅")
            st.rerun()

        if not eligible:
            st.warning(
                f"Kural İhlali: Minimum 60 günlük kontuar süresi dolmadan release verilemez. "
                f"Kalan: {selected['kalan_gun']} gün."
            )
        elif not selected["vardiya_uyumu"]:
            st.warning("Release öncesinde mentor–menti vardiya uyum aksiyonu kapatılmalıdır.")

        release_disabled = (not eligible) or (not selected["vardiya_uyumu"]) or selected["durum"] == "Release Verildi"
        if st.button("✓ Nihai Release Onayla", type="primary", disabled=release_disabled, use_container_width=True):
            selected["durum"] = "Release Verildi"
            if not selected["lufthansa_release_aciklama"]:
                selected["lufthansa_release_aciklama"] = f"Release {date.today():%d.%m.%Y} tarihinde onaylandı."
            st.toast(f'{selected["ad_soyad"]} için release onaylandı.', icon="✅")
            st.rerun()

with tab_bulk:
    st.markdown(
        '<div class="hint"><b>Gelecek entegrasyonu:</b> Standart şablonu doldurup CSV veya XLSX olarak yükleyebilirsiniz. '
        'Sicil numarası mevcut olan satırlar mükerrer kayıt oluşmaması için atlanır.</div>',
        unsafe_allow_html=True,
    )
    template_columns = [
        "sicil_no", "ad_soyad", "sinif_egitimi_tarihleri", "mentor_ad_soyad",
        "vardiya_uyumu", "kontuar_trn_baslangic", "mentor_notu",
        "lufthansa_release_aciklama", "durum",
    ]
    template_df = pd.DataFrame(columns=template_columns)
    st.download_button(
        "⬇ Toplu Veri Yükleme Şablonunu İndir",
        data=template_df.to_csv(index=False, sep=";", encoding="utf-8-sig").encode("utf-8-sig"),
        file_name="lufthansa_trn_yukleme_sablonu.csv",
        mime="text/csv",
        use_container_width=True,
    )
    uploaded = st.file_uploader("CSV / Excel Dosyası Seç", type=["csv", "xlsx", "xls"])
    if uploaded is not None:
        try:
            if uploaded.name.lower().endswith(".csv"):
                try:
                    incoming = pd.read_csv(uploaded, sep=None, engine="python")
                except UnicodeDecodeError:
                    uploaded.seek(0)
                    incoming = pd.read_csv(uploaded, sep=None, engine="python", encoding="latin-1")
            else:
                incoming = pd.read_excel(uploaded)

            missing = [c for c in template_columns[:6] if c not in incoming.columns]
            if missing:
                st.error("Eksik zorunlu sütunlar: " + ", ".join(missing))
            else:
                st.dataframe(incoming.head(20), use_container_width=True, hide_index=True)
                if st.button("Dosyadaki Kayıtları Listeye Ekle", type="primary", use_container_width=True):
                    known_ids = {r["sicil_no"].upper() for r in records}
                    added, skipped = 0, 0
                    for _, row in incoming.iterrows():
                        sicil = str(row.get("sicil_no", "")).strip().upper()
                        name = str(row.get("ad_soyad", "")).strip()
                        if not sicil or not name or sicil in known_ids:
                            skipped += 1
                            continue
                        start = pd.to_datetime(row["kontuar_trn_baslangic"], dayfirst=True).date()
                        target, remaining = calculate_dates(start)
                        raw_fit = str(row.get("vardiya_uyumu", "")).strip().casefold()
                        fit = raw_fit in {"true", "1", "evet", "uyumlu", "yes"}
                        status = str(row.get("durum", "Kontuar TRN (Devam Ediyor)")).strip()
                        if status not in STATUSES:
                            status = "Kontuar TRN (Devam Ediyor)" if fit else "Aksiyon Gerekiyor"
                        records.append({
                            "sicil_no": sicil,
                            "ad_soyad": name,
                            "sinif_egitimi_tarihleri": str(row.get("sinif_egitimi_tarihleri", "")),
                            "mentor_ad_soyad": str(row.get("mentor_ad_soyad", "Atanmadı")),
                            "vardiya_uyumu": fit,
                            "kontuar_trn_baslangic": start,
                            "hedef_release_tarihi": target,
                            "kalan_gun": remaining,
                            "mentor_notu": "" if pd.isna(row.get("mentor_notu")) else str(row.get("mentor_notu", "")),
                            "lufthansa_release_aciklama": "" if pd.isna(row.get("lufthansa_release_aciklama")) else str(row.get("lufthansa_release_aciklama", "")),
                            "durum": status,
                        })
                        known_ids.add(sicil)
                        added += 1
                    st.toast(f"{added} kayıt eklendi, {skipped} kayıt atlandı.", icon="✅")
                    st.rerun()
        except ImportError:
            st.error("Excel dosyasını okumak için ortamda Excel motoru bulunmuyor. Dosyayı CSV olarak kaydedip tekrar yükleyin.")
        except Exception as exc:
            st.error(f"Dosya okunamadı: {exc}")

st.caption("Lufthansa TRN Portalı · Operasyonel prototip · Minimum kontuar eğitim süresi: 60 gün")
