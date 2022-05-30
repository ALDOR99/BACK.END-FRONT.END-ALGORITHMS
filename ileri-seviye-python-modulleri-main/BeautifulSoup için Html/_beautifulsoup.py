html_doc ="""

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>hello man</title>
</head>

<body>
    <h1 id="header">
        python kursu
    </h1>
    <div class="grup1">

        <h2>
            programlama
        </h2>

        <ul>
            <li>menü1</li>
            <li>menü2</li>
             <li>menü3</li>
        </ul>

    </div>

    <div class="grup2">

        <h2>
            Modüller
        </h2>

        <ul>
            <li>menü1</li>
            <li>menü2</li>
             <li>menü3</li>
        </ul>

    </div>
    <img src="dsa.PNG" alt="">

</body>
</html>

"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,"html.parser")

result = soup.prettify()
result = soup.title
result = soup.head
result = soup.body
result = soup.title.name
result = soup.title.string

result = soup.h1
result = soup.h2
result = soup.h2.name
result = soup.h2.string
print(result)

result =soup.find_all("h2")
print("-"*30)
result =soup.find_all("h2")[0]
result =soup.find_all("h2")[1]
print("-"*30)
result = soup.div
result = soup.find_all("div")
result = soup.find_all("div")[1]
result = soup.find_all("div")[1].ul.find_all("li")

result = soup.div.findChildren()

result = soup.div.findNextSibling()
result = soup.div.findNextSibling().findNextSibling()
print(result)









































