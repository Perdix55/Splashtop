import streamlit as st
import streamlit.components.v1 as components

# App Store URLs
IOS_APP_STORE_URL = "https://apps.apple.com/app/splashtop-sos/id1230853703"
GOOGLE_PLAY_STORE_URL = "https://play.google.com/store/apps/details?id=com.splashtop.sos&pcampaignid=web_share"

# JavaScript code to detect device and redirect
redirect_script = f"""
<script>
(function() {{
    // Get user agent
    const userAgent = navigator.userAgent || navigator.vendor || window.opera;
    
    // Detect iOS devices
    const isIOS = /iPad|iPhone|iPod/.test(userAgent) && !window.MSStream;
    
    // Detect Android devices
    const isAndroid = /android/i.test(userAgent);
    
    // Determine redirect URL
    let redirectUrl = null;
    if (isIOS) {{
        redirectUrl = "{IOS_APP_STORE_URL}";
    }} else if (isAndroid) {{
        redirectUrl = "{GOOGLE_PLAY_STORE_URL}";
    }}
    
    // Redirect if device detected
    if (redirectUrl) {{
        window.location.href = redirectUrl;
    }}
}})();
</script>
"""

def main():
    st.set_page_config(
        page_title="Splashtop SOS - App Store Redirect",
        page_icon="📱",
        layout="centered"
    )
    
    # Hide Streamlit menu and footer
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # Display loading message
    st.title("📱 Redirecting to App Store...")
    st.info("Please wait while we redirect you to the appropriate app store.")
    
    # Inject JavaScript for device detection and redirection
    components.html(redirect_script, height=0)
    
    # Fallback message for non-mobile devices
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem;">
        <p>If you're not redirected automatically, please choose your device:</p>
        <p>
            <a href="{}" style="margin-right: 1rem;">📱 iOS App Store</a>
            <a href="{}">🤖 Google Play Store</a>
        </p>
    </div>
    """.format(IOS_APP_STORE_URL, GOOGLE_PLAY_STORE_URL), unsafe_allow_html=True)

if __name__ == "__main__":
    main()


