import webbrowser
import os

html_path = os.path.abspath('cftc_持仓报告_2026-05-12.html')
url = f'file:///{html_path}'
webbrowser.open(url)

# 指定浏览器（如Edge）
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
webbrowser.get('edge').open(url)