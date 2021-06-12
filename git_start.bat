git config --global user.name "RSFfen"
git config --global user.email "rsf61.fen@gmail.com"
pip freeze > requirements.txt
git remote add origin https://github.com/RSFfen/project1.git
git branch -M main
git push -u origin main
heroku login