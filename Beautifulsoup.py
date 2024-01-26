from bs4 import BeautifulSoup



html = '''
<!DOCTYPE html>
<html>
<head>
<title>Example Page</title>
</head>
<body>
<h1>Example Heading</h1>
<p>This is an example paragraph.</p>
<p class="example_class">This is an example paragraph with a class.</p>
<p id="example_id">This is an example paragraph with an ID.</p>
</body>
</html>
'''


soup = BeautifulSoup(html, 'html.parser')
print(soup)