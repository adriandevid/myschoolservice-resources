import pdfkit
import urllib.request
import re

fp = urllib.request.urlopen("http://minio.minhaescolasga.online:9000/certificates/approved-enrollment/index.html")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

match = re.search(r'<style.*?>(.*?)</style>', mystr, re.DOTALL | re.IGNORECASE)
css = ""
body= ""

if match:
    css = match.group(1).strip()
else:
    print("Tag <style> não encontrada.")

matchBody = re.search(r'<body.*?>(.*?)</body>', mystr, re.DOTALL | re.IGNORECASE)

if match:
    body = matchBody.group(1).strip()
else:
    print("Tag <body> não encontrada.")


config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

print(body)
options = {
    'orientation': 'Landscape',
    'page-size': 'A4',
    'encoding': "UTF-8"
}

html = """
           <style>"""+ css +"""<style>
           <body>
                              """+ body +"""
                          </body>
       """

pdfkit.from_string(html, 'saida.pdf', options=options, configuration=config)