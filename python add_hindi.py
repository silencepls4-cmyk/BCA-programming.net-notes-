import os

# Yeh folder path check karega jahan aapki HTML files hain
folder_path = "./"

# Yeh poora translation code hai jo direct har HTML file mein jud jayega
translation_code = """
<!-- Universal Hindi Translator Script -->
<div id="google_translate_element" style="display:none;"></div>
<script type="text/javascript">
    function googleTranslateElementInit() {
        new google.translate.TranslateElement({
            pageLanguage: 'en',
            includedLanguages: 'hi',
            autoDisplay: false
        }, 'google_translate_element');

        var checkInterval = setInterval(function () {
            var selectField = document.querySelector('.goog-te-combo');
            if (selectField) {
                selectField.value = 'hi';
                selectField.dispatchEvent(new Event('change'));
                clearInterval(checkInterval);
            }
        }, 200);
    }
</script>
<script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
<style>
    .goog-te-banner-frame.skiptranslate { display: none !important; }
    body { top: 0px !important; }
    pre, code, .badge, th, script, style { translate: no; }
</style>
</body>
"""

print("Sabhi HTML files mein direct shuddh Hindi translation code joda ja raha hai...")

count = 0
for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Check karein ki translation code pehle se to nahi laga hai
        if "googleTranslateElementInit" not in content:
            if "</body>" in content:
                # </body> ko replace karke poora translation code add kar dega
                updated_content = content.replace("</body>", translation_code)
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)
                print(f"[Success] Updated: {filename}")
                count += 1
            else:
                print(f"[Skipped] </body> tag nahi mila: {filename}")
        else:
            print(f"[Already Exists] Translation code pehle se hai: {filename}")

print(f"\nKaam pura ho gaya! Kul {count} HTML files mein shuddh Hindi translation code lag chuki hai.")
