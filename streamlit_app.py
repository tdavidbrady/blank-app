# ==========================================
# DEMO VERSION: NO LIVE API CALLS
# Perfectly stable for presentations and portfolios.
# ==========================================

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from datetime import datetime, timedelta

# --- 0. VERSION METADATA ---
VERSION_NAME = "RBMI Put-Write Dashboard"
VERSION_NUM = "01-029-DEMO"
VERSION_DATE = "April 19, 2026"

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Rational Basis | DEMO",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. PERMANENT BRANDING & STYLE LOCK ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .corp-header {
        font-family: 'Arial Black', sans-serif;
        font-weight: 900; font-size: 26px; text-transform: uppercase;
        letter-spacing: 3px; color: #ffffff; line-height: 1.1;
        transform: scaleX(1.15); transform-origin: left; margin-bottom: 0px;
    }
    .version-text {
        font-family: 'Courier New', monospace; color: #e3b341; font-size: 12px; font-weight: bold; margin-top: 5px;
    }
    [data-testid="stMetricValue"] { font-size: 26px !important; font-weight: 700 !important; }
    [data-testid="stMetricDelta"] { font-size: 15px !important; }
    .taco-box {
        padding: 20px 15px; border-radius: 10px; border: 1px solid #30363d;
        background-color: #161b22; margin-bottom: 10px; display: flex; flex-direction: column; align-items: center; justify-content: center;
    }
    .taco-box h1 { margin: 0px !important; padding: 0px !important; line-height: 1 !important; }
    .taco-box p { margin: 5px 0px 0px 0px !important; color: #8b949e; font-size: 12px; letter-spacing: 1px; }
    div[data-testid="column"]:nth-of-type(1) { border-right: 2px solid #30363d !important; padding-right: 25px !important; }
    div[data-testid="column"]:nth-of-type(2) { padding-left: 25px !important; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; white-space: pre-wrap; background-color: transparent;
        border-radius: 4px 4px 0px 0px; gap: 1px; padding-top: 10px; padding-bottom: 10px; font-weight: bold; font-size: 16px;
    }
    .instruction-text { color: #8b949e; font-size: 14px; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DYNAMIC CLOCK COMPONENT ---
def minute_clock():
    return components.html("""
        <div id="clock" style="font-family: 'Courier New', monospace; color: #8b949e; font-size: 13.5px; font-weight: bold; padding-top: 5px;"></div>
        <script>
        function updateClock() {
            const now = new Date();
            const options = { timeZone: 'America/New_York', weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit', hour12: true };
            document.getElementById('clock').innerHTML = now.toLocaleString('en-US', options) + " EST";
        }
        setInterval(updateClock, 60000); updateClock();
        </script>""", height=60)

# --- 4. MOCKED DATA ENGINES (DEMO MODE) ---
MASTER_SECTORS = ["Healthcare", "Energy & Utilities", "Industrials", "Consumer Defensive", "Materials", "Tech & Comms"]

STOCKED_PONDS = {
    "Healthcare": ["JNJ", "UNH", "LLY"],
    "Energy & Utilities": ["XOM", "CVX", "NEE"],
    "Industrials": ["HON", "UPS", "BA"],
    "Consumer Defensive": ["PG", "KO", "WMT"],
    "Materials": ["LIN", "SHW", "NEM"],
    "Tech & Comms": ["AAPL", "MSFT", "GOOGL"]
}

def load_symbol_database_mock():
    # Flattens the STOCKED_PONDS dict into a dataframe
    data = []
    for sector, symbols in STOCKED_PONDS.items():
        for sym in symbols:
            data.append({"Symbol": sym, "Sector": sector})
    return pd.DataFrame(data)

def fetch_weather_metrics_mock():
    return {
        "^GSPC": {"current": 5123.45, "vs_open": 15.20, "vs_close": 32.10, "pct_close": 0.63},
        "^VIX": {"current": 14.25, "vs_open": -0.15, "vs_close": -0.85, "pct_close": -5.6}
    }

def get_taco_macro_data_mock():
    return 0.04, 4.35, 2.6 # SP Ret, T-Yield, Inflation

def calculate_taco(sp_ret, t_yield, infl, approval):
    p = 0
    if sp_ret >= 0: p += 0
    elif sp_ret > -0.05: p += 15
    else: p += 25
    if t_yield < 4.0: p += 0
    elif t_yield <= 4.5: p += 15
    else: p += 25
    if infl < 2.2: p += 0
    elif infl <= 2.8: p += 15
    else: p += 25
    if approval > 45: p += 0
    elif approval >= 40: p += 15
    else: p += 25
    return p

def get_sector_trend_multiplier_mock(sector_name):
    return 1.1 # Always returns a tailwind for the demo

def get_detailed_prospects_mock(ticker_list, target_days, risk_free_rate, vix_level, taco_score, risk_mode):
    # This mock guarantees that the UI features (Gamma Trap, Earnings Trap, Alpha Strike) 
    # will fire perfectly for presentation purposes.
    today = datetime.now()
    
    t1 = ticker_list[0] if len(ticker_list) > 0 else "DEMO1"
    t2 = ticker_list[1] if len(ticker_list) > 1 else "DEMO2"
    t3 = ticker_list[2] if len(ticker_list) > 2 else "DEMO3"

    results = [
        {
            "Symbol": t1, "Price": 45.50, "DTE": 14, "Safety Buffer (%)": 3.5, "Div Yield (%)": 1.2,
            "Target Strike": 44.00, "Bid": 0.65, "ROC (%)": 1.47, "AROC (%)": 38.5, 
            "Prob. Assign": 38.2, "IV": 28.5, "IV Rank": 65.0, "Next Earnings": (today + timedelta(days=50)).strftime('%Y-%m-%d')
        }, # Triggers Gamma Trap (Orange)
        {
            "Symbol": t2, "Price": 52.00, "DTE": 35, "Safety Buffer (%)": 7.0, "Div Yield (%)": 2.5,
            "Target Strike": 48.50, "Bid": 0.90, "ROC (%)": 1.85, "AROC (%)": 19.3, 
            "Prob. Assign": 25.1, "IV": 32.0, "IV Rank": 82.0, "Next Earnings": (today + timedelta(days=4)).strftime('%Y-%m-%d')
        }, # Triggers Earnings Trap (Red)
        {
            "Symbol": t3, "Price": 62.50, "DTE": 42, "Safety Buffer (%)": 8.5, "Div Yield (%)": 3.8,
            "Target Strike": 57.00, "Bid": 1.55, "ROC (%)": 2.71, "AROC (%)": 23.6, 
            "Prob. Assign": 16.5, "IV": 24.5, "IV Rank": 45.0, "Next Earnings": (today + timedelta(days=60)).strftime('%Y-%m-%d')
        }  # The Perfect Alpha Strike
    ]
    return pd.DataFrame(results)

# --- 5. TOP ROW (HEADER & WEATHER) ---
t_left, t_right = st.columns([1, 4])
with t_left:
    st.markdown('<p class="corp-header">Rational Basis<br>Managed Investments</p>', unsafe_allow_html=True)
    minute_clock()
    st.markdown(f'<div style="margin-top: -15px;"><p style="color: #e3b341; font-size: 13px; font-weight: bold; margin-bottom: 0px;">{VERSION_NAME}</p><p class="version-text">v{VERSION_NUM} | {VERSION_DATE}</p></div>', unsafe_allow_html=True)

with t_right:
    w_data = fetch_weather_metrics_mock()
    sp = w_data["^GSPC"]; vx = w_data["^VIX"]
    m1, m2, m3 = st.columns(3)
    m1.caption("S&P 500"); m1.metric("Price", f"{sp['current']:,.2f}")
    s1, s2 = m1.columns(2); s1.metric("vs Open", f"{sp['vs_open']:+,.2f}"); s2.metric("vs Close", f"{sp['vs_close']:+,.2f}", delta=f"{sp['pct_close']:.2f}%")
    m2.caption("VIX (Fear Index)"); m2.metric("Level", f"{vx['current']:.2f}")
    v1, v2 = m2.columns(2); v1.metric("vs Open", f"{vx['vs_open']:+.2f}", delta_color="inverse"); v2.metric("vs Close", f"{vx['vs_close']:+.2f}", delta_color="inverse")
    m3.caption("Put-Call Ratio"); m3.metric("Ratio", "0.98")
    p1, p2 = m3.columns(2); p1.metric("vs Open", "-0.01"); p2.metric("vs Close", "+0.04")

st.divider()

# --- 6. TAB ARCHITECTURE ---
tab_exec, tab_scan, tab_instr = st.tabs([":bar_chart: Execution Dashboard", ":telescope: Market Prospector", ":blue_book: Operations Manual"])

# ==========================================
# TAB 1: EXECUTION DASHBOARD (DEMO)
# ==========================================
with tab_exec:
    b_left, b_right = st.columns([1, 4])
    symbol_db = load_symbol_database_mock()
    available_sectors = sorted(list(set(MASTER_SECTORS)))

    with b_left:
        st.subheader("TACO Index")
        approval_val = st.number_input("Approval Rating (%)", 0, 100, 42, key="exec_approval")
        sp_r, t_y, inf = get_taco_macro_data_mock()
        t_score = calculate_taco(sp_r, t_y, inf, approval_val)
        t_color = "green" if t_score < 31 else "orange" if t_score < 61 else "red"
        st.markdown(f'<div class="taco-box"><h1 style="color:{t_color};">{t_score}</h1><p>SCORE</p></div>', unsafe_allow_html=True)
        st.divider()
        st.markdown("**Algorithmic Targeting**")
        risk_mode = st.radio("Strategy", ["Moderate", "Conservative"], horizontal=True, label_visibility="collapsed", key="exec_risk")
        target_days = {"Closest Expiration": 0, "Approx 14 Days": 14, "Approx 30 Days": 30, "Approx 45 Days": 45}[st.selectbox("Target Timeframe", ["Closest Expiration", "Approx 14 Days", "Approx 30 Days", "Approx 45 Days"], index=3, key="exec_dte")]
        max_price = st.number_input("Max Stock Price ($)", 10, 500, 65, key="exec_max") 
        selected_sector = st.selectbox("Focus Sector", available_sectors, key="exec_sector")

    with b_right:
        st.subheader(f"Execution Scanner: {selected_sector}")
        sector_tickers = symbol_db[symbol_db['Sector'] == selected_sector]['Symbol'].tolist()
        
        # Pulling from Mock Engine
        current_vix = w_data["^VIX"]['current']
        scan_results = get_detailed_prospects_mock(sector_tickers, target_days, t_y, current_vix, t_score, risk_mode)
        affordable = scan_results[(scan_results['Price'] > 0) & (scan_results['Price'] <= max_price)].copy() if not scan_results.empty else pd.DataFrame()
        
        if not affordable.empty:
            def highlight_earnings(val):
                try: return 'background-color: #721c24; color: #f8d7da;' if datetime.strptime(val, '%Y-%m-%d') < datetime.now() + timedelta(days=14) else ''
                except: return ''
            def highlight_dte(val):
                try: return 'background-color: #d97706; color: #ffffff;' if int(val) < 21 else ''
                except: return ''

            # Display the core table
            display_df = affordable.drop(columns=['Div Yield (%)'], errors='ignore') 
            try: styled_df = display_df.style.map(highlight_earnings, subset=['Next Earnings']).map(highlight_dte, subset=['DTE'])
            except: styled_df = display_df.style.applymap(highlight_earnings, subset=['Next Earnings']).applymap(highlight_dte, subset=['DTE'])
            st.dataframe(styled_df.format({"Price": "${:.2f}", "Safety Buffer (%)": "{:.1f}%", "Target Strike": "${:.2f}", "Bid": "${:.2f}", "ROC (%)": "{:.2f}%", "AROC (%)": "{:.1f}%", "Prob. Assign": "{:.1f}%", "IV": "{:.1f}%", "IV Rank": lambda x: f"{x:.0f}"}), hide_index=True, use_container_width=True)
            
            # --- THE ALPHA STRIKE RECOMMENDATION ENGINE ---
            def is_earnings_safe(date_str):
                if date_str == "N/A": return True
                try: return datetime.strptime(date_str, '%Y-%m-%d') >= datetime.now() + timedelta(days=14)
                except: return True
                
            candidates = affordable[
                (affordable['DTE'] >= 21) & 
                (affordable['Next Earnings'].apply(is_earnings_safe))
            ].copy()
            
            if candidates.empty:
                st.markdown("""
                <div style="background-color: #161b22; padding: 15px; border-radius: 5px; border: 1px solid #30363d; margin-top: 10px; margin-bottom: 15px;">
                    <p style="margin-bottom: 0px; font-weight: bold; color: #8b949e; font-size: 15px;">&#x1F6E1; CAPITAL PRESERVATION MODE ACTIVE</p>
                    <p style="color: #c9d1d9; font-size: 13px; margin-top: 5px; margin-bottom: 0px;">The algorithm is not recommending a contract in this sector today. All affordable candidates currently trigger the Gamma Warning (DTE < 21) or face an impending Earnings Trap. Capital preservation takes priority over forced yield.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                sector_mult = get_sector_trend_multiplier_mock(selected_sector)
                trend_text = "a macroeconomic tailwind" if sector_mult > 1 else "a macroeconomic headwind" if sector_mult < 1 else "a neutral market trend"
                
                candidates['Alpha_Score'] = (
                    candidates['AROC (%)'] * (1 - (candidates['Prob. Assign'] / 100)) * candidates['Safety Buffer (%)'] * sector_mult * (1 + (candidates['Div Yield (%)'] / 100))
                )
                winner = candidates.loc[candidates['Alpha_Score'].idxmax()]
                
                st.markdown(f"""
                <div style="background-color: #0d2a1b; padding: 15px; border-radius: 5px; border: 1px solid #2ea043; margin-top: 10px; margin-bottom: 15px;">
                    <p style="margin-bottom: 5px; font-weight: bold; color: #3fb950; font-size: 16px;">&#x1F3AF; ALPHA STRIKE CANDIDATE: {winner['Symbol']}</p>
                    <p style="color: #c9d1d9; font-size: 14px; margin-top: 0px; margin-bottom: 0px;">
                    <strong>Target Strike:</strong> ${winner['Target Strike']:.2f} | <strong>Premium:</strong> ${winner['Bid']:.2f} | <strong>AROC:</strong> {winner['AROC (%)']:.1f}%<br>
                    <em>Why it won:</em> This contract offers an optimal risk-adjusted yield with a <strong>{winner['Safety Buffer (%)']:.1f}% safety buffer</strong>. 
                    It avoids the Gamma trap ({int(winner['DTE'])} days out), clears the earnings window, benefits from a <strong>{winner['Div Yield (%)']:.1f}% dividend parachute</strong>, 
                    and is currently trading with {trend_text}.
                    </p>
                </div>
                """, unsafe_allow_html=True)

            # --- THE DASHBOARD LEGEND ---
            st.markdown("""
            <div style="background-color: #161b22; padding: 15px; border-radius: 5px; border: 1px solid #30363d; margin-top: 0px;">
                <p style="margin-bottom: 5px; font-weight: bold; color: #8b949e; font-size: 14px;">&#x1F4CA; DASHBOARD LEGEND & COLOR KEYS</p>
                <ul style="font-size: 13px; color: #c9d1d9; margin-bottom: 10px;">
                    <li><span style="background-color: #721c24; color: #f8d7da; padding: 2px 6px; border-radius: 3px;">Red Row</span> <strong>The Earnings Trap:</strong> An earnings report is scheduled within the next 14 days. Selling options over binary events carries massive assignment risk.</li>
                    <li><span style="background-color: #d97706; color: #ffffff; padding: 2px 6px; border-radius: 3px;">Orange DTE</span> <strong>The Gamma Trap Warning:</strong> Contract expires in less than 21 days. High risk of rapid assignment if the stock price drops quickly.</li>
                </ul>
                <p style="margin-bottom: 5px; font-weight: bold; color: #8b949e; font-size: 14px;">&#x1F4C8; VOLATILITY FAILSAFES</p>
                <ul style="font-size: 13px; color: #c9d1d9; margin-bottom: 0px;">
                    <li><strong>IV (Implied Volatility):</strong> The market's expectation of the stock's future price swings. Higher IV generally equals higher premiums, but indicates higher perceived risk.</li>
                    <li><strong>IV Rank:</strong> Evaluates current IV against the stock's own 1-year historical range (0 to 100). An IV Rank of 80 means volatility is higher than it has been 80% of the time over the last year. (We want to sell when IV Rank is elevated).</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.warning(f"No candidates found in {selected_sector} under ${max_price}.")

# ==========================================
# TAB 2: MARKET PROSPECTOR (DISABLED)
# ==========================================
with tab_scan:
    st.subheader("Market-Wide S&P 1500 Prospector")
    
    st.markdown("""
    <div style="background-color: #21262d; padding: 20px; border-radius: 8px; border: 2px solid #30363d; text-align: center; margin-top: 20px;">
        <h3 style="color: #e3b341; margin-bottom: 10px;">&#x26A0; MODULE DISABLED IN DEMO ENVIRONMENT</h3>
        <p style="color: #c9d1d9; font-size: 15px; max-width: 800px; margin: 0 auto;">
        In the live production version, this module actively scrapes Wikipedia for S&P 1500 constituents, downloads live 
        financial data via the Yahoo Finance API, and runs them through a rigorous fundamental gauntlet (Free Cash Flow, 
        Current Ratios, Dividend Safety) to automatically replenish the proprietary tracking database.<br><br>
        <em>Because this process requires live, unthrottled API access, it has been disabled in this demonstration build to ensure optimal stability.</em>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# TAB 3: OPERATIONS MANUAL
# ==========================================
with tab_instr:
    st.subheader("Dashboard Standard Operating Procedures (SOP)")
    st.markdown("""
    ### Welcome to the Rational Basis Managed Investments Dashboard
    This proprietary engine is designed to execute a high-probability, risk-managed put-write strategy (Phase 1 of the Wheel Strategy). It ruthlessly filters out fundamental garbage and actively guards against options-pricing traps to target a sustainable 2% to 2.5% monthly yield.
    
    ---
    
    #### Stage 1: The Market Prospector (Weekend Sweep)
    *Run this module once a week to replenish your proprietary database.*
    1. **Set Fundamental Pillars:** Adjust the sliders for your minimum baseline of corporate health (Market Cap, Positive Revenue, Free Cash Flow, Current Ratio, and Dividend Safety).
    2. **Run Market Sweep:** The engine will scrape all S&P 1500 constituents, discard anything over your max capital limit, and process the survivors through the fundamental gauntlet.
    3. **Inject into Tracker:** Review the survivors and inject them directly into your underlying CSV tracking list. These are the ONLY stocks you are permitted to trade.
    
    #### Stage 2: The Execution Dashboard (Daily Operations)
    *Use this module to discover mathematically optimal contracts.*
    1. **Review Macro Weather:** Analyze the S&P 500, VIX (Fear Index), and custom TACO Score at the top of your screen to judge overall market stress.
    2. **Select Parameters:** Choose your target timeframe (**45 Days** is the recommended institutional sweet spot) and focus sector.
    3. **Analyze the Alpha Strike:** If market conditions permit, the engine will recommend a single "Best in Class" contract based on its calculated Expected Value (Risk-Adjusted AROC, Safety Buffer, Dividend Parachute, and Macro Sector Trend).
    4. **Obey the Visual Guardrails:** * &#x1F6E1; **Capital Preservation Mode:** If active, the engine recommends walking away. Do not force a trade.
        * &#x1F7E7; **Orange DTE:** Gamma Trap Warning. Contract expires in < 21 days. Proceed with extreme caution.
        * &#x1F7E5; **Red Earnings:** Earnings Trap Warning. Imminent binary event. Selling here is strictly gambling.
    
    ---
    
    *Disclaimer: This tool is for educational, analytical, and informational purposes only. It is not an automated trading robot. All generated math and recommendations should be verified with your broker prior to order execution.*
    """, unsafe_allow_html=True)
