import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta


# =============================================================================
# SAYFA AYARLARI VE KURUMSAL TASARIM
# =============================================================================
st.set_page_config(
    page_title="İstasyon TRN Takip Portalı",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --navy:#05164D;
        --yellow:#FFAC00;
        --bg:#F4F6F9;
        --white:#FFFFFF;
        --green:#16845B;
        --red:#C93F49;
        --text:#18243D;
        --muted:#738096;
    }

    html, body, [class*="css"] {
        font-family:'Inter', sans-serif;
    }

    .stApp {
        background:var(--bg);
        color:var(--text);
    }

    .block-container {
        max-width:1450px;
        padding-top:1.35rem;
        padding-bottom:3rem;
    }

    #MainMenu, footer {
        visibility:hidden;
    }

    .hero {
        background:linear-gradient(
            125deg,
            #05164D 0%,
            #0A2B70 72%,
            #153A83 100%
        );
        border-radius:18px;
        padding:24px 28px;
        color:white;
        margin-bottom:18px;
        box-shadow:0 12px 30px rgba(5,22,77,.18);
        position:relative;
        overflow:hidden;
    }

    .hero:after {
        content:"";
        position:absolute;
        width:180px;
        height:180px;
        border:30px solid rgba(255,172,0,.14);
        border-radius:50%;
        right:-55px;
        top:-76px;
    }

    .hero-row {
        display:flex;
        gap:17px;
        align-items:center;
        position:relative;
        z-index:2;
    }

    .brand-badge {
        width:58px;
        height:58px;
        min-width:58px;
        border-radius:50%;
        display:flex;
        align-items:center;
        justify-content:center;
        background:var(--yellow);
        color:var(--navy);
        font-size:28px;
        box-shadow:0 5px 16px rgba(0,0,0,.18);
    }

    .hero h1 {
        margin:0;
        font-size:clamp(1.35rem,3vw,2.15rem);
        letter-spacing:-.03em;
    }

    .hero p {
        margin:6px 0 0;
        opacity:.82;
        font-size:.92rem;
    }

    .login-wrap {
        max-width:760px;
        margin:16px auto 0;
    }

    div[data-testid="stForm"] {
        background:white;
        border:1px solid #E4E9F0;
        border-radius:14px;
        padding:18px;
        box-shadow:0 5px 18px rgba(15,33,65,.06);
    }

    .eyebrow {
        color:#8C6500;
        font-size:.72rem;
        font-weight:800;
        letter-spacing:.08em;
        text-transform:uppercase;
        margin-bottom:5px;
    }

    .section-title {
        color:var(--navy);
        font-size:1.12rem;
        font-weight:800;
        margin:18px 0 10px;
    }

    .subtle {
        color:var(--muted);
        font-size:.8rem;
    }

    .metric-card {
        background:white;
        border-radius:14px;
        padding:17px 18px;
        min-height:120px;
        box-shadow:0 5px 18px rgba(15,33,65,.07);
        border-top:4px solid var(--accent);
    }

    .metric-label {
        color:#697386;
        font-size:.75rem;
        font-weight:700;
        text-transform:uppercase;
        letter-spacing:.05em;
        min-height:35px;
    }

    .metric-value {
        color:var(--navy);
        font-size:1.9rem;
        font-weight:800;
        margin-top:7px;
    }

    .metric-note {
        color:#8B95A7;
        font-size:.72rem;
    }

    .info-card {
        background:white;
        border:1px solid #E5EAF0;
        border-radius:13px;
        padding:15px 17px;
        box-shadow:0 3px 12px rgba(20,33,61,.05);
        height:100%;
    }

    .info-label {
        color:#8893A4;
        font-size:.69rem;
        text-transform:uppercase;
        font-weight:800;
    }

    .info-value {
        color:var(--navy);
        font-size:1rem;
        font-weight:750;
        margin-top:3px;
    }

    .demo-box {
        background:#FFF8E5;
        border:1px solid #F0D58C;
        border-radius:10px;
        padding:11px 13px;
        color:#68501B;
        font-size:.78rem;
    }

    .hint {
        background:#EDF3FF;
        border-left:4px solid #315AAB;
        border-radius:8px;
        padding:10px 13px;
        color:#2A3D65;
        font-size:.82rem;
    }

    .audit-note {
        background:#FFFFFF;
        border:1px solid #E5E9EF;
        border-radius:11px;
        padding:12px 14px;
        margin:7px 0;
    }

    .stButton > button,
    .stDownloadButton > button {
        border-radius:10px;
        font-weight:700;
        min-height:43px;
        width:100%;
    }

    .stButton > button[kind="primary"] {
        background:var(--navy);
        border-color:var(--navy);
    }

    div[data-baseweb="tab-list"] {
        gap:7px;
    }

    button[data-baseweb="tab"] {
        background:white;
        border-radius:10px;
        padding:9px 15px;
    }

    [data-testid="stDataFrame"] {
        background:white;
        border-radius:12px;
        overflow:auto;
    }

    @media (max-width:768px) {
        .block-container {
            padding:11px 11px 34px;
        }

        .hero {
            padding:19px 16px;
            border-radius:14px;
        }

        .brand-badge {
            width:47px;
            height:47px;
            min-width:47px;
            font-size:22px;
        }

        .hero p {
            font-size:.78rem;
        }

        .metric-card {
            min-height:103px;
            padding:13px;
            margin-bottom:4px;
        }

        .metric-value {
            font-size:1.55rem;
        }

        div[data-testid="stHorizontalBlock"] {
            gap:.55rem;
        }

        .stButton > button,
        .stDownloadButton > button {
            width:100%;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =============================================================================
# SABİTLER VE ÖRNEK VERİ ÜRETİCİLERİ
# =============================================================================
ADMIN_PASSWORD = "chef2026"

FLIGHTS = [
    "FL1299 - A320 / MUC",
    "FL1301 - A321 / FRA",
    "FL1305 - A320 / FRA",
    "FL1313 - A321 / MUC",
    "FL1407 - A320 / STR",
    "FL1411 - A321 / DUS",
]

DUTIES = [
    "Check-in İşlemleri",
    "Boarding Operasyonu",
    "Doküman Kontrolü",
    "Bagaj / Gate Sorun Çözümü",
    "Transfer Yolcu İşlemleri",
    "Özel Hizmet Gerektiren Yolcu",
]

SHIFTS = [
    "03:40–11:40",
    "09:00–17:00",
    "14:30–22:30",
    "Diğer",
]

COMPETENCIES = [
    "Başarılı",
    "Geliştirilmeli",
    "Kritik Hata",
]

PROCESS_STATUSES = [
    "Eğitimde",
    "İzlemede",
    "Değerlendirme Aşaması",
    "Release Uygun",
    "Release Verildi",
]


def seed_users():
    """Prototip için örnek mentor hesaplarını döndürür."""
    return {
        "selin.kaya": {
            "password": "mentor123",
            "full_name": "Selin Kaya",
        },
        "murat.aksoy": {
            "password": "mentor123",
            "full_name": "Murat Aksoy",
        },
        "burak.sahin": {
            "password": "mentor123",
            "full_name": "Burak Şahin",
        },
    }


def seed_trainees():
    """Mentor atamalarını içeren örnek TRN personel havuzu."""
    return [
        {
            "code": "TR1042",
            "name": "Ahmet Yılmaz",
            "mentor": "selin.kaya",
            "status": "Eğitimde",
        },
        {
            "code": "TR1087",
            "name": "Elif Demir",
            "mentor": "murat.aksoy",
            "status": "Değerlendirme Aşaması",
        },
        {
            "code": "TR1115",
            "name": "Can Eren",
            "mentor": "selin.kaya",
            "status": "İzlemede",
        },
        {
            "code": "TR1168",
            "name": "Zeynep Arslan",
            "mentor": "burak.sahin",
            "status": "Release Uygun",
        },
        {
            "code": "TR1203",
            "name": "Mert Çelik",
            "mentor": "murat.aksoy",
            "status": "Eğitimde",
        },
        {
            "code": "TR1249",
            "name": "Derya Koç",
            "mentor": "burak.sahin",
            "status": "İzlemede",
        },
    ]


def seed_evaluations():
    """IST çıkışlı maskeli uçuşlarla örnek değerlendirmeler."""
    today = date.today()

    samples = [
        (
            "EV-0001",
            8,
            "selin.kaya",
            "Selin Kaya",
            "TR1042",
            "Ahmet Yılmaz",
            "09:00–17:00",
            FLIGHTS[1],
            DUTIES[0],
            4,
            "Başarılı",
            "DCS adımlarını doğru uyguladı; işlem hızı gelişiyor.",
            "Yoğun uçuşta süre takibi yapılacak.",
            "Eğitimde",
        ),
        (
            "EV-0002",
            7,
            "murat.aksoy",
            "Murat Aksoy",
            "TR1087",
            "Elif Demir",
            "03:40–11:40",
            FLIGHTS[0],
            DUTIES[2],
            5,
            "Başarılı",
            "Seyahat dokümanlarını eksiksiz kontrol etti.",
            "Final gözlem planlanabilir.",
            "Release Uygun",
        ),
        (
            "EV-0003",
            5,
            "selin.kaya",
            "Selin Kaya",
            "TR1115",
            "Can Eren",
            "14:30–22:30",
            FLIGHTS[3],
            DUTIES[1],
            2,
            "Geliştirilmeli",
            "Boarding anons sıralamasında desteğe ihtiyaç duydu.",
            "Bir sonraki uçuşta anons akışı tekrar edilmeli.",
            "İzlemede",
        ),
        (
            "EV-0004",
            4,
            "burak.sahin",
            "Burak Şahin",
            "TR1168",
            "Zeynep Arslan",
            "09:00–17:00",
            FLIGHTS[4],
            DUTIES[3],
            5,
            "Başarılı",
            "Irregularity senaryosunu bağımsız yönetti.",
            "Release değerlendirmesi olumlu.",
            "Release Uygun",
        ),
        (
            "EV-0005",
            2,
            "murat.aksoy",
            "Murat Aksoy",
            "TR1203",
            "Mert Çelik",
            "09:00–17:00",
            FLIGHTS[2],
            DUTIES[2],
            1,
            "Kritik Hata",
            "Vize kontrol adımında doğrulama desteği gerekti.",
            "Doküman eğitimi yenilenmeli ve çift kontrol uygulanmalı.",
            "Eğitimde",
        ),
        (
            "EV-0006",
            1,
            "burak.sahin",
            "Burak Şahin",
            "TR1249",
            "Derya Koç",
            "14:30–22:30",
            FLIGHTS[5],
            DUTIES[1],
            4,
            "Başarılı",
            "Boarding kapanış ve mutabakat adımlarını doğru tamamladı.",
            "Bir ek yoğun uçuş gözlemi önerilir.",
            "İzlemede",
        ),
    ]

    output = []

    for (
        record_id,
        days_ago,
        username,
        mentor,
        code,
        trainee,
        shift,
        flight,
        duty,
        score,
        competency,
        note,
        action,
        status,
    ) in samples:
        operation_day = today - timedelta(days=days_ago)

        output.append(
            {
                "kayit_id": record_id,
                "zaman_damgasi": f"{operation_day:%Y-%m-%d} 12:00:00",
                "mentor_kullanici": username,
                "mentor_ad_soyad": mentor,
                "trn_sicil": code,
                "trn_ad_soyad": trainee,
                "operasyon_tarihi": operation_day,
                "vardiya": shift,
                "ucus_bilgisi": flight,
                "gorev_alani": duty,
                "mentor_puani": score,
                "yetkinlik_seviyesi": competency,
                "degerlendirme_notu": note,
                "aksiyon_maddeleri": action,
                "surec_durumu": status,
                "son_guncelleme": (
                    f"{operation_day:%Y-%m-%d} 12:00:00"
                ),
            }
        )

    return output


# =============================================================================
# SESSION STATE VE ORTAK YARDIMCI FONKSİYONLAR
# =============================================================================
def initialize_state():
    defaults = {
        "users": seed_users(),
        "trainees": seed_trainees(),
        "evaluations": seed_evaluations(),
        "authenticated": False,
        "role": None,
        "username": None,
        "full_name": None,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def logout():
    """Aktif kullanıcının oturumunu kapatır."""
    st.session_state.authenticated = False
    st.session_state.role = None
    st.session_state.username = None
    st.session_state.full_name = None


def reset_demo_data():
    """Kullanıcı, personel ve değerlendirme verilerini yeniler."""
    st.session_state.users = seed_users()
    st.session_state.trainees = seed_trainees()
    st.session_state.evaluations = seed_evaluations()


def make_record_id():
    """Her değerlendirme için benzersiz kayıt numarası üretir."""
    return "EV-" + datetime.now().strftime("%Y%m%d%H%M%S%f")


def trainee_label(item):
    """TRN personelini sicil ve ad soyad ile görüntüler."""
    return f"{item['code']} - {item['name']}"


def evaluations_dataframe(records):
    """Değerlendirme listesini düzenli DataFrame'e dönüştürür."""
    columns = [
        "kayit_id",
        "zaman_damgasi",
        "mentor_ad_soyad",
        "trn_sicil",
        "trn_ad_soyad",
        "operasyon_tarihi",
        "vardiya",
        "ucus_bilgisi",
        "gorev_alani",
        "mentor_puani",
        "yetkinlik_seviyesi",
        "degerlendirme_notu",
        "aksiyon_maddeleri",
        "surec_durumu",
        "son_guncelleme",
    ]

    df = pd.DataFrame(records)

    if df.empty:
        return pd.DataFrame(columns=columns)

    for column in columns:
        if column not in df.columns:
            df[column] = ""

    return df[columns].sort_values(
        ["operasyon_tarihi", "zaman_damgasi"],
        ascending=False,
    )


def csv_bytes(records):
    """Kayıtları Excel'in açabileceği UTF-8 CSV verisine çevirir."""
    return (
        evaluations_dataframe(records)
        .to_csv(
            index=False,
            sep=";",
            encoding="utf-8-sig",
        )
        .encode("utf-8-sig")
    )


def render_header(subtitle):
    """Kurumsal üst başlığı oluşturur."""
    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-row">
                <div class="brand-badge">✈</div>
                <div>
                    <h1>İstasyon TRN Takip ve Değerlendirme Portalı</h1>
                    <p>{subtitle}</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_metric(label, value, note, color):
    """Özel tasarımlı KPI kartı oluşturur."""
    st.markdown(
        f"""
        <div class="metric-card" style="--accent:{color}">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


initialize_state()


# =============================================================================
# GİRİŞ VE MENTOR KAYIT EKRANI
# =============================================================================
def authentication_page():
    render_header(
        "Yolcu Hizmetleri On-the-Job Training süreçleri için "
        "güvenli operasyon portalı"
    )

    st.markdown(
        '<div class="login-wrap">',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="eyebrow">Yetkilendirilmiş Erişim</div>',
        unsafe_allow_html=True,
    )

    login_tab, signup_tab = st.tabs(
        [
            "Giriş Yap",
            "Mentor Hesabı Oluştur",
        ]
    )

    with login_tab:
        role_choice = st.radio(
            "Giriş profili",
            ["Mentor", "Yetkili / Şef"],
            horizontal=True,
            key="login_role_choice",
        )

        if role_choice == "Mentor":
            with st.form("mentor_login"):
                username = st.text_input(
                    "Kullanıcı Adı",
                    placeholder="ad.soyad",
                )

                password = st.text_input(
                    "Şifre",
                    type="password",
                )

                submitted = st.form_submit_button(
                    "Mentor Girişi",
                    type="primary",
                    use_container_width=True,
                )

            if submitted:
                key = username.strip().lower()
                user = st.session_state.users.get(key)

                if user and user["password"] == password:
                    st.session_state.authenticated = True
                    st.session_state.role = "mentor"
                    st.session_state.username = key
                    st.session_state.full_name = user["full_name"]

                    st.toast(
                        "Giriş başarılı.",
                        icon="✅",
                    )
                    st.rerun()

                else:
                    st.error(
                        "Kullanıcı adı veya şifre hatalı."
                    )

            st.markdown(
                """
                <div class="demo-box">
                    <b>Demo mentor:</b> selin.kaya
                    &nbsp;·&nbsp;
                    <b>Şifre:</b> mentor123
                </div>
                """,
                unsafe_allow_html=True,
            )

        else:
            with st.form("admin_login"):
                admin_password = st.text_input(
                    "Yetkili / Şef Parolası",
                    type="password",
                )

                submitted = st.form_submit_button(
                    "Yetkili Konsoluna Gir",
                    type="primary",
                    use_container_width=True,
                )

            if submitted:
                if admin_password == ADMIN_PASSWORD:
                    st.session_state.authenticated = True
                    st.session_state.role = "admin"
                    st.session_state.username = "admin"
                    st.session_state.full_name = "Yetkili / Şef"

                    st.toast(
                        "Yetkili girişi başarılı.",
                        icon="✅",
                    )
                    st.rerun()

                else:
                    st.error(
                        "Yetkili parolası hatalı."
                    )

            st.markdown(
                """
                <div class="demo-box">
                    <b>Demo yetkili parolası:</b> chef2026
                </div>
                """,
                unsafe_allow_html=True,
            )

    with signup_tab:
        with st.form(
            "mentor_signup",
            clear_on_submit=True,
        ):
            full_name = st.text_input(
                "Ad Soyad *",
                placeholder="Ad Soyad",
            )

            new_username = st.text_input(
                "Kullanıcı Adı *",
                placeholder="ad.soyad",
            )

            column1, column2 = st.columns(2)

            with column1:
                new_password = st.text_input(
                    "Şifre *",
                    type="password",
                )

            with column2:
                confirm_password = st.text_input(
                    "Şifre Tekrar *",
                    type="password",
                )

            accepted = st.checkbox(
                "Bilgilerimin bu prototip oturumunda "
                "saklanmasını kabul ediyorum."
            )

            created = st.form_submit_button(
                "Mentor Hesabı Oluştur",
                type="primary",
                use_container_width=True,
            )

        if created:
            key = new_username.strip().lower()

            if (
                not full_name.strip()
                or not key
                or not new_password
            ):
                st.error(
                    "Tüm zorunlu alanları doldurun."
                )

            elif " " in key:
                st.error(
                    "Kullanıcı adında boşluk kullanılamaz."
                )

            elif key in st.session_state.users:
                st.error(
                    "Bu kullanıcı adı zaten kayıtlı."
                )

            elif len(new_password) < 6:
                st.error(
                    "Şifre en az 6 karakter olmalıdır."
                )

            elif new_password != confirm_password:
                st.error(
                    "Şifreler eşleşmiyor."
                )

            elif not accepted:
                st.error(
                    "Devam etmek için oturum içi saklama "
                    "onayını işaretleyin."
                )

            else:
                st.session_state.users[key] = {
                    "password": new_password,
                    "full_name": full_name.strip(),
                }

                st.success(
                    "Mentor hesabı oluşturuldu. "
                    "Giriş sekmesinden oturum açabilirsiniz."
                )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )


# =============================================================================
# MENTOR PANELİ
# =============================================================================
def mentor_panel():
    username = st.session_state.username
    full_name = st.session_state.full_name

    render_header(
        f"Mentor Paneli · Hoş geldiniz, {full_name}"
    )

    top1, top2, top3 = st.columns([2, 1, 1])

    with top1:
        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-label">Aktif Kullanıcı</div>
                <div class="info-value">{full_name}</div>
                <div class="subtle">Mentor yetkisi</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with top2:
        my_count = sum(
            record["mentor_kullanici"] == username
            for record in st.session_state.evaluations
        )

        render_metric(
            "Kayıtlarım",
            my_count,
            "Toplam değerlendirme",
            "#315AAB",
        )

    with top3:
        if st.button(
            "Güvenli Çıkış",
            use_container_width=True,
        ):
            logout()
            st.rerun()

    assigned = [
        trainee
        for trainee in st.session_state.trainees
        if trainee["mentor"] == username
    ]

    if not assigned:
        st.info(
            "Henüz hesabınıza atanmış bir TRN personeli bulunmuyor. "
            "Yetkiliyle iletişime geçin."
        )
        return

    new_tab, history_tab, edit_tab = st.tabs(
        [
            "＋ Hızlı Uçuş Değerlendirmesi",
            "Geçmiş Kayıtlarım",
            "✎ Kayıt Düzenle",
        ]
    )

    with new_tab:
        st.markdown(
            '<div class="section-title">'
            "Yeni Operasyon Değerlendirmesi"
            "</div>",
            unsafe_allow_html=True,
        )

        with st.form(
            "new_evaluation",
            clear_on_submit=True,
        ):
            column1, column2 = st.columns(2)

            with column1:
                trainee_choice = st.selectbox(
                    "TRN Personeli *",
                    [
                        trainee_label(trainee)
                        for trainee in assigned
                    ],
                )

                operation_date = st.date_input(
                    "Operasyon Tarihi *",
                    value=date.today(),
                    max_value=date.today(),
                )

                shift = st.selectbox(
                    "Vardiya *",
                    SHIFTS,
                )

                flight = st.selectbox(
                    "IST Çıkışlı Uçuş / Uçak *",
                    FLIGHTS,
                )

            with column2:
                duty = st.selectbox(
                    "Görev / Eğitim Alanı *",
                    DUTIES,
                )

                score = st.slider(
                    "Mentor Puanı",
                    min_value=1,
                    max_value=5,
                    value=3,
                )

                competency = st.selectbox(
                    "Yetkinlik Seviyesi *",
                    COMPETENCIES,
                )

                process_status = st.selectbox(
                    "İstasyon Süreç Durumu *",
                    PROCESS_STATUSES,
                )

            note = st.text_area(
                "Detaylı Mentor Değerlendirme Notu *",
                placeholder=(
                    "Gözlenen güçlü yönleri ve geliştirilmesi "
                    "gereken noktaları yazın..."
                ),
                height=110,
            )

            actions = st.text_area(
                "Aksiyon Maddeleri",
                placeholder=(
                    "Sonraki uçuşta uygulanacak takip veya "
                    "eğitim aksiyonları..."
                ),
                height=90,
            )

            saved = st.form_submit_button(
                "Değerlendirmeyi Kaydet",
                type="primary",
                use_container_width=True,
            )

        if saved:
            if len(note.strip()) < 10:
                st.error(
                    "Değerlendirme notu en az 10 karakter olmalıdır."
                )

            else:
                selected_trainee = next(
                    trainee
                    for trainee in assigned
                    if trainee_label(trainee) == trainee_choice
                )

                now_text = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

                st.session_state.evaluations.append(
                    {
                        "kayit_id": make_record_id(),
                        "zaman_damgasi": now_text,
                        "mentor_kullanici": username,
                        "mentor_ad_soyad": full_name,
                        "trn_sicil": selected_trainee["code"],
                        "trn_ad_soyad": selected_trainee["name"],
                        "operasyon_tarihi": operation_date,
                        "vardiya": shift,
                        "ucus_bilgisi": flight,
                        "gorev_alani": duty,
                        "mentor_puani": score,
                        "yetkinlik_seviyesi": competency,
                        "degerlendirme_notu": note.strip(),
                        "aksiyon_maddeleri": actions.strip(),
                        "surec_durumu": process_status,
                        "son_guncelleme": now_text,
                    }
                )

                selected_trainee["status"] = process_status

                st.toast(
                    "Uçuş değerlendirmesi başarıyla kaydedildi.",
                    icon="✅",
                )
                st.rerun()

    with history_tab:
        my_records = [
            record
            for record in st.session_state.evaluations
            if record["mentor_kullanici"] == username
        ]

        if not my_records:
            st.info(
                "Henüz değerlendirme kaydınız bulunmuyor."
            )

        else:
            display_df = evaluations_dataframe(
                my_records
            ).rename(
                columns={
                    "operasyon_tarihi": "Tarih",
                    "trn_sicil": "Sicil",
                    "trn_ad_soyad": "TRN Personeli",
                    "ucus_bilgisi": "Uçuş",
                    "gorev_alani": "Görev",
                    "mentor_puani": "Puan",
                    "yetkinlik_seviyesi": "Yetkinlik",
                    "surec_durumu": "Süreç",
                }
            )

            st.dataframe(
                display_df[
                    [
                        "Tarih",
                        "Sicil",
                        "TRN Personeli",
                        "Uçuş",
                        "Görev",
                        "Puan",
                        "Yetkinlik",
                        "Süreç",
                    ]
                ],
                use_container_width=True,
                hide_index=True,
            )

            st.download_button(
                "Kendi Kayıtlarımı CSV / Excel Uyumlu İndir",
                data=csv_bytes(my_records),
                file_name=(
                    f"mentor_degerlendirmeleri_"
                    f"{username}_{date.today():%Y%m%d}.csv"
                ),
                mime="text/csv",
                use_container_width=True,
            )

    with edit_tab:
        my_records = [
            record
            for record in st.session_state.evaluations
            if record["mentor_kullanici"] == username
        ]

        if not my_records:
            st.info(
                "Düzenlenebilecek kayıt bulunmuyor."
            )

        else:
            options = {
                (
                    f"{record['operasyon_tarihi']:%d.%m.%Y} · "
                    f"{record['trn_sicil']} · "
                    f"{record['ucus_bilgisi']} · "
                    f"{record['kayit_id']}"
                ): record
                for record in sorted(
                    my_records,
                    key=lambda item: item["zaman_damgasi"],
                    reverse=True,
                )
            }

            selected_label = st.selectbox(
                "Düzenlenecek Kayıt",
                list(options.keys()),
            )

            selected = options[selected_label]

            with st.form("edit_evaluation"):
                column1, column2 = st.columns(2)

                with column1:
                    edit_score = st.slider(
                        "Mentor Puanı",
                        1,
                        5,
                        int(selected["mentor_puani"]),
                    )

                    edit_competency = st.selectbox(
                        "Yetkinlik Seviyesi",
                        COMPETENCIES,
                        index=COMPETENCIES.index(
                            selected["yetkinlik_seviyesi"]
                        ),
                    )

                with column2:
                    edit_status = st.selectbox(
                        "Süreç Durumu",
                        PROCESS_STATUSES,
                        index=PROCESS_STATUSES.index(
                            selected["surec_durumu"]
                        ),
                    )

                edit_note = st.text_area(
                    "Değerlendirme Notu",
                    value=selected["degerlendirme_notu"],
                    height=110,
                )

                edit_actions = st.text_area(
                    "Aksiyon Maddeleri",
                    value=selected["aksiyon_maddeleri"],
                    height=90,
                )

                updated = st.form_submit_button(
                    "Değişiklikleri Kaydet",
                    type="primary",
                    use_container_width=True,
                )

            if updated:
                if len(edit_note.strip()) < 10:
                    st.error(
                        "Değerlendirme notu en az 10 karakter olmalıdır."
                    )

                else:
                    selected["mentor_puani"] = edit_score
                    selected["yetkinlik_seviyesi"] = edit_competency
                    selected["surec_durumu"] = edit_status
                    selected["degerlendirme_notu"] = edit_note.strip()
                    selected["aksiyon_maddeleri"] = edit_actions.strip()
                    selected["son_guncelleme"] = (
                        datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )
                    )

                    st.toast(
                        "Kayıt güncellendi.",
                        icon="✅",
                    )
                    st.rerun()


# =============================================================================
# YETKİLİ / ŞEF KONSOLU
# =============================================================================
def admin_console():
    render_header(
        "Yetkili / Şef Konsolu · Tüm istasyon eğitim "
        "performansının merkezi görünümü"
    )

    records = st.session_state.evaluations

    exit_column, spacer = st.columns([1, 4])

    with exit_column:
        if st.button(
            "Güvenli Çıkış",
            use_container_width=True,
        ):
            logout()
            st.rerun()

    unique_trainees = {
        record["trn_sicil"]
        for record in records
    }

    critical_count = sum(
        record["yetkinlik_seviyesi"] == "Kritik Hata"
        or int(record["mentor_puani"]) <= 1
        for record in records
    )

    if records:
        flight_counts = pd.Series(
            [
                record["trn_ad_soyad"]
                for record in records
            ]
        ).value_counts()
    else:
        flight_counts = pd.Series(dtype=int)

    if not flight_counts.empty:
        leader = flight_counts.index[0]
        leader_count = int(flight_counts.iloc[0])
    else:
        leader = "—"
        leader_count = 0

    kpi_columns = st.columns(4)

    kpis = [
        (
            "Toplam Değerlendirme",
            len(records),
            "Tüm kayıtlar",
            "#315AAB",
        ),
        (
            "Aktif TRN",
            len(unique_trainees),
            "Değerlendirilen personel",
            "#FFAC00",
        ),
        (
            "Kritik Not",
            critical_count,
            "Acil takip gerektiren",
            "#C93F49",
        ),
        (
            "En Çok Uçuşa Giren",
            leader,
            f"{leader_count} değerlendirme",
            "#16845B",
        ),
    ]

    for column, item in zip(kpi_columns, kpis):
        with column:
            render_metric(*item)

    dashboard_tab, audit_tab, tools_tab = st.tabs(
        [
            "Analitik & Filtreler",
            "Denetim Tablosu",
            "Yönetim Araçları",
        ]
    )

    with dashboard_tab:
        st.markdown(
            '<div class="section-title">'
            "Gelişmiş Filtreleme"
            "</div>",
            unsafe_allow_html=True,
        )

        mentor_names = sorted(
            {
                record["mentor_ad_soyad"]
                for record in records
            }
        )

        trainee_names = sorted(
            {
                (
                    f"{record['trn_sicil']} - "
                    f"{record['trn_ad_soyad']}"
                )
                for record in records
            }
        )

        flight_names = sorted(
            {
                record["ucus_bilgisi"]
                for record in records
            }
        )

        filter1, filter2, filter3 = st.columns(3)

        with filter1:
            search = st.text_input(
                "Anlık Arama",
                placeholder=(
                    "Mentor, sicil, personel, uçuş..."
                ),
            )

            selected_mentors = st.multiselect(
                "Mentor",
                mentor_names,
            )

        with filter2:
            selected_trainees = st.multiselect(
                "TRN Personeli",
                trainee_names,
            )

            selected_flights = st.multiselect(
                "Uçuş",
                flight_names,
            )

        with filter3:
            default_start = min(
                (
                    record["operasyon_tarihi"]
                    for record in records
                ),
                default=date.today(),
            )

            start_date = st.date_input(
                "Başlangıç Tarihi",
                value=default_start,
            )

            end_date = st.date_input(
                "Bitiş Tarihi",
                value=date.today(),
            )

        query = search.strip().casefold()
        filtered = []

        for record in records:
            joined = " ".join(
                [
                    record["mentor_ad_soyad"],
                    record["trn_sicil"],
                    record["trn_ad_soyad"],
                    record["ucus_bilgisi"],
                    record["gorev_alani"],
                    record["degerlendirme_notu"],
                ]
            ).casefold()

            trainee_full = (
                f"{record['trn_sicil']} - "
                f"{record['trn_ad_soyad']}"
            )

            if query and query not in joined:
                continue

            if (
                selected_mentors
                and record["mentor_ad_soyad"]
                not in selected_mentors
            ):
                continue

            if (
                selected_trainees
                and trainee_full
                not in selected_trainees
            ):
                continue

            if (
                selected_flights
                and record["ucus_bilgisi"]
                not in selected_flights
            ):
                continue

            if not (
                start_date
                <= record["operasyon_tarihi"]
                <= end_date
            ):
                continue

            filtered.append(record)

        st.caption(
            f"{len(filtered)} değerlendirme gösteriliyor"
        )

        if filtered:
            filtered_df = evaluations_dataframe(
                filtered
            )

            summary = (
                filtered_df
                .groupby(
                    [
                        "trn_sicil",
                        "trn_ad_soyad",
                    ],
                    as_index=False,
                )
                .agg(
                    degerlendirme_sayisi=(
                        "kayit_id",
                        "count",
                    ),
                    ortalama_puan=(
                        "mentor_puani",
                        "mean",
                    ),
                )
                .sort_values(
                    [
                        "degerlendirme_sayisi",
                        "ortalama_puan",
                    ],
                    ascending=[False, False],
                )
            )

            summary["ortalama_puan"] = (
                summary["ortalama_puan"].round(2)
            )

            st.markdown(
                '<div class="section-title">'
                "TRN Performans Özeti"
                "</div>",
                unsafe_allow_html=True,
            )

            st.dataframe(
                summary.rename(
                    columns={
                        "trn_sicil": "Sicil",
                        "trn_ad_soyad": "TRN Personeli",
                        "degerlendirme_sayisi": "Uçuş / Kayıt",
                        "ortalama_puan": "Ortalama Puan",
                    }
                ),
                use_container_width=True,
                hide_index=True,
            )

            score_summary = (
                filtered_df
                .groupby(
                    "mentor_ad_soyad",
                    as_index=False,
                )
                .agg(
                    kayit_sayisi=(
                        "kayit_id",
                        "count",
                    ),
                    ortalama_puan=(
                        "mentor_puani",
                        "mean",
                    ),
                )
            )

            score_summary["ortalama_puan"] = (
                score_summary["ortalama_puan"].round(2)
            )

            st.markdown(
                '<div class="section-title">'
                "Mentor Aktivite Özeti"
                "</div>",
                unsafe_allow_html=True,
            )

            st.dataframe(
                score_summary.rename(
                    columns={
                        "mentor_ad_soyad": "Mentor",
                        "kayit_sayisi": "Kayıt Sayısı",
                        "ortalama_puan": "Ortalama Puan",
                    }
                ),
                use_container_width=True,
                hide_index=True,
            )

        else:
            st.info(
                "Seçilen filtrelere uygun kayıt bulunamadı."
            )

    with audit_tab:
        st.markdown(
            '<div class="section-title">'
            "Kronolojik Denetim Kaydı"
            "</div>",
            unsafe_allow_html=True,
        )

        if not records:
            st.info(
                "Denetim kaydı bulunmuyor."
            )

        else:
            audit_df = evaluations_dataframe(
                records
            ).rename(
                columns={
                    "kayit_id": "Kayıt ID",
                    "zaman_damgasi": "Oluşturma",
                    "mentor_ad_soyad": "Mentor",
                    "trn_sicil": "Sicil",
                    "trn_ad_soyad": "TRN Personeli",
                    "operasyon_tarihi": "Tarih",
                    "vardiya": "Vardiya",
                    "ucus_bilgisi": "Uçuş / Uçak",
                    "gorev_alani": "Görev",
                    "mentor_puani": "Puan",
                    "yetkinlik_seviyesi": "Yetkinlik",
                    "degerlendirme_notu": "Mentor Notu",
                    "aksiyon_maddeleri": "Aksiyon",
                    "surec_durumu": "Süreç",
                    "son_guncelleme": "Son Güncelleme",
                }
            )

            visible_columns = [
                "Kayıt ID",
                "Tarih",
                "Mentor",
                "Sicil",
                "TRN Personeli",
                "Vardiya",
                "Uçuş / Uçak",
                "Görev",
                "Puan",
                "Yetkinlik",
                "Mentor Notu",
                "Aksiyon",
                "Süreç",
                "Son Güncelleme",
            ]

            st.dataframe(
                audit_df[visible_columns],
                use_container_width=True,
                hide_index=True,
                height=450,
            )

            record_options = {
                (
                    f"{record['operasyon_tarihi']:%d.%m.%Y} · "
                    f"{record['mentor_ad_soyad']} · "
                    f"{record['trn_sicil']} · "
                    f"{record['kayit_id']}"
                ): record
                for record in sorted(
                    records,
                    key=lambda item: item["zaman_damgasi"],
                    reverse=True,
                )
            }

            chosen = st.selectbox(
                "Detayını Görüntüle",
                list(record_options.keys()),
            )

            detail = record_options[chosen]

            detail1, detail2, detail3 = st.columns(3)

            detail1.metric(
                "Mentor",
                detail["mentor_ad_soyad"],
            )

            detail2.metric(
                "TRN Personeli",
                (
                    f"{detail['trn_sicil']} - "
                    f"{detail['trn_ad_soyad']}"
                ),
            )

            detail3.metric(
                "Puan",
                f"{detail['mentor_puani']} / 5",
            )

            st.markdown(
                f"""
                <div class="audit-note">
                    <b>Değerlendirme:</b><br>
                    {detail["degerlendirme_notu"]}
                    <br><br>
                    <b>Aksiyon:</b><br>
                    {
                        detail["aksiyon_maddeleri"]
                        or "Aksiyon girilmedi."
                    }
                </div>
                """,
                unsafe_allow_html=True,
            )

    with tools_tab:
        st.markdown(
            '<div class="section-title">'
            "Raporlama ve Test Verisi Yönetimi"
            "</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="hint">
                Dışa aktarılan UTF-8 CSV dosyası Excel ile
                doğrudan açılabilir. Sıfırlama işlemi mevcut
                oturumdaki kayıtları örnek veri setine döndürür.
            </div>
            """,
            unsafe_allow_html=True,
        )

        tool1, tool2 = st.columns(2)

        with tool1:
            st.download_button(
                "Tüm Değerlendirme Raporunu İndir",
                data=csv_bytes(records),
                file_name=(
                    "istasyon_trn_tum_rapor_"
                    f"{date.today():%Y%m%d}.csv"
                ),
                mime="text/csv",
                use_container_width=True,
            )

        with tool2:
            if st.button(
                "Verileri Sıfırla / Örnek Verileri Yükle",
                use_container_width=True,
            ):
                reset_demo_data()

                st.toast(
                    "Örnek veriler yeniden yüklendi.",
                    icon="✅",
                )
                st.rerun()

        st.markdown(
            '<div class="section-title">'
            "Mentor Hesapları ve Atamalar"
            "</div>",
            unsafe_allow_html=True,
        )

        accounts = []

        for username, user in st.session_state.users.items():
            assigned_names = [
                trainee_label(trainee)
                for trainee in st.session_state.trainees
                if trainee["mentor"] == username
            ]

            accounts.append(
                {
                    "Kullanıcı Adı": username,
                    "Mentor": user["full_name"],
                    "Atanan TRN Sayısı": len(assigned_names),
                    "Atanan Personel": (
                        ", ".join(assigned_names)
                        or "Atama yok"
                    ),
                }
            )

        st.dataframe(
            pd.DataFrame(accounts),
            use_container_width=True,
            hide_index=True,
        )


# =============================================================================
# ROL BAZLI UYGULAMA YÖNLENDİRMESİ
# =============================================================================
if not st.session_state.authenticated:
    authentication_page()

elif st.session_state.role == "mentor":
    mentor_panel()

elif st.session_state.role == "admin":
    admin_console()

else:
    logout()
    st.rerun()


st.caption(
    "İstasyon TRN Portalı · Operasyonel prototip · "
    "Veriler aktif oturumda saklanır"
)
