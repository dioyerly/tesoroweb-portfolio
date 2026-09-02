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
        background-color: #0a0e27;
        color: #e0e0e0;
    }
    
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
        font-size: 2.5rem;
        background: linear-gradient(135deg, #00d9ff, #9d4edd);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
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
        font-size: 1.35rem;
        font-weight: 700;
        margin: 2.2rem 0 1rem;
        letter-spacing: 0;
    }

    .tech-grid {
        display: grid;
        grid-template-columns: repeat(6, minmax(0, 1fr));
        gap: 0.9rem;
        margin-bottom: 1.5rem;
    }

    .tech-card {
        min-height: 132px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 0.75rem;
        padding: 1rem 0.65rem;
        background: linear-gradient(145deg, #111a3b, #18265a);
        border: 1px solid rgba(125, 227, 255, 0.3);
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.18);
        transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
    }

    .tech-card:hover {
        transform: translateY(-4px);
        border-color: #7de3ff;
        box-shadow: 0 12px 26px rgba(0, 217, 255, 0.2);
    }

    .tech-logo {
        width: 54px;
        height: 54px;
        object-fit: contain;
    }

    .tech-name {
        color: #ffffff !important;
        font-size: 0.84rem;
        font-weight: 600;
        line-height: 1.2;
        text-align: center;
        margin: 0;
    }

    @media (max-width: 900px) {
        .tech-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    }

    @media (max-width: 520px) {
        .tech-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
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

st.markdown('<h3 style="color: #00d9ff; text-align: center; margin: 2rem 0 1.5rem;">Una mirada a TESOROWEB</h3>', unsafe_allow_html=True)

project_images = [
    ("Panel de control de tesorería", "PANEL DE CONTROLDE TESORERIA.PNG"),
    ("Conciliación de pagos", "CONCILIACION DE PAGOS.PNG"),
    ("Procesamiento e ingreso de pagos", "PROCESAMIENTO EINGRESO DE PAGOS.PNG"),
    ("Consola de pagos programados", "CONSOLA DE PAGOS PROGRAMADOS.PNG"),
    ("Administración de proveedores", "PANEL ADMIN PROVEEDORES.PNG"),
    ("Administración de sociedades", "PANEL ADMIN SOCIEDADES.PNG"),
    ("Administración de usuarios", "PANEL ADMIN USUARIOS.PNG"),
]

image_columns = st.columns(2)
for index, (caption, filename) in enumerate(project_images):
    image_path = Path(__file__).parent / "imagenes" / filename
    with image_columns[index % 2]:
        if image_path.exists():
            st.image(str(image_path), caption=caption, use_container_width=True)

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
    ("Docker", "https://cdn.simpleicons.org/docker/2496ED"),
    ("OpenAI", "https://cdn.simpleicons.org/openai/FFFFFF"),
    ("OCR / PDF", "https://cdn.simpleicons.org/adobeacrobatreader/EC1C24"),
])

show_technologies("Visualización y dashboards", [
    ("Plotly", "https://cdn.simpleicons.org/plotly/3F4F75"),
    ("Matplotlib", "https://cdn.simpleicons.org/matplotlib/11557C"),
    ("Streamlit", "https://cdn.simpleicons.org/streamlit/FF4B4B"),
])

show_technologies("Tecnologías en crecimiento", [
    ("PostgreSQL", "https://cdn.simpleicons.org/postgresql/4169E1"),
    ("SQLAlchemy", "https://cdn.simpleicons.org/sqlalchemy/D71F00"),
    ("Claude", "https://cdn.simpleicons.org/claude/D97757"),
    ("Gunicorn", "https://cdn.simpleicons.org/gunicorn/499848"),
    ("Nginx", "https://cdn.simpleicons.org/nginx/009639"),
    ("SMTP", "https://cdn.simpleicons.org/maildotru/168DE2"),
    ("Celery", "https://cdn.simpleicons.org/celery/37814A"),
    ("APScheduler", "https://cdn.simpleicons.org/clockify/03A9F4"),
    ("JWT", "https://cdn.simpleicons.org/jsonwebtokens/000000"),
    ("AWS", "https://cdn.simpleicons.org/amazonaws/FF9900"),
    ("Railway", "https://cdn.simpleicons.org/railway/FFFFFF"),
    ("Vercel", "https://cdn.simpleicons.org/vercel/FFFFFF"),
    ("GitHub Actions", "https://cdn.simpleicons.org/githubactions/2088FF"),
    ("pytest", "https://cdn.simpleicons.org/pytest/0A9EDC"),
    ("REST API", "https://cdn.simpleicons.org/fastapi/009688"),
    ("Swagger / OpenAPI", "https://cdn.simpleicons.org/swagger/85EA2D"),
])

st.markdown("---")

# CONTACTO
st.markdown('<h2 id="contacto" class="section-title">📞 Contacto</h2>', unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <p style="font-size: 1.1rem; color: #b0b0b0; margin-bottom: 2rem;">
            ¿Interesado en trabajar juntos? Conectemos
        </p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("[💬 WhatsApp](https://wa.me/5811126425994)")

with col2:
    st.markdown("[📧 Email](mailto:dioyer321@gmail.com)")

with col3:
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/dioyerly-rodriguez-349992255/)")

st.markdown("---")

# FOOTER
st.markdown("""
    <div style="text-align: center; padding: 2rem; border-top: 1px solid rgba(0, 217, 255, 0.1); color: #888; font-size: 0.9rem;">
        <p>&copy; 2026 Dioyerly Rodriguez. Todos los derechos reservados.</p>
    </div>
""", unsafe_allow_html=True)
