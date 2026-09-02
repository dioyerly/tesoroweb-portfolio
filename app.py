from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Dioyerly Rodriguez - Data Scientist & AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS
st.markdown("""
    <style>
    body {
        background: #080d21;
        color: #e0e0e0;
    }

    .stApp {
        background:
            radial-gradient(circle at 8% 18%, rgba(0, 217, 255, 0.12), transparent 24rem),
            radial-gradient(circle at 92% 48%, rgba(157, 78, 221, 0.13), transparent 26rem),
            linear-gradient(135deg, #080d21 0%, #101936 52%, #150f2e 100%);
    }

    .main .block-container { max-width: 1180px; padding-top: 2rem; }

    [data-testid="stMarkdownContainer"],
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li {
        color: #dce8ff !important;
    }

    [data-testid="stMarkdownContainer"] strong {
        color: #ffffff !important;
    }

    [data-testid="stTextInput"] label,
    [data-testid="stTextArea"] label,
    [data-testid="stSelectbox"] label {
        color: #dce8ff !important;
        font-weight: 600 !important;
    }

    .project-card p,
    .project-card strong {
        color: #dce8ff !important;
    }

    .project-card h3 { color: #7de3ff !important; }
    
    .hero-section {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f4d 100%);
        border-radius: 15px;
        margin-bottom: 3rem;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #00d9ff, #9d4edd);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: #00d9ff;
        margin-bottom: 1rem;
    }
    
    .section-title {
        font-size: 2.15rem;
        background: linear-gradient(135deg, #00d9ff, #9d4edd);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    .project-card {
        background: linear-gradient(135deg, rgba(0, 217, 255, 0.05), rgba(157, 78, 221, 0.05));
        border: 1px solid rgba(0, 217, 255, 0.2);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    
    .project-card:hover {
        border-color: rgba(0, 217, 255, 0.5);
        box-shadow: 0 0 30px rgba(0, 217, 255, 0.1);
    }
    
    .tech-group-title {
        color: #7de3ff !important;
        font-size: 1.15rem;
        font-weight: 700;
        margin: 1.5rem 0 0.8rem;
        letter-spacing: 0;
    }

    .tech-grid {
        display: grid;
        grid-template-columns: repeat(6, minmax(0, 1fr));
        gap: 0.7rem;
        margin-bottom: 1rem;
    }

    .tech-card {
        min-height: 108px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        padding: 0.7rem 0.45rem;
        background: linear-gradient(145deg, rgba(17, 26, 59, 0.9), rgba(24, 38, 90, 0.72));
        border: 1px solid rgba(125, 227, 255, 0.3);
        border-radius: 12px;
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.22);
        transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
    }

    .tech-card:hover {
        transform: translateY(-4px);
        border-color: #7de3ff;
        box-shadow: 0 12px 26px rgba(0, 217, 255, 0.2);
    }

    .tech-logo {
        width: 44px;
        height: 44px;
        object-fit: contain;
    }

    .tech-name {
        color: #ffffff !important;
        font-size: 0.78rem;
        font-weight: 600;
        line-height: 1.2;
        text-align: center;
        margin: 0;
    }

    .stTextInput input,
    .stTextArea textarea,
    [data-baseweb="select"] > div {
        color: #ffffff !important;
        background-color: rgba(8, 13, 33, 0.78) !important;
        border-color: rgba(125, 227, 255, 0.35) !important;
    }

    @media (max-width: 900px) {
        .tech-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    }

    @media (max-width: 520px) {
        .tech-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    }

    .contact-panel {
        padding: 1.5rem;
        background: linear-gradient(145deg, rgba(14, 25, 58, 0.92), rgba(31, 17, 57, 0.88));
        border: 1px solid rgba(125, 227, 255, 0.28);
        border-radius: 14px;
        box-shadow: 0 14px 35px rgba(0, 0, 0, 0.2);
    }

    .contact-link {
        display: block;
        padding: 0.8rem;
        color: #ffffff !important;
        text-align: center;
        text-decoration: none !important;
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid rgba(125, 227, 255, 0.22);
        border-radius: 10px;
        font-weight: 600;
    }

    .contact-link:hover { border-color: #7de3ff; background: rgba(0, 217, 255, 0.12); }
    .contact-link img { width: 25px; height: 25px; vertical-align: middle; margin-right: 0.45rem; }

    .contact-form {
        display: flex;
        flex-direction: column;
        gap: 0.65rem;
        padding: 1.5rem;
        background: linear-gradient(145deg, rgba(14, 25, 58, 0.92), rgba(31, 17, 57, 0.88));
        border: 1px solid rgba(125, 227, 255, 0.28);
        border-radius: 14px;
        box-shadow: 0 14px 35px rgba(0, 0, 0, 0.2);
    }

    .contact-form label { color: #dce8ff; font-weight: 600; font-size: 0.9rem; }
    .contact-form input,
    .contact-form select,
    .contact-form textarea {
        width: 100%;
        box-sizing: border-box;
        padding: 0.75rem;
        color: #ffffff;
        background: rgba(8, 13, 33, 0.9);
        border: 1px solid rgba(125, 227, 255, 0.35);
        border-radius: 8px;
        font: inherit;
    }

    .contact-form textarea { min-height: 120px; resize: vertical; }
    .contact-form input::placeholder,
    .contact-form textarea::placeholder { color: #9fb8e8; }
    .contact-form button {
        margin-top: 0.4rem;
        padding: 0.8rem;
        color: #071125;
        background: linear-gradient(135deg, #00d9ff, #7de3ff);
        border: 0;
        border-radius: 8px;
        font-weight: 700;
        cursor: pointer;
    }
    .contact-form button:hover { box-shadow: 0 0 20px rgba(0, 217, 255, 0.35); }

    .gallery-counter {
        color: #9fb8e8 !important;
        text-align: center;
        font-size: 0.82rem;
        margin: 0.2rem 0 0.7rem;
    }

    .gallery-arrow button {
        min-height: 3rem !important;
        font-size: 1.5rem !important;
        padding: 0 !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #00d9ff, #3a86ff) !important;
        color: #0a0e27 !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 2rem; border-bottom: 1px solid rgba(0, 217, 255, 0.1); margin-bottom: 2rem;">
        <h1 style="margin: 0; background: linear-gradient(135deg, #00d9ff, #9d4edd); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Dioyerly Rodriguez</h1>
        <div style="display: flex; gap: 2rem; font-size: 0.9rem;">
            <a href="#sobre-mi" style="color: #e0e0e0; text-decoration: none;">Sobre mí</a>
            <a href="#proyectos" style="color: #e0e0e0; text-decoration: none;">Proyectos</a>
            <a href="#skills" style="color: #e0e0e0; text-decoration: none;">Skills</a>
            <a href="#contacto" style="color: #e0e0e0; text-decoration: none;">Contacto</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Data Scientist & AI</h1>
        <p class="hero-subtitle">Especialista en Automatización</p>
        <p style="color: #b0b0b0; font-size: 1.1rem;">Transformo procesos manuales en soluciones inteligentes que generan impacto real</p>
    </div>
""", unsafe_allow_html=True)

# SOBRE MÍ
st.markdown('<h2 id="sobre-mi" class="section-title">👤 Sobre mí</h2>', unsafe_allow_html=True)

st.markdown("""
    Soy especialista en **Ciencia de Datos e IA** con experiencia desarrollando soluciones que automatizan procesos operacionales complejos.
    
    **Formación:** Administración de Empresas (Venezuela) + Data Scientist & AI (Argentina)
    
    **Mi enfoque:** Automatización, análisis de datos y desarrollo de soluciones inteligentes que resuelven problemas reales desde el principio hasta el final.
    
    Lo que me diferencia es el conocimiento profundo de los problemas operacionales y la capacidad de transformarlos en aplicaciones escalables que generan valor tangible.
""")

st.markdown("---")

# PROYECTOS
st.markdown('<h2 id="proyectos" class="section-title">📁 Proyectos</h2>', unsafe_allow_html=True)

# TESOROWEB
st.markdown("""
    <div class="project-card">
        <h3 style="color: #00d9ff; margin-bottom: 0.5rem;">🚀 TESOROWEB</h3>
        <p style="color: #9d4edd; font-size: 1.1rem; margin-bottom: 1rem;"><strong>Plataforma SaaS de Gestión de Pagos</strong></p>
        <p style="color: #b0b0b0; margin-bottom: 1rem;">Automatización inteligente de tesorería que ahorra 20+ horas/mes y elimina errores manuales.</p>
        <p style="margin: 1rem 0;"><strong>Funcionalidades:</strong></p>
        <p style="color: #b0b0b0;">
        ✓ Extracción automática de PDFs (OCR) | 
        ✓ Conciliación inteligente con banco | 
        ✓ Dashboard de gastos vs ventas | 
        ✓ Multi-empresa y multi-usuario | 
        ✓ Reportes automáticos para auditoría
        </p>
        <p style="margin-top: 1rem;"><strong>Beneficios principales:</strong><br>
        → Ahorra 20 horas/mes en tesorería<br>
        → Automatiza pagos sin errores<br>
        → Control total de flujo de caja
        </p>
        <p style="margin-top: 1rem;"><strong>Stack:</strong> Python, Flask, SQLite, JavaScript, PDF Processing, IA</p>
        <p style="color: #888; font-size: 0.9rem; margin-top: 1rem;">⏱️ 2 meses de desarrollo | 🎯 Buscando clientes</p>
    </div>
""", unsafe_allow_html=True)

st.markdown('<h3 style="color: #00d9ff; text-align: center; margin: 1.5rem 0 0.5rem;">Una mirada a TESOROWEB</h3>', unsafe_allow_html=True)

project_images = [
    ("Panel de control de tesorería", "PANEL DE CONTROLDE TESORERIA.PNG"),
    ("Conciliación de pagos", "CONCILIACION DE PAGOS.PNG"),
    ("Procesamiento e ingreso de pagos", "PROCESAMIENTO EINGRESO DE PAGOS.PNG"),
    ("Consola de pagos programados", "CONSOLA DE PAGOS PROGRAMADOS.PNG"),
    ("Administración de proveedores", "PANEL ADMIN PROVEEDORES.PNG"),
    ("Administración de sociedades", "PANEL ADMIN SOCIEDADES.PNG"),
    ("Administración de usuarios", "PANEL ADMIN USUARIOS.PNG"),
]

if "project_image_index" not in st.session_state:
    st.session_state.project_image_index = 0

gallery_images = [
    (caption, Path(__file__).parent / "imagenes" / filename)
    for caption, filename in project_images
    if (Path(__file__).parent / "imagenes" / filename).exists()
]

if gallery_images:
    previous, image_area, next_image = st.columns([1, 10, 1], vertical_alignment="center")
    with previous:
        if st.button("‹", key="previous_project_image", help="Imagen anterior"):
            st.session_state.project_image_index = (st.session_state.project_image_index - 1) % len(gallery_images)
    with image_area:
        current_index = st.session_state.project_image_index % len(gallery_images)
        caption, image_path = gallery_images[current_index]
        st.image(str(image_path), caption=caption, use_container_width=True)
        st.markdown(
            f'<p class="gallery-counter">{current_index + 1} / {len(gallery_images)} · Usa las flechas para explorar</p>',
            unsafe_allow_html=True,
        )
    with next_image:
        if st.button("›", key="next_project_image", help="Imagen siguiente"):
            st.session_state.project_image_index = (st.session_state.project_image_index + 1) % len(gallery_images)
else:
    st.info("Las capturas de TESOROWEB todavía no están disponibles.")

col1, col2 = st.columns(2)
with col1:
    if st.button("📽️ Ver Demo TESOROWEB", key="tesoroweb_demo"):
        st.info("📍 Link a la demo: [Próximamente]")
with col2:
    if st.button("💻 Repositorio GitHub", key="tesoroweb_repo"):
        st.info("📍 GitHub: github.com/dioyerly/tesoroweb-portfolio")

st.markdown("---")

# OTROS PROYECTOS
st.markdown("""
    <div class="project-card">
        <h3 style="color: #00d9ff; margin-bottom: 1rem;">📧 Sistema de Agenda + Recordatorios</h3>
        <p style="color: #b0b0b0;">Sistema automático de recordatorios por email para tareas y eventos. Gestión completa de calendario con notificaciones inteligentes.</p>
        <p style="margin-top: 1rem;"><strong>Stack:</strong> Python, Flask, Email Automation</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="project-card">
        <h3 style="color: #00d9ff; margin-bottom: 1rem;">🔄 Conciliación Automática</h3>
        <p style="color: #b0b0b0;">Comparación y conciliación inteligente entre facturas del sistema de gestión interno vs ARCA. Detección automática de discrepancias y generación de reportes.</p>
        <p style="margin-top: 1rem;"><strong>Stack:</strong> Python, Data Processing, SQL</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="project-card">
        <h3 style="color: #00d9ff; margin-bottom: 1rem;">📄 Transcripción de PDFs</h3>
        <p style="color: #b0b0b0;">Herramienta para transcribir y limpiar datos de resúmenes de tarjetas corporativas. Extrae información y la adapta automáticamente para subir al sistema de gestión.</p>
        <p style="margin-top: 1rem;"><strong>Stack:</strong> Python, OCR, PDF Processing, Data Cleaning</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="project-card">
        <h3 style="color: #00d9ff; margin-bottom: 1rem;">🏢 Sistema Integral de Gestión</h3>
        <p style="color: #b0b0b0;">Plataforma completa que integra agenda, tareas repetitivas, carga en lote a Odoo, gestión de cuentas de empleados, descarga de planillas de nómina y pagos a proveedores.</p>
        <p style="margin-top: 1rem;"><strong>Stack:</strong> Python, Flask, Odoo API, SQL, JavaScript</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# SKILLS
st.markdown('<h2 id="skills" class="section-title">💻 Stack Tecnológico & Skills</h2>', unsafe_allow_html=True)

def show_technologies(title, technologies):
    cards = "".join(
        f'<div class="tech-card"><img class="tech-logo" src="{logo_url}" alt="Logo de {name}"><p class="tech-name">{name}</p></div>'
        for name, logo_url in technologies
    )
    st.markdown(
        f'<h3 class="tech-group-title">{title}</h3><div class="tech-grid">{cards}</div>',
        unsafe_allow_html=True,
    )


show_technologies("Herramientas que manejo", [
    ("Python", "https://cdn.simpleicons.org/python/3776AB"),
    ("Flask", "https://cdn.simpleicons.org/flask/FFFFFF"),
    ("SQLite", "https://cdn.simpleicons.org/sqlite/003B57"),
    ("Pandas", "https://cdn.simpleicons.org/pandas/150458"),
    ("Excel", "https://cdn.simpleicons.org/microsoftexcel/217346"),
    ("HTML5", "https://cdn.simpleicons.org/html5/E34F26"),
    ("CSS3", "https://cdn.simpleicons.org/css/1572B6"),
    ("JavaScript", "https://cdn.simpleicons.org/javascript/F7DF1E"),
    ("Git", "https://cdn.simpleicons.org/git/F05032"),
    ("GitHub", "https://cdn.simpleicons.org/github/FFFFFF"),
    ("OpenAI", "https://cdn.simpleicons.org/openai/FFFFFF"),
    ("Streamlit", "https://cdn.simpleicons.org/streamlit/FF4B4B"),
    ("OCR / PDF", "https://api.iconify.design/mdi:file-search-outline.svg?color=%237DE3FF"),
])

show_technologies("Tecnologías en crecimiento", [
    ("SQLAlchemy", "https://cdn.simpleicons.org/sqlalchemy/D71F00"),
    ("Claude", "https://cdn.simpleicons.org/claude/D97757"),
    ("Railway", "https://cdn.simpleicons.org/railway/FFFFFF"),
    ("Vercel", "https://cdn.simpleicons.org/vercel/FFFFFF"),
    ("GitHub Actions", "https://cdn.simpleicons.org/githubactions/2088FF"),
    ("REST API", "https://cdn.simpleicons.org/fastapi/009688"),
    ("Swagger / OpenAPI", "https://cdn.simpleicons.org/swagger/85EA2D"),
])

st.markdown("---")

# CONTACTO
st.markdown('<h2 id="contacto" class="section-title">📞 Conectemos</h2>', unsafe_allow_html=True)

contact_left, contact_right = st.columns([0.85, 1.15], gap="large")
with contact_left:
    st.markdown('<div class="contact-panel">', unsafe_allow_html=True)
    st.markdown('<p style="color: #c9d6ff; margin-top: 0;">Cuéntame qué proceso quieres automatizar o qué producto digital tienes en mente.</p>', unsafe_allow_html=True)
    st.markdown('<a class="contact-link" href="https://wa.me/5811126425994" target="_blank"><img src="https://cdn.simpleicons.org/whatsapp/25D366">WhatsApp</a>', unsafe_allow_html=True)
    st.markdown('<br><a class="contact-link" href="https://www.linkedin.com/in/dioyerly-rodriguez-349992255/" target="_blank"><img src="https://cdn.simpleicons.org/linkedin/0A66C2">LinkedIn</a>', unsafe_allow_html=True)
    st.markdown('<br><a class="contact-link" href="https://github.com/dioyerly/tesoroweb-portfolio" target="_blank"><img src="https://cdn.simpleicons.org/github/FFFFFF">GitHub</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with contact_right:
    st.markdown("""
        <form class="contact-form" action="https://formsubmit.co/dioyer321@gmail.com" method="POST">
            <input type="hidden" name="_subject" value="Nueva consulta desde tu portafolio">
            <input type="hidden" name="_template" value="table">
            <input type="hidden" name="_captcha" value="true">
            <input type="hidden" name="_next" value="https://tesoroweb-portfolio-gqb4lcqngpomudwmwks4xy.streamlit.app/">
            <label for="contact-name">Tu nombre</label>
            <input id="contact-name" type="text" name="name" placeholder="¿Cómo te llamas?" required>
            <label for="contact-email">Tu correo</label>
            <input id="contact-email" type="email" name="email" placeholder="tu@correo.com" required>
            <label for="contact-topic">¿En qué te puedo ayudar?</label>
            <select id="contact-topic" name="topic" required>
                <option value="Automatización">Automatización</option>
                <option value="Análisis de datos">Análisis de datos</option>
                <option value="TESOROWEB">TESOROWEB</option>
                <option value="Otro proyecto">Otro proyecto</option>
            </select>
            <label for="contact-message">Cuéntame brevemente tu idea</label>
            <textarea id="contact-message" name="message" placeholder="¿Qué necesitas resolver?" required></textarea>
            <button type="submit">✉️ Enviar consulta</button>
        </form>
    """, unsafe_allow_html=True)

st.markdown("---")

# FOOTER
st.markdown("""
    <div style="text-align: center; padding: 2rem; border-top: 1px solid rgba(0, 217, 255, 0.1); color: #888; font-size: 0.9rem;">
        <p>&copy; 2026 Dioyerly Rodriguez. Todos los derechos reservados.</p>
    </div>
""", unsafe_allow_html=True)
