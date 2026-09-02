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
        width: 100%;
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
        <h1 class="hero-title">Data Scientist & AI Developer</h1>
        <p class="hero-subtitle">Automatización · IA · Gestión de Datos</p>
        <p style="color: #b0b0b0; font-size: 1.1rem;">Transformo procesos manuales en soluciones inteligentes</p>
    </div>
""", unsafe_allow_html=True)

# SOBRE MÍ
st.markdown('<h2 id="sobre-mi" class="section-title">👤 Sobre mí</h2>', unsafe_allow_html=True)

st.markdown("""
    Soy especialista en **Ciencia de Datos e IA** con experiencia desarrollando soluciones que automatizan procesos complejos.
    
    Mi enfoque: convertir problemas operacionales en aplicaciones escalables que generan impacto real.
    
    **Áreas de expertise:**
    - Automatización con IA y OCR
    - Gestión de datos y procesamiento
    - Desarrollo de aplicaciones SaaS
    - Reconocimiento de patrones
    - Conciliación automática de datos
""")

st.markdown("---")

# PROYECTOS
st.markdown('<h2 id="proyectos" class="section-title">📁 Proyectos</h2>', unsafe_allow_html=True)

# TESOROWEB
st.markdown("""
    <div class="project-card">
        <h3 style="color: #00d9ff; margin-bottom: 1rem;">🚀 TESOROWEB - Automatización de Gestión de Pagos</h3>
        <p style="color: #b0b0b0;">Plataforma SaaS que automatiza 80% del trabajo manual en tesorería usando IA.</p>
        <p style="margin: 1rem 0;"><strong>Funcionalidades:</strong></p>
        <p style="color: #b0b0b0;">
        ✓ Extracción automática de PDFs (OCR) | 
        ✓ Conciliación inteligente con banco | 
        ✓ Dashboard de gastos vs ventas | 
        ✓ Multi-empresa y multi-usuario
        </p>
        <p style="margin-top: 1rem;"><strong>Stack:</strong> Python, Flask, SQLite, JavaScript, PDF Processing</p>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("📽️ Ver Demo de TESOROWEB"):
        st.info("Demo: [Link a tu app o video]")

with col2:
    if st.button("💻 Ver Repositorio"):
        st.info("GitHub: [Link a tu repo]")

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
    st.markdown("[💬 WhatsApp](https://wa.me/5491234567890)")

with col2:
    st.markdown("[📧 Email](mailto:dioyerly@example.com)")

with col3:
    st.markdown("[🔗 LinkedIn](https://linkedin.com/in/dioyerly)")

st.markdown("---")

# FOOTER
st.markdown("""
    <div style="text-align: center; padding: 2rem; border-top: 1px solid rgba(0, 217, 255, 0.1); color: #888; font-size: 0.9rem;">
        <p>&copy; 2026 Dioyerly Rodriguez. Todos los derechos reservados.</p>
    </div>
""", unsafe_allow_html=True)
