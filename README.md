<h1>使用方式:</h1>
<ol>
    <li>clone git 專案</li>
    <li>在專案中啟動 venv</li>
    <li>pip install -r requirements.txt</li>
    <li>建立.env檔案</li>
    <li>
        複製以下項目到.env中
        <p>
            SQLALCHEMY_DATABASE_URI = "your db url"<br/>
        <p> 
    </li>
    <li>引入根目錄中的db.sql到自己的mysql browser(ex: mysql workbench、mariadb(Heidi DB))</li>
    <li>streamlit run app.py</li>
</ol>