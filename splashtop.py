import streamlit as st
import streamlit.components.v1 as components

# App Store URLs
IOS_APP_STORE_URL = "https://apps.apple.com/app/splashtop-sos/id1230853703"
GOOGLE_PLAY_STORE_URL = "https://play.google.com/store/apps/details?id=com.splashtop.sos&pcampaignid=web_share"
# Android market URL for direct Play Store app opening
GOOGLE_PLAY_MARKET_URL = "market://details?id=com.splashtop.sos"

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
    
    # Create redirect HTML using form submission to break out of iframe
    redirect_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="margin:0;padding:0;">
        <script>
        (function() {{
            // Get user agent
            const userAgent = navigator.userAgent || navigator.vendor || window.opera;
            
            // Detect iOS devices (including iPad on iOS 13+)
            const isIOS = /iPad|iPhone|iPod/.test(userAgent) || 
                         (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
            
            // Detect Android devices - improved detection
            const isAndroid = /android/i.test(userAgent) || 
                             /Android/i.test(navigator.platform) ||
                             (navigator.userAgentData && navigator.userAgentData.platform === 'Android');
            
            // Determine redirect URL
            let redirectUrl = null;
            let fallbackUrl = null;
            if (isIOS) {{
                redirectUrl = "{IOS_APP_STORE_URL}";
            }} else if (isAndroid) {{
                // Use market:// URL for Android with web fallback
                redirectUrl = "{GOOGLE_PLAY_MARKET_URL}";
                fallbackUrl = "{GOOGLE_PLAY_STORE_URL}";
            }}
            
            // Redirect if device detected using multiple methods
            if (redirectUrl) {{
                // Function to perform redirect
                function doRedirect(url) {{
                    // Method 1: Try to break out of iframe directly
                    try {{
                        if (window.top && window.top !== window.self) {{
                            window.top.location.href = url;
                            return true;
                        }}
                    }} catch (e) {{
                        // Cross-origin error, try other methods
                    }}
                    
                    // Method 2: Create a form and submit it to break out of iframe
                    try {{
                        const form = document.createElement('form');
                        form.method = 'GET';
                        form.action = url;
                        form.target = '_top';
                        document.body.appendChild(form);
                        form.submit();
                        return true;
                    }} catch (e) {{
                        // Form submission failed
                    }}
                    
                    // Method 3: Create a link with target="_top" and click it
                    try {{
                        const link = document.createElement('a');
                        link.href = url;
                        link.target = '_top';
                        link.style.display = 'none';
                        document.body.appendChild(link);
                        link.click();
                        return true;
                    }} catch (e) {{
                        // Link click failed
                    }}
                    
                    // Method 4: Fallback - redirect within iframe
                    try {{
                        window.location.href = url;
                        return true;
                    }} catch (e) {{
                        return false;
                    }}
                }}
                
                // For Android, try market:// first, then fallback to web URL
                if (isAndroid && fallbackUrl) {{
                    // Try market:// URL first
                    const redirected = doRedirect(redirectUrl);
                    // If market:// doesn't work (e.g., Play Store app not installed), fallback to web
                    if (redirected) {{
                        setTimeout(function() {{
                            // If still on page after 500ms, market:// might have failed
                            if (document.visibilityState === 'visible') {{
                                doRedirect(fallbackUrl);
                            }}
                        }}, 500);
                    }} else {{
                        // If redirect failed immediately, use web URL
                        doRedirect(fallbackUrl);
                    }}
                }} else {{
                    // For iOS, just redirect
                    doRedirect(redirectUrl);
                }}
            }}
        }})();
        </script>
        <div style="text-align:center;padding:50px;font-family:Arial,sans-serif;">
            <h2>Redirecting to App Store...</h2>
            <p id="countdown" style="font-size:16px;color:#666;">Redirecting in 2 seconds...</p>
            <p>If you're not redirected, please click below:</p>
            <p>
                <a id="iosLink" href="{IOS_APP_STORE_URL}" target="_top" style="margin-right:20px;color:#007AFF;text-decoration:none;font-size:18px;padding:15px 30px;border:2px solid #007AFF;border-radius:8px;display:inline-block;background:#f0f8ff;">📱 iOS App Store</a>
                <a id="androidLink" href="{GOOGLE_PLAY_MARKET_URL}" data-fallback="{GOOGLE_PLAY_STORE_URL}" target="_top" style="color:#007AFF;text-decoration:none;font-size:18px;padding:15px 30px;border:2px solid #007AFF;border-radius:8px;display:inline-block;background:#f0f8ff;">🤖 Google Play</a>
            </p>
        </div>
        <script>
        // Auto-click the appropriate link after a short delay
        (function() {{
            const userAgent = navigator.userAgent || navigator.vendor || window.opera;
            const isIOS = /iPad|iPhone|iPod/.test(userAgent) || 
                         (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
            // Improved Android detection
            const isAndroid = /android/i.test(userAgent) || 
                             /Android/i.test(navigator.platform) ||
                             (navigator.userAgentData && navigator.userAgentData.platform === 'Android');
            
            let targetLink = null;
            if (isIOS) {{
                targetLink = document.getElementById('iosLink');
            }} else if (isAndroid) {{
                targetLink = document.getElementById('androidLink');
            }}
            
            if (targetLink) {{
                // For Android, handle market:// URL with fallback
                if (isAndroid && targetLink.dataset.fallback) {{
                    // Try market:// URL first, fallback to web URL if it doesn't work
                    const originalHref = targetLink.href;
                    targetLink.addEventListener('click', function(e) {{
                        // Market URL is already set as href, so it will try first
                        // If it fails, fallback after a delay
                        setTimeout(function() {{
                            // Check if we're still on the page (market:// might have failed)
                            if (document.visibilityState === 'visible') {{
                                targetLink.href = targetLink.dataset.fallback;
                                // Try clicking again with web URL
                                setTimeout(function() {{
                                    targetLink.click();
                                }}, 100);
                            }}
                        }}, 800);
                    }}, {{ once: true }});
                }}
                
                // Countdown
                let countdown = 1;
                const countdownEl = document.getElementById('countdown');
                const timer = setInterval(function() {{
                    if (countdown > 0) {{
                        countdownEl.textContent = 'Redirecting in ' + countdown + ' second' + (countdown > 1 ? 's' : '') + '...';
                        countdown--;
                    }} else {{
                        clearInterval(timer);
                        countdownEl.textContent = 'Redirecting now...';
                        // Auto-click the link
                        targetLink.click();
                    }}
                }}, 1000);
            }}
        }})();
        </script>
    </body>
    </html>
    """
    
    # Use components.html - make it full screen
    components.html(redirect_html, height=600, scrolling=False)
    
    # Fallback message for non-mobile devices
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem;">
        <p>If you're not redirected automatically, please choose your device:</p>
        <p>
            <a href="{}" target="_blank" style="margin-right: 1rem; text-decoration: none; color: #007AFF; font-size: 18px;">📱 iOS App Store</a>
            <a href="{}" target="_blank" style="text-decoration: none; color: #007AFF; font-size: 18px;">🤖 Google Play Store</a>
        </p>
    </div>
    """.format(IOS_APP_STORE_URL, GOOGLE_PLAY_STORE_URL), unsafe_allow_html=True)

if __name__ == "__main__":
    main()

