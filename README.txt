Sweetex AI GitHub Upload Package

1. Unzip files
2. Upload all files to your GitHub repo (sweetex-ai):
   - server.py
   - requirements.txt
   - render.yaml

3. Go to https://render.com
4. Login with GitHub
5. Click New + -> Blueprint
6. Select your sweetex-ai repo
7. Click Deploy

After deploy, update your HTML:
Replace:
fetch('http://localhost:5000/analyze')
With:
fetch('https://YOUR-RENDER-URL.onrender.com/analyze')
