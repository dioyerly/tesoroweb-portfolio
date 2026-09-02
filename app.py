import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="TESOROWEB",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado
st.markdown("""
    <style>
    :root {
        --primary: #00d9ff;
        --secondary: #9d4edd;
        --bg: #0a0e27;
        --text: #e0e0e0;
    }
    
    * {
        margin: 0;
        padding: 0;
    }
    
    body {
        background-color: #0a0e27;
        color: #e0e0e0;
    }
    
    .main {
        background-color: #0a0e27;
    }
    
    /* HERO */
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
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: #b0b0b0;
        margin-bottom: 2rem;
    }
    
    /* CARDS */
    .feature-card {
        background: linear-gradient(135deg, rgba(0, 217, 255, 0.05), rgba(157, 78, 221, 0.05));
        border: 1px solid rgba(0, 217, 255, 0.2);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
    }
    
    .feature-icon {
        font-size: 3rem;
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
    
    .tech-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
        gap: 1rem;
    }
    
    .tech-item {
        background: rgba(0, 217, 255, 0.05);
        border: 1px solid rgba(0, 217, 255, 0.1);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
    }
    
    .tech-icon {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    
    .price-card {
        background: linear-gradient(135deg, rgba(157, 78, 221, 0.1), rgba(0, 217, 255, 0.05));
        border: 2px solid rgba(0, 217, 255, 0.2);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
    }
    
    .price-number {
        font-size: 2.5rem;
        color: #9d4edd;
        font-weight: 700;
        margin: 1rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #00d9ff, #3a86ff) !important;
        color: #0a0e27 !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 0.6rem 1.5rem !important;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 30px rgba(0, 217, 255, 0.3) !important;
    }
    </style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 2rem; border-bottom: 1px solid rgba(0, 217, 255, 0.1); margin-bottom: 2rem;">
        <h1 style="margin: 0; background: linear-gradient(135deg, #00d9ff, #9d4edd); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">🚀 TESOROWEB</h1>
        <div style="display: flex; gap: 2rem;">
            <a href="#funcionalidades" style="color: #e0e0e0; text-decoration: none;">Funcionalidades</a>
            <a href="#stack" style="color: #e0e0e0; text-decoration: none;">Stack</a>
            <a href="#precios" style="color: #e0e0e0; text-decoration: none;">Precios</a>
            <a href="#contacto" style="color: #e0e0e0; text-decoration: none;">Contacto</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Automatización Inteligente de Pagos</h1>
        <p class="hero-subtitle">De 20 horas/mes en Excel → 2 horas con IA</p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("📞 Solicitar Demo"):
        st.success("¡Contacta a través de WhatsApp o Email para tu demo!")

st.markdown("---")

# FUNCIONALIDADES
st.markdown('<h2 id="funcionalidades" class="section-title">⚡ Funcionalidades</h2>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📄</div>
            <h3 style="color: #00d9ff;">Extracción Automática</h3>
            <p style="color: #b0b0b0;">Sube PDF → La IA lee automáticamente</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">✅</div>
            <h3 style="color: #00d9ff;">Conciliación Inteligente</h3>
            <p style="color: #b0b0b0;">Compara con banco automáticamente</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3 style="color: #00d9ff;">Dashboard de Gastos</h3>
            <p style="color: #b0b0b0;">Visualiza gasto por proveedor</p>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <h3 style="color: #00d9ff;">Control Total</h3>
            <p style="color: #b0b0b0;">Cero errores, auditoría completa</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# STACK TECNOLÓGICO
st.markdown('<h2 id="stack" class="section-title">💻 Stack Tecnológico</h2>', unsafe_allow_html=True)

tech_items = [
    ("🐍", "Python"),
    ("⚡", "Flask"),
    ("💾", "SQLite"),
    ("🎨", "HTML/CSS"),
    ("✨", "JavaScript"),
    ("🤖", "IA/PDF"),
    ("📊", "Conciliación"),
    ("🔐", "Seguridad"),
]

cols = st.columns(len(tech_items))
for i, (icon, tech) in enumerate(tech_items):
    with cols[i]:
        st.markdown(f"""
            <div class="tech-item">
                <div class="tech-icon">{icon}</div>
                <p style="color: #e0e0e0;">{tech}</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# PRECIOS
st.markdown('<h2 id="precios" class="section-title">💰 Planes</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="price-card">
            <h3 style="color: #00d9ff;">Starter</h3>
            <div class="price-number">$2.990</div>
            <p>/mes • Hasta 100 pagos</p>
            <p style="font-size: 0.9rem; color: #b0b0b0;">1 usuario</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Comenzar", key="starter"):
        st.info("Contáctanos para más detalles")

with col2:
    st.markdown("""
        <div class="price-card" style="border-color: #9d4edd; box-shadow: 0 0 30px rgba(157, 78, 221, 0.2);">
            <h3 style="color: #00d9ff;">Profesional ⭐</h3>
            <div class="price-number">$4.990</div>
            <p>/mes • Hasta 500 pagos</p>
            <p style="font-size: 0.9rem; color: #b0b0b0;">3 usuarios</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Comenzar", key="pro"):
        st.info("¡La opción más popular!")

with col3:
    st.markdown("""
        <div class="price-card">
            <h3 style="color: #00d9ff;">Enterprise</h3>
            <div class="price-number">$7.990</div>
            <p>/mes • Ilimitado</p>
            <p style="font-size: 0.9rem; color: #b0b0b0;">10 usuarios</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Contactar", key="enterprise"):
        st.info("Solución empresarial personalizada")

st.markdown("---")

# CONTACTO
st.markdown('<h2 id="contacto" class="section-title">📞 Contacto</h2>', unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <p style="font-size: 1.1rem; color: #b0b0b0; margin-bottom: 2rem;">
            ¿Interesado? Solicita una demo sin compromiso
        </p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("[💬 WhatsApp](https://wa.me/5491234567890)", unsafe_allow_html=True)

with col2:
    st.markdown("[📧 Email](mailto:info@tesoroweb.com)", unsafe_allow_html=True)

with col3:
    st.markdown("[🔗 LinkedIn](https://linkedin.com)", unsafe_allow_html=True)

# FOOTER
st.markdown("""
    <div style="text-align: center; padding: 2rem; border-top: 1px solid rgba(0, 217, 255, 0.1); color: #888; font-size: 0.9rem; margin-top: 3rem;">
        <p>&copy; 2026 TESOROWEB. Automatización de pagos para pymes.</p>
    </div>
""", unsafe_allow_html=True)