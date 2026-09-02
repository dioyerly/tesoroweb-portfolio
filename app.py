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
    
    .tech-item {
        background: rgba(0, 217, 255, 0.05);
        border: 1px solid rgba(0, 217, 255, 0.1);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
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

skills = [
    ("🐍", "Python"),
    ("⚡", "Flask"),
    ("💾", "SQL/SQLite"),
    ("🎨", "HTML/CSS"),
    ("✨", "JavaScript"),
    ("🤖", "IA/ML"),
    ("📊", "Data Analysis"),
    ("🔐", "Seguridad"),
    ("📄", "OCR/PDF"),
    ("🔄", "Conciliación"),
    ("📈", "Visualización"),
    ("🚀", "Automatización"),
]

cols = st.columns(4)
for i, (icon, skill) in enumerate(skills):
    with cols[i % 4]:
        st.markdown(f"""
            <div class="tech-item">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">{icon}</div>
                <p style="color: #e0e0e0; font-size: 0.9rem;">{skill}</p>
            </div>
        """, unsafe_allow_html=True)

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
